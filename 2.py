def caesar_encrypt(plaintext, k):
    ciphertext = ""
    k = k % 26
    for ch in plaintext.upper():
        if 'A' <= ch <= 'Z':
            p = ord(ch) - ord('A')
            c = (p + k) % 26
            ciphertext += chr(c + ord('A'))
        else:
            ciphertext += ch
    return ciphertext

# Dữ liệu
plaintext = "Minh"
k = 32

ciphertext = caesar_encrypt(plaintext, k)
print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
