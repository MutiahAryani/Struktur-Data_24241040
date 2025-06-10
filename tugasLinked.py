class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def tambah_di_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def hapus_awal(self):
        if self.head is None:
            print("List kosong")
            return

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
        print("Node awal dihapus")

    def hapus_akhir(self):
        if self.head is None:
            print("List kosong")
            return

        if self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None
        print("Node akhir dihapus")

    def hapus_berdasarkan_nilai(self, nilai):
        if self.head is None:
            print("List kosong")
            return

        temp = self.head
        while temp:
            if temp.data == nilai:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                print(f"Node dengan nilai {nilai} dihapus")
                return
            temp = temp.next
        print(f"Node dengan nilai {nilai} tidak ditemukan")

    def tampilkan(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Contoh penggunaan
dll = DoubleLinkedList()
dll.tambah_di_akhir(10)
dll.tambah_di_akhir(20)
dll.tambah_di_akhir(30)
dll.tambah_di_akhir(40)

print("Sebelum penghapusan:")
dll.tampilkan()

dll.hapus_awal()
dll.hapus_akhir()
dll.hapus_berdasarkan_nilai(20)

print("Setelah penghapusan:")
dll.tampilkan()