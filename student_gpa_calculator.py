student_id=str(input('Enter your student ID: '))
student_marks = float(input('Enter the marks for Programing: '))
student_marks1 = float(input('Enter the marks for Hardware: '))
student_marks2 = float(input('Enter the marks for Academic Writting: '))
student_marks3 = float(input('Enter the marks for French: '))
def grade_point():
    if 0.0 <= student_marks< 50.0 :
        return 0.00
    elif 50.0 <= student_marks <55.0:
        return 1.0
    elif 55.0 <= student_marks <60.0:
        return 1.5
    elif 60.0 <= student_marks <65.0:
        return 2.0
    elif 65.0 < student_marks <70.0:
        return 2.5
    elif 70.0 <= student_marks <75.0:
        return 3.0
    elif 75.0 <= student_marks <80.0:
        return 3.5
    elif 80 <= student_marks <= 100:
        return 4.0
    else:
        student_marks
def grade_point1():
    if 0.0 <= student_marks1< 50.0 :
        return 0.00
    elif 50.0 <= student_marks1 <55.0:
        return 1.0
    elif 55.0 <= student_marks1<60.0:
        return 1.5
    elif 60.0 <= student_marks1<65.0:
        return 2.0
    elif 65.0 < student_marks1 <70.0:
        return 2.5
    elif 70.0 <= student_marks1 <75.0:
        return 3.0
    elif 75.0 <= student_marks1 <80.0:
        return 3.5
    elif 80 <= student_marks1<= 100:
        return 4.0
    else:
        student_marks1
def grade_point2():
    if 0.0 <= student_marks2< 50.0 :
        return 0.00
    elif 50.0 <= student_marks2 <55.0:
        return 1.0
    elif 55.0 <= student_marks2<60.0:
        return 1.5
    elif 60.0 <= student_marks2<65.0:
        return 2.0
    elif 65.0 < student_marks2 <70.0:
        return 2.5
    elif 70.0 <= student_marks2 <75.0:
        return 3.0
    elif 75.0 <= student_marks2 <80.0:
        return 3.5
    elif 80 <= student_marks2 <= 100:
        return 4.0
    else:
        student_marks2
def grade_point3():
    if 0.0 <= student_marks3< 50.0 :
        return 0.00
    elif 50.0 <= student_marks3 <55.0:
        return 1.0
    elif 55.0 <= student_marks3 <60.0:
        return 1.5
    elif 60.0 <= student_marks3 <65.0:
        return 2.0
    elif 65.0 < student_marks3 <70.0:
        return 2.5
    elif 70.0 <= student_marks3 <75.0:
        return 3.0
    elif 75.0 <= student_marks3 <80.0:
        return 3.5
    elif 80 <= student_marks3 <= 100:
        return 4.0
    else:
        student_marks3
def grade_letter():
    if 0.0 <= student_marks< 50.0 :
        return 'F'
    elif 50.0 <= student_marks <55.0:
        return 'D'
    elif 55.0 <= student_marks <60.0:
        return 'D+'
    elif 60.0 <= student_marks <65.0:
        return 'C'
    elif 65.0 < student_marks <70.0:
        return 'C+'
    elif 70.0 <= student_marks <75.0:
        return 'B'
    elif 75.0 <= student_marks <80.0:
        return 'B+'
    elif 80 <= student_marks <= 100:
        return 'A'
    else:
        student_marks
def grade_letter1():
    if 0.0 <= student_marks1< 50.0 :
        return 'F'
    elif 50.0 <= student_marks1 <55.0:
        return 'D'
    elif 55.0 <= student_marks1<60.0:
        return 'D+'
    elif 60.0 <= student_marks1<65.0:
        return 'C'
    elif 65.0 < student_marks1<70.0:
        return 'C+'
    elif 70.0 <= student_marks1 <75.0:
        return 'B'
    elif 75.0 <= student_marks1<80.0:
        return 'B+'
    elif 80 <= student_marks1<= 100:
        return 'A'
    else:
        student_marks1
def grade_letter2():
    if 0.0 <= student_marks2< 50.0 :
        return 'F'
    elif 50.0 <= student_marks2 <55.0:
        return 'D'
    elif 55.0 <= student_marks2 <60.0:
        return 'D+'
    elif 60.0 <= student_marks2 <65.0:
        return 'C'
    elif 65.0 < student_marks2 <70.0:
        return 'C+'
    elif 70.0 <= student_marks2 <75.0:
        return 'B'
    elif 75.0 <= student_marks2 <80.0:
        return 'B+'
    elif 80 <= student_marks2 <= 100:
        return 'A'
    else:
        student_marks2
def grade_letter3():
    if 0.0 <= student_marks3< 50.0 :
        return 'F'
    elif 50.0 <= student_marks3 <55.0:
        return 'D'
    elif 55.0 <= student_marks3 <60.0:
        return 'D+'
    elif 60.0 <= student_marks3 <65.0:
        return 'C'
    elif 65.0 < student_marks3 <70.0:
        return 'C+'
    elif 70.0 <= student_marks3 <75.0:
        return 'B'
    elif 75.0 <= student_marks3 <80.0:
        return 'B+'
    elif 80 <= student_marks3 <= 100:
        return 'A'
    else:
        student_marks3

def weighted_grade_point():
    gpa_0 = grade_point()
    credit_hours0 = 3.00
    w_g_p_a = gpa_0 * credit_hours0
    return w_g_p_a
def weighted_grade_point1():
    gpa_0 = grade_point1()
    credit_hours0 = 3.00
    w_g_p_a = gpa_0 * credit_hours0
    return w_g_p_a
def weighted_grade_point2():
    gpa_0 = grade_point2()
    credit_hours0 = 3.00
    w_g_p_a = gpa_0 * credit_hours0
    return w_g_p_a
def weighted_grade_point3():
    gpa_0 = grade_point3()
    credit_hours0 = 3.00
    w_g_p_a = gpa_0 * credit_hours0
    return w_g_p_a

def student_SGPA ():
    wgpa=weighted_grade_point()
    wgpa0=weighted_grade_point1()
    wgpa1=weighted_grade_point2()
    wgpa2=weighted_grade_point3()
    sum0=wgpa+wgpa0+wgpa1+wgpa2
    sum1= 12.00
    SGPA = sum0 / sum1
    print(SGPA)
    return SGPA

wgpa=weighted_grade_point()
wgpa0=weighted_grade_point1()
wgpa1=weighted_grade_point2()
wgpa2=weighted_grade_point3()
sum0=wgpa+wgpa0+wgpa1+wgpa2

def semester_class():
    SGPA = student_SGPA()
    if 0.0 <= SGPA < 1:
        return 'Fail'
    elif 1.00 <= SGPA <2.0:
        return 'Pass'
    elif 2.00 <= SGPA <2.50:
        return 'Third Class'
    elif 2.50 <= SGPA <3.00:
        return 'Second class lower'
    elif 3.00 <= SGPA < 3.60:
        return 'Second class lower'
    elif 3.60 <= SGPA <= 4.00:
        return 'Second class lower'
    else:
        return SGPA
    

def output_():
    student_id0=student_id
    student_marks0=str(student_marks )
    sum1=str(sum0)
    student_SGPA0=str(student_SGPA())
    semester_class0=str(semester_class())
    student_marks_1 = str(student_marks1)
    student_marks_2 = str(student_marks2)
    student_marks_3 = str(student_marks3)
    grade_point0 =str(grade_point())
    grade_point_1 =str(grade_point1())
    grade_point_2 =str(grade_point2())
    grade_point_3 =str(grade_point3())
    grade_letter0=str(grade_letter())
    grade_letter_1 =str(grade_letter1())
    grade_letter_2 =str(grade_letter2())
    grade_letter_3 =str(grade_letter3()) 

    weighted_grade_point0 = str(weighted_grade_point())
    weighted_grade_point_1= str(weighted_grade_point1())
    weighted_grade_point_2= str(weighted_grade_point2())
    weighted_grade_point_3= str(weighted_grade_point3())
    print('')
    print('FIRST SEMESTER RESULTS')
    print('*************************')
    print('STUDENT ID: '+student_id0)
    print('Course Title        '+'Marks      '+ 'Grade      '+ 'CHrs     '+ 'GP      '+   'WGP                  ')
    print('******************************************************************************')
    print('Programing          ' + student_marks0+  '         '+ grade_letter0+ '         3      '+ grade_point0 + '     '+ weighted_grade_point0 )
    print('Hardware            ' + student_marks_1+ '         '+ grade_letter_1+'         3      '+ grade_point_1 +'     '+ weighted_grade_point_1 )
    print('Accademic Writing   ' + student_marks_2+ '         '+ grade_letter_2+'         3      '+ grade_point_2 +'     '+ weighted_grade_point_2 )
    print('French              ' + student_marks_3+ '         '+ grade_letter_3+'         3      '+ grade_point_3 +'     '+ weighted_grade_point_3 )
    print('*******************************************************************************')
    print('                                                                '+'CHrs = 12         ' + 'WGP='+ sum1 )
    print('SGPA:    '+ student_SGPA0)
    print('Semester Class: '+ semester_class0)
    print('---------------END OF RESULTS--------------')

output_()
list_yn=['YES']
new_student=input("Is there another student? yes or no : ").upper()
if new_student in list_yn:
    print(output_())