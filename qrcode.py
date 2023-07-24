import qrcode

qr = qrcode.QRcode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECTION_L,
                   box_size = 10,
                   border = 4,
                   )
qr.add_data("https://www.youtube.com/watch?v=XasK8e1rUlE")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color ="white")
img.save("advance.png")
img.show()