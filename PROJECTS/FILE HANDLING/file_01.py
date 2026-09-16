students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 72}
]
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(sorted_students)