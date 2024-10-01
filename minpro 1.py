def total_harga_barang():

    
    harga_barang = float(input("masukkan angka harga barang: "))
    jumlah_pembelian = float(input("masukkan angka jumlah pembelian : "))
    total_harga_barang = harga_barang * jumlah_pembelian
    print(f"Total harga barang: Rp {total_harga_barang:.2f}")

    
    if total_harga_barang > 250000: 
        diskon = total_harga_barang * 0.25
        total_setelah_diskon = total_harga_barang - diskon  
        print(f"Diskon 25%: Rp {diskon:.2f}")
        print(f"Total setelah diskon: Rp {total_setelah_diskon:.2f}")
        print("anda mendaptkan diskon. ")
    else:
        print("anda tidak mendapakan diskon.")


while True:
    total_harga_barang()
    print()
    pilihan = input("Apakah anda ingin menghitung lagi? (y/t): ")
    if pilihan == 't':
        break 
    print("Terima Kasih")