---
doc_id: asset_eboss_dr16_lya_bao_2020_markitdown_sdss_bao_only_directory
title: "eBOSS DR16 Lyman-alpha BAO MarkItDown SDSS BAO-only Directory Conversion"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_eboss_dr16_lya_bao_2020
next_gate: use curated likelihood-release parse for source-product decisions
last_updated: 2026-06-17
---

# eBOSS DR16 Lyman-alpha BAO MarkItDown SDSS BAO-only Directory Conversion

Quality state: `low_fidelity_search_text`.

This is a direct [MarkItDown](https://github.com/microsoft/markitdown) conversion of the SDSS SVN BAO-only directory page
<https://svn.sdss.org/public/data/eboss/DR16cosmo/tags/v1_0_1/likelihoods/BAO-only/>.

<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="/svnindex.xsl"?>
<!DOCTYPE svn [
  <!ELEMENT svn   (index)>
  <!ATTLIST svn   version CDATA #REQUIRED
                  href    CDATA #REQUIRED>
  <!ELEMENT index (updir?, (file | dir)*)>
  <!ATTLIST index name    CDATA #IMPLIED
                  path    CDATA #IMPLIED
                  rev     CDATA #IMPLIED
                  base    CDATA #IMPLIED>
  <!ELEMENT updir EMPTY>
  <!ELEMENT file  EMPTY>
  <!ATTLIST file  name    CDATA #REQUIRED
                  href    CDATA #REQUIRED>
  <!ELEMENT dir   EMPTY>
  <!ATTLIST dir   name    CDATA #REQUIRED
                  href    CDATA #REQUIRED>
]>
<svn version="1.6.11 (r934486)"
     href="http://subversion.tigris.org/">
  <index rev="27531" path="/eboss/DR16cosmo/tags/v1_0_1/likelihoods/BAO-only" base="data">
    <updir />
    <file name="README.txt" href="README.txt" />
    <file name="sdss_DR12_LRG_BAO_DMDH.txt" href="sdss_DR12_LRG_BAO_DMDH.txt" />
    <file name="sdss_DR12_LRG_BAO_DMDH_covtot.txt" href="sdss_DR12_LRG_BAO_DMDH_covtot.txt" />
    <file name="sdss_DR16_ELG_BAO_DVtable.txt" href="sdss_DR16_ELG_BAO_DVtable.txt" />
    <file name="sdss_DR16_LRG_BAO_DMDH.txt" href="sdss_DR16_LRG_BAO_DMDH.txt" />
    <file name="sdss_DR16_LRG_BAO_DMDH_covtot.txt" href="sdss_DR16_LRG_BAO_DMDH_covtot.txt" />
    <file name="sdss_DR16_LYAUTO_BAO_DMDHgrid.txt" href="sdss_DR16_LYAUTO_BAO_DMDHgrid.txt" />
    <file name="sdss_DR16_LYxQSO_BAO_DMDHgrid.txt" href="sdss_DR16_LYxQSO_BAO_DMDHgrid.txt" />
    <file name="sdss_DR16_QSO_BAO_DMDH.txt" href="sdss_DR16_QSO_BAO_DMDH.txt" />
    <file name="sdss_DR16_QSO_BAO_DMDH_covtot.txt" href="sdss_DR16_QSO_BAO_DMDH_covtot.txt" />
  </index>
</svn>
