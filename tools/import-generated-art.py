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
