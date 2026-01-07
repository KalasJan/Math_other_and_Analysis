# Priklad - prevody mezi ciselnymi soustavami

# a) Jak vypada cislo 486586165461 ve dvojkove soustave?
a = 486586165461
print (f'Číslo {a} je po převodu do dvojkové soustavy {bin(a)}.')

# b) Ktere cislo v desitkove soustave ma tvar 01010111011001?
b = 0b01010111011001
print (f'{bin(b)} ve dvojkove soustave je v desitkove {int(b)}.')

# c) jak vypada desitkove cislo 18544818548 v sestnactkove
c = 18544818548
print (f'{c} v desitkove soustave je v hexadecimalni (zaklad je 16) číslo {hex(c)}.')

# d) jak vypada cislo 218A5F68C8
d = 0x218A5F68C8
print (f'{hex(d)} v sestnactkove soustave je v dekadické soustavě číslo {int(d)}.')

# e) prevod A298CF do dvojkove je?
e = 0xA298CF
print (f'{hex(e)} v sestnactkove soustave je ve dvojkove číslo {bin(e)}.')

# f) prevod 1010000100110 v 16kove je?
f = 0b1010000100110
print (f'{bin(f)} v sestnactkove soustave je ve dvojkove číslo {hex(f)}.')