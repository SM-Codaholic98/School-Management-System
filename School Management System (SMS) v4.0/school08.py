import pickle
from datetime import date

stu={}
sch={}

def calculateAge(birthDate, year):
    today = date.today()
    age = year - birthDate.year - ((today.month, today.day) <(birthDate.month, birthDate.day)) 
    return age


def INSERT_STU_REC():
    f=open('SMS_STU.dat','rb')
    stu={}
    while True:
        try:
            stu=pickle.load(f)
        except EOFError:
            break
    f.close()
    
    print(stu)
    
    f=open('SMS_STU_EXAM_CC.dat','wb')
    ans='i'
    while ans.lower()=='i':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& INSERT STUDENT'S CO-CURRICULAR RECORD &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s_admno=int(input("Enter the admission number of the student to insert Student's CO-CURRICULAR RECORD: "))
        print()
        found=False
        for i in stu:
            if i==s_admno:
                found=True
                s_name=stu[i][0]
                print("Admission Number of",s_name,"is: ",s_admno)
                s_fn=stu[i][1]
                s_mn=stu[i][2]
                s_cls=stu[i][3]
                s_house=stu[i][25]
                s_sec=input("Enter Student's Section: ").upper()
                s_sex=stu[i][4]
                s_dob=stu[i][5]
                s_phno=stu[i][6]
                s_email=stu[i][7]
                s_add=stu[i][8]
                s_gen=input("Enter the student's grade in General Studies: ")
                s_wor=input("Enter the student's grade in Work Experience: ")
                s_gam=input("Enter the student's grade in Games & Sports: ")
                s_hf=input("Enter the student's grade in Health & Fitness: ")
                s_sew=input("Enter the student's grade in SEWA(social work done by the student): ")
                s_gol=input("Enter the student's GOAL(what you aspire to be): ")
                s_str=input("Enter the student's Strength: " )
                s_itr=input("Enter the student's Interest and Hobbies: ")
                s_res=input("Enter the student's Responsibilities Discharged or Exceptional Achievements: " )
                s_hgt=input("Enter the student's Height(in cm): " )
                s_wgt=input("Enter the student's Weight(in kgs): " )
                s_bg=input("Enter the student's Blood Group: ")
                s_vil=input("Enter the student's Vision(L): ")
                s_vir=input("Enter the student's Vision(R): ")
                s_dtl=input("Enter the student's Dental Hygine: ")
                
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_phno,s_email,s_add,2020,0,s_house,s_sec,s_gen,s_wor,s_gam,s_hf,s_sew,s_gol,s_str,s_itr,s_res,s_hgt,s_wgt,s_bg,s_vil,s_vir,s_dtl]
                
                pickle.dump(sch,f)
                
        if found==False:
            print("*** STUDENT'S RECORD HAS NOT BEEN FOUND !!! ***")
            print("--> Please provide the correct admission number of the student to store the Student's CO-CURRICULAR RECORD __/\__")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
        print()
        ans=input("Press 'i/I' to insert more Student's CO-CURRICULAR RECORD: ")
        print()
    f.close()


def DISPLAY_co_curi():
    f=open('SMS_STU_EXAM_CC.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='d'
    while ans.lower()=='d':
        ADMNO=int(input("Enter the admission number of the student to display the Student's CO-CURRICULAR DETAILS: "))
        print()
        print('-----------------------------------------------------------------------------------------------')
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% STUDENT'S CO-CURRICULAR DETAILS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print('-----------------------------------------------------------------------------------------------')
        print('%5s'%'SL','%7s'%'SUBJECT','%9s'%'GRADE')
        print('-----------------------------------------------------------------------------------------------')
        found=False      
        for i in sch:
         if i==ADMNO:
            print('%5s'%'1','%7s'%'GENERAL STUDIES','%9s'%sch[i][13])
            print('%5s'%'2','%7s'%'WORK EXPERIANCE','%9s'%sch[i][14])
            print('%5s'%'3','%7s'%'GAMES AND SPORTS','%9s'%sch[i][15])
            print('%5s'%'4','%7s'%'HEALTH & FITNESS','%9s'%sch[i][16])
            print('%5s'%'5','%7s'%'SEWA','%9s'%sch[i][17])
            print('-----------------------------------------------------------------------------------------------')
            print()
                            
            print("Student's GOAL(what you aspire to be) is: ",sch[i][18])
            print("Student's STREGTH is: ",sch[i][19])
            print("Student's INTERST AND HOOBIES are: ",sch[i][20])
            print("Student's  RESPONSIBILITES DISCHARGED/EXCEPTIONAL ACHIEVEMENTS is: ",sch[i][21])
            
            print()
            
            print("Student's HEIGHT is: ",sch[i][22])
            print("Student's WEIGHT is: ",sch[i][23])
            print("Student's BLOOD GROUP is: ",sch[i][24])
            print("Student's VISON(L) is: ",sch[i][25])
            print("Student's VISON(R) is: ",sch[i][26])
            print("Student's DENTAL HYGIENE is: ",sch[i][27])
            found=True
            print('-----------------------------------------------------------------------------------------------')
            
        if found==False:
         print("*** STUDENT'S RECORD HAS NOT BEEN FOUND !!! ***")
         print("--> Please provide the correct admission number of the student to display the Student's CO-CURRICULAR DETAILS __/\__")
         
        print()
        ans=input("Press 'd/D' to display more Student's CO-CURRICULAR DETAILS: ")
        print()
    f.close()