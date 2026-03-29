# Assignment – Python Basics

## 1. Grade Checker

### Code:

```python
score = int(input("Enter your score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

### Explanation:

Uses if-elif-else conditions to assign grades based on score ranges.

---

## 2. Student Grades (Dictionary)

### Code:

```python
students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Student")
    print("3. View All Students")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade

    elif choice == "2":
        name = input("Enter student name: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
        else:
            print("Student not found")

    elif choice == "3":
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
```

### Output Screenshot:

(Add screenshot here)

### Explanation:

Uses a dictionary to store student names and grades with options to add, update, and display data.

---

## 3. Write to a File

### Code:

```python
file = open("sample.txt", "w")
file.write("Hello, this is a sample file.")
file.close()
```

### Explanation:

Creates a file and writes content using write mode.

---

## 4. Read from a File

### Code:

```python
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
```

### Explanation:

Reads content from a file and displays it using read mode.