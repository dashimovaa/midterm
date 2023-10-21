 # task 1
while True:
    name = input("Enter your name please: ")
    salary_input = input("Enter your desired salary level: ")

    if salary_input.isdigit():
        salary = int(salary_input)
        tax_level = salary * 0.2
        print(f"{name}, the tax level you will pay with the salary {salary} is {tax_level}")
        break
    else:
        print(f"{name}, please enter your desired salary as a digit.")

# task 2
print("Please choose the operation you want to perform:")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Exponentiation")

def perform_operation(choice, numbers):
     if choice == 1:
         return sum(numbers)
     elif choice == 2:
         result = 1
         for num in numbers:
             result *= num
         return result
     elif choice == 3:
         result = numbers[0]
         for num in numbers[1:]:
             if num == 0:
                 return "Division by zero is not allowed."
             result /= num
         return result
     elif choice == 4:
         return numbers[0] ** numbers[1]
     else:
         return "Invalid choice."
try:
     choice = int(input())

     if choice in (1, 2, 3, 4):
         input_str = input(f"Please enter two numbers for the chosen operation, comma separated: ")
         numbers = [float(x) for x in input_str.split(',')]

         result = perform_operation(choice, numbers)
         print(result)
     else:
         print("Invalid choice. Please select a valid operation (1, 2, 3, or 4).")
except ValueError:
     print("Please enter valid numbers for the operation.")


# task 3

def generate_fibonacci(length):
    if length <= 0:
        return []
    elif length == 1:
        return [1]
    elif length == 2:
        return [1, 1]
    else:
        fibonacci_sequence = [1, 1]
        while len(fibonacci_sequence) < length:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)
        return fibonacci_sequence

try:
    user_input = int(input("Please enter the length of Fibonacci sequence: "))
    if user_input <= 0:
        print("Please enter a positive integer for the sequence length.")
    else:
        fibonacci_sequence = generate_fibonacci(user_input)
        print(f"The Fibonacci sequence for {user_input} is")
        print(', '.join(map(str, fibonacci_sequence)))
except ValueError:
    print("Please enter a valid integer for the sequence length.")

#task 4
unique_items = set()
non_unique_items = []

while True:
    print("1. Enter items")
    print("2. Exit")

    choice = input()

    if choice == '1':
        input_str = input("Enter items separated by commas: ")
        items = [item.strip() for item in input_str.split(',')]
        items_set = set(items)

        unique_items.update(items_set)

        for item in items_set:
            count = items.count(item)
            if count > 1:
                non_unique_items.append((item, count))

        print("Items are saved")
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please select 1 or 2.")

print("Unique items:", unique_items)
print("Non-unique items:", tuple(non_unique_items))

#task5
try:

    tasks = []

    while True:
        print("\nTo-Do List Manager:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task) # сейчас поясню за append, это такая штука которая добавляет к уже существующему внтури tasks
            print("Task added: ", task)

        elif choice == "2":
            if not tasks:
                print("No tasks in the list.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "3":
            if not tasks:
                print("No tasks to mark as completed.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    task_number = int(input("Enter the task number to mark as completed: ")) - 1
                    if 0 <= task_number < len(tasks):
                        print(f"Task '{tasks[task_number]}' marked as completed.")
                        tasks.pop(task_number)
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Enter a valid task number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")
except ValueError:
    print("Error: ")





