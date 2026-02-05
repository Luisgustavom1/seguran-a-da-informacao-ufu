import random

def GEN(seed: list[int]) -> list[int]:
    random.seed(str(seed))
    key_len = 4 * len(seed)
    return [random.randint(0, 1) for _ in range(key_len)]

def ENC(K: list[int], M: list[int]) -> list[int]:
    # XOR bit a bit
    return [bit_k ^ bit_m for bit_k, bit_m in zip(K, M)]

def DEC(K: list[int], C: list[int]) -> list[int]:
    # XOR bit a bit
    return [bit_k ^ bit_c for bit_k, bit_c in zip(K, C)]

