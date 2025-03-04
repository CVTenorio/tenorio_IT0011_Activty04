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
    print ("-" * 20) 
    
def file_open(records, filename):
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None) 
            for row in reader:
                records.append((int (row[0]), (row[1], row[2]), float(row[3]), float(row[4])))
        print(f"File '{filename}' opened successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found")
    except Exception as e:
        print(f"An error occured: {e}")

def file_save(records, filename):
    try:
        with open(filename, 'w' newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Student ID', 'First Name', 'Last Name', 'Class Standing', 'Major Exam Grade'])
            for record in records:
                writer.writerow([record[0], record[1][0], record[1][1], record[2], record[3]])
        print(f"File '{filename}' saved successfully.")
    except Exception as e:
        print(f"An error occuredL {e}")   
        
def save_as_file(records):
    filename = input("Enter the new filename (e.g., students.csv): ")
    file_save(records, filename)
    
def display_all_students_order_by_lastname(records):
    sorted_records = sorted(records, key=lambda x: x[1][1])
    for record in sorted_records:
        display_record(record)

def display_student_record(records, student_id):
    found = False
    for record in records:
        if record[0] == student_id:
            record_display(record)
            found = True
            break
    if not found:
        print("Student ID not found. ")

def add_record(records):
    try:
        student_id = int(input("Enter Student ID (6 digits): ")) 
        if len(str(student_id)) != 6:
            print("Student ID must be 6 digits.")
            return
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = float(input("Enter Class Standing: "))
        major_exam = float(input("Enter Major Exam Grade:"))      
    
        records.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully, ")
    except ValueError:
        print("Invalid input. Please enter valid numbers for ID and Grades.")
        
def edit_record(records, student_id):
    for i, record in enumerate(records):
        if record[0] == student_id:
            try:
                first_name = input("Enter First Name: ")
                last_name = input ("Enter Last Name: ")
                class_standing = input("Enter Class Standing: ")
                major_exam = input ("Enter Major Exam Grade: ")
                
                if first_name:
                    records[i] = (records[i][0], (first_name, records[i][1][1]), records[i][2], records[i][3])
                if last_name:
                    records[i] = (records[i][0], (last_name, records[i][1][1]), records[i][2], records[i][3])   
                if class_standing:
                    records[i] = (records[i][0], records[i][1], float(class_standing), records[i][3])
                if major_exam:
                    records[i] = (records[i][0], records[i][1], records[i][2], float(major_exam))
                
                print("Record updated successfully.")
                return
            except ValueError:
                print("Invalid input. Please enter valid numbers for grades.")
    print("Student ID not found.")
    
def delete_record(records, student_id):
    """Deletes a student record."""
    for i, record in enumerate(records):
        if record[0] == student_id:
            del records[i]
            print("Record deleted successfully.")
            return
    print("Student ID not found.") 
    
def main():
    records = []
    filename = ""         
    
    