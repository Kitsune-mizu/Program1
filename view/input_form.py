# view/input_form.py
class InputForm:
    @staticmethod
    def input_data():
        print("Masukkan Data Mahasiswa")
        nim = input("NIM: ")
        nama = input("Nama: ")
        jurusan = input("Jurusan: ")
        return nim, nama, jurusan
