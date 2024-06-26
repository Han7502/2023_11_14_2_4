import random

#建立一個function
def getStudents(student_nums:int=1, scores_nums:int=2) -> list[list]:
    '''
    參數:student_nums ->學生人數\n
    參數:scores_nums ->科目數
    '''
   
    with open('names.txt',mode='r',encoding='utf-8') as file:
        names:str = file.read()

    nameList:list[str]=names.split('\n')
    students:list[list] = []
    names:list[str] = random.choices(nameList, k=student_nums)
    for name in names:
        stu:list[int|str] = []
        stu.append(name)
        for i in range(scores_nums):
            stu.append(random.randint(40,100))
        students.append(stu)
    return students
