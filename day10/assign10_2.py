class Node:
    def __init__(self, emp_id):
        self.emp_id = emp_id
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert Employee ID
    def insert(self, emp_id):
        new_node = Node(emp_id)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print("Employee Inserted")

    # Display Employee IDs
    def display(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head
        while temp:
            print(temp.emp_id, end=" -> ")
            temp = temp.next
        print("None")

    # Search Employee ID
    def search(self, emp_id):
        temp = self.head

        while temp:
            if temp.emp_id == emp_id:
                print("Employee Found")
                return
            temp = temp.next

        print("Employee Not Found")

    # Delete Employee ID
    def delete(self, emp_id):
        temp = self.head

        if temp and temp.emp_id == emp_id:
            self.head = temp.next
            print("Employee Deleted")
            return

        prev = None

        while temp and temp.emp_id != emp_id:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Employee Not Found")
            return

        prev.next = temp.next
        print("Employee Deleted")

    # Count Employees
    def count(self):
        c = 0
        temp = self.head

        while temp:
            c += 1
            temp = temp.next

        print("Total Employees:", c)

    # Reverse Linked List
    def reverse(self):
        prev = None
        current = self.head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev
        print("Linked List Reversed")


# Main Program
ll = LinkedList()

while True:
    print("\n1. Insert")
    print("2. Display")
    print("3. Search")
    print("4. Delete")
    print("5. Count")
    print("6. Reverse")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        ll.insert(emp_id)

    elif choice == 2:
        ll.display()

    elif choice == 3:
        emp_id = int(input("Enter Employee ID to Search: "))
        ll.search(emp_id)

    elif choice == 4:
        emp_id = int(input("Enter Employee ID to Delete: "))
        ll.delete(emp_id)

    elif choice == 5:
        ll.count()

    elif choice == 6:
        ll.reverse()

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")