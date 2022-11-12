'''
A fun little QR Code generator and decoder

Inspired by:
   https://www.freecodecamp.org/news/python-projects-for-beginners/#qr-code-encoder-decoder-python-project

Skills:
  - 

Add-ons:
  - command-line arguments
  - functions
  - optionally show the QR code after creation

'''

import argparse
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

def make_qrcode(qr_msg, qr_data:dict,img_args:dict):
    try:
        code = qrcode.QRCode(**qr_data)
        code.add_data(qr_msg)
        code.make(fit=True)
        return code.make_image(**img_args)
    except Exception as e:
        print(str(e))
        return None

def read_qrcode(filename:str):
    print(f'Reading {filename}')
    return Image.open(filename)

parser = argparse.ArgumentParser(description="A qrcode generator / decoder implemented in Python.")
parser.add_argument("--data","-d",action="store",help="Data to encode")
parser.add_argument("--file","-f",action="store",help="File to use (will be overwritten if --data is provided, otherwise will be read)")
parser.add_argument("--fill_color","-c",action="store",help="Code color. Use the color name, e.g. black", default='black')
parser.add_argument("--back_color","-k",action="store",help="Background color. Use the color name, e.g. white", default='white')
parser.add_argument("--box_size","-x",action="store",type=int,help="Width of the corner boxes",default=10)
parser.add_argument("--border","-b",action="store",type=int,help="Border width in pixels",default=4)
parser.add_argument("--qr_version","-q",action="store",type=int,help="Size of the QRCode to build. 1 = 21x21 image",default=2)
parser.add_argument("--show","-s",action="store_true",help="Display the image after creating it")
args = parser.parse_args()

qr_image = None
qr_data = {
    "version":args.qr_version,
    "box_size":args.box_size,
    "border":args.border,
}
img_args = {
    "fill_color":args.fill_color,
    "back_color":args.back_color,
}

if not args.data and args.file is not None:
    with read_qrcode(args.file) as qr_data:
        print(decode(qr_data,symbols=None))
else:
    qr_image = make_qrcode(args.data,qr_data,img_args)

    if qr_image is not None and args.file is not None:
        qr_image.save(args.file)
        print('Saved QR code as {}'.format(args.file))
        if args.show:
            qr_image.show()
