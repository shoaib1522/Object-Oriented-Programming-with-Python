'''
Given Lab03t.pgm is Text PGM file, has a text header
as described below and rest of the part is sequences
of bytes as binary for the shade of gray of specific pixel

Header
	P5 as first two character followed by a newline
	then two integers width and height of image in pixels
				separated by a space followed by a newline
	then the total number of shades of gray followed by a newline
	and lastly the data in binary form of length width X height
'''

class BinaryPGM:
	pass

def ReadBinaryPGM(pgmFileName):

	img = BinaryPGM()

	f = open(pgmFileName, "rb")

	img.header = f.readline().rstrip()
	img.width, img.height = f.readline().decode().rstrip().split(" ")
	img.shades = f.readline().rstrip()

	img.width = int(img.width)
	img.height = int(img.height)
	img.shades = int(img.shades)

	bytes = f.read()

	f.close()

	img.data = []
	for byte in bytes:
		img.data.append(byte)

	return img

def WriteBinaryPGM(newpgmFileName, img):

	f = open(newpgmFileName, "wb")

	f.write(img.header)
	f.write("\n".encode())
	f.write(str(img.width).encode())
	f.write(" ".encode())
	f.write(str(img.height).encode())
	f.write("\n".encode())
	f.write(str(img.shades).encode())
	f.write("\n".encode())

	line = 0
	for num in img.data:
		f.write(num.to_bytes(1, byteorder='big', signed=False))

	f.close()

def main():

	img = ReadBinaryPGM("Lab03b1.pgm")

	print("Image properties")
	print(img.header)
	print(img.width)
	print(img.height)
	print(img.shades)
	print(len(img.data))
	print(img.width*img.height)

	newImg = img
	for i in range(img.width*img.height):

		newImg.data[i] = int((img.data[i]-100) / 100 * 255)
		if newImg.data[i] < 0:
			newImg.data[i] = 0
		if newImg.data[i] > 255:
			newImg.data[i] = 255
	

	WriteBinaryPGM("Lab03b2.pgm", img)

	return

main()
