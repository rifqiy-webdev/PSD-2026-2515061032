def menu():
    print("=== Sistem Parkir ===")
    print("1. Masukkan kendaraan ke slot parkir")
    print("2. Keluarkan kendaraan dari slot parkir")
    print("3. Tampilkan kondisi parkir")
    print("4. Keluar")

def main():
    slots = [None] * 5  # untuk contoh kita buat 5 slot parkir
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            kosong = []
            for i, val in enumerate(slots):
                if val is None:
                    kosong.append(i)

            if len(kosong) == 0:
                print("Parkir penuh!")
            else:
                plat = input("Masukkan nomor plat kendaraan: ")
                slot = kosong[0]  # isi slot kosong pertama
                slots[slot] = plat
                print(f"Kendaraan {plat} diparkir di slot {slot+1}")  # tampilkan mulai dari 1

        elif choice == 2:
            plat = input("Masukkan nomor plat kendaraan yang keluar: ")
            if plat in slots:
                slot = slots.index(plat)
                slots[slot] = None
                print(f"Kendaraan {plat} keluar dari slot {slot+1}")
            else:
                print("Kendaraan tidak ditemukan di parkiran.")

        elif choice == 3:
            print("=== Kondisi Parkir ===")
            for i in range(5):
                if slots[i] is None:
                    print(f"Slot {i+1}: kosong")
                else:
                    print(f"Slot {i+1}: {slots[i]}")

        elif choice == 4:
            running = False
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
