import time
import random
import statistics

from cripto import GEN, ENC, DEC

def calc_hamming_distance(l1, l2):
    return sum(b1 != b2 for b1, b2 in zip(l1, l2))

def test():
    seed_base = [1, 0, 1, 1, 0, 0, 1, 1]
    msg_base = [1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    
    init = time.perf_counter()
    for _ in range(3000):
        k = GEN(seed_base)
        c = ENC(k, msg_base)
        m = DEC(k, c)
        assert msg_base == m
    fim = time.perf_counter()
    print(f"1. TEMPO DE EXECUÇÃO (3000 ciclos): {fim - init:.5f} segundos")

    visited_ciphers = set()
    collisions = 0
    for i in range(500):
        s = [random.randint(0, 1) for _ in range(8)]
        k = GEN(s)
        c = tuple(ENC(k, msg_base))
        if c in visited_ciphers:
            collisions += 1
        visited_ciphers.add(c)
    print(f"2. COLISÕES: {collisions}")

    k = GEN(seed_base)
    c_orig = ENC(k, msg_base)
    diffusion = []
    for i in range(len(msg_base)):
        msg_alt = list(msg_base)
        msg_alt[i] = 1 - msg_alt[i] # inverte 1 bit da mensagem
        c_alt = ENC(k, msg_alt)
        diffusion.append(calc_hamming_distance(c_orig, c_alt))
    print(f"3. DIFUSÃO: Média de {statistics.mean(diffusion):.2f} bits alterados")

    confusion = []
    for i in range(len(seed_base)):
        seed_alt = list(seed_base)
        seed_alt[i] = 1 - seed_alt[i] # inverte 1 bit da seed
        k_alt = GEN(seed_alt)
        c_alt = ENC(k_alt, msg_base)
        confusion.append(calc_hamming_distance(c_orig, c_alt))
    print(f"4. CONFUSÃO: Média de {statistics.mean(confusion):.2f} bits alterados")

if __name__ == "__main__":
    test()
