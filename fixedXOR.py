#!/usr/bin/python3

from binascii import hexlify, unhexlify


print("--input:")
input1 = "1c0111001f010100061a024b53535009181c"
input2 = "686974207468652062756c6c277320657965"
print(input1)
print(input2)
print("")

bytes1, bytes2 = unhexlify(input1), unhexlify(input2)

print("--binary:")
print(bytes1)
print(bytes2)
print("")

print("--result:")
result = hex(int(input1, 16) ^ int(input2, 16))[2:]
print(result)
print(unhexlify(result))
