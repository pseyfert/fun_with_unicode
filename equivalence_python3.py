import unicodedata

uone = chr(0x00c5) #Å = LATIN CAPITAL LETTER A WITH RING ABOVE

utoo = chr(0x212b) #Å = ANGSTROM SIGN

print(uone, "\t", unicodedata.name(uone))
print(utoo, "\t", unicodedata.name(utoo))

print("are these the same?", uone==utoo)
print("are these canonically equivalent?", unicodedata.normalize('NFD',uone)==unicodedata.normalize('NFD',utoo))

uone = chr(0xfb00) # ﬀ
utoo = chr(0x0066)+chr(0x0066) # ff


print(uone, "\t", unicodedata.name(uone))
print(utoo, "\t", unicodedata.name(utoo[0]), " twice")
print("are these the same?", uone==utoo)
print("are these canonically equivalent?", unicodedata.normalize('NFD',uone)==unicodedata.normalize('NFD',utoo))
print("are these compatible equivalent?", unicodedata.normalize('NFKD',uone)==unicodedata.normalize('NFKD',utoo))

