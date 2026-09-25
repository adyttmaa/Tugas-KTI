class Enigma:
    def __init__(self):
        self.rotors = [
            {'w': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'n': 'Q'},
            {'w': 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'n': 'E'},
            {'w': 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'n': 'V'}
        ]
        self.reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        self.pos = [15, 13, 11]
        self.ring = [16, 2, 6]
        self.pb = self.make_plugboard("CA HK SB")

    def make_plugboard(self, pairs):
        pb = {chr(i + 65): chr(i + 65) for i in range(26)}
        for a, b in [p for p in pairs.split()]:
            pb[a] = b
            pb[b] = a
        return pb

    def step(self):
        n1 = ord(self.rotors[1]['n']) - 65
        n2 = ord(self.rotors[2]['n']) - 65

        step_mid = self.pos[2] == n2
        step_left = self.pos[1] == n1

        if step_mid:
            self.pos[1] = (self.pos[1] + 1) % 26
        elif step_left:
            self.pos[1] = (self.pos[1] + 1) % 26

        if step_left:
            self.pos[0] = (self.pos[0] + 1) % 26

        self.pos[2] = (self.pos[2] + 1) % 26

    def encrypt_char(self, c):
        self.step()

        c = self.pb[c]
        c_val = ord(c) - 65

        for i in range(2, -1, -1):
            offset = self.pos[i] - self.ring[i]
            idx = (c_val + offset) % 26
            char_mapped = self.rotors[i]['w'][idx]
            c_val = (ord(char_mapped) - 65 - offset) % 26

        c_val = ord(self.reflector[c_val]) - 65

        for i in range(3):
            offset = self.pos[i] - self.ring[i]
            char_to_find = chr(((c_val + offset) % 26) + 65)
            idx = self.rotors[i]['w'].index(char_to_find)
            c_val = (idx - offset) % 26

        return self.pb[chr(c_val + 65)]


enigma = Enigma()
ciphertext_3 = "PYTZQHFHJQTKIHXKBLJIQNUKNVDGDFZIGFUXLK"
plaintext_3 = "".join([enigma.encrypt_char(c) for c in ciphertext_3])

print("--- HASIL DEKRIPSI ENIGMA MACHINE ---")
print(f"Ciphertext : {ciphertext_3}")
print(f"Plaintext  : {plaintext_3}")