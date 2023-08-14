import random
from guess1 import cek


jawaban = random.randint(1, 10)

tebakan = int(input("masukan angka dari 1 s/d 10"))

if cek(tebakan, jawaban):
    print("jawaban kamu benar")
else:
    print("jawaban kamu salah")
