# Kelas Node
class Node:
    def __init__(self, data):
        self.data = data         # Menyimpan nilai data dari node
        self.prev = None         # Pointer ke node sebelumnya
        self.next = None         # Pointer ke node selanjutnya

# Kelas DoubleLinkedList
class DoubleLinkedList:
    def __init__(self):
        self.head = None         # Pointer ke node pertama dari linked list

# Menambahkan Node (append)
    def append(self, data):
        new_node = Node(data)    # Buat node baru dengan data
        if not self.head:        # Jika list kosong
            self.head = new_node
            return
        curr = self.head
        while curr.next:         # Iterasi sampai akhir list
            curr = curr.next
        curr.next = new_node     # Set next dari node terakhir ke new_node
        new_node.prev = curr     # Set prev dari new_node ke node terakhir

# Menampilkan Isi Linked List
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

# Menghapus Node Awal
    def delete_awal(self):
        if not self.head:                    # List kosong
            print("Linked list kosong!")
            return
        if not self.head.next:              # Hanya ada 1 node
            self.head = None
        else:
            self.head = self.head.next      # Geser head ke node berikutnya
            self.head.prev = None           # Putuskan hubungan ke node lama

# Menghapus Node Akhir
    def delete_akhir(self):
        if not self.head:
            print("Linked list kosong!")
            return
        curr = self.head
        if not curr.next:                   # Hanya ada satu node
            self.head = None
            return
        while curr.next:                    # Cari node terakhir
            curr = curr.next
        curr.prev.next = None               # Putuskan hubungan dengan node terakhir

# Menghapus Node Berdasarkan Nilai
    def delete_berdasarkan_nilai(self, target):
        if not self.head:
            print("Linked list kosong!")
            return

        curr = self.head

        if curr.data == target:
            self.delete_awal()              # Hapus jika target ada di head
            return

        while curr:
            if curr.data == target:
                if curr.next:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                else:
                    curr.prev.next = None   # Hapus jika node terakhir
                return
            curr = curr.next
        print(f"Data {target} tidak ditemukan dalam linked list.")

# Contoh Penggunaan
dll = DoubleLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

# Menampilkan dan Menghapus Node
print("Linked list awal:")
dll.display()

print("\nHapus node awal:")
dll.delete_awal()
dll.display()

print("\nHapus node akhir:")
dll.delete_akhir()
dll.display()

print("\nHapus node dengan nilai 20:")
dll.delete_berdasarkan_nilai(20)
dll.display()

print("\nCoba hapus data yang tidak ada (50):")
dll.delete_berdasarkan_nilai(50)