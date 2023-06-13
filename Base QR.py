import qrcode

def generar_codigo_qr(texto):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    imagen_qr = qr.make_image(fill_color="black", back_color="white")
    imagen_qr.show()  # Mostrar la imagen del código QR generado

texto_usuario = input("Ingrese el texto o enlace para generar el código QR: ")
generar_codigo_qr(texto_usuario)

