
nameList=["David Jackson","Steven Son","Trevor Philips","Andy Camaron"]
lessonList=["Math","Physics","Music","Programming","Chemistry"]
count=3
isTrue=False
choose=0
studentLessonCount=0
studentLesson=[]
option=""
index=1

def showResult(lessonName,note):
    text=f"{lessonName} passed this lesson. Grade Note: "
    if note>90:
        text+="AA"
    elif note>70:
        text+="BB"
    elif note>50:
        text+="CC"
    elif note>30:
        text+="DD"
    else:
        text=f"{lessonName} failed this lesson.Grade Note:FF "
    return text

for i in range(0,3):
    nameInput=input("Please your enter first and last name: ")
    for name in nameList:
        if name==nameInput :
            isTrue=True
            print("Welcome")
            break
    if isTrue:
        break
    count = count - 1
    if count==0:
        print("Please try again later")
        exit()
    print("Wrong name,try again!")

for lesson in lessonList:
    print(f"{index}-{lesson}") 
    index+=1
for y in range(0,5):
    choose=int(input("Please enter lesson number:"))
    studentLesson.append(lessonList[choose-1])
    studentLessonCount+=1
    option=input("Could you select continue lesson ? Y / N")
    if option=="N" or option=="n":
        break
    if studentLessonCount==5:
        break
if studentLessonCount<3:
    print("You failed in class")
    exit()

print(studentLesson)

mathDict={}
pyhDict={}
muDict={}
cheDict={}
proDict={}
total=0

for lesson in studentLesson:
    print(lesson)
    midterm=float(input("Midterm: "))
    final=float(input("Final: "))
    project=float(input("Project: "))
    if lesson=="Math":
            mathDict["midterm"]=midterm
            mathDict["final"]=final
            mathDict["project"]=project
            total=(midterm*0.3) + (final*0.5) + (project*0.2) 
            print(showResult(lesson,total))
    elif lesson=="Physics":
            pyhDict["midterm"]=midterm
            pyhDict["final"]=final
            pyhDict["project"]=project
            total=(midterm*0.3) + (final*0.5) + (project*0.2) 
            print(showResult(lesson,total))
    elif lesson=="Music":
            muDict["midterm"]=midterm
            muDict["final"]=final
            muDict["project"]=project
            total=(midterm*0.3) + (final*0.5) + (project*0.2) 
            print(showResult(lesson,total))
    elif lesson=="Chemistry":
            cheDict["midterm"]=midterm
            cheDict["final"]=final
            cheDict["project"]=project
            total=(midterm*0.3) + (final*0.5) + (project*0.2) 
            print(showResult(lesson,total))
    elif lesson=="Programming":
            proDict["midterm"]=midterm
            proDict["final"]=final
            proDict["project"]=project
            total=(midterm*0.3) + (final*0.5) + (project*0.2) 
            print(showResult(lesson,total))
        




    


