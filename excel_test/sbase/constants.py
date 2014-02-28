PERSON_TYPE_ADMIN = 0
PERSON_TYPE_PARENT = 1
PERSON_TYPE_STUDENT = 2
PERSON_TYPE_TEACHER = 3

PERSON_TYPE_ADMIN_STR = '0'
PERSON_TYPE_PARENT_STR = '1'
PERSON_TYPE_STUDENT_STR = '2'
PERSON_TYPE_TEACHER_STR = '3'


PERSON_TYPE_ID_DICT = {'Administrator':PERSON_TYPE_ADMIN, 
                    'Parent': PERSON_TYPE_PARENT, 
                    'Student': PERSON_TYPE_STUDENT,
                    'Teacher': PERSON_TYPE_TEACHER}

PERSON_TYPE_NAME_DICT = {PERSON_TYPE_ADMIN: 'Administrator', 
                    PERSON_TYPE_PARENT: 'Parent', 
                    PERSON_TYPE_STUDENT: 'Student',
                    PERSON_TYPE_TEACHER: 'Teacher',
                    PERSON_TYPE_ADMIN_STR: 'Administrator', 
                    PERSON_TYPE_PARENT_STR: 'Parent', 
                    PERSON_TYPE_STUDENT_STR: 'Student',
                    PERSON_TYPE_TEACHER_STR: 'Teacher'}

ALLOWED_TIME_INPUT_FORMATS = (
    '%H',     # '14:30'
    '%H:%M',     # '14:30'
    '%I %p',     # '2:30 PM'
    '%I:%M %p',     # '2:30 PM'
    '%H:%M:%S',     # '14:30'
    '%I:%M:%S %p',     # '2:30 PM'
)

GRADE_YEAR_CHOICES_DICT = {
    -2: 'Toddler / Primary-1',
    -1: 'Pre-K / Primary-2',
    0: 'Kindergarten / Primary-3',
    1: '1st Grade / Lower Elementary-1',
    2: '2nd Grade / Lower Elementary-2',
    3: '3rd Grade / Lower Elementary-3',
    4: '4th Grade / Upper Elementary-4',
    5: '5th Grade / Upper Elementary-5',
    6: '6th Grade / Upper Elementary-6',
    7: '7th Grade / Middle School-7',
    8: '8th Grade / Middle School-8',
    9: '9th Grade / Middle School-9',
}