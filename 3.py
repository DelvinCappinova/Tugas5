def nilai_ips():
    matkul = int(input("Masukkan jumlah mata kuliah: "))
    total_nilai = 0
    total_sks = 0
    for i in range(matkul):
        nilaimatkul = str(input(f"Nilai MK {i+1} :")).upper()
        if nilaimatkul == 'A':
            nilai = 4
        elif nilaimatkul == 'B':
            nilai = 3
        elif nilaimatkul == 'C':
            nilai = 2
        elif nilaimatkul == 'D':
            nilai = 1
            
        sks = 3
        total_nilai += nilai * sks
        total_sks += sks
    ips = total_nilai / total_sks
        
    print(f"IPS Anda adalah: {ips:.2f}")
nilai_ips()
 