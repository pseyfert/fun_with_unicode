import unicodedata

uone = unichr(0x00c5) # LATIN CAPITAL LETTER A WITH RING ABOVE

utoo = unichr(0x212b) # ANGSTROM SIGN

print uone, "\t", unicodedata.name(uone)
print utoo, "\t", unicodedata.name(utoo)

print "are these the same?", uone==utoo
print "are these canonically equivalent?", unicodedata.normalize('NFD',uone)==unicodedata.normalize('NFD',utoo)

splitup = unicodedata.decomposition(uone)

first = unichr(int(splitup[0:4],16))
second = unichr(int(splitup[5:9],16))
print first,
print "\t",
print second,
print "\t", unicodedata.name(first), unicodedata.name(second)

print "are these the same?", uone==first+second
print "are these canonically equivalent?", unicodedata.normalize('NFD',uone)==unicodedata.normalize('NFD',first+second)
print "are these compatible equivalent?", unicodedata.normalize('NFKD',uone)==unicodedata.normalize('NFKD',first+second)


