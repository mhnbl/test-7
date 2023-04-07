class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
  
    # Mengece apakah stack kosong
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
  
    # Method untuk menambahakan elemen ke stack ke paling atas
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
  
    # Menghapus elemen paling atas pada stack
    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
  
    # Print Stack
    def print(self):
        pointer = self.head
        if self.isempty():
            print("Tumpukan Kosong")
        else:
            while pointer is not None:
                print(f"- {pointer.data}")
                pointer = pointer.next
            return   

stack = Stack()

print("\nTumpukan Sebelum diubah:")
stack.print()

stack.push("Buku Ekonomi")
stack.push("Buku Seni Budaya")
stack.push("Buku Tulis")
stack.push("Buku Novel")
stack.push("Buku B.Inggris")

print("\n Buku setelah ditumpuk:")
stack.print()

print('\n Buku yang akan diambil dari tumpukan:')
print(stack.pop())
print(stack.pop())

print('\n Tumpukan setelah buku diambil:')
stack.print()

# stack = []
# #Menampilkan stack yang kososng
# print("\nTumpukan Buku")
# print(stack)

# #Menambahkan element keldalam stack (PUSH)
# stack.append('Buku IPA')
# stack.append('Buku Matematika')
# stack.append('Buku B.Indonesia')
# stack.append('Buku Ekonomi')
# stack.append('Buku Tulis')#TOP

# #Menampilkan Stack setelah ditambhan elemen
# print("\nBuku setelah ditumpuk:")
# x = len(stack)-1
# for i in range(len(stack)):
#     print(f'-{stack[x]}')
#     x -=1

# #Menampilkan elemen yang ingin dihapus (POP)
# print('\nBuku yang akan diambil dari tumpukan:')
# print(stack.pop())
# print(stack.pop())

# #Menampilkan Stack setelah dihapus
# print('\nTumpukan setelah buku diambil:')
# x = len(stack)-1
# for i in range(len(stack)):
#     print(f'-{stack[x]}')
#     x -=1





