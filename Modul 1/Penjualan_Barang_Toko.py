# Collection data
dftrBarang = [
    ['Kode Barang', 'Nama Barang', 'Jumlah yang Terjual', 'Harga Satuan', 'Pendapatan'],
    ['B01', 'Televisi', 10, 2000000, 20000000],
    ['B02', 'Kipas angin', 15, 232000, 3480000],
    ['B03', 'Mesin cuci', 8, 3200000, 25600000],
    ['B04', 'Komputer', 15, 3800000, 57000000],
    ['B05', 'Blender', 20, 800000, 16000000]
]

# Fungsi menu utama
def menuUtama():
    print('''
    ==========Data Penjualan di Toko Elektronik==========\n
    Menu :
        1. Menampilkan Daftar Barang 
        2. Menambah Data Barang
        3. Mengubah Data Barang
        4. Menghapus Data Barang
        5. Exit Program
    ''')

# Fungsi untuk menampilkan column data
def printColumn(item):
    space = 25
    print("|", end="")
    print(f'{item}', end ='')
    for j in range(space - len(str(item))):
        print(' ', end ='')
    

# Fungsi untuk menampilkan baris data
def printRow(index):
    printColumn(dftrBarang[index][0])
    printColumn(dftrBarang[index][1])
    printColumn(dftrBarang[index][2])
    printColumn(dftrBarang[index][3])
    printColumn(dftrBarang[index][4])
    print('')

# Fungsi mencari barang
def cariIndexBarang(namaBarang):
    for i in range(len(dftrBarang)):
        if namaBarang == dftrBarang[i][1]:
            return i
        else:
            None

# fungsi untuk menambah data
def tambahData() :
    namaBarang = str(input('Masukkan nama barang yang ingin ditambahkan : ')).capitalize()
    index = cariIndexBarang(namaBarang)
    if (index == None):
        jumlahBarang = int(input('Masukkan jumlah barang  :'))
        hargaBarang = int(input('Masukkan harga barang : '))
        pendapatan = jumlahBarang * hargaBarang
        inputSimpan = str(input('Tekan Y jika ingin menyimpan data dan tekan N jika tidak ingin menyimpan (Y/N) :  ')).upper()
        if inputSimpan == 'Y':
            dftrBarang.append(
            [
            f'B0{len(dftrBarang)}',
            namaBarang,
            jumlahBarang,
            hargaBarang,
            pendapatan
            ]
            )
            print('----Data tersimpan----\n')
            print('\t\t\t+++++++Daftar Barang yang Sudah Terjual+++++++')
            for i in range (len(dftrBarang)):
                printRow(i)
    else:
        print('----Data sudah ada----')

# Fungsi untuk mengubah value
def ubahData():
    inputKolom = str(input('Masukkan nama kolom yang ingin diubah (Kode/Nama/Jumlah/Harga)? ')).capitalize()
    if inputKolom == 'Kode':
        kodeBarang = str(input('Masukkan kode barang : '))
        inputSimpan = str(input('Tekan Y jika ingin mengubah data dan tekan N jika tidak ingin mengubah (Y/N) :  ')).upper()
        if inputSimpan == 'Y':
            dftrBarang[index][0] = kodeBarang
            print('----Data telah diperbaharui----\n')
            print('\t\t\t+++++++Daftar Barang yang Sudah Terjual+++++++')
            for i in range (len(dftrBarang)):
                printRow(i)
    elif inputKolom == 'Nama':
        nameBarang = str(input('Nasukkan nama barang : ')).capitalize()
        inputSimpan = str(input('Tekan Y jika ingin mengubah data dan tekan N jika tidak ingin mengubah (Y/N) :  ')).upper()
        if inputSimpan == 'Y':
            dftrBarang[index][1] = nameBarang
            print('----Data telah diperbaharui----\n')
            print('\t\t\t+++++++Daftar Barang yang Sudah Terjual+++++++')
            for i in range (len(dftrBarang)):
                printRow(i)
    elif inputKolom == 'Jumlah':
        jmlBarang = int(input('Masukkan jumlah barang : '))
        inputSimpan = str(input('Tekan Y jika ingin menyimpan data dan tekan N jika tidak ingin menyimpan (Y/N) :  ')).upper()
        if inputSimpan == 'Y':
            dftrBarang[index][2] = jmlBarang
            dftrBarang[index][4] = jmlBarang * dftrBarang[index][3]
            print('----Data telah diperbaharui----\n')
            print('\t\t\t+++++++Daftar Barang yang Sudah Terjual+++++++')
            for i in range (len(dftrBarang)):
                printRow(i)
    elif inputKolom == 'Harga':
        hrgaBarang = int(input('Masukkan harga barang : '))
        inputSimpan = str(input('Tekan Y jika ingin menyimpan data dan tekan N jika tidak ingin menyimpan (Y/N) :  ')).upper()
        if inputSimpan == 'Y':
            dftrBarang[index][3] = hrgaBarang
            dftrBarang[index][4] = hrgaBarang * dftrBarang[index][2]
            print('----Data telah diperbaharui----\n')
            print('\t\t\t+++++++Daftar Barang yang Sudah Terjual+++++++')
            for i in range (len(dftrBarang)):
                printRow(i)
         
# Fungsi untuk menghapus data
def deleteData():
    namaBarang = str(input('Masukkan nama barang yang ingin dihapus : ')).capitalize()
    index = cariIndexBarang(namaBarang)
    if (index == None):
            print("----Data tidak ada----")
    else:
        inputSimpan = str(input('Tekan Y jika ingin menghapus data dan tekan N jika tidak ingin menghapus (Y/N) :  ')).upper()
        if inputSimpan == 'Y':
            dftrBarang.pop(index)
            print('----Data terhapus----\n')
            print('\t\t\t+++++++Daftar Barang yang Sudah Terjual+++++++')
            for i in range (len(dftrBarang)):
                printRow(i) 
       
    
# Run the application
# Menu Utama
while(True): 
    menuUtama()
    inputMenu = int(input('Masukkan angka Menu yang ingin dijalankan [1-5]: '))

# Fitur 1 Menu Read Data
    if inputMenu == 1:
        while(True):
            print('''*Menu Menampilkan Data*
                1. Tampilkan seluruh data
                2. Tampilkan data tertentu
                3. Kembali ke menu utama
            ''')
            menuRead = int(input('Masukkan angka menu menampilkan data (1-3) : '))
            if menuRead == 1 :
                if len(dftrBarang) == 0:
                    print('----Tidak ada data----')
                else:
                    print('\t\t\t+++++++Daftar Barang yang Sudah Terjual+++++++')
                    for i in range(len(dftrBarang)):
                        printRow(i)
            elif menuRead == 2 :
                if len(dftrBarang) == 0:
                    print('----Tidak ada data----')
                else :
                    print('----Daftar barang yang tersedia----')
                    for i in range (1,len(dftrBarang)):
                        print(str(i)+". " + dftrBarang[i][1])
                    namaBarang = str(input('Masukkan nama barang : ')).capitalize()
                    index = cariIndexBarang(namaBarang)
                    if (index == None):
                        print("----Data tidak ada----")
                    else:
                        printRow(0)
                        printRow(index)
            elif menuRead == 3:
                inputSimpan = str(input('Tekan Y jika ingin kembali ke menu utama dan tekan N jika tidak ingin kembali ke menu utama (Y/N) :  ')).upper()
                if inputSimpan == 'Y':
                    break
            else:
                print('Pilihan yang anda masukkan salah, silahkan pilih menu (1 - 3)')

# Fitur 2 Menu Create Data
    elif inputMenu == 2:
        while(True):
            print('''*Menu Tambah Data*
                1. Menambahkan data
                2. Kembali ke menu utama
            ''')
            menuCreate = int(input('Masukkan angka menu tambah data (1-2) : '))
            if menuCreate == 1:
                tambahData()
            elif menuCreate == 2:
                inputSimpan = str(input('Tekan Y jika ingin kembali ke menu utama dan tekan N jika tidak ingin kembali ke menu utama (Y/N) :  ')).upper()
                if inputSimpan == 'Y':
                    break
            else:
                print('Pilihan yang anda masukkan salah, silahkan pilih menu (1 - 2)')


# Fitur 3 Menu Update Data
    elif inputMenu == 3:
        while(True):
            print('''*Menu Ubah Data*
                1. Mengubah data
                2. Kembali ke menu utama
            ''')
            menuEdit = int(input('Masukkan angka menu edit data (1-2) : '))
            if menuEdit == 1:
                print('----Daftar barang yang tersedia----')
                for i in range (1,len(dftrBarang)):
                    print(str(i)+". " + dftrBarang[i][1])
                namaBarang = str(input('Masukkan nama barang yang ingin diupdate : ')).capitalize()
                index = cariIndexBarang(namaBarang)
                if (index == None):
                    print("----Data tidak ada----")
                else:
                    printRow(0)
                    printRow(index)
                    inputUpdate = str(input('Tekan Y jika ingin melanjutkan update data dan tekan N jika tidak ingin melakukan update (Y/N) :  ')).upper()
                    if inputUpdate == 'Y':
                        ubahData()
            elif menuEdit == 2:
                inputSimpan = str(input('Tekan Y jika ingin kembali ke menu utama dan tekan N jika tidak ingin kembali ke menu utama (Y/N) :  ')).upper()
                if inputSimpan == 'Y':
                    break
            else:
                print('Pilihan yang anda masukkan salah, silahkan pilih menu (1 - 2)')


# Fitur 4 Menghapus Data
    elif inputMenu == 4:
        while(True):
            print('''*Menu Hapus Data*
                1. Menghapus data
                2. Kembali ke menu utama
            ''')
            menuHapus = int(input('Masukkan angka menu hapus data (1-2) : '))
            if menuHapus == 1:
                print('----Daftar barang yang tersedia---- ')
                for i in range (1,len(dftrBarang)):
                    print(str(i)+". " + dftrBarang[i][1])
                deleteData()
            elif menuHapus == 2:
                inputSimpan = str(input('Tekan Y jika ingin kembali ke menu utama dan tekan N jika tidak ingin kembali ke menu utama (Y/N) :  ')).upper()
                if inputSimpan == 'Y':
                    break
            else:
                print('Pilihan yang anda masukkan salah, silahkan pilih menu (1 - 2)')
    elif inputMenu == 5:
        inputSimpan = str(input('Tekan Y jika ingin keluar dari program dan tekan N jika tidak ingin keluar (Y/N) :  ')).upper()
        if inputSimpan == 'Y':
            print('---Terima kasih dan sampai jumpa---')
            break
    else:
        print('Pilihan yang anda masukkan salah, silahkan pilih menu 1 - 5')
  
