import qrcode

data = input("enter a link:").strip()
file= input("enter file name:").strip()

qr = qrcode.QRCode()
qr.add_data(data)

img = qr.make_image()

img.save(file)
print("file created!")