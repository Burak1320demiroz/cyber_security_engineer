def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

def sha1(message):
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    message += b'\x80'
    while (len(message) * 8 + 64) % 512 != 0:
        message += b'\x00'
    message += original_bit_len.to_bytes(8, 'big')
    
    H0 = 0x67452301
    H1 = 0xEFCDAB89
    H2 = 0x98BADCFE
    H3 = 0x10325476
    H4 = 0xC3D2E1F0
    
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        W = [int.from_bytes(block[j:j+4], 'big') for j in range(0, 64, 4)]
        for j in range(16, 80):
            W.append(left_rotate(W[j-3] ^ W[j-8] ^ W[j-14] ^ W[j-16], 1))
        
        A, B, C, D, E = H0, H1, H2, H3, H4
        
        for j in range(80):
            if 0 <= j < 20:
                F = (B & C) | ((~B) & D)
                K = 0x5A827999
            elif 20 <= j < 40:
                F = B ^ C ^ D
                K = 0x6ED9EBA1
            elif 40 <= j < 60:
                F = (B & C) | (B & D) | (C & D)
                K = 0x8F1BBCDC
            else:
                F = B ^ C ^ D
                K = 0xCA62C1D6
            
            temp = (left_rotate(A, 5) + F + E + K + W[j]) & 0xFFFFFFFF
            E = D
            D = C
            C = left_rotate(B, 30)
            B = A
            A = temp
        
        H0 = (H0 + A) & 0xFFFFFFFF
        H1 = (H1 + B) & 0xFFFFFFFF
        H2 = (H2 + C) & 0xFFFFFFFF
        H3 = (H3 + D) & 0xFFFFFFFF
        H4 = (H4 + E) & 0xFFFFFFFF
    
    return ''.join(f'{h:08x}' for h in [H0, H1, H2, H3, H4])

# **Test**
message = b"Burak"
hash_value = sha1(message)
print("SHA-1 Hash:", hash_value)
