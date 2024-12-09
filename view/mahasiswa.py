# view/mahasiswa.py
from data.mahasiswa import Mahasiswa
from view.input_form import InputForm

class ViewMahasiswa:
    def __init__(self):
        self.list_mahasiswa = []

    def tambah_data(self):
        nim, nama, jurusan = InputForm.input_data()
        mahasiswa_baru = Mahasiswa(nim, nama, jurusan)
        self.list_mahasiswa.append(mahasiswa_baru)
        print("Data berhasil ditambahkan!")

    def tampilkan_data(self):
        print("\nDaftar Mahasiswa:")
        for i, mhs in enumerate(self.list_mahasiswa, start=1):
            print(f"{i}. {mhs}")

    def hapus_data(self):
        self.tampilkan_data()
        try:
            idx = int(input("Masukkan nomor mahasiswa yang ingin dihapus: "))
            self.list_mahasiswa.pop(idx - 1)
            print("Data berhasil dihapus!")
        except (IndexError, ValueError):
            print("Nomor tidak valid.")

    def ubah_data(self):
        self.tampilkan_data()
        try:
            idx = int(input("Masukkan nomor mahasiswa yang ingin diubah: "))
            nim, nama, jurusan = InputForm.input_data()
            self.list_mahasiswa[idx - 1] = Mahasiswa(nim, nama, jurusan)
            print("Data berhasil diubah!")
        except (IndexError, ValueError):
            print("Nomor tidak valid.")
