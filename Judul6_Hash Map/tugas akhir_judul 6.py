class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True

            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i

            else:
                if first_deleted != -1:
                    i = first_deleted

                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True

        return False

    def search(self, key):
        idx = self.hash_function(key)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.EMPTY:
                return None

            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]

        return None

    def remove_key(self, key):
        entry = self.search(key)

        if entry is None:
            return False

        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\n===== DATA MAHASISWA =====")

        for i in range(self.SIZE):
            if self.table[i].state == SlotState.OCCUPIED:
                print(
                    f"NPM: {self.table[i].key} | Nama: {self.table[i].value}"
                )


def main():
    mahasiswa = HashMapOpenAddressing()

    while True:
        print("\n===== MENU DATA MAHASISWA =====")
        print("1. Tambah Mahasiswa")
        print("2. Cari Mahasiswa")
        print("3. Hapus Mahasiswa")
        print("4. Tampilkan Semua Data")
        print("5. Keluar")

        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            npm = int(input("Masukkan NPM: "))
            nama = input("Masukkan Nama: ")

            if mahasiswa.insert(npm, nama):
                print("Data berhasil disimpan.")
            else:
                print("Hash Table penuh!")

        elif pilihan == 2:
            npm = int(input("Masukkan NPM yang dicari: "))

            hasil = mahasiswa.search(npm)

            if hasil:
                print(f"Data ditemukan")
                print(f"NPM  : {hasil.key}")
                print(f"Nama : {hasil.value}")
            else:
                print("Data tidak ditemukan.")

        elif pilihan == 3:
            npm = int(input("Masukkan NPM yang akan dihapus: "))

            if mahasiswa.remove_key(npm):
                print("Data berhasil dihapus.")
            else:
                print("Data tidak ditemukan.")

        elif pilihan == 4:
            mahasiswa.display()

        elif pilihan == 5:
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()