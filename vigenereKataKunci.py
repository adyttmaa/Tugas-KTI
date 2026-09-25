# Tabel frekuensi relatif huruf Bahasa Indonesia (dalam persentase)
freq_ind = {
    'A': 19.4, 'B': 2.2, 'C': 1.4, 'D': 4.2, 'E': 9.0, 'F': 0.8,
    'G': 4.0, 'H': 2.4, 'I': 9.4, 'J': 0.8, 'K': 4.6, 'L': 4.0,
    'M': 3.8, 'N': 9.6, 'O': 2.0, 'P': 3.0, 'Q': 0.01, 'R': 5.4,
    'S': 5.6, 'T': 5.0, 'U': 4.4, 'V': 0.3, 'W': 0.4, 'X': 0.01,
    'Y': 1.2, 'Z': 0.01
}

def hitung_chi_square(teks_blok):
    skor_geser = []
    panjang = len(teks_blok)
    
    # Uji seluruh 26 kemungkinan huruf kunci
    for geser in range(26):
        skor = 0
        teks_dekripsi = ""
        
        # Lakukan dekripsi sementara pada blok ini
        for char in teks_blok:
            c_val = ord(char) - ord('A')
            p_val = (c_val - geser) % 26
            teks_dekripsi += chr(p_val + ord('A'))
            
        # Hitung seberapa jauh kemiringannya dari standar bahasa Indonesia
        for huruf in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            observed = teks_dekripsi.count(huruf)
            expected = panjang * (freq_ind[huruf] / 100)
            if expected > 0:
                skor += ((observed - expected) ** 2) / expected
        
        huruf_kunci = chr(geser + ord('A'))
        skor_geser.append((skor, huruf_kunci))
        
    # Urutkan dari skor terkecil (paling cocok dengan bahasa asli)
    skor_geser.sort(key=lambda x: x[0])
    return skor_geser

ciphertext = "FIRADAOIXASAQEHAUVVKKNVRRHOAEGTEVTZDNOHIJAQMVETAUOGN"
panjang_kunci = 6
blok = [""] * panjang_kunci

# Pecah menjadi 6 blok
for i, char in enumerate(ciphertext):
    blok[i % panjang_kunci] += char

print("--- 3 TEBAKAN KUNCI TERATAS PER BLOK (CHI-SQUARE) ---\n")
for i in range(panjang_kunci):
    tebakan = hitung_chi_square(blok[i])
    print(f"Blok {i+1} ({blok[i]}):")
    # Menampilkan 3 hasil dengan skor kemiripan terbaik
    print(f"  1. '{tebakan[0][1]}' (Skor: {tebakan[0][0]:.2f})")
    print(f"  2. '{tebakan[1][1]}' (Skor: {tebakan[1][0]:.2f})")
    print(f"  3. '{tebakan[2][1]}' (Skor: {tebakan[2][0]:.2f})\n")