class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class LeaderboardBST:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)

        return root

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    def find_max(self, root):
        if root is None:
            return None

        current = root
        while current.right is not None:
            current = current.right

        return current.key

    def find_min(self, root):
        if root is None:
            return None

        current = root
        while current.left is not None:
            current = current.left

        return current.key


def main():
    leaderboard = LeaderboardBST()

    pilih = 0

    while pilih != 5:
        print("\n=== LEADERBOARD GAME ===")
        print("1. Tambah skor pemain")
        print("2. Tampilkan leaderboard")
        print("3. Lihat skor tertinggi")
        print("4. Lihat skor terendah")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            try:
                skor = int(input("Masukkan skor pemain: "))
                leaderboard.insert(skor)
                print("Skor berhasil ditambahkan!")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            print("Leaderboard (terendah -> tertinggi):")
            leaderboard.inorder(leaderboard.root)
            print()

        elif pilih == 3:
            max_score = leaderboard.find_max(leaderboard.root)

            if max_score is not None:
                print(f"Skor tertinggi (Juara 1): {max_score}")
            else:
                print("Leaderboard masih kosong")

        elif pilih == 4:
            min_score = leaderboard.find_min(leaderboard.root)

            if min_score is not None:
                print(f"Skor terendah: {min_score}")
            else:
                print("Leaderboard masih kosong")

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()