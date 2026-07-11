# Projects

특정 작품을 완성하기 위한 설계·장면·원고·퇴고를 보관한다. 프로젝트마다
어느 세계를 상속하는지, 현재 상태가 무엇인지, 원고와 세계 문서의 경계를
README에 적는다.

## Project Home 원칙

새 프로젝트의 진입점은 손으로 관리하는 `README.md` 하나다. 이 저장소에서는
README가 Home Note 역할을 한다. `HOME.md`와 `story.md`를 동시에 필수화하지 않는다.

- 자동 생성 대시보드·쿼리 목록이 아니라, 작가가 지금 중요한 것을 직접
  배열한 작업 지도다.
- 최소 구성: 전제(premise)·형식·상속 세계·상태, 열린 질문, 다음 행동
  하나.
- 아이디어 원본은 `knowledge/`에 두고 링크한다. 프로젝트로 복사하지
  않는다.

작품이 장편화되어 인물 사망, 약속 회수, 지식 상태, 타임라인을 기계적으로 검사할
필요가 생기면 `tools/story-skills` schema를 선택형 adapter로 도입한다. 새 작품이
처음부터 모든 상태 파일을 만들 필요는 없다. 세 번 이상 반복해서 관리 비용이 생긴
작업만 자동화한다.

release 작업이 시작되면 작품 아래 `release/candidates/`, `release/published/`,
`reviews/release/`, `reviews/retention/`을 필요한 시점에 만든다. 움직이는 draft를
직접 published로 취급하지 않고, 고정 baseline을 통과한 snapshot만 승격한다.

QFUDS SAGA의 소설·프로젝트 생산물은 2026-07-10에 종료되어 Git 이력으로만
보존한다.
