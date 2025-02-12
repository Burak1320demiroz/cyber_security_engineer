import math
import struct

class MD5:
    def __init__(self, message):
        self.message = message.encode()
        self.A = 0x67452301
        self.B = 0xefcdab89
        self.C = 0x98badcfe
        self.D = 0x10325476
        self.K = [int(2**32 * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]
        self.S = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
        self._process()

    def _pad_message(self):
        message = bytearray(self.message)
        original_length = len(message) * 8
        message.append(0x80)

        while (len(message) * 8) % 512 != 448:
            message.append(0)

        message += struct.pack('<Q', original_length)
        return message

    def _rotate_left(self, x, n):
        return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

    def _process(self):
        message = self._pad_message()
        for i in range(0, len(message), 64):
            chunk = message[i:i+64]
            A, B, C, D = self.A, self.B, self.C, self.D
            M = [int.from_bytes(chunk[j:j+4], byteorder='little') for j in range(0, 64, 4)]
            for j in range(64):
                if j < 16:
                    F = (B & C) | (~B & D)
                    g = j
                elif j < 32:
                    F = (D & B) | (~D & C)
                    g = (5 * j + 1) % 16
                elif j < 48:
                    F = B ^ C ^ D
                    g = (3 * j + 5) % 16
                else:
                    F = C ^ (B | ~D)
                    g = (7 * j) % 16
                F = (F + A + self.K[j] + M[g]) & 0xFFFFFFFF
                A = D
                D = C
                C = B
                B = (B + self._rotate_left(F, self.S[j])) & 0xFFFFFFFF

            self.A = (self.A + A) & 0xFFFFFFFF
            self.B = (self.B + B) & 0xFFFFFFFF
            self.C = (self.C + C) & 0xFFFFFFFF
            self.D = (self.D + D) & 0xFFFFFFFF

    def hexdigest(self):
        return ''.join(f'{x:02x}' for x in struct.pack('<4I', self.A, self.B, self.C, self.D))

# **Test**
md5_hash = MD5("Burak")
print(f"MD5 Hash: {md5_hash.hexdigest()}")
