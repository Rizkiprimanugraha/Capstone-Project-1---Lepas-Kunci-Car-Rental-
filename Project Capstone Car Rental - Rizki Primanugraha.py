from tabulate import tabulate

headers = ['Index', 'Nama Mobil', 'Kapasitas', 'Stok', 'Harga']
listmobil = [['Avanza Veloz', '6', 7, 550000],
             ['Kijang Innova', '7', 5, 750000],
             ['Fortuner VRZ', '5', 3, 1200000],
             ['Alphard 2.5G', '7', 4, 1500000]]
cart = []

def mencarimobil():
    while True:
        indexmobil = int(input('Masukkan index mobil yang dicari: '))
        if indexmobil > len(listmobil) - 1:
            print('Data yang anda masukkan tidak ada. Silahkan masukkan kembali angka yang tersedia.')
            break
        else:
            print('Daftar Mobil :')
            print(tabulate([listmobil[indexmobil]], headers=["Nama","Kapasitas","Stok","Harga"], tablefmt="grid"))

def isDigit(angka):
    return angka.isdigit()

def inputAngka(teks):
    userInput=input(teks)
    while not isDigit(userInput):
        print('Input yang anda masukkan tidak valid.')
        userInput=input(teks)
    return userInput

while True:
    pilihanmenu = inputAngka('''
============= Selamat Datang di Lepas Kunci Rental Car =============
                    Sewa Mobil Gak Pake Ribet
                      
            List Menu:
            1. Menampilkan Daftar Mobil
            2. Menambah Daftar Mobil
            3. Mengganti Daftar Mobil
            4. Menghapus Daftar Mobil
            5. Melakukan Sewa Mobil
            6. Keluar
            Masukkan Angka : ''')

    if pilihanmenu == '1':
        while True:
            submenu1 = inputAngka('''              
                1. Tabel Daftar Mobil
                2. Cari Mobil            
                3. Kembali ke Menu Utama
                Masukkan menu yang ingin dijalankan : ''')

            if submenu1 == '1':
                print(tabulate(listmobil, headers=headers, tablefmt="grid", showindex=True))
                break
            elif submenu1 == '2':
                print(tabulate(listmobil, headers=headers, tablefmt="grid", showindex=True))
                mencarimobil()
                break
            elif submenu1 == '3':
                break
            else:
                print('Data yang anda masukkan tidak ada. Silahkan masukkan kembali angka yang tersedia.')
    
    elif pilihanmenu == '2':
        while True:
            submenu2 = inputAngka('''              
            1. Tambah Daftar Mobil
            2. Kembali ke Menu Utama            
            Masukkan menu yang ingin dijalankan : ''')
            if submenu2 == '1':
                    indexmobil=input(str('Masukkan Index Mobil: '))
                    namamobil=input(str('Masukkan Nama Mobil Baru: ')).lower()
                    kapasitasmobil=input(str('Masukkan Kapasitas Penumpang Mobil Baru: '))
                    stokmobil=int(inputAngka('Masukkan Stok Mobil Baru yang tersedia: '))
                    hargasewa=int(inputAngka('Masukkan Harga Sewa Mobil Baru: '))
                    checker=input('Apakah anda yakin ingin menyimpan data Mobil berikut? (ya/tidak): ').lower()
                    listmobil.append([namamobil,kapasitasmobil,stokmobil,hargasewa])
                    if checker=='ya':
                        print('Data mobil baru berhasil disimpan')
                        print(tabulate(listmobil, headers=headers, tablefmt="grid", showindex=True))
                        break
                    elif checker=='tidak':
                        print('Data mobil tidak disimpan')
                    else:
                        print('Data yang anda masukkan tidak ada. Silahkan masukkan kembali angka yang tersedia.')
            elif submenu2 == '2':
                break
            else:
                print('Data yang anda masukkan tidak ada. Silahkan masukkan kembali angka yang tersedia.')
                
    elif pilihanmenu == '3':
        while True:
            submenu3 = inputAngka('''              
            1. Memperbaharui Daftar Mobil
            2. Kembali ke Menu Utama            
            Masukkan menu yang ingin dijalankan : ''')
            if submenu3 == '1':
                    print(tabulate(listmobil, headers=headers, tablefmt="grid", showindex=True))
                    print('\n')
                    indexmobil=int(inputAngka('Masukkan Index Mobil: '))
                    print(tabulate([listmobil[indexmobil]], headers=headers, tablefmt="grid", showindex=True))
                    checker=input('Apakah anda ingin melanjutkan proses update data Mobil ? (ya/tidak): ')
                    if checker=='ya':
                        namamobil=input(str('Masukkan Nama Mobil Baru: ')).lower()
                        kapasitasmobil=input(str('Masukkan Kapasitas Penumpang Mobil Baru: ')).lower()
                        stokmobil=int(inputAngka('Masukkan Stok Mobil Baru yang tersedia: '))
                        hargasewa=int(input('Masukkan Harga Sewa Mobil Baru: '))
                        checker=input('Apakah anda yakin ingin menyimpan data Mobil berikut? (ya/tidak): ').lower()
                        [listmobil[indexmobil]]=[[namamobil,kapasitasmobil,stokmobil,hargasewa]]
                        print(tabulate(listmobil, headers=headers, tablefmt="grid", showindex=True))
                        print('Data Anda berhasil diupdate')
                    elif checker=='tidak':
                        break
                    else:
                        print('Data yang anda masukkan tidak ada. Silahkan masukkan kembali angka yang tersedia.')
            elif submenu3 == '2':
                break
            else:
                print('Data yang anda masukkan tidak ada. Silahkan masukkan kembali angka yang tersedia.')

    elif pilihanmenu == '4':
        while True:
            submenu4 = inputAngka('''              
            1. Menghapus Daftar Mobil
            2. Kembali ke Menu Utama            
            Masukkan menu yang ingin dijalankan : ''')
            if submenu4 == '1':
                    indexmobil=int(inputAngka('Masukkan Index Mobil: '))
                    print(tabulate([listmobil[indexmobil]], headers=headers, tablefmt="grid", showindex=True))
                    checker=input('Apakah anda ingin melanjutkan proses menghapus data Mobil ? (ya/tidak): ').lower()
                    if checker=='ya':
                        del listmobil[indexmobil]
                        print(tabulate(listmobil, headers=headers, tablefmt="grid", showindex=True))
                        print('Data Anda berhasil dihapus')
                    elif checker=='tidak':
                        break
                    else:
                        print('Data yang anda masukkan tidak ada. Silahkan masukkan kembali angka yang tersedia.')
            if submenu4 == '2':
                break
                        
    elif pilihanmenu == '5':
        while True:
            submenu5 = inputAngka('''              
            1. Melakukan Sewa Mobil
            2. Kembali ke Menu Utama            
            Masukkan menu yang ingin dijalankan : ''')
            print('\n')
            if submenu5 == '1':
                mobildisewa = []

                while True:
                    datasementara = []
                    print(tabulate(listmobil, headers=headers, showindex="always", tablefmt="grid"))
                    print('\n')
                    indexmobil = int(inputAngka('Masukkan Index Mobil yang ingin disewa : '))
                    jumlahmobil = int(inputAngka('Masukkan Jumlah Mobil yang ingin disewa : '))
                    while True:
                        if jumlahmobil <= 0:
                            print('Angka yang anda masukkan tidak valid.')
                            break
                        elif jumlahmobil <= listmobil[indexmobil][2]:
                            datasementara.append(listmobil[indexmobil][0])
                            datasementara.append(jumlahmobil)
                            datasementara.append(listmobil[indexmobil][3])
                            print('Stok tersedia. Silahkan lanjutkan Transaksi')
                            mobildisewa.append(datasementara)
                            headers = ["Nama", "Jumlah", "Harga"]
                            print(tabulate(mobildisewa, headers=headers, tablefmt="grid"))
                            
                            checker = input('Apakah anda ingin menyewa mobil yang Lain? (ya/tidak)  : ').lower()
                            if checker == 'ya':
                                continue
                            elif checker == 'tidak':
                                print(tabulate(mobildisewa, headers=headers, tablefmt="grid"))
                                print('Lepas Kunci Rental Car')
                                print('Sewa Mobil Gak Pake Ribet\n')
                                print('Pembayaran Sewa Mobil')
                                
                                totalharga = sum(item[1] * item[2] for item in mobildisewa)
                                
                            print(tabulate(mobildisewa, headers=headers, tablefmt="grid"))
                            print(f'Total yang harus dibayar = {totalharga}')
                            
                            while True:
                                jumlahuang = int(inputAngka('Masukkan jumlah uang : '))
                                if jumlahuang >= totalharga:
                                    kembali = jumlahuang - totalharga
                                    print('\nTerima kasih\nNikmati berkendara dengan Lepas Kunci')
                                    print(f'Uang kembali anda : {kembali}')
                                    break
                                else:
                                    kekurangan = totalharga - jumlahuang
                                    print(f'Uang kurang sebesar {kekurangan}. Mohon masukkan nominal yang sesuai')
                            break
                        else:
                            print('Stok tidak mencukupi. Silakan masukkan angka sesuai dengan yang ada di Tabel.')
                            break
            if submenu5 == '2':
                break
                                
    elif pilihanmenu =='6':
        print(f'Terima kasih sudah menggunakan jasa Lepas Kunci')
        exit
    else:
        print('Data yang anda masukkan tidak ada. Silahkan masukkan kembali angka yang tersedia')