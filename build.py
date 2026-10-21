import base64,json,os
here=os.path.dirname(os.path.abspath(__file__))
names=['gcard','gring','gengr','kit1','kit2','kit3','kit4','kit5','p1','p2','p3','khero','app']
img={n:'data:image/jpeg;base64,'+base64.b64encode(open(f'{here}/assets/{n}.jpg','rb').read()).decode() for n in names}
src=open(f'{here}/src.html').read().replace('__IMG__',json.dumps(img))
import re
def svg(m):
    d=open(f"{here}/assets/svg/{m.group(1)}.svg",'rb').read()
    return 'data:image/svg+xml;base64,'+base64.b64encode(d).decode()
src=re.sub(r'__SVG:([a-z-]+)__',svg,src)
src=re.sub(r'__JPG:([a-z0-9-]+)__',lambda m:'data:image/jpeg;base64,'+base64.b64encode(open(f'{here}/assets/{m.group(1)}.jpg','rb').read()).decode(),src)
src=re.sub(r'__PNG:([a-z0-9-]+)__',lambda m:'data:image/png;base64,'+base64.b64encode(open(f'{here}/assets/{m.group(1)}.png','rb').read()).decode(),src)
src=re.sub(r'__WEBP:([a-z0-9-]+)__',lambda m:'data:image/webp;base64,'+base64.b64encode(open(f'{here}/assets/{m.group(1)}.webp','rb').read()).decode(),src)
src=re.sub(r'__INLINE:([a-z-]+)__',lambda m:open(f'{here}/assets/svg/{m.group(1)}.svg').read(),src)
open(f'{here}/artifact.html','w').write(src)
doc='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'+src+'</body></html>'
open(f'{here}/index.html','w').write(doc)
print(len(src)//1024,'KB')
