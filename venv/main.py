#Program Manajemen Kontak#

def melihat_kontak():
    # melihat semua kontak
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
    else:
        print("Kontak masih kosong!")
        return 1

def menambah_kontak():
        #menambahkan kontak
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan nomor hp kontak yang baru: ")
        email = input("Masukkan email kontak yang baru: ")
        kontak_baru = {'nama':nama, 'HP':HP, 'email':email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan")

def menghapus_kontak():
    # menghapus kontak
    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus - 1]
        print("Kontak yang dimaksud sudah dihapus")


kontak1 = {'nama' : "Ari", 'HP': '085894836361', 'email': 'nuruladhari2@gmail.com'}
kontak2 = {'nama' : "Nrladhari", 'HP': '0812240924588', 'email': 'nrladhari@gmail.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukan pilihan menu kontak (1,2,3,atau 4): ")

    if pilihan == '1':
        melihat_kontak()

    elif pilihan == '2':
        menambah_kontak()

    elif pilihan == '3':
        menghapus_kontak()

    elif pilihan == '4':
        #keluar dari kontak
         break
    else:
        print("Anda memasukkan pilian yang salah!")