def calculate_average(marks):
    return sum(marks) / len(marks)


def find_grade(average):
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def input_marks(number_of_subjects):
    marks = []

    for subject_number in range(1, number_of_subjects + 1):
        mark = float(input(f"Enter marks for subject {subject_number}: "))

        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100.")

        marks.append(mark)

    return marks


def main():
    print("Student Grade Calculator")

    try:
        subject_count = int(input("Enter the number of subjects: "))

        if subject_count <= 0:
            raise ValueError("Number of subjects must be positive.")

        marks = input_marks(subject_count)
        average = calculate_average(marks)
        grade = find_grade(average)

        print(f"\nTotal marks: {sum(marks):.2f}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()