#!/usr/bin/python3
import binascii


def tableEncode(sextets):
    # print("toTableEnconde: " + str(sextets))
    table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    return table[sextets]


def hexToBase64(toB64):
    # convert it to chr from b64 table

    # hex to binary

    hex2bin = {
        '0': '0000', '1': '0001', '2': '0010',
        '3': '0011', '4': '0100', '5': '0101',
        '6': '0110', '7': '0111', '8': '1000',
        '9': '1001', 'a': '1010', 'b': '1011',
        'c': '1100', 'd': '1101', 'e': '1110',
        'f': '1111'}
    strBinary = ""
    for i in toB64:
        strBinary += hex2bin[i]
    print("binary:......" + strBinary)

    # this should produce "TWE="
    # strBinary = "0100110101100001"

    # read (every 6 bit)*4 if empty add padding
    b64 = ""
    i = 1
    temp6Bits = ''
    for bit in strBinary:
        temp6Bits += bit
        if int(i) % 6 == 0:
            b64 += tableEncode(int(temp6Bits, 2))
            # print("temp6Bits: " + temp6Bits)
            temp6Bits = ""
        i += 1
    # print(temp6Bits)
    if len(temp6Bits) == 4:
        b64 += tableEncode(int((temp6Bits + '00'), 2))
        b64 += '='
    elif len(temp6Bits) == 2:
        b64 += tableEncode(int((temp6Bits + '0000'), 2))
        b64 += '=='
    return b64


hexadecimal = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print("hexadecimal:." + str(hexadecimal))
base64 = hexToBase64(hexadecimal.lower())
print("base64:......" + str(base64))
