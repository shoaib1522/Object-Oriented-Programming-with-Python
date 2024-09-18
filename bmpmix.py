import struct

def half_image(f):
    f = open(f,"rb+")
    f.seek(18)
    w = "%s" % struct.unpack("i", f.read(4))
    h = "%s" % struct.unpack("i", f.read(4))
    f.seek(28)
    d = "%s" % struct.unpack("H", f.read(2))
    print("width=",w)
    print("height=",h)
    print("bits per pixel=",d)
    
    f.seek(54)
    a = [[[0,0,0] for i in range(int(w))] for j in range(int(h))]
    lc = int(w)*3  # count of bytes read on one scan line
    brl = lc % 4  # bytes peddings on scan line
    for i in range(int(h)-1,-1,-1):
        for j in range(int(w)):
            a[i][j][0] = int.from_bytes(f.read(1), byteorder ='big')  #"%s" % struct.unpack("b",f.read(1))
            a[i][j][1] = int.from_bytes(f.read(1), byteorder ='big')  #"%s" % struct.unpack("b",f.read(1))
            a[i][j][2] = int.from_bytes(f.read(1), byteorder ='big')  #"%s" % struct.unpack("b",f.read(1))
            lc += 3
        f.read(brl)
    
    f.seek(54)
    for i in range(int(h)-1,-1,-1):
        for j in range(int(w)//2):
            b = 255 - int(a[i][j][0])
            f.write(b.to_bytes(1, byteorder ='big'))
            b = 255 - int(a[i][j][1])
            f.write(b.to_bytes(1, byteorder ='big'))
            b = 255 - int(a[i][j][2])
            f.write(b.to_bytes(1, byteorder ='big'))
        for j in range(int(w)//2, int(w)):
            b = int(a[i][j][0])
            f.write(b.to_bytes(1, byteorder ='big'))
            b = int(a[i][j][1])
            f.write(b.to_bytes(1, byteorder ='big'))
            b = int(a[i][j][2])
            f.write(b.to_bytes(1, byteorder ='big'))
            #f.write(str(b).encode())
        f.write(int(0).to_bytes(brl, byteorder ='big'))
    
    f.close()

def main():
    file = input("Input the bmp file name with extension (.bmp): ")
    half_image(file)

main()
