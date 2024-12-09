# main.py
from view.mahasiswa import ViewMahasiswa

def main():
    view_mhs = ViewMahasiswa()

    while True:
        print("\nMenu Utama")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Hapus Data Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            view_mhs.tambah_data()
        elif pilihan == "2":
            view_mhs.tampilkan_data()
        elif pilihan == "3":
            view_mhs.hapus_data()
        elif pilihan == "4":
            view_mhs.ubah_data()
        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
