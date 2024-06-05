class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)
print("Warning !!!!!! ⚠️⚠️⚠️⚠️⚠️⚠️\n Quyidagi misollarni hammasi ham hayotiy LIFO misollarga to'g'ri kelmasligi mumkin")
print("Customer Example>>>>>>>>>>>>>>>>>>>>>>>>>>")
customer = Stack()

customer.push('customer1')
customer.push('customer2')
customer.push('customer3')
customer.push('customer4')
customer.push('customer5')

print("Stack:", customer.items)

top_item = customer.pop()
print("Popped:", top_item)
print(" Customer Stack after pop:", customer.items)

peeked_item = customer.peek()
print("Peeked:", peeked_item)
print(" Customer Stack size:", customer.size())


print("Task Example>>>>>>>>>>>>>>>>>>>>>>>>>>")
task_stack = Stack()

task_stack.push("Write report")
task_stack.push("Prepare presentation")
task_stack.push("Review project proposal")
task_stack.push("Call client")
task_stack.push("Reply to emails")
task_stack.push("Research new ideas")

print("To-Do List :", task_stack.items)

print("\nLet's start completing tasks:")
while not task_stack.is_empty():
    next_task = task_stack.peek()
    print("Next task:", next_task)
    completed_task = task_stack.pop()
    print("Completed:", completed_task)

print("\nAll tasks completed! Remaining tasks:", task_stack.size())







print("Python Course Example>>>>>>>>>>>>>>>>>>>>>>>>>>")
python_backend = Stack()

python_backend.push("Foundation")
python_backend.push("Python Basics")
python_backend.push("Object oriented programming with python")
python_backend.push("Database(Postgresql)")
python_backend.push("Python Advanced")

print("Python Course modules :", python_backend.items)

print("\nLet's start completing modules:")
while not python_backend.is_empty():
    next_module = python_backend.peek()
    print("Next module:", next_module)
    completed_module = python_backend.pop()
    print("Completed:", completed_module)

print("\nAll tasks completed! Remaining tasks:", python_backend.size())
print("\n\n")


print("Message Example>>>>>>>>>>>>>>>>>>>>>>>>>>")
message = Stack()

message.push("Hello")
message.push("Teacher")
message.push("How are you doing ?")
message.push("I hope you are doing well ")
message.push("I wanted to ask you something")


print("New messages :", message.items)

print("\nOrder of new messages:")
while not message.is_empty():
    next_message = message.peek()
    print("Last message:", next_message)
    read_message = message.pop()
    print("Completed:", read_message)

print("\nAll messages are read ! Remaining unread messages:", message.size())

print("Phone_calls Example>>>>>>>>>>>>>>>>>>>>>>>>>>")
phone_calls = Stack()
phone_calls.push("Mother")
phone_calls.push("Friend")
phone_calls.push("Coursmate")
phone_calls.push("Teacher")
phone_calls.push("Brother")



print("Recent phone calls :", phone_calls.items)

print("\nOrder of new income calls:")
while not phone_calls.is_empty():
    next_call = phone_calls.peek()
    print("Last income call:", next_call)
    answered_call = phone_calls.pop()
    print("Answered call:", answered_call)

print("\nAll messages are read ! Remaining unread messages:", phone_calls.size())
print("\n")




class PlateStack:
    def __init__(self):
        self.plates = []

    def is_empty(self):
        return len(self.plates) == 0

    def put_plate_on_top(self, plate):
        self.plates.append(plate)

    def take_plate_from_top(self):
        if not self.is_empty():
            return self.plates.pop()
        else:
            print("Error: Stack is empty")

    def view_top_plate(self):
        if not self.is_empty():
            return self.plates[-1]
        else:
            print("Error: Stack is empty")

    def stack_size(self):
        return len(self.plates)


plate_stack = PlateStack()

plate_stack.put_plate_on_top("Plate 1")
plate_stack.put_plate_on_top("Plate 2")
plate_stack.put_plate_on_top("Plate 3")

print("Plates at the buffet:", plate_stack.plates)

taken_plate = plate_stack.take_plate_from_top()
print("Plate taken by a customer:", taken_plate)
print("Plates left at the buffet after taking:", plate_stack.plates)

removed_plate = plate_stack.take_plate_from_top()
print("Plate removed by staff:", removed_plate)
print("Plates left at the buffet after removal:", plate_stack.plates)
