import hashlib

def sha1_hash(text):
    return hashlib.sha1(text.encode()).hexdigest()

def brute_force_sha1(hash_value, wordlist_path):
    try:
        with open(wordlist_path, "r", encoding="utf-8") as f:
            for line in f:
                word = line.strip()
                if sha1_hash(word) == hash_value:
                    print(f"[+] Parola bulundu: {word}")
                    return word
        print("[-] Parola bulunamadı!")
    except FileNotFoundError:
        print("Hata: Wordlist dosyası bulunamadı.")

hash_input = input("SHA-1 hash değerini girin: ").strip()

wordlist_file = input("Wordlist dosya yolunu girin: ").strip()

brute_force_sha1(hash_input, wordlist_file)
