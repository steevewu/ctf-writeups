from PIL import Image
from os import path

dir = path.dirname(__file__)


output = Image.open(dir + '/output.png')
flag = output.copy()
width, height = output.size
pos = lambda x, y: ((2134266 + x * 727) % width, (4501511 + y * 727) % height)


key = output.getpixel(pos(0, 0))
key = [x ^ y for x, y in zip(key, [0xff, 0xff, 0xff])]


for i in range(width):
    for j in range(height):
        pixel = output.getpixel(pos(i, j))
        pixel = tuple(x ^ y for x, y in zip(pixel, key))
        flag.putpixel((i, j), pixel)

flag.save(dir + '/flag.png')