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


class ATM:
    def __init__(self):
        self.queue = Queue()

    def join_queue(self, person):
        self.queue.enqueue(person)
        print(f"{person} joined the ATM queue.")

    def process_transaction(self):
        if not self.queue.is_empty():
            person = self.queue.dequeue()
            print(f"{person} is currently processing their transaction.")
            self.check_next_person()
        else:
            print("No one in the queue.")

    def check_next_person(self):
        if not self.queue.is_empty():
            next_person = self.queue.peek()
            print(f"The next person in the queue is: {next_person}")
        else:
            print("Queue is empty.")

    def queue_size(self):
        return self.queue.size()



atm = ATM()

atm.join_queue("John")
atm.join_queue("Sarah")
atm.join_queue("Michael")
atm.join_queue("Emily")

print("\nCurrent queue size:", atm.queue_size())

print("\nProcessing transactions:")
atm.process_transaction()
atm.process_transaction()
atm.process_transaction()
atm.process_transaction()
atm.process_transaction()

print("\nCurrent queue size after processing:", atm.queue_size())
