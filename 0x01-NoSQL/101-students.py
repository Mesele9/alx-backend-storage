#!/usr/bin/env python3
""" Top students """


def top_students(mongo_collection):
    """ a Python function that returns all students sorted by average score"""
    students = mongo_collection.find()

    for student in students:
        total_score = 0
        count = 0
        for topic in student['topics']:
            total_score += topic['score']
            count += 1

        student['averageScore'] = round(total_score / count, 2)

    students_sorted = sorted(students, key=lambda x: x['averageScore'],
                             reverse=True)

    return students_sorted

