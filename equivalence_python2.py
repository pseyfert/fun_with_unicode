import unicodedata

uone = unichr(0x00c5) # LATIN CAPITAL LETTER A WITH RING ABOVE

utoo = unichr(0x212b) # ANGSTROM SIGN

print uone, "\t", unicodedata.name(uone)
print utoo, "\t", unicodedata.name(utoo)

print "are these the same?", uone==utoo
print "are these canonically equivalent?", unicodedata.normalize('NFD',uone)==unicodedata.normalize('NFD',utoo)

uone = unichr(0xfb00)
utoo = unichr(0x0066)+unichr(0x0066)


print uone, "\t", unicodedata.name(uone)
print utoo, "\t", unicodedata.name(utoo[0]), " twice"
print "are these the same?", uone==utoo
print "are these canonically equivalent?", unicodedata.normalize('NFD',uone)==unicodedata.normalize('NFD',utoo)
print "are these compatible equivalent?", unicodedata.normalize('NFKD',uone)==unicodedata.normalize('NFKD',utoo)

