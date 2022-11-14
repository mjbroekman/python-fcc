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
import PIL
from PIL import Image, ImageShow
from pyzbar.pyzbar import decode
import qrcode

def make_qrcode(qr_msg, qr_data:dict,img_args:dict):
    """Create the QR Code image

    Args:
        qr_msg (_type_): The message to encode
        qr_data (dict): dict of initialization keywords
        img_args (dict): dict of image keywords

    Returns:
        QRCode PILImage
    """
    try:
        code = qrcode.QRCode(**qr_data)
        code.add_data(qr_msg)
        code.make(fit=True)
        return code.make_image(**img_args)
    except (FileNotFoundError,PIL.UnidentifiedImageError,ValueError,TypeError) as e:
        print(str(e))
        raise TypeError(e)

def read_qrcode(filename:str) -> Image.Image:
    """Returns an Image object from the provided file

    Args:
        filename (str): File to open as an Image

    Returns:
        Image.Image: Image data
    """
    print(f'Reading {filename}')
    return Image.open(filename)

parser = argparse.ArgumentParser(description="A qrcode generator / decoder implemented in Python.")
parser.add_argument("--data","-d",action="store",help="Data to encode")
parser.add_argument("--file","-f",action="store",help="File to use (will be overwritten if --data is provided)")
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
img_file = args.file

if not args.data and img_file is not None:
    with read_qrcode(img_file) as qr_data:
        print(decode(qr_data,symbols=None))
else:
    qr_image = make_qrcode(args.data,qr_data,img_args)

    if qr_image is not None and img_file is not None:
        qr_image.save(img_file)
        print(f'Saved QR code as {img_file}')
        if args.show:
            ImageShow.show(qr_image)
