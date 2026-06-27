<!--
  ============================================================
  SAMPLE README — Panel 1 (left animation + 5 stacked right strips)
  ============================================================
  UPLOAD THESE FILES TO THE REPO ROOT (same folder as README.md):
    panel1_left.svg            (animated console: title, code, VAROON)
    strip_before_yt.svg        (top frame + cyan above YouTube)      -- not clickable
    strip_youtube.svg          (YouTube chip row)                    -- clickable
    strip_email.svg            (Email chip row)                      -- clickable
    strip_profileviews.svg     (Profile Views chip row)              -- clickable
    strip_after_pv.svg         (cyan + bottom frame below Profile)   -- not clickable

  HOW IT WORKS:
  - The panel is split into a LEFT animation tile + a RIGHT half that is sliced
    into 5 full-width horizontal strips, stacked in ONE table cell. Each strip
    carries its own slice of cyan + bezel, so the panel reassembles seamlessly.
  - The 3 chip strips are each wrapped in <a> -> clickable. The before/after
    strips are clickable regions too (they just point at the profile / are inert);
    that's fine per your spec -- only the whole panel must NOT be one big link.
  - The cut lines fall in the cyan gaps between chips, so nothing is split.

  PROFILE VIEWS LIVE COUNT:
  - strip_profileviews.svg shows a static "35" in GameBoy font (matches design).
  - To make the count LIVE, that strip would need to embed a remote badge, which
    forces a non-GameBoy digit font. Kept static-GameBoy here; ask if you want the
    live-badge variant for this strip.
-->

<!-- ===== PANEL 1: HEADER (left tile + 5 stacked right strips) ===== -->
<table cellspacing="0" cellpadding="0" border="0"><tr>

  <!-- LEFT: the animation -->
  <td valign="top"><img src="./panel1_left.svg" alt="Hi! Have you met VAROON" height="329"></td>

  <!-- RIGHT: 5 full-width strips stacked in one cell -->
  <td valign="top">
    <img src="./strip_before_yt.svg" alt="" width="279"><br>
    <a href="https://youtube.com/@varoonsnook"><img src="./strip_youtube.svg" alt="YouTube: VAROONSNOOK" width="279"></a><br>
    <a href="mailto:mcblcvr@gmail.com"><img src="./strip_email.svg" alt="Email: MCBLCVR" width="279"></a><br>
    <a href="https://github.com/McVarHQ"><img src="./strip_profileviews.svg" alt="Profile Views" width="279"></a><br>
    <img src="./strip_after_pv.svg" alt="" width="279">
  </td>

</tr></table>
