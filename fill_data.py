from datetime import datetime, timedelta
import faker
import sqlite3
from random import randint, choice

NUMBER_STUDENTS = 40
NUMBER_GROUPS = 3
NUMBER_DISCIPLINES = 6
NUMBER_TEACHERS = 5
NUMBER_GRADES = 400

def generate_fake_data(number_students, number_groups, number_disciplines, number_teachers, number_grades):
    fake_students = []
    fake_groups = []
    fake_disciplines = []
    fake_teachers = []
    fake_grades = []

    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_groups):
        fake_groups.append(fake_data.random_digit_not_null())

    for _ in range(number_disciplines):
        fake_disciplines.append(fake_data.localized_ean8())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_grades):
        fake_grades.append(fake_data.random_int(1, 12))
    return fake_students, fake_groups, fake_disciplines, fake_teachers, fake_grades


def prepare_data(students, groups, disciplines, teachers, grades):
    for_students = []
    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS) ))

    for_groups = []
    for group in groups:
        for_groups.append((group, ))

    for_disciplines = []
    for discipline in disciplines:
        for_disciplines.append((discipline, randint(1, NUMBER_TEACHERS)))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher, ))

    for_grades = []
    count_students = 1
    count_grades = 0
    while count_students <= 40:
        if count_grades < 19:
            for_grades.append((choice(grades), datetime.now().date() - timedelta(randint(1, 250)), count_students,
                               randint(1, NUMBER_DISCIPLINES)))
            count_grades += 1
        else:
            for_grades.append((choice(grades), datetime.now().date() - timedelta(randint(1, 250)), count_students,
                               randint(1, NUMBER_DISCIPLINES)))
            count_grades = 0
            count_students += 1
    return for_students, for_groups, for_disciplines, for_teachers, for_grades


def insert_data_to_db(students, groups, disciplines, teachers, grades):
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()

        sql_to_students = '''INSERT INTO students(fullname, groups_id)
                            VALUES (?, ?)'''
        cur.executemany(sql_to_students, students)

        sql_to_groups = '''INSERT OR IGNORE INTO groups(name)
                        VALUES (?)'''
        cur.executemany(sql_to_groups, groups)

        sql_to_disciplines = '''INSERT INTO disciplines(name, teachers_id)  
                                VALUES (?, ?)'''
        cur.executemany(sql_to_disciplines, disciplines)

        sql_to_teachers = '''INSERT INTO teachers(fullname)
                            VALUES (?)'''
        cur.executemany(sql_to_teachers, teachers)

        sql_to_grades = '''INSERT INTO grades(grade, date_of, student_id, discipline_id)
                        VALUES (?, ?, ? , ?)'''
        cur.executemany(sql_to_grades, grades)

        con.commit()


def execute_query(sql):
    with open(sql, 'r') as base:
        sql = base.read()

    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


add_print_params = {
    1: '5 студентов с наибольшим средним баллом по всем предметам',
    2: 'студенты с наивысшим средним баллом по определенному предмету',
    3: 'средний балл в группах по определенному предмету',
    4: 'средний балл на потоке (по всей таблице оценок)',
    5: 'какие курсы читает определенный преподаватель',
    6: 'список студентов в определенной группе',
    7: 'оценки студентов в отдельной группе по определенному предмету.',
    8: 'средний балл, который ставит определенный преподаватель по своим предметам',
    9: 'список курсов, которые посещает определенный студент',
    10: 'Список курсов, которые определенному студенту читает определенный преподаватель'
}


def print_query_result(sql_file_number):
    print(add_print_params[sql_file_number])
    print(execute_query(f'{sql_file_number}.sql'))



def insert_db():
    students, groups, disciplines, teachers, grades = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS,
    NUMBER_DISCIPLINES, NUMBER_TEACHERS, NUMBER_GRADES))
    insert_data_to_db(students, groups, disciplines, teachers, grades)
