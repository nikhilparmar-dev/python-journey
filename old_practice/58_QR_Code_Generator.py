
import qrcode

text = input("Enter Some text that you wanted to make qr code: ")

qr = qrcode.make(text)

qr.save("generatedqr.png")

print("Qr code generated successfully")