#!/usr/bin/python3

from binascii import hexlify, unhexlify


print("--input:")
a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


#33 122
bIndex = 0.0
out = ""
print("char:    Decoded:")
for i in range(48, 122):
    char = format(ord(chr(i)), "x")
    #print(char)
    b = ""
    for j in range(int(len(a)/2)):
        b += char
    out = hex(int(a, 16) ^ int(b, 16))
    #print(out) 
    out = out.replace("0x", "")    
    #print(bytes.fromhex(out))
    print("0x", end="") 
    print(char, end="")
    print(":-> ", end="")
    print(unhexlify(out.replace(' ', '').replace('\n', '')))
print("\nResolution is XOR with value '0x78'\n")
#output = "Index: " + repr(bIndex) + " Phrase: " + out
#print(output)
