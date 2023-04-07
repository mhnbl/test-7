class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
 
    def isEmpty(self):
        return self.front == None
    
    def print(self):
        if self.front is None:
            print("Antrian Kosong")
        else:
            pointer = self.front
            while pointer is not None:
                print("|",pointer.data, end=" | ")
                pointer = pointer.next

    # Method untuk mneambahkan elemen
    def enQueue(self, item):
        temp = Node(item)
 
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
        
 
    # Method untuk menghapus elemen
    def deQueue(self):
 
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if(self.front == None):      
            self.rear = None
 
que = Queue()

#Print Queue saat kososng
print("\nAntrian Bank Syariah Indonesia")


#Menambah elemen yang akan dimasukan ke queue 
que.enQueue("A23")
que.enQueue("A24")
que.enQueue("A25")
que.enQueue("A26")
que.enQueue("A27")


#Menampilkan Queue yang telah ditambhakan
print("\nNomor Antrian yang ada:")
que.print()

#Menghapus elemen pada Queue
que.deQueue()

print("\n\nNomor Antrian Setelah dipanggil:")
que.print()


# # Inisialisasi Queue
# queue = []
# print(f'\nNomor Antrian: {queue}')

# #Menambahakan elemen ke Queue (Enqueue)
# queue.append('A23') #Front
# queue.append('A24')
# queue.append('A25')
# queue.append('A26')
# queue.append('A27')
# queue.append('A28')

# #Menyatakan Queue sebeluan perubahan
# print("\nNomor Antrian: ")
# print(queue)
  
# # Menghapus elemen pada Queue (Dequeue)
# print("\nNomor Antrian yang akan dipanggil:")
# print(queue.pop(0))

# #Hasil penghapausan elemen Queue
# print("\nSetelah nomor dipanggil: ")
# print(f'{queue}\n')