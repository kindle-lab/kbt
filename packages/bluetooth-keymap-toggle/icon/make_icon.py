"""Draw the library cover for the Bluetooth + Key Mapping scriptlet.

Usage: python3 make_icon.py icon.png
Requires Pillow and macOS Arial Bold. Output: 520x804 grayscale PNG
(2x the 260x402 cover size Kindle generates for scriptlets).
"""
from PIL import Image, ImageDraw, ImageFont
import sys
W,H=520,804; K=4
img=Image.new("L",(W*K,H*K),255); d=ImageDraw.Draw(img)
s=lambda v:int(v*K)
F="/System/Library/Fonts/Supplemental/Arial Bold.ttf"
# frame
d.rectangle([s(12),s(12),s(W-12),s(H-12)],outline=0,width=s(10))
# bluetooth badge
cx,cy,r=260,235,112
d.ellipse([s(cx-r),s(cy-r),s(cx+r),s(cy+r)],fill=0)
h,w=72,38
P=lambda x,y:(s(cx+x),s(cy+y))
path=[P(-w,-h/2),P(w,h/2),P(0,h),P(0,-h),P(w,-h/2),P(-w,h/2)]
d.line(path,fill=255,width=s(15),joint="curve")
for p in (path[0],path[-1]): d.ellipse([p[0]-s(7.5),p[1]-s(7.5),p[0]+s(7.5),p[1]+s(7.5)],fill=255)
# keyboard
kx0,ky0,kx1,ky1=84,395,436,548
d.rounded_rectangle([s(kx0),s(ky0),s(kx1),s(ky1)],radius=s(20),outline=0,width=s(9))
gap=7; kw=26; kh=24
rows=[(10,0),(9,0),(8,0)]
y=ky0+22
for n,off in rows:
    tot=n*kw+(n-1)*gap; x=(W-tot)/2
    for i in range(n):
        d.rounded_rectangle([s(x),s(y),s(x+kw),s(y+kh)],radius=s(5),fill=0)
        x+=kw+gap
    y+=kh+gap-4
# space bar
sw=180; d.rounded_rectangle([s((W-sw)/2),s(y+2),s((W+sw)/2),s(y+2+kh-4)],radius=s(5),fill=0)
# dotted link between badge and keyboard
for yy in (362,377):
    d.ellipse([s(260-4),s(yy-4),s(260+4),s(yy+4)],fill=0)
# text
def ctext(t,y,size,fill=0):
    f=ImageFont.truetype(F,s(size)); b=d.textbbox((0,0),t,font=f)
    d.text((s(W/2)-(b[2]-b[0])/2-b[0],s(y)),t,font=f,fill=fill)
ctext("BLUETOOTH",585,58)
ctext("KEY MAPPING",655,48)
ctext("Kindle",728,30,fill=90)
img=img.resize((W,H),Image.LANCZOS)
img.save(sys.argv[1],optimize=True)
if len(sys.argv)>2:
    img.resize((260,402),Image.LANCZOS).save(sys.argv[2],optimize=True)
