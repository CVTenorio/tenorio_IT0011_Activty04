import csv
import os

def grade_calculation(class_standing, major_exam):
    return 0.6 * class_standing + 0.4 * major_exam

def record_display(record):
    print(f"Student ID: {record[0]}")
    print(f"Student Name: {record[1][0]} {record[1][1]}")
    print(f"Class Standing: {record[2]}")
    print(f"Major Exam Grade: {record[3]}")
    print(f"Final Grade: {grade_calculation(record[2], record[3]):.2f}")
    print("-" * 20)

def file_open(records, filename):
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader:
                records.append((int(row[0]), (row[1], row[2]), float(row[3]), float(row[4])))
        print(f"File '{filename}' opened successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def file_save(records, filename):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Student ID', 'First Name', 'Last Name', 'Class Standing', 'Major Exam Grade'])
            for record in records:
                writer.writerow([record[0], record[1][0], record[1][1], record[2], record[3]])
        print(f"File '{filename}' saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")   

def save_as_file(records):
    filename = input("Enter the new filename (e.g., students.csv): ")
    file_save(records, filename)

def display_all_students_order_by_lastname(records):
    sorted_records = sorted(records, key=lambda x: x[1][1])
    for record in sorted_records:
        record_display(record)

def display_all_students_order_by_grade(records):
    sorted_records = sorted(records, key=lambda x: grade_calculation(x[2], x[3]), reverse=True)
    for record in sorted_records:
        record_display(record)

def display_student_record(records, student_id):
    found = False
    for record in records:
        if record[0] == student_id:
            record_display(record)
            found = True
            break
    if not found:
        print("Student ID not found.")

def add_record(records):
    try:
        student_id = int(input("Enter Student ID (6 digits): ")) 
        if len(str(student_id)) != 6:
            print("Student ID must be 6 digits.")
            return
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = float(input("Enter Class Standing: "))
        major_exam = float(input("Enter Major Exam Grade: "))      
    
        records.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully.")
    except ValueError:
        print("Invalid input. Please enter valid numbers for ID and Grades.")

def edit_record(records, student_id):
    for i, record in enumerate(records):
        if record[0] == student_id:
            try:
                first_name = input("Enter First Name (press enter to keep current): ")
                last_name = input("Enter Last Name (press enter to keep current): ")
                class_standing = input("Enter Class Standing (press enter to keep current): ")
                major_exam = input("Enter Major Exam Grade (press enter to keep current): ")
                
                first_name = first_name if first_name else record[1][0]
                last_name = last_name if last_name else record[1][1]
                class_standing = float(class_standing) if class_standing else record[2]
                major_exam = float(major_exam) if major_exam else record[3]
                
                records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
                print("Record updated successfully.")
                return
            except ValueError:
                print("Invalid input. Please enter valid numbers for grades.")
    print("Student ID not found.")

def delete_record(records, student_id):
    for i, record in enumerate(records):
        if record[0] == student_id:
            del records[i]
            print("Record deleted successfully.")
            return
    print("Student ID not found.")

def main():
    records = []
    filename = ""
    
    while True:
        print("\nRecord Management Program")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students (Order by Last Name)")
        print("5. Show All Students (Order by Grade)")
        print("6. Show Student Record")
        print("7. Add Record")
        print("8. Edit Record")
        print("9. Delete Record")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            filename = input("Enter filename: ")
            file_open(records, filename)
        elif choice == '2':
            if filename:
                file_save(records, filename)
            else:
                print("Please open a file first.")
        elif choice == '3':
            save_as_file(records)
        elif choice == '4':
            display_all_students_order_by_lastname(records)
        elif choice == '5':
            display_all_students_order_by_grade(records)
        elif choice == '6':
            try:
                student_id = int(input("Enter Student ID: "))
                display_student_record(records, student_id)
            except ValueError:
                print("Invalid input. Please enter a valid student ID.")
        elif choice == '7':
            add_record(records)
        elif choice == '8':
            try:
                student_id = int(input("Enter Student ID to edit: "))
                edit_record(records, student_id)
            except ValueError:
                print("Invalid input. Please enter a valid student ID.")
        elif choice == '9':
            try:
                student_id = int(input("Enter Student ID to delete: "))
                delete_record(records, student_id)
            except ValueError:
                print("Invalid input. Please enter a valid student ID.")
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
