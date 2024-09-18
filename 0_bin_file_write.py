f = open("01.txt", 'wb')
text = [48, 97, 32, 13, 10, 65]
for s in text:
	# 4 is no of byte, big is big endian
	f.write(s.to_bytes(4, byteorder='big'))
f.close()
