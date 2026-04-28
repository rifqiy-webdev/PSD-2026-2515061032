def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort(rating, nama, n):
    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            if rating[j] > rating[pos]:  # terbesar dulu
                pos = j

        if pos != i:
            tukar(rating, i, pos)
            tukar(nama, i, pos)


def main():
    try:
        n = int(input("Masukkan jumlah tempat: "))
    except ValueError:
        print("Input tidak valid!")
        return

    nama = []
    rating = []

    for i in range(n):
        print("\nData ke-", i + 1)
        nama.append(input("Nama tempat: "))
        
        while True:
            try:
                nilai = float(input("Rating: "))
                rating.append(nilai)
                break
            except ValueError:
                print("Masukkan angka yang valid!")

    print("\n=== Sistem Rekomendasi Tempat Magang berdasarkan Rating Tertinggi ===")

    print("\nSebelum diurutkan:")
    for i in range(n):
        print(nama[i], "-", rating[i])

    selection_sort(rating, nama, n)

    print("\nSetelah diurutkan:")
    for i in range(n):
        print(nama[i], "-", rating[i])


if __name__ == "__main__":
    main()