from PIL import Image, ImageColor

f = "test.png"

def rgb2hex(r, g, b): # vals => str
    return '{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(h):
    return ImageColor.getcolor(h, "RGB")

def hex2asc(h): # str => str
    return "".join([str(ord(x)).zfill(3) for x in h])

def segm(arr, n):
    return [arr[x:x+n] for x in range(0, len(arr), n)]

def flt(arr):
    return [y for x in arr for y in x] # [[()]] => [()]

def encode(n, log=False):
    with Image.open(n) as img:
        img.load()
    w, h = img.size
    rgbdat = list(img.getdata())
    hexdat = [rgb2hex(*i) for i in rgbdat]
    ascdat = [hex2asc(j) for j in hexdat]
    pix = segm(ascdat, w)
    jpix = ["".join(y) for y in pix]
    jjpix = "-".join(jpix)
    if log:
        print(rgbdat)
        print(hexdat)
        print(ascdat)
        print(pix)
        print(jpix)
        print(jjpix)
    return jjpix

def decode(s, log=False):
    grid = s.split("-")
    ascstr = [segm(row, 18) for row in grid]
    asclst = [[segm(pixel, 3) for pixel in row] for row in ascstr]
    hexlst = [[[chr(int(val)) for val in pixel] for pixel in row] for row in asclst]
    jhex =  [[hex2rgb("#"+"".join(pixel)) for pixel in row] for row in hexlst]
    rgb = flt(jhex)
    w = len(jhex[0])
    h = len(jhex)
    if log:
        print(grid)
        print(ascstr)
        print(asclst)
        print(hexlst)
        print(jhex)
        print(rgb)
        print(len(jhex[0]), len(jhex))
    im = Image.new("RGB", [w, h])
    im.putdata(rgb)
    im.save("decoded.png")

enc = encode(f, True)
print()
dec = decode(enc, True)