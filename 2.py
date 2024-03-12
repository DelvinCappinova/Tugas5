def ganjil(bawah, atas):
    angka_ganjil = []
    if bawah > atas:
        for i in range(bawah, atas -1, -1):
            if i % 2 == 1:
                angka_ganjil.append(i)
    else:
        for i in range(bawah, atas + 1):
            if i % 2 == 1:
                angka_ganjil.append(i)
    return ', '.join(map(str, angka_ganjil))


bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))

print(f"{ganjil(bawah, atas)}.")