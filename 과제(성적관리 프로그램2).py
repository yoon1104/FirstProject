#학생들 정보 저장 전역변수 
list_1=[]
list_2=[]
list_3=[]
list_4=[]
list_5=[]
list_6=[]
#학생들 기본정도 입력 받기
def v_input_s():
    student_id=input("학번: ")
    return student_id
def v_input_n():
    name=input("이름: ")
    return name
def v_input_e():
    english=int(input("영어: "))
    return english
def v_input_c():
    c_language=int(input("C-언어: "))
    return c_language
def v_input_p():
    python=int(input("파이썬: "))
    return python

#총점 구하기 - 사실상 안쓴다=list_6으로 대체        
def v_total(a,b,c):
    return a+b+c
#평균 구하기
def v_average(total):
    return total//3 #정수값만 받음

#학점 구하기
def v_grade(a):
    if a>90:
        grade='A+'
    elif a==90:
        grade='A'
    elif a>85:
        grade='A-'
    elif a>80:
        grade='B+'
    elif a==80:
        grade='B'
    elif a>=75:
        grade='B-'
    elif a>70:
        grade='C+'
    elif a==70:
        grade='C'
    elif a>=65:
        grade='C-'
    elif a>60:
        grade='D+'
    elif a==60:
        grade='D'
    elif a>55:
        grade='D-'
    else:
        grade='F'
    return grade

#삭제함수
def remove(list,i):
    return list.remove(i)

#탐색함수
def search_function(list_id,list_name):
    print("학번과 이름을 입력하세요")
    search_id = int(input("학번: "))
    search_name= input("이름 ")
    if search_id in list_id:
        print("값이 리스트에 있다")
    if search_name in list_name:
        print("값이 리스트에 있다")

#80점이상 학생 수 카운트 함수
def upstudent(list_t):
    count=0
    for i in list_t:
        if list_t[i]>=240:
            count+=i

    return count
        
#등수 구하기(내림차순으로 숫자가 낮을수록 +1)
def v_rank(scores):
    sorted_scores=sorted(scores,reverse = True) 
    ranks = [sorted_scores.index(s) + 1 for s in scores]
    
#같은 등수가 나올경우 같은 등수를 주기위한 코드(정렬함수->내림차순)
    rank_dict={}
    for idx, score in enumerate(sorted_scores):
        if score not in rank_dict:
            rank_dict[score]=idx+1
    return [rank_dict[score] for score in scores]

#출력
def v_output(student_id, name, english, c_language, python, total, average, grade, rank):
       print(f"{student_id:<10} {name:<10} {english:>4} {c_language:>9} {python:>8} {total:>9} {average:>9} {grade:^14} {rank:>0}") #칸수 맞추기 위해 범위 지정



#각 학생들마다 정보 저장(삽입함수)
def Insert_function():
    for i in range(5):
        list_1.append(v_input_s())
        list_2.append(v_input_n())
        list_3.append(v_input_e())
        list_4.append(v_input_c())
        list_5.append(v_input_p())
        list_6.append(v_total(list_3[i],list_4[i],list_5[i]))



def main():
    Insert_function()
    #등수로 변환한값 변수에 저장
    rankings=v_rank(list_6)

    print("                                    성적관리 프로그램                                   ")
    print("=======================================================================================")
    print("학번        이름          영어     C-언어   파이썬     총점      평균      학점    등수")
    print("=======================================================================================")

    
    for i in range(5):
        v_output(list_1[i],list_2[i],list_3[i],list_4[i],list_5[i],list_6[i],v_average(list_6[i]),v_grade(v_average(list_6[i])),rankings[i])

main()
