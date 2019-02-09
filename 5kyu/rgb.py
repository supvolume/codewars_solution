""" solution for RGB To Hex Conversion challenge
convert 0-255 to hexadecimal code
the number that exceed 255 will be rounded"""

def rgb(r, g, b):
    hexColor=''
    for c in (r, g, b):
        if c >255:
            c=255
        elif c<0:
            c=0
        hexC = str(hex(c)).upper()
        if len(hexC) <4:
            twoNum = '0'+hexC[2]
        else:
            twoNum = hexC[2:]
        hexColor=''.join([hexColor,twoNum])
    return hexColor