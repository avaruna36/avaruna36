<!--
  ============================================================
  SAMPLE README — Panel 1 (split: animated tile + clickable chips)
  ============================================================
  UPLOAD THESE FILES TO THE REPO ROOT (same folder as README.md):
    panel1_left.svg          (animated console: title, code, VAROON)
    tile_youtube.svg         (clickable YouTube chip)
    tile_email.svg           (clickable Email chip)
    tile_profileviews.svg    (clickable Profile Views chip — static "35";
                              live count is the badge variant noted below)

  HOW THE SPLIT WORKS / WHY:
  - GitHub renders SVGs via <img>: SMIL animation RUNS, but links INSIDE an SVG
    do NOT. So the panel is split into tiles laid out by an HTML <table>:
      * LEFT cell  = panel1_left.svg (the animation). Not clickable (no links needed).
      * RIGHT cells = the three chips, each its own <img> wrapped in <a> -> clickable.
  - The seam between left tile and chip column falls in the empty cyan gap after
    VAROON, so it should be invisible. If your browser/zoom shows a hairline gap,
    that's GitHub's responsive image scaling; see the SINGLE-IMAGE fallback at the
    bottom (one complete panel, animation + chips, but chips not clickable).

  PROFILE VIEWS LIVE COUNT:
  - tile_profileviews.svg shows a static "35" in GameBoy font (matches design).
  - For a LIVE count, swap that chip's <img> for the komarev badge (commented in).
    Its digits are the service's font, not GameBoy — unavoidable for a live number.
-->

<!-- ===== PANEL 1: HEADER (split tiles) ===== -->
<table cellspacing="0" cellpadding="0" border="0"><tr>
  <td valign="top" rowspan="3"><img src="./panel1_left.svg" alt="Hi! Have you met VAROON" height="329"></td>
  <td valign="top"><a href="https://youtube.com/@varoonsnook"><img src="./tile_youtube.svg" alt="YouTube: VAROONSNOOK"></a></td>
</tr>
<tr>
  <td valign="top"><a href="mailto:mcblcvr@gmail.com"><img src="./tile_email.svg" alt="Email: MCBLCVR"></a></td>
</tr>
<tr>
  <td valign="top"><a href="https://github.com/McVarHQ"><img src="./tile_profileviews.svg" alt="Profile Views"></a></td>
  <!-- LIVE count alternative (digits in service font, not GameBoy):
  <td valign="top"><a href="https://github.com/McVarHQ"><img src="https://komarev.com/ghpvc/?username=McVarHQ&style=flat-square&color=803F64&label=PROFILE+VIEWS"></a></td>
  -->
</tr></table>

<br>

<!--
  ===== SINGLE-IMAGE FALLBACK (if the split shows gaps) =====
  One complete panel SVG (animation + chips drawn inside). Looks perfectly
  seamless, but the chips are NOT clickable. Uncomment to use instead:

  <p><img src="./panel1_anim.svg" alt="Hi! Have you met VAROON" width="880"></p>
-->
