import qrcode
print("\t\t\tWelcome to Shadman's QR Code generator \n\n")

link = input("Enter the Link for QR code: ")
print("\n")

print("\tNext enter the QR code Box size's info~")
print("\n")
print("\tfor-example & reccomendation: version = 1 & box_size = 40 & border = 3")
print("\n")

version = input("Enter the Version: ")
print("\n")
box_size = input("Enter the box_size: ")
print("\n")
border = input("Enter the border: ")
print("\n")

features = qrcode.QRCode(version=version,box_size=box_size,border=border)


features.add_data(link)
features.make(fit=True)

fill_color = input("Fill front color for the QR Code (ex: 'black'): ")
print("\n")
back_color = input("Fill the background color for the QR code (eg: 'white'): ")
print("\n")

generate_image = features.make_image(fill_color=fill_color,back_color=back_color)

filename = input("Enter the filename to save the QR code (eg: 'ShadsLinkedInQr.png'): \n")
print("\n")
generate_image.save(filename)