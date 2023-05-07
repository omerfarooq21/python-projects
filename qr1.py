import qrcode
from PIL import Image
  
qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=4,) 
a = input("enter the input for qrcode")
qr.add_data(a) 
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="lightblue")
b= input("enter the name")
img.save(b)
