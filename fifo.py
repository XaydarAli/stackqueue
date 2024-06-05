
class SupermarketCheckout:
    def __init__(self):
        self.queue = Queue()

    def enqueue_customer(self, customer):
        self.queue.enqueue(customer)
        print(f"{customer} joined the queue.")

    def dequeue_customer(self):
        if not self.queue.is_empty():
            customer = self.queue.dequeue()
            print(f"{customer} has been served and left the queue.")
            return customer
        else:
            print("Error: Queue is empty")

    def peek_next_customer(self):
        if not self.queue.is_empty():
            next_customer = self.queue.peek()
            print(f"Next customer in line: {next_customer}")
            return next_customer
        else:
            print("Error: Queue is empty")

    def queue_size(self):
        size = self.queue.size()
        print(f"Number of customers in queue: {size}")
        return size

    def is_checkout_open(self):
        if self.queue.is_empty():
            print("Checkout is currently closed.")
        else:
            print("Checkout is open and serving customers.")

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.items)
print(" SUPER MARKETDAGI KASSA MISOLI \n\n")
checkout = SupermarketCheckout()
checkout.is_checkout_open()
checkout.enqueue_customer("Alice")
checkout.enqueue_customer("Bob")
checkout.is_checkout_open()
checkout.queue_size()
checkout.peek_next_customer()
checkout.dequeue_customer()
checkout.dequeue_customer()
checkout.dequeue_customer()
print("\n\n")
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.items)

front_item = queue.dequeue()
print("Dequeued:", front_item)
print("Queue after dequeue:", queue.items)

peeked_item = queue.peek()
print("Peeked:", peeked_item)
print("Queue size:", queue.size())



