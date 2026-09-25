def decrypt_caesar(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            geser = ord(char) - shift
            if geser < ord('A'):
                geser += 26
            plaintext += chr(geser)
        else:
            plaintext += char
    return plaintext


def decrypt_vigenere(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_idx = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_idx]) - ord('A')
            geser = ord(char) - shift

            if geser < ord('A'):
                geser += 26
            plaintext += chr(geser)

            key_idx = (key_idx + 1) % len(key)
        else:
            plaintext += char
    return plaintext


ciphertext_1 = "DPETLA XLSLDTDHL XPYOLALE DZLW JLYR MPCMPOL DLEF DLXL WLTY"

print("--- HASIL BRUTE-FORCE CAESAR CIPHER ---")
for k in range(1, 15):
    hasil_dekripsi = decrypt_caesar(ciphertext_1, k)
    if k == 11:
        print(f"Kunci {k:2}: {hasil_dekripsi} <--- (JAWABAN BENAR)")
    else:
        print(f"Kunci {k:2}: {hasil_dekripsi}")

ciphertext_2 = "FIRADA OIXASAQ EHAU VVKKNVRR HOAEGTEV TZDNO HIJA QMVETAUOGN"
kata_kunci = "NEGARA"

print("\n--- HASIL DEKRIPSI VIGENERE CIPHER ---")
print(f"Kata Kunci : {kata_kunci}")
print(f"Plaintext  : {decrypt_vigenere(ciphertext_2, kata_kunci)}")