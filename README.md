<!--
  SAMPLE README — Panel 1. Upload to repo root:
    panel1_left.svg, strip_before_yt.svg, strip_youtube.svg, strip_email.svg
    (and panel1_anim.svg only if you use the FALLBACK at the bottom)

  Profile Views removed. Chips: YouTube (top), Email (bottom).
  Two cells: [left animation] | [right column of 3 stacked strips].
  Strips use display:block + no whitespace between tags to kill inline gaps.
-->

<!-- ============ PRIMARY: clickable chips ============ -->
<table cellspacing="0" cellpadding="0" border="0"><tr>
<td valign="top"><img src="./panel1_left.svg" alt="Hi! Have you met VAROON" height="329" style="display:block"></td><td valign="top"><img src="./strip_before_yt.svg" width="279" alt="" style="display:block"><a href="https://youtube.com/@varoonsnook" style="display:block;line-height:0"><img src="./strip_youtube.svg" width="279" alt="YouTube: VAROONSNOOK" style="display:block"></a><a href="mailto:mcblcvr@gmail.com" style="display:block;line-height:0"><img src="./strip_email.svg" width="279" alt="Email: MCBLCVR" style="display:block"></a></td>
</tr></table>

<!-- ============ FALLBACK (if the strips still show gaps) ============
     One complete panel SVG: perfectly seamless, animation + both chips drawn in,
     but chips are NOT clickable. Delete the table above and uncomment this:

<p><img src="./panel1_anim.svg" alt="Hi! Have you met VAROON" width="880"></p>
-->
