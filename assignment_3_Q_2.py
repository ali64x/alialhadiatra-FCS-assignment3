class Car:
    def __init__(self, make, color, plate_number):
        self.make = make
        self.color = color
        self.plate_number = plate_number

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, car):
        self.items.append(car)
        
    def isEmpty(self):
        return len(self.items) == 0

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)

    def front(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            return None

car_queue = Queue()

while True: # O(n) n being the number of cars the user decides to add to the queue i.e the number of tries before he decides to enter 3 
    print("Car Wash Program Menu:")
    print("1. Insert a car to the queue")
    print("2. Remove the car from the queue")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        make = input("Enter the car's make: ")
        color = input("Enter the car's color: ")
        plate_number = int(input("Enter the car's plate number: "))
        new_car = Car(make, color, plate_number)
        car_queue.enqueue(new_car)# add the new car to the queue 
        print(f"Car {make} {color} with plate number {plate_number} added to the queue.")

    elif choice == '2':
        if not car_queue.isEmpty():
            removed_car = car_queue.dequeue()
            print(f"Car {removed_car.make} {removed_car.color} with plate number {removed_car.plate_number} removed from the queue.")
        else:
            print("Queue is empty. No cars to remove.")

    elif choice == '3':
        break

    else:
        print("Invalid choice. Please select a valid option.")

print("Car wash program closed.")
