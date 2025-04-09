#Install the needed libraries
import qrcode
import qrcode.constants
#Create a function that collects text and converts to a qrcode
def generate_qrcode(text):
    qr = qrcode.QRCode(
        version= 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    #Save the qrcode as an image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")
#Run the function

generate_qrcode("https://pypi.org/project/qrcode/")