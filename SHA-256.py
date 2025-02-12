def right_rotate(value, shift, size=32):
    return ((value >> shift) | (value << (size - shift))) & 0xFFFFFFFF

def sha256(message):
    # Başlangıç hash değerleri (H0 - H7)
    H = [
        0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A,
        0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19
    ]
    
    # SHA-256 için sabitler (K0 - K63)
    K = [
        0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5, 0x3956C25B, 0x59F111F1, 0x923F82A4, 0xAB1C5ED5,
        0xD807AA98, 0x12835B01, 0x243185BE, 0x550C7DC3, 0x72BE5D74, 0x80DEB1FE, 0x9BDC06A7, 0xC19BF174,
        0xE49B69C1, 0xEFBE4786, 0x0FC19DC6, 0x240CA1CC, 0x2DE92C6F, 0x4A7484AA, 0x5CB0A9DC, 0x76F988DA,
        0x983E5152, 0xA831C66D, 0xB00327C8, 0xBF597FC7, 0xC6E00BF3, 0xD5A79147, 0x06CA6351, 0x14292967,
        0x27B70A85, 0x2E1B2138, 0x4D2C6DFC, 0x53380D13, 0x650A7354, 0x766A0ABB, 0x81C2C92E, 0x92722C85,
        0xA2BFE8A1, 0xA81A664B, 0xC24B8B70, 0xC76C51A3, 0xD192E819, 0xD6990624, 0xF40E3585, 0x106AA070,
        0x19A4C116, 0x1E376C08, 0x2748774C, 0x34B0BCB5, 0x391C0CB3, 0x4ED8AA4A, 0x5B9CCA4F, 0x682E6FF3,
        0x748F82EE, 0x78A5636F, 0x84C87814, 0x8CC70208, 0x90BEFFFA, 0xA4506CEB, 0xBEF9A3F7, 0xC67178F2
    ]
    
    # Mesajı byte dizisine çevirme
    message = bytearray(message, 'ascii')
    original_length = len(message) * 8
    
    # Padding (Ön İşleme)
    message.append(0x80)  # 1 bit ekle
    while (len(message) * 8 + 64) % 512 != 0:
        message.append(0)
    message += original_length.to_bytes(8, 'big')  # Orijinal uzunluğu ekle
    
    # 512-bit bloklara ayırma
    for chunk_index in range(0, len(message), 64):
        chunk = message[chunk_index:chunk_index + 64]
        W = [int.from_bytes(chunk[i:i+4], 'big') for i in range(0, 64, 4)]
        
        # Mesaj planlama (16-63. kelimeleri oluştur)
        for i in range(16, 64):
            s0 = right_rotate(W[i-15], 7) ^ right_rotate(W[i-15], 18) ^ (W[i-15] >> 3)
            s1 = right_rotate(W[i-2], 17) ^ right_rotate(W[i-2], 19) ^ (W[i-2] >> 10)
            W.append((W[i-16] + s0 + W[i-7] + s1) & 0xFFFFFFFF)
        
        # Geçici değişkenleri ayarla
        a, b, c, d, e, f, g, h = H
        
        # Ana hash döngüsü
        for i in range(64):
            S1 = right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)
            ch = (e & f) ^ ((~e) & g)
            temp1 = (h + S1 + ch + K[i] + W[i]) & 0xFFFFFFFF
            S0 = right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF
            
            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF
        
        # Hash değerlerini güncelleme
        H = [(H[i] + v) & 0xFFFFFFFF for i, v in enumerate([a, b, c, d, e, f, g, h])]
    
    # Son 256-bitlik hash çıktısı
    return ''.join(f'{value:08x}' for value in H)

# Örnek kullanım
print(sha256("Burak"))
