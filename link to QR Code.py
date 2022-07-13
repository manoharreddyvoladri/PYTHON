#pip install pyqrcode
#pip install pypng
import pyqrcode
from pyqrcode import QRCode
s=str(input("please paste the link below"))
#Genrates QR code
url = pyqrcode.create(s)
#creates and save the svg file as "myqr.svg"
url.svg("myqr.svg", scale =8)
#create and save the png file namingmyqr,png
url.png("myqr.png", scale = 6)
print("you can the QR code in the downloads ")
