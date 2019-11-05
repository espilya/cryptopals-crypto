#!/usr/bin/python3

hex = "Hello"

def tableEncode( sextets ):
    table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    #print(table[sextets])  
    return table[sextets]
        
    
def toBase64( str ):

    
    #convert it to chr from b64 table
    
    #convert to binary values
    strBinary = ''.join(format(ord(i), 'b') for i in str) 
    print(strBinary)
    
    #read (every 6 bit)*4 if empty add padding
    b64 = ""
    i = 0
    for bit in strBinary:
        temp6Bits = ""
        if(int(i)%6==0): 
            print(bit)  
            b64.join(tableEncode(int(bit, 2)))
            temp6Bits = ""
        temp6Bits.join(bit)
        i += 1

        
            
    
    
    
    
toBase64(hex)

