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
    file_name = input("What would you like to name your QRCode file as: " )
    img.save(file_name + ".png")
    print("Your new QRCode has been created.")
#Run the function

url = input("Enter your url: ")
generate_qrcode(url)