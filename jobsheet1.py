import random
from guess import Tebak


class Tebakan:
    def __init__(self):
        self.jawaban = random.randint(1, 10)


game = Tebakan()

tebakan_input = int(input("Masukkan angka dari 1 s/d 10: "))
jawaban = game.jawaban

tebak_game = Tebak(tebakan_input, jawaban)

if tebak_game.cek():
    print("Kamu benar!")
else:
    print("Kamu salah.")
