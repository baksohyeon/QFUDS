import contextlib
import importlib.util
import os
import pathlib
import tempfile
import unittest


MODULE_PATH = pathlib.Path(__file__).parents[1] / "scripts" / "fiction_gate.py"
SPEC = importlib.util.spec_from_file_location("fiction_gate", MODULE_PATH)
fiction_gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fiction_gate)


VALID_HOME = """# Demo

## Classification
- Work id: `demo`
- State: `drafting`
- Style profile: `inline`
- Canon promotion authority/rule: user approval

## Drafts And Reviews
- Current draft: drafts/001.md

## Current Next Action
Revise the opening.
"""


@contextlib.contextmanager
def workspace():
    previous = pathlib.Path.cwd()
    with tempfile.TemporaryDirectory() as directory:
        root = pathlib.Path(directory)
        os.chdir(root)
        try:
            yield root
        finally:
            os.chdir(previous)


def write(root, relative, text):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return relative


class FictionGateTests(unittest.TestCase):
    def test_passes_minimal_project_and_zettel(self):
        with workspace() as root:
            files = [
                write(root, "fiction/projects/demo/README.md", VALID_HOME),
                write(root, "fiction/projects/demo/drafts/001.md", "# Draft\n"),
                write(
                    root,
                    "fiction/knowledge/notes/idea.md",
                    "---\ntype: zettel\nkind: idea\ncreated: 2026-07-11\n"
                    "source-ids: []\nrelated-notes: []\nrelated-projects: []\n---\n# Idea\n",
                ),
            ]
            errors, _ = fiction_gate.check(files)
            self.assertEqual(errors, [])

    def test_rejects_incomplete_project_home(self):
        with workspace() as root:
            path = write(root, "fiction/projects/demo/README.md", "# Demo\n")
            errors, _ = fiction_gate.check([path])
            self.assertTrue(any("project Home Note missing" in error for error in errors))

    def test_rejects_fenced_zettel_metadata(self):
        with workspace() as root:
            path = write(root, "fiction/knowledge/notes/bad.md", "# Bad\n```yaml\ntype: zettel\n```\n")
            errors, _ = fiction_gate.check([path])
            self.assertTrue(any("top-of-file YAML" in error for error in errors))

    def test_rejects_project_artifact_without_home(self):
        with workspace() as root:
            path = write(root, "fiction/projects/orphan/drafts/001.md", "# Draft\n")
            errors, _ = fiction_gate.check([path])
            self.assertTrue(any("has no project Home Note" in error for error in errors))

    def test_rejects_unpinned_release_candidate_name(self):
        with workspace() as root:
            write(root, "fiction/projects/demo/README.md", VALID_HOME)
            path = write(root, "fiction/projects/demo/release/candidates/demo_v1.md", "# Candidate\n")
            errors, _ = fiction_gate.check([path])
            self.assertTrue(any("baseline short SHA" in error for error in errors))

    def test_rejects_published_snapshot_without_evidence(self):
        with workspace() as root:
            write(root, "fiction/projects/demo/README.md", VALID_HOME)
            path = write(root, "fiction/projects/demo/release/published/demo_v1.md", "# Published\n")
            errors, _ = fiction_gate.check([path])
            self.assertTrue(any("state released" in error for error in errors))
            self.assertTrue(any("retention gate" in error for error in errors))
            self.assertTrue(any("release checklist" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
