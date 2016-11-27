from collections import deque

decoded = []

with open("image_with_flag_defect.jpg.hamming", "rb") as fh:

    x = fh.read()
    f = map(ord, x)

    for i in xrange(0, len(f), 15):
        s = deque(f[i:i+15], maxlen=15)
        b = deque(maxlen=15)
        
        for c in s:
            b.append([int(p) for p in bin(c)[2:].zfill(8)])
        

        for bit_pos in xrange(8):
            c1 = b[0][bit_pos] ^ b[2][bit_pos] ^ b[4][bit_pos] ^ b[6][bit_pos] ^ b[8][bit_pos] ^ b[10][bit_pos] ^ b[12][bit_pos] ^ b[14][bit_pos]
            c2 = b[1][bit_pos] ^ b[2][bit_pos] ^ b[5][bit_pos] ^ b[6][bit_pos] ^ b[9][bit_pos] ^ b[10][bit_pos] ^ b[13][bit_pos] ^ b[14][bit_pos]
            c4 = b[3][bit_pos] ^ b[4][bit_pos] ^ b[5][bit_pos] ^ b[6][bit_pos] ^ b[11][bit_pos] ^ b[12][bit_pos] ^ b[13][bit_pos] ^ b[14][bit_pos]
            c8 = b[7][bit_pos] ^ b[8][bit_pos] ^ b[9][bit_pos] ^ b[10][bit_pos] ^ b[11][bit_pos] ^ b[12][bit_pos] ^ b[13][bit_pos] ^ b[14][bit_pos]

            e = "".join(map(str, [c8, c4, c2, c1]))
            ei = int(e, 2)
            if ei != 0:
                b[ei-1][bit_pos] ^= 1

        out = [int("".join(map(str, it)), 2) for it in b]
        decoded.extend([out[2], out[4], out[5], out[6], out[8], out[9], out[10], out[11], out[12], out[13], out[14]])

with open("image_with_flag_defect.jpg", "wb") as fho:
    s = "".join(map(chr, decoded))
    fho.write(s)
