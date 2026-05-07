def selection_sort(buku, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if buku[j].lower() < buku[min_idx].lower():
                min_idx = j

      
        if min_idx != i:
            buku[i], buku[min_idx] = buku[min_idx], buku[i]


def binary_search(buku, n, target):
    l = 0
    r = n - 1

    while l <= r:
        m = l + (r - l) // 2
        print(f"Sedang cek buku: {buku[m]}")

        if buku[m].lower() == target.lower():
            return m
        elif buku[m].lower() < target.lower():
            print("Mencari di kanan...")
            l = m + 1
        else:
            print("Mencari di kiri...")
            r = m - 1

    return -1


def main():
    try:
        n = int(input("Masukkan jumlah buku: "))
    except ValueError:
        print("Input tidak valid!")
        return

    buku = []
    print("\nMasukkan judul buku:")
    for i in range(n):
        judul = input(f"Buku ke-{i+1}: ")
        buku.append(judul)

    print("\n Buku Sebelum diurutkan:")
    print(buku)

    selection_sort(buku, n)

    print("\n Buku Setelah diurutkan (A-Z):")
    print(buku)

    target = input("\nMasukkan judul buku yang ingin dicari: ")


    pos = binary_search(buku, n, target)

    if pos != -1:
        if pos < n // 2:
            print(f"\n Buku '{target}' ditemukan pada indeks {pos} di area awal ")
        else:
            print(f"\n Buku '{target}' ditemukan pada indeks {pos} di area akhir ")
    else:
        print("\n Buku tidak ditemukan")


if __name__ == "__main__":
    main()