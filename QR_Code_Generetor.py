import qrcode


# One way to generate QR Code :

"""
generate_image = qrcode.make("Your Desire data.")

generate_image.save('Your folder where you want to save the image. It must be in PNG format.')

"""

# Second way to generate QR Code :


features = qrcode.QRCode(version = 1, box_size = 40,border = 3)
features.add_data = ('Your Desire data.')
features.make(fit = True)
generate_image = features.make_image(fill_color = "green", back_color = "white")
generate_image.save('Your folder where you want to save the image. It must be in PNG format.')
