
students_info = [[], [], [], []]

# 함수 이름은 변경 가능합니다.


def Menu1(name, mid_score, final_score):
    # 사전에 학생 정보 저장하는 코딩
    students_info[0].append(name)
    students_info[1].append(int(mid_score))
    students_info[2].append(int(final_score))

# menu 2


def Menu2(grad_info):
    for i in range(len(grad_info[0])):
        mid_score = grad_info[1][i]
        final_score = grad_info[2][i]
        grade = (mid_score+final_score)/2
        if grade >= 90:
            students_info[3][i] = 'A'
        elif grade >= 80:
            students_info[3][i] = 'B'
        elif grade >= 80:
            students_info[3][i] = 'C'
        else:
            students_info[3][i] = 'D'
    # 학점 부여 하는 코딩

# menu 3


def Menu3(students_info):
    # 출력 코딩
    print('--------------------')
    print('name  mid  final  grade ')
    print('--------------------')
    for i in range(len(students_info[0])):
        print(students_info[0][i], students_info[1][i],
              students_info[2][i], students_info[3][i])

# menu 4


def Menu4(delete_name, students_info):
    # 학생 정보 삭제하는 코딩
    a = students_info.index(delete_name)
    for i in range(4):
        del students_info[i][a]


# 학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True:
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        # 학생 정보 입력받기
        info_student = input('Enter name mid-score final-score')
        name = info_student.split(' ')[0]
        mid_score = info_student.split(' ')[1]
        final_score = info_student.split(' ')[2]
        # 예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        if float(mid_score) % 1 != 0 and float(final_score) % 1 != 0:
            print("Wrong number. Choose again")
        # 예외사항이 아닌 입력인 경우 1번 함수 호출
        else:
            Menu1(name, mid_score, final_score)

    elif choice == "2":
        # 예외사항 처리(저장된 학생 정보의 유무)
        if len(students_info[0]) == 0:
            print('No student data!')
        else:
            Menu2(students_info)
            print('Grading to all students')

    elif choice == "3":
        # 예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        if len(students_info[0]) == len(students_info[3]) and len(students_info[0]) > 0:
            Menu3(students_info)
        # 예외사항이 아닌 경우 3번 함수 호출
        else:
            if len(students_info[0]) == 0:
                print('No student data!')
            else:
                print('There is a student who didnt get grade')

    elif choice == "4":
        # 예외사항 처리(저장된 학생 정보의 유무)
        if len(students_info[0]) == 0:
            print('No student data!')
        # 예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        else:
            delete_name = input('Enter the name to delete : ')
        # 입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        # 있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
            if delete_name in students_info[0]:
                Menu4(delete_name, students_info)
                print(f'{delete_name} student information is deleted.')
            else:
                print('Not exist name!')

    elif choice == "5":
        # 프로그램 종료 메세지 출력
        # 반복문 종료
        print("Exit Program!")
        break

    else:
        # "Wrong number. Choose again." 출력
        print("Wrong number. Choose again")
