def ma_hoa_caesar(text, k):
    ket_qua = ""
    for ky_tu in text:
        if ky_tu.isalpha():
            base = ord('A') if ky_tu.isupper() else ord('a')
            ma_moi = (ord(ky_tu) - base + k) % 26 + base
            ket_qua += chr(ma_moi)
        else:
            ket_qua += ky_tu
    return ket_qua

# Dữ liệu đầu vào
chuoi_goc = "Minh"
khoa = 32  # STT = 32
chuoi_ma_hoa = ma_hoa_caesar(chuoi_goc, khoa)
print("Chuỗi đã mã hóa:", chuoi_ma_hoa)
