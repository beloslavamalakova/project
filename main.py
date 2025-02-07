
from algos.simple_algorithms import match_serial_dictatorship
from data.data_generation import generate_preferences

if __name__ == "__main__":
    students, colleges = generate_preferences(
        num_students=10, num_colleges=4, min_capacity=2, max_capacity=4, phi_students=0.5, phi_colleges=0.5
    )

    master_list = list(range(10))
    matching = match_serial_dictatorship(students, colleges, master_list)

    print("STUDENTS:")
    for student in students.values():
        print(student)

    print("\nCOLLEGES:")
    for college in colleges.values():
        print(college)

    print("\nMATCHING:")
    for student_id, college_id in matching.items():
        print(f"Student {student_id} matched to College {college_id}")
    