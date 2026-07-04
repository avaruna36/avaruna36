#!/usr/bin/env python3
"""
divider.svg (v2) — NOT a panel. A single row of small static multicolored
dashes; one slightly taller/wider bar (the "cursor") slides across them,
bouncing wall to wall. No bevel, no frame.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import palette as P

COLORS=[P.PALETTE["curry_gold"], P.PALETTE["fireball_red"],
        P.PALETTE["aqueduct_cyan"], P.PALETTE["classic_green"],
        P.PALETTE["ipa_D1C02B"], P.PLUM_LIGHT, P.PALETTE["blackberry"]]
CURSOR=P.PLUM_LIGHT

ML=30; MR=22; OFF=9; PW=865; CW=ML+PW+OFF+MR   # 926 canvas, matches panels
DASH_W=14; DASH_H=6; GAP=8; PITCH=DASH_W+GAP
CH=20; CY=CH/2

def px(v): return f"{v:.1f}"

def build():
    x0=ML; x1=ML+PW; span=x1-x0
    n=int((span+GAP)//PITCH)
    x0=ML+(span-(n*PITCH-GAP))/2
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CW} {CH}" width="{CW}" height="{CH}">']
    dash_y=CY-DASH_H/2
    for i in range(n):
        c=COLORS[i%len(COLORS)]
        x=x0+i*PITCH
        s.append(f'<rect x="{px(x)}" y="{px(dash_y)}" width="{DASH_W}" height="{DASH_H}" rx="1" fill="{c}"/>')
    cw=DASH_W+6; ch=DASH_H+8
    left=x0-2; right=x0+(n-1)*PITCH+DASH_W-cw+2
    s.append(
      f'<rect x="{px(left)}" y="{px(CY-ch/2)}" width="{cw}" height="{ch}" rx="1.5" fill="{CURSOR}">'
      f'<animate attributeName="x" values="{px(left)};{px(right)};{px(left)}" '
      f'keyTimes="0;0.5;1" dur="3.2s" calcMode="spline" '
      f'keySplines="0.45 0 0.55 1;0.45 0 0.55 1" repeatCount="indefinite"/>'
      f'</rect>')
    s.append('</svg>')
    return ''.join(s)

def main():
    out=os.environ.get("OUT","divider.svg")
    open(out,'w').write(build())
    print(f"wrote {out} {CW}x{CH}")

if __name__=="__main__":
    main()
