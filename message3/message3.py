clef = 'AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M'

message = 'AFXFFG XADXGFV GDFDVVVVDAFX-FVDXXFAGFAGVF XGDDGAXXADFDV GFGVVDXDVFGXF FX VD GGGDVVXG GV VVGGGGV GAAF GVVXAVGFGG XDDFAVAF.AGGVXDG F VGVXVGGD VFXXFXAXDFAGGDAVG VGGG VVAXDGAGVVAGXAGFGXADGDVG:GXFXVFXDVFXDGGVGXDFG GGF V X VVGGGGD XVAGVAVVGDFFGGXGVAG!DAGFX AFDAGFFFVAAAGGAGXVFFG!FX G DGDAG 4XDG'

cle = 'CRYPTO'

cleeeee = len(message) // len(clef)
print (len(message) // len(cle))


c = message[:48]
o = message[48:96]
p = message[96:144]
r = message[144:192]
t = message[192:240]
y = message[240:288]

c = message[:48]
r = message[144:192]


print('c:', c)
print('o:', o)
print('p:', p)
print('r:', r)
print('t:', t)
print('y:', y)

print("")
print("ohhohhoa")
print("")

print('c:', c)
print('r:', r)
print('y:', y)
print('p:', p)
print('t:', t)
print('o:', o)

def decrypt(message, clef, cle):
    hauteur = len(message) // len(cle)

    return hauteur

    
print(decrypt(message, clef, cle))



