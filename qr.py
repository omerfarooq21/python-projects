import qrcode
from PIL import Image
img=qrcode.make("https://www.youtube.com/channel/UCDKJBKCFev77OmafQrndueg")
img.save("omerchannel.jpg")
