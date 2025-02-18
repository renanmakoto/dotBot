import pyqrcode
def generate_qr():
    data = input("Enter text or URL to generate QR Code: ")
    qr = pyqrcode.create(data)
    qr.png("qr.png", scale=8)
    print("QR Code successfully generated and saved as 'qr.png'.")
