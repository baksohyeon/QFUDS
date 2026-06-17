---
doc_id: asset_eboss_dr16_lya_bao_2020_markitdown_sdss_dataveccov_lya_forest_directory
title: "eBOSS DR16 Lyman-alpha BAO MarkItDown SDSS Data-Vector/Covariance Directory Conversion"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_eboss_dr16_lya_bao_2020
next_gate: download raw FITS assets only under a size-aware plan
last_updated: 2026-06-17
---

# eBOSS DR16 Lyman-alpha BAO MarkItDown SDSS Data-Vector/Covariance Directory Conversion

Quality state: `low_fidelity_search_text`.

This is a direct [MarkItDown](https://github.com/microsoft/markitdown) conversion of the SDSS SVN Lyman-alpha
data-vector/covariance directory page
<https://svn.sdss.org/public/data/eboss/DR16cosmo/tags/v1_0_1/dataveccov/lya_forest/>.

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
  <index rev="27531" path="/eboss/DR16cosmo/tags/v1_0_1/dataveccov/lya_forest" base="data">
    <updir />
    <file name="README.txt" href="README.txt" />
    <file name="cf_LYA_in_LYA_LYA_in_LYB_z_0_10-exp.fits.gz" href="cf_LYA_in_LYA_LYA_in_LYB_z_0_10-exp.fits.gz" />
    <file name="cf_LYA_in_LYA_LYA_in_LYB_z_0_10.fits.gz" href="cf_LYA_in_LYA_LYA_in_LYB_z_0_10.fits.gz" />
    <file name="cf_z_0_10-exp.fits.gz" href="cf_z_0_10-exp.fits.gz" />
    <file name="cf_z_0_10.fits.gz" href="cf_z_0_10.fits.gz" />
    <file name="metal_dmat_LYA_in_LYA_LYA_in_LYB_z_0_10.fits" href="metal_dmat_LYA_in_LYA_LYA_in_LYB_z_0_10.fits" />
    <file name="metal_dmat_z_0_10.fits" href="metal_dmat_z_0_10.fits" />
    <file name="metal_xdmat_LYA_in_LYB_z_0_10.fits" href="metal_xdmat_LYA_in_LYB_z_0_10.fits" />
    <file name="metal_xdmat_z_0_10.fits" href="metal_xdmat_z_0_10.fits" />
    <file name="xcf_LYA_in_LYB_z_0_10-exp.fits.gz" href="xcf_LYA_in_LYB_z_0_10-exp.fits.gz" />
    <file name="xcf_LYA_in_LYB_z_0_10.fits.gz" href="xcf_LYA_in_LYB_z_0_10.fits.gz" />
    <file name="xcf_z_0_10-exp.fits.gz" href="xcf_z_0_10-exp.fits.gz" />
    <file name="xcf_z_0_10.fits.gz" href="xcf_z_0_10.fits.gz" />
  </index>
</svn>
