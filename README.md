<!--
  ============================================================
  SAMPLE README — Panel 1 (gap-free strips + live Profile Views)
  ============================================================
  UPLOAD TO REPO ROOT:
    panel1_left.svg, strip_before_yt.svg, strip_youtube.svg,
    strip_email.svg, strip_profileviews.svg, strip_after_pv.svg

  GAP FIX: each strip is in its OWN table row with border-collapse:collapse and
  zero padding/line-height, and there is NO whitespace between tags inside a cell.
  That removes the inline-image whitespace that caused the white lines.

  PROFILE VIEWS: the strip shows the GameBoy "PROFILE VIEWS" label (value slot left
  open). The LIVE count is the komarev badge placed right after it in the same row
  (plum #803F64 to match). Its digits are the badge font (not GameBoy) — the
  accepted trade for a live number. Replace McVarHQ with your username.
-->

<table style="border-collapse:collapse;border-spacing:0" cellspacing="0" cellpadding="0" border="0">
<tr>
<td rowspan="5" valign="top" style="padding:0;line-height:0"><img src="./panel1_left.svg" alt="Hi! Have you met VAROON" height="329"></td>
<td valign="top" style="padding:0;line-height:0"><img src="./strip_before_yt.svg" width="279" alt=""></td>
</tr>
<tr><td valign="top" style="padding:0;line-height:0"><a href="https://youtube.com/@varoonsnook"><img src="./strip_youtube.svg" width="279" alt="YouTube: VAROONSNOOK"></a></td></tr>
<tr><td valign="top" style="padding:0;line-height:0"><a href="mailto:mcblcvr@gmail.com"><img src="./strip_email.svg" width="279" alt="Email: MCBLCVR"></a></td></tr>
<tr><td valign="middle" style="padding:0;line-height:0;position:relative"><a href="https://github.com/McVarHQ"><img src="./strip_profileviews.svg" width="279" alt="Profile Views"></a><a href="https://github.com/McVarHQ"><img src="https://komarev.com/ghpvc/?username=McVarHQ&style=flat-square&color=803F64&label=" alt="views" valign="middle"></a></td></tr>
<tr><td valign="top" style="padding:0;line-height:0"><img src="./strip_after_pv.svg" width="279" alt=""></td></tr>
</table>
