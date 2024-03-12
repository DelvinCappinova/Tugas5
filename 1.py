def perkalian():

    angka1 = int(input("Masukkan angka pertama :"))
    angka2 = int(input("Masukkan angka kedua :"))
    hasilperkalian = angka1*angka2
    print (f"{angka1}x{angka2}=", end='')
    for perkalian in range(1,angka1 + 1):
        print (angka2, end= '' )
        if perkalian == angka1:
            print ('=', end ='')
        else:
            print ('+', end ='')
    print (hasilperkalian)
perkalian()