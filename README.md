<!--
  ============================================================
  SAMPLE README — Panel 1 (animated header) test
  ============================================================
  HOW TO TEST THIS ON GITHUB
  1. Create a repo named EXACTLY your username (e.g. McVarHQ/McVarHQ)
     -> a repo whose name == your username renders its README on your profile.
     (Any test repo also works; the profile-view counter just needs a stable repo.)
  2. Upload BOTH files to the repo root:
       - README.md            (this file)
       - panel1_anim.svg      (the animated header panel)
  3. Open the repo on GitHub. The SVG animation plays in the rendered README
     (GitHub runs SMIL inside <img>). The links below the panel are clickable.

  NOTES / KNOWN GITHUB CONSTRAINTS (so nothing surprises you):
  - GitHub renders the SVG via <img>, which is sandboxed: SMIL animation RUNS,
    but links INSIDE the SVG do NOT work. That is why the clickable links live
    in the README body, directly under the panel (handoff decision B5).
  - One image can carry only one wrapping link on GitHub, so the three targets
    (YouTube / Email / Profile Views) are real markdown links in a row beneath
    the panel rather than per-chip hotspots on the image.
  - Profile Views is a LIVE counter (komarev). Its digits are in the counter
    service's font, not Early-GameBoy — that is unavoidable for a live count.
    The "PROFILE VIEWS" chip drawn inside the panel is the GameBoy-styled label;
    the live number is the badge in the link row.
-->

<!-- ===================== PANEL 1: HEADER ===================== -->

<p align="center">
  <img src="./panel1_anim.svg" alt="Hi! Have you met VAROON" width="880">
</p>

<!-- Clickable links for the chips shown in the panel above -->
<p align="center">
  <a href="https://youtube.com/@varoonsnook">
    <img alt="YouTube" src="https://img.shields.io/badge/YOUTUBE-VAROONSNOOK-D31E25?style=flat-square&labelColor=2A0608">
  </a>
  &nbsp;
  <a href="mailto:mcblcvr@gmail.com">
    <img alt="Email" src="https://img.shields.io/badge/EMAIL-MCBLCVR-D7A32E?style=flat-square&labelColor=2A2008">
  </a>
  &nbsp;
  <a href="https://github.com/McVarHQ">
    <img alt="Profile Views" src="https://komarev.com/ghpvc/?username=McVarHQ&style=flat-square&color=803F64&label=PROFILE+VIEWS">
  </a>
</p>
