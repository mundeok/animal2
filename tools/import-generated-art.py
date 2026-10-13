"""Slice GPT-generated atlases; no illustration is drawn by this script."""
from pathlib import Path
from PIL import Image
import shutil

root = Path(__file__).resolve().parents[1]
out = root / 'static' / 'garden-gpt-v1'

def cell(im,x,y):
    w,h=im.size
    return im.crop((round(x*w/4),round(y*h/4),round((x+1)*w/4),round((y+1)*h/4)))

im=Image.open(out/'tileset-source.png').convert('RGBA')
for y,kind in enumerate(['grass','flowers','path']):
    for x in range(4):
        cell(im,x,y).resize((64,64),Image.Resampling.NEAREST).save(out/f'{kind}-{x}.png')
for x,kind in enumerate(['bush','tree','hole','bed']):
    cell(im,x,3).resize((64,64),Image.Resampling.NEAREST).save(out/f'{kind}.png')

im=Image.open(out/'explorer-source.png').convert('RGBA')
sprites=[]
for y in range(4):
    for x in range(4):
        c=cell(im,x,y)
        bounds=c.getchannel('A').point(lambda a:255 if a>100 else 0).getbbox()
        sprites.append((y,x,c.crop(bounds)))
scale=72/max(c.height for _,_,c in sprites)
for y,x,c in sprites:
    c=c.resize((round(c.width*scale),round(c.height*scale)),Image.Resampling.NEAREST)
    canvas=Image.new('RGBA',(64,80))
    canvas.alpha_composite(c,((64-c.width)//2,78-c.height))
    canvas.save(out/f'explorer-{y}-{x}.png')

p=root/'index.html'
s=p.read_text(encoding='utf-8').replace('static/garden-v2/','static/garden-gpt-v1/').replace('.svg\')`','.png\')`')
s=s.replace("charDir = 1; p.style.transform = \"scaleX(-1)\"", "charDir = 2; p.style.transform = \"scaleX(1)\"")
s=s.replace('[0, 1, 3].forEach(dir', '[0, 1, 2, 3].forEach(dir')
s=s.replace('explorer-${dir}-${f}.svg','explorer-${dir}-${f}.png')
s=s.replace("if ([0, 1, 2, 3, 23].includes(t))", "if ([0, 1, 2, 3, 23].includes(t))")
s=s.replace("if (t === 3) d.classList.add('garden-tree');", "if (t === 3) d.style.backgroundImage = \"url('static/garden-gpt-v1/tree.png')\";")
s=s.replace("if (t === 23) d.classList.add('garden-hole');", "if (t === 23) d.style.backgroundImage = \"url('static/garden-gpt-v1/hole.png')\";")
s=s.replace("_fgTiles.push({cls: tileCls, x, y, emoji})", "_fgTiles.push({cls: tileCls, x, y, emoji, background: mapName === 'garden' ? d.style.backgroundImage : ''})")
s=s.replace('_fgTiles.forEach(({cls, x, y, emoji})', '_fgTiles.forEach(({cls, x, y, emoji, background})')
s=s.replace("if (emoji) d.innerText = emoji;\n                fg.appendChild(d);", "if (background) { d.style.backgroundImage = background; d.classList.add('garden-ground'); }\n                if (emoji) d.innerText = emoji;\n                fg.appendChild(d);")
# Remove obsolete SVG-specific decoration rules.
s='\n'.join(line for line in s.split('\n') if not any(k in line for k in ['.garden-tree {','.garden-hole {','.garden-hole::after']))
s=s.replace('height: calc(100% / 9 * 1.333333); margin-top: calc(-100% / 9 * .333333)', 'height: calc(100% / 9 * 1.25); margin-top: calc(-100% / 9 * .25)')
p.write_text(s,encoding='utf-8')

