#Install the needed libraries
import qrcode
#Create a function that collects text and converts to a qrcode
def generate_qrcode(text):
    qr = qrcode.QRCode(
        version= 1,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)

#Save the qrcode as an image
#Run the function