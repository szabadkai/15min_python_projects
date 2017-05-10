from flask import Flask
from PIL import Image

im = Image.open('a49aea40-27e9-43d8-bbde-19c4af035b60.jpg')
width, height = im.size
SCALE = " .:-=+*#%@"
BIGSCALE = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
MAX_INTENSITY = 3 * 255


def translate_pix(intensity, scale=SCALE):
    i = int(intensity * (len(scale) - 1))
    return scale[i]


macs = "<body bgcolor=black style='font-family:monospace; color:white; font-weight:700'>"
for y in range(0, height, 7):
    for x in range(0, width, 4):
        i = im.getpixel((x, y))
        intensity = sum(i) / MAX_INTENSITY
        macs += translate_pix(intensity)
    macs += "<br>"
macs += "</body>"
app = Flask(__name__)


@app.route('/')
def hello():
    return macs
