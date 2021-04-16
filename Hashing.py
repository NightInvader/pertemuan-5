Pass = str(input('Masukkan Password : '))
import string
import random
PanjangPass = len(Pass)
if PanjangPass<8:
    print('password kurang panjang, minimal 8 karakter')
else:
    if ' ' in Pass:
        print('password menngandung spasi')
    else:
        Pass = string.ascii_letters
        print('Hasil Hashing', ''.join(random.choice(Pass) for i in range (PanjangPass)))
