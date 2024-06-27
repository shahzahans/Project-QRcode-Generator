import qrcode #library that I used according to geeksforgeeks.org
print("\t\t\tWelcome to Shadman's QR Code generator \n\n")

link = input("Enter the Link for QR code: ") #inserts the Link
print("\n")

print("\tNext enter the QR code Box size's info~")
print("\n")
print("\tfor-example & reccomendation: version = 1 & box_size = 40 & border = 3") #Recomendation
print("\n")

version = input("Enter the Version: ") #inserts the version
print("\n")
box_size = input("Enter the box_size: ") #inserts the box_size
print("\n")
border = input("Enter the border: ") #inserts the border
print("\n")

features = qrcode.QRCode(version=version,box_size=box_size,border=border) #Calls the size function


features.add_data(link) #Calls the link function
features.make(fit=True) #Fits the QR code with the proper size

fill_color = input("Fill front color for the QR Code (ex: 'black'): ") #inserts the front color
print("\n")
back_color = input("Fill the background color for the QR code (eg: 'white'): ") #inserts the background color
print("\n")

generate_image = features.make_image(fill_color=fill_color,back_color=back_color) #calls the color function

filename = input("Enter the filename to save the QR code (eg: 'ShadsLinkedInQr.png'): \n")
print("\n")
generate_image.save(filename) #generate the file
