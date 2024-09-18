# # i = 16

# # # Create one byte from the integer 16
# # single_byte = i.to_bytes(1, byteorder='big', signed=True) 
# # print(single_byte)

# # # Create four bytes from the integer
# # four_bytes = i.to_bytes(4, byteorder='big', signed=True)
# # print(four_bytes)

# # # Compare the difference to little endian
# # print(i.to_bytes(4, byteorder='little', signed=True))

# # Create bytes from a list of integers with values from 0-255
# bytes_from_list = bytes([255, 254, 253, 252])
# print(bytes_from_list)

# # # Create a byte from a base 2 integer
# # one_byte = int('11110000', 2)
# # print(one_byte)

# # # Print out binary string (e.g. 0b010010)
# # print(bin(22))

# # Create an int from bytes. Default is unsigned.
# # some_bytes = b'\x00\xF0'
# # i = int.from_bytes(some_bytes, byteorder='big')
# # print(i)

# # # Create a signed int
# # i = int.from_bytes(b'\x00\x0F', byteorder='big', signed=True)
# # print(i)

# # Use a list of integers 0-255 as a source of byte values
# i = int.from_bytes([255, 0, 0, 0], byteorder='big')
# print(i)



import struct
var = struct.pack('hhl',1,2,3)
print(var)
var = struct.pack('iii',1,2,3)
print(var)