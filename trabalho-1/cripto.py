import random, os, secrets

def _xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

def GEN(seed: list[int]) -> list[int]:
    random.seed(str(seed))
    key_len = 4 * len(seed)
    return [random.randint(0, 1) for _ in range(key_len)]

def ENC(K: list[int], M: list[int]) -> list[int]:
    BLOCK_SIZE = len(K)
    # using CBC to encrypt
    IV = [secrets.randbelow(256) for _ in range(BLOCK_SIZE)]
    C = []
    prev_block = IV

    for i in range(0, len(M), BLOCK_SIZE):
        block = M[i:i + BLOCK_SIZE]
        mixed = _xor_bytes(prev_block, block)
        cypher = _xor_bytes(K[i:i + BLOCK_SIZE], mixed) 
        C.extend(cypher)
        prev_block = cypher

    return IV + C

def DEC(K: list[int], C: list[int]) -> list[int]:
    BLOCK_SIZE = len(K)
    IV = C[:BLOCK_SIZE]
    C = C[BLOCK_SIZE:]
    M = []
    prev_block = IV

    for i in range(0, len(C), BLOCK_SIZE):
        block = C[i:i + BLOCK_SIZE]
        
        mixed = _xor_bytes(K[i:i + BLOCK_SIZE], block)
        msg_block = _xor_bytes(mixed, prev_block)
        M.extend(msg_block)
        prev_block = block

    return M

