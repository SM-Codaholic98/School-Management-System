import pickle
import random
from datetime import date

sch={}

def calculateAge(birthDate, year):
    today = date.today()
    age = year - birthDate.year - ((today.month, today.day) <(birthDate.month, birthDate.day)) 
    return age


def INSERT_STU_REC():
    f=open('SMS_STU.dat','wb')
    ans='i'
    while ans.lower()=='i':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& INSERT STUDENT'S RECORD &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s_admno=random.randint(1000,9999)
        s_name=input("Enter the student's Full Name: ")
        print("Admission Number of",s_name,"is: ",s_admno)
        s_fn=input("Enter the student's Father's Name: ")
        s_mn=input("Enter the student's Mother's Name: ")
        s_gn=input("Enter the student's Guardian's Name: ")
        s_cls=input("Enter the student's class: ").upper()
        s_sex=input("Enter the student's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
        s_dob=input("Enter the student's Date Of Birth (DD/MM/YYYY): ")
        
        print()
        print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
        s_fphno=int(input("Enter the student's Father's Mobile/Phone Number: +91 "))
        s_mphno=int(input("Enter the student's Mother's Mobile/Phone Number: +91 "))
        s_gcno=int(input("Enter the student's Guardian's Contact Number: +91 "))
        print()
        
        s_email=input("Enter the student's Father's/Mother's Email Address: ")
        s_add=input("Enter the student's House Address: ")
        
        print()
        s_bus=input('''--x--x-- NOTE: Bus service will be available for the student, if the distance(in Km) between student's house address and school is less 31Km --x--x--
                    Whether the student wants to avail for the bus service, Enter 'Yes/No': ''').upper()
        s_dist=eval(input("Enter the distance(in Km) between student's House Address and School: "))
        if s_dist>=31:
            print()
            print("~~~ If distance(in Km) between student's house address and school is equal to or more than 31 km, then bus service is not available for the student admission number-",s_admno,"and student name-",s_name,"~~~")
            s_bus='NO'
            
        s_house=random.choice(['Gandhi','Hansraj','Dayanand','Tagore','Netaji','Patel'])
        
        found_cls=False
        found_sex=False
        found_email=False
        found_fphno=False
        found_mphno=False
        found_gcno=False
        
        if len(str(s_fphno))==10:
            sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
            found_fphno=True
        else:
            print()
            print("~~~ Invalid mobile/phone number of the student's father has been entered !!! ~~~")
            print("--> Please provide the valid mobile/phone number of the student's father to store the student's details __/\__")
            print()
            print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
            s_fphno=int(input("Enter the student's Father's Mobile/Phone Number: +91 "))
            if len(str(s_fphno))==10:
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
                found_fphno=True
            else:
                print()
                found_fphno=False
                print("~~~ Invalid mobile/phone number of the student's father's has been entered !!! ~~~")
                
        if len(str(s_mphno))==10:
            sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
            found_mphno=True
        else:
            print()
            print("~~~ Invalid mobile/phone number of the student's mother's has been entered !!! ~~~")
            print("--> Please provide the valid mobile/phone number of the student's mother's to store the student's details __/\__")
            print()
            print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
            s_mphno=int(input("Enter the student's Mother's Mobile/Phone Number: +91 "))
            if len(str(s_mphno))==10:
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
                found_mphno=True
            else:
                print()
                found_mphno=False
                print("~~~ Invalid mobile/phone number of the student's mother's has been entered !!! ~~~")
                
        if len(str(s_gcno))==10:
            sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
            found_gcno=True
        else:
            print()
            print("~~~ Invalid contact number of the student's guardian's has been entered !!! ~~~")
            print("--> Please provide the valid contact number of the student's guardian's to store the student's details __/\__")
            print()
            print("// Note:- Contact number must be of 10 digits (without ISD code) //")
            s_gcno=int(input("Enter the student's Guardian's Contact Number: +91 "))
            if len(str(s_gcno))==10:
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
                found_gcno=True
            else:
                print()
                found_gcno=False
                print("~~~ Invalid contact number of the student's guardian's has been entered !!! ~~~")
        
        if s_cls=='LKG' or s_cls=='UKG' or s_cls=='1' or s_cls=='ONE' or s_cls=='I' or s_cls=='2' or s_cls=='TWO' or s_cls=='II' or s_cls=='3' or s_cls=='THREE' or s_cls=='III' or s_cls=='4' or s_cls=='FOUR' or s_cls=='IV' or s_cls=='5' or s_cls=='FIVE' or s_cls=='V' or s_cls=='6' or s_cls=='SIX' or s_cls=='VI' or s_cls=='7' or s_cls=='SEVEN' or s_cls=='VII' or s_cls=='8' or s_cls=='EIGHT' or s_cls=='VIII' or s_cls=='9' or s_cls=='NINE' or s_cls=='IX' or s_cls=='10' or s_cls=='TEN' or s_cls=='X' or s_cls=='11' or s_cls=='ELEVEN' or s_cls=='XI' or s_cls=='12' or s_cls=='TWELEVE' or s_cls=='XII':
            sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
            found_cls=True
        else:
            print()
            print("~~~ Invalid class of the student has been entered !!! ~~~")
            print("--> Please provide the valid class of the student to store the student's details __/\__")
            print()
            s_cls=input("Enter the student's Class: ").upper()
            if s_cls=='LKG' or s_cls=='UKG' or s_cls=='1' or s_cls=='ONE' or s_cls=='I' or s_cls=='2' or s_cls=='TWO' or s_cls=='II' or s_cls=='3' or s_cls=='THREE' or s_cls=='III' or s_cls=='4' or s_cls=='FOUR' or s_cls=='IV' or s_cls=='5' or s_cls=='FIVE' or s_cls=='V' or s_cls=='6' or s_cls=='SIX' or s_cls=='VI' or s_cls=='7' or s_cls=='SEVEN' or s_cls=='VII' or s_cls=='8' or s_cls=='EIGHT' or s_cls=='VIII' or s_cls=='9' or s_cls=='NINE' or s_cls=='IX' or s_cls=='10' or s_cls=='TEN' or s_cls=='X' or s_cls=='11' or s_cls=='ELEVEN' or s_cls=='XI' or s_cls=='12' or s_cls=='TWELEVE' or s_cls=='XII':
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
                found_cls=True
            else:
                print()
                found_cls=False
                print("~~~ Invalid class of the student has been entered !!! ~~~")
                
        if s_sex=='MALE' or s_sex=='FEMALE' or s_sex=='THIRD GENDER' or s_sex=='M' or s_sex=='F' or s_sex=='TG' :
            sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
            found_sex=True
        else:
            print()
            print("~~~ Invalid sex of the student has been entered !!! ~~~")
            print("--> Please provide the valid sex of the student to store the student's details __/\__")
            print()
            s_sex=input("Enter the student's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
            if s_sex=='MALE' or s_sex=='FEMALE' or s_sex=='THIRD GENDER' or s_sex=='M' or s_sex=='F' or s_sex=='TG' :
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
                found_sex=True
            else:
                print()
                found_sex=False
                print("~~~ Invalid sex of the student has been entered !!! ~~~")
                
        if '@' and '.com' in s_email:
            sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
            found_email=True
        else:
            print()
            print("~~~ Student's father's/mother's email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the student's father/mother to store the student's details __/\__")
            print()
            s_email=input("Enter the student's Father's/Mother's Email Address: ")
            if '@' and '.com' in s_email:
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
                found_email=True
            else:
                print()
                found_email=False
                print("~~~ Student's father's/mother's email address doesn't contain '@' or '.com' !!! ~~~")
                
        if found_cls==True and found_sex==True and found_email==True and found_fphno==True and found_mphno==True and found_gcno==True:
            pickle.dump(sch,f)
            print()
            print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY INSERTED !!! ***")
        else:
            print()
            print("*** STUDENT'S RECORD HAS NOT BEEN INSERTED !!! ***")
            print("--> Something went wrong in provided data, please provide the proper data of the student to store the student's record __/\__")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        print()
        ans=input("Press 'i/I' to insert more student's record: ")
        print()
    f.close()
    
    
def COMPUTE_STU_FEE():
    f=open('SMS_STU.dat','rb+')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='c'
    while ans.lower()=='c':
     ADMNO=int(input("Enter the admission number of the student to compute the Student's FEE STRUCTURE: "))
     found=False
     for i in sch:
       if i==ADMNO:
        found=True
        sch[i][9]=sch[i][9]+1
        spl = sch[i][5].split('/')
        s_d = int(spl[0])
        s_m = int(spl[1])
        s_y = int(spl[2])
        s_age = calculateAge(date(s_y, s_m, s_d), sch[i][9])
        sch[i][10] = s_age
        if sch[i][10]==4:
            if sch[i][3]=='LKG':
                tuition=2500
                hostel=0
                mess=0
                library=100
                laboratory=0
                development=5000
                exam=1000
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                peoples=2000
                miscellaneous=500
                monthly=tuition+hostel+mess+library+laboratory+development+exam+bus+peoples+miscellaneous
                annual=monthly*12
                sch[i][11]=tuition
                sch[i][12]=hostel
                sch[i][13]=mess
                sch[i][14]=library
                sch[i][15]=laboratory
                sch[i][16]=development
                sch[i][17]=exam
                sch[i][18]=bus
                sch[i][19]=peoples
                sch[i][20]=miscellaneous
                sch[i][21]=monthly
                sch[i][22]=annual
                
        elif sch[i][10]==5:
            if sch[i][3]=='UKG':
                sch[i][11]=2700
                sch[i][12]=0
                sch[i][13]=0
                sch[i][14]=100
                sch[i][15]=0
                sch[i][16]=5000
                sch[i][17]=1000
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                sch[i][18]=bus
                sch[i][19]=2000
                sch[i][20]=500
                sch[i][21]=sch[i][11]+sch[i][12]+sch[i][13]+sch[i][14]+sch[i][15]+sch[i][16]+sch[i][17]+sch[i][18]+sch[i][19]+sch[i][20]
                sch[i][22]=sch[i][21]*12
                
        elif sch[i][10]==6:
            if sch[i][3]=='ONE' or sch[i][3]=='1' or sch[i][3]=='I':
                sch[i][11]=2900
                sch[i][12]=0
                sch[i][13]=0
                sch[i][14]=150
                sch[i][15]=350
                sch[i][16]=5000
                sch[i][17]=1000
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                sch[i][18]=bus
                sch[i][19]=2000
                sch[i][20]=500
                sch[i][21]=sch[i][11]+sch[i][12]+sch[i][13]+sch[i][14]+sch[i][15]+sch[i][16]+sch[i][17]+sch[i][18]+sch[i][19]+sch[i][20]
                sch[i][22]=sch[i][21]*12
                
        elif sch[i][10]==7:
            if sch[i][3]=='TWO' or sch[i][3]=='2' or sch[i][3]=='II':
                sch[i][11]=3100
                sch[i][12]=0
                sch[i][13]=0
                sch[i][14]=200
                sch[i][15]=350
                sch[i][16]=5000
                sch[i][17]=1000
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                sch[i][18]=bus
                sch[i][19]=2000
                sch[i][20]=500
                sch[i][21]=sch[i][11]+sch[i][12]+sch[i][13]+sch[i][14]+sch[i][15]+sch[i][16]+sch[i][17]+sch[i][18]+sch[i][19]+sch[i][20]
                sch[i][22]=sch[i][21]*12
                
        elif sch[i][10]==8:
            if sch[i][3]=='THREE' or sch[i][3]=='3' or sch[i][3]=='III':
                sch[i][11]=3300
                sch[i][12]=0
                sch[i][13]=0
                sch[i][14]=250
                sch[i][15]=400
                sch[i][16]=5000
                sch[i][17]=1000
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                sch[i][18]=bus
                sch[i][19]=2000
                sch[i][20]=500
                sch[i][21]=sch[i][11]+sch[i][12]+sch[i][13]+sch[i][14]+sch[i][15]+sch[i][16]+sch[i][17]+sch[i][18]+sch[i][19]+sch[i][20]
                sch[i][22]=sch[i][21]*12
                
        elif sch[i][10]==9:
            if sch[i][3]=='FOUR' or sch[i][3]=='4' or sch[i][3]=='IV':
                sch[i][11]=3500
                sch[i][12]=0
                sch[i][13]=0
                sch[i][14]=300
                sch[i][15]=400
                sch[i][16]=5000
                sch[i][17]=1000
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                sch[i][18]=bus
                sch[i][19]=2000
                sch[i][20]=500
                sch[i][21]=sch[i][11]+sch[i][12]+sch[i][13]+sch[i][14]+sch[i][15]+sch[i][16]+sch[i][17]+sch[i][18]+sch[i][19]+sch[i][20]
                sch[i][22]=sch[i][21]*12
                
        elif sch[i][10]==10:
            if sch[i][3]=='FIVE' or sch[i][3]=='5' or sch[i][3]=='V':
                sch[i][11]=3700
                sch[i][12]=0
                sch[i][13]=0
                sch[i][14]=350
                sch[i][15]=450
                sch[i][16]=5000
                sch[i][17]=1000
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                sch[i][18]=bus
                sch[i][19]=2000
                sch[i][20]=500
                sch[i][21]=sch[i][11]+sch[i][12]+sch[i][13]+sch[i][14]+sch[i][15]+sch[i][16]+sch[i][17]+sch[i][18]+sch[i][19]+sch[i][20]
                sch[i][22]=sch[i][21]*12
                
        elif sch[i][10]==11:
            if sch[i][3]=='SIX' or sch[i][3]=='6' or sch[i][3]=='VI':
                print("~~~ Whether the Student wants to stay in school hostel, STUDENT'S ADMISSION NUMBER -",i,",STUDENT'S NAME -",sch[i][0],"and STUDENT'S CLASS -",sch[i][3],"Enter 'Yes/No' ~~~")
                h_choice=input("Enter the choice of the student: ").upper()
                if h_choice=='YES':
                    hostel=16000
                    mess=4000
                else:
                    hostel=0
                    mess=0
                sch[i][11]=3900
                sch[i][12]=hostel
                sch[i][13]=mess
                sch[i][14]=400
                sch[i][15]=450
                sch[i][16]=5000
                sch[i][17]=1000
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                sch[i][18]=bus
                sch[i][19]=2000
                sch[i][20]=500
                sch[i][21]=sch[i][11]+sch[i][12]+sch[i][13]+sch[i][14]+sch[i][15]+sch[i][16]+sch[i][17]+sch[i][18]+sch[i][19]+sch[i][20]
                sch[i][22]=sch[i][21]*12
                
        elif sch[i][10]==12:
            if sch[i][3]=='SEVEN' or sch[i][3]=='7' or sch[i][3]=='VII':
                print("~~~ Whether the Student wants to stay in school hostel, STUDENT'S ADMISSION NUMBER -",i,",STUDENT'S NAME -",sch[i][0],"and STUDENT'S CLASS -",sch[i][3],"Enter 'Yes/No' ~~~")
                h_choice=input("Enter the choice of the student: ").upper()
                if h_choice=='YES':
                    hostel=16000
                    mess=4000
                else:
                    hostel=0
                    mess=0
                sch[i][11]=4100
                sch[i][12]=hostel
                sch[i][13]=mess
                sch[i][14]=450
                sch[i][15]=500
                sch[i][16]=5000
                sch[i][17]=1000
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                sch[i][18]=bus
                sch[i][19]=2000
                sch[i][20]=500
                sch[i][21]=sch[i][11]+sch[i][12]+sch[i][13]+sch[i][14]+sch[i][15]+sch[i][16]+sch[i][17]+sch[i][18]+sch[i][19]+sch[i][20]
                sch[i][22]=sch[i][21]*12
                
        elif sch[i][10]==13:
            if sch[i][3]=='EIGHT' or sch[i][3]=='8' or sch[i][3]=='VIII':
                print("~~~ Whether the Student wants to stay in school hostel, STUDENT'S ADMISSION NUMBER -",i,",STUDENT'S NAME -",sch[i][0],"and STUDENT'S CLASS -",sch[i][3],"Enter 'Yes/No' ~~~")
                h_choice=input("Enter the choice of the student: ").upper()
                if h_choice=='YES':
                    hostel=16000
                    mess=4000
                else:
                    hostel=0
                    mess=0
                sch[i][11]=4300
                sch[i][12]=hostel
                sch[i][13]=mess
                sch[i][14]=500
                sch[i][15]=500
                sch[i][16]=5000
                sch[i][17]=1500
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                sch[i][18]=bus
                sch[i][19]=2000
                sch[i][20]=1000
                sch[i][21]=sch[i][11]+sch[i][12]+sch[i][13]+sch[i][14]+sch[i][15]+sch[i][16]+sch[i][17]+sch[i][18]+sch[i][19]+sch[i][20]
                sch[i][22]=sch[i][21]*12
                
        elif sch[i][10]==14:
            if sch[i][3]=='NINE' or sch[i][3]=='9' or sch[i][3]=='IX':
                print("~~~ Whether the Student wants to stay in school hostel, STUDENT'S ADMISSION NUMBER -",i,",STUDENT'S NAME -",sch[i][0],"and STUDENT'S CLASS -",sch[i][3],"Enter 'Yes/No' ~~~")
                h_choice=input("Enter the choice of the student: ").upper()
                if h_choice=='YES':
                    hostel=16000
                    mess=4000
                else:
                    hostel=0
                    mess=0
                sch[i][11]=4500
                sch[i][12]=hostel
                sch[i][13]=mess
                sch[i][14]=550
                sch[i][15]=1000
                sch[i][16]=5000
                sch[i][17]=1500
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                sch[i][18]=bus
                sch[i][19]=2000
                sch[i][20]=1000
                sch[i][21]=sch[i][11]+sch[i][12]+sch[i][13]+sch[i][14]+sch[i][15]+sch[i][16]+sch[i][17]+sch[i][18]+sch[i][19]+sch[i][20]
                sch[i][22]=sch[i][21]*12
                
        elif sch[i][10]==15:
            if sch[i][3]=='TEN' or sch[i][3]=='10' or sch[i][3]=='X':
                print("~~~ Whether the Student wants to stay in school hostel, STUDENT'S ADMISSION NUMBER -",i,",STUDENT'S NAME -",sch[i][0],"and STUDENT'S CLASS -",sch[i][3],"Enter 'Yes/No' ~~~")
                h_choice=input("Enter the choice of the student: ").upper()
                if h_choice=='YES':
                    hostel=16000
                    mess=4000
                else:
                    hostel=0
                    mess=0
                sch[i][11]=4700
                sch[i][12]=hostel
                sch[i][13]=mess
                sch[i][14]=600
                sch[i][15]=1000
                sch[i][16]=5000
                sch[i][17]=1500
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                sch[i][18]=bus
                sch[i][19]=2000
                sch[i][20]=1000
                sch[i][21]=sch[i][11]+sch[i][12]+sch[i][13]+sch[i][14]+sch[i][15]+sch[i][16]+sch[i][17]+sch[i][18]+sch[i][19]+sch[i][20]
                sch[i][22]=sch[i][21]*12
                
        elif sch[i][10]==16:
            if sch[i][3]=='ELEVEN' or sch[i][3]=='11' or sch[i][3]=='XI':
                print("~~~ Whether the Student wants to stay in school hostel, STUDENT'S ADMISSION NUMBER -",i,",STUDENT'S NAME -",sch[i][0],"and STUDENT'S CLASS -",sch[i][3],"Enter 'Yes/No' ~~~")
                h_choice=input("Enter the choice of the student: ").upper()
                if h_choice=='YES':
                    hostel=16000
                    mess=4000
                else:
                    hostel=0
                    mess=0
                sch[i][11]=4900
                sch[i][12]=hostel
                sch[i][13]=mess
                sch[i][14]=650
                sch[i][15]=2000
                sch[i][16]=5000
                sch[i][17]=1500
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                sch[i][18]=bus
                sch[i][19]=2000
                sch[i][20]=1200
                sch[i][21]=sch[i][11]+sch[i][12]+sch[i][13]+sch[i][14]+sch[i][15]+sch[i][16]+sch[i][17]+sch[i][18]+sch[i][19]+sch[i][20]
                sch[i][22]=sch[i][21]*12
                
        elif sch[i][10]==17:
            if sch[i][3]=='TWELEVE' or sch[i][3]=='12' or sch[i][3]=='XII':
                print("~~~ Whether the Student wants to stay in school hostel, STUDENT'S ADMISSION NUMBER -",i,",STUDENT'S NAME -",sch[i][0],"and STUDENT'S CLASS -",sch[i][3],"Enter 'Yes/No' ~~~")
                h_choice=input("Enter the choice of the student: ").upper()
                if h_choice=='YES':
                    hostel=16000
                    mess=4000
                else:
                    hostel=0
                    mess=0
                sch[i][11]=5100
                sch[i][12]=hostel
                sch[i][13]=mess
                sch[i][14]=700
                sch[i][15]=2000
                sch[i][16]=5000
                sch[i][17]=1500
                if sch[i][23]=='YES':
                    if sch[i][24]<1:
                        bus=0
                    elif sch[i][24]>=1 and sch[i][24]<6:
                        bus=1000
                    elif sch[i][24]>=6 and sch[i][24]<11:
                        bus=1035   # 5 km * 7
                    elif sch[i][24]>=11 and sch[i][24]<16:
                        bus=1105   # 5 km * 14
                    elif sch[i][24]>=16 and sch[i][24]<21:
                        bus=1190   # 5 km * 17
                    elif sch[i][24]>=21 and sch[i][24]<31:
                        bus=1290   # 5 km * 20
                    else:
                        sch[i][23]=='NO'
                else:
                    bus=0
                    sch[i][23]=='NO'
                sch[i][18]=bus
                sch[i][19]=2000
                sch[i][20]=1200
                sch[i][21]=sch[i][11]+sch[i][12]+sch[i][13]+sch[i][14]+sch[i][15]+sch[i][16]+sch[i][17]+sch[i][18]+sch[i][19]+sch[i][20]
                sch[i][22]=sch[i][21]*12
                
        else:
            print("-->",sch[i][0],"is above 17 years old, so the student can't be admitted to the school __/\__")
            
        pickle.dump(sch,f)
        
     if found==False:
        print("*** STUDENT'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct admission number of the student to compute the Student's FEE STRUCTURE __/\__")
        
     print()
     ans=input("Press 'c/C' to compute more Student's FEE STRUCTURE: ")
     print()
    f.close()
    
    
def DISP_ALL_STU_REC():
    f=open('SMS_STU.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
    print("{:<12} {:<12} {:<12} {:<12} {:<12} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("S_Admno",
                                                                                                                                                 "S_Name",
                                                                                                                                                 "S_Father's Name",
                                                                                                                                                 "S_Mother's Name",
                                                                                                                                                 "S_Class",
                                                                                                                                                 "S_House",
                                                                                                                                                 "S_Age",
                                                                                                                                                 "S_Sex",
                                                                                                                                                 "S_Phno.",
                                                                                                                                                 "S_Email address",
                                                                                                                                                 "S_House address",
                                                                                                                                                 "S_Tuition fee",
                                                                                                                                                 "S_Hostel fee",
                                                                                                                                                 "S_Mess fee",
                                                                                                                                                 "S_Library fee",
                                                                                                                                                 "S_Laboratory fee",
                                                                                                                                                 "S_Development fee",
                                                                                                                                                 "S_Exam fee",
                                                                                                                                                 "S_Bus fee",
                                                                                                                                                 "S_Peoples fund",
                                                                                                                                                 "S_Miscellaneous fee",
                                                                                                                                                 "S_Monthly fee",
                                                                                                                                                 "S_Annual fee",
                                                                                                                                                 "Year"))
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')      
    for j in sch:
        print("{:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(j,
                                                                                                                                                     sch[j][0],
                                                                                                                                                     sch[j][1],
                                                                                                                                                     sch[j][2],
                                                                                                                                                     sch[j][3],
                                                                                                                                                     sch[j][25],
                                                                                                                                                     sch[j][10],
                                                                                                                                                     sch[j][4],
                                                                                                                                                     sch[j][6],
                                                                                                                                                     sch[j][7],
                                                                                                                                                     sch[j][8],
                                                                                                                                                     sch[j][11],
                                                                                                                                                     sch[j][12],
                                                                                                                                                     sch[j][13],
                                                                                                                                                     sch[j][14],
                                                                                                                                                     sch[j][15],
                                                                                                                                                     sch[j][16],
                                                                                                                                                     sch[j][17],
                                                                                                                                                     sch[j][18],
                                                                                                                                                     sch[j][19],
                                                                                                                                                     sch[j][20],
                                                                                                                                                     sch[j][21],
                                                                                                                                                     sch[j][22],
                                                                                                                                                     sch[j][9]))
    f.close()
  
    
def APPEND_STU_REC():
    f=open('SMS_STU.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
    f.close()
    
    f=open('SMS_STU.dat','ab')
    ans='a'
    while ans.lower()=='a':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& APPEND STUDENT'S RECORD &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s_admno=random.randint(1000,9999)
        s_name=input("Enter the student's Full Name: ")
        print("Admission Number of",s_name,"is: ",s_admno)
        s_fn=input("Enter the student's Father's Name: ")
        s_mn=input("Enter the student's Mother's Name: ")
        s_gn=input("Enter the student's Guardian's Name: ")
        s_cls=input("Enter the student's class: ").upper()
        s_sex=input("Enter the student's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
        s_dob=input("Enter the student's Date Of Birth (DD/MM/YYYY): ")
        
        print()
        print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
        s_fphno=int(input("Enter the student's Father's Mobile/Phone Number: +91 "))
        s_mphno=int(input("Enter the student's Mother's Mobile/Phone Number: +91 "))
        s_gcno=int(input("Enter the student's Guardian's Contact Number: +91 "))
        print()
        
        s_email=input("Enter the student's Father's/Mother's Email Address: ")
        s_add=input("Enter the student's House Address: ")
        
        print()
        s_bus=input('''--x--x-- NOTE: Bus service will be available for the student, if the distance(in Km) between student's house address and school is less 31Km --x--x--
                    Whether the student wants to avail for the bus service, Enter 'Yes/No': ''').upper()
        s_dist=eval(input("Enter the distance(in Km) between student's House Address and School: "))
        if s_dist>=31:
            print()
            print("~~~ If distance(in Km) between student's house address and school is equal to or more than 31 km, then bus service is not available for the student admission number-",s_admno,"and student name-",s_name,"~~~")
            s_bus='NO'
            
        s_house=random.choice(['Gandhi','Hansraj','Dayanand','Tagore','Netaji','Patel'])
        
        found_cls=False
        found_sex=False
        found_email=False
        found_fphno=False
        found_mphno=False
        found_gcno=False
        
        if len(str(s_fphno))==10:
            sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
            found_fphno=True
        else:
            print()
            print("~~~ Invalid mobile/phone number of the student's father has been entered !!! ~~~")
            print("--> Please provide the valid mobile/phone number of the student's father to store the student's details __/\__")
            print()
            print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
            s_fphno=int(input("Enter the student's Father's Mobile/Phone Number: +91 "))
            if len(str(s_fphno))==10:
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
                found_fphno=True
            else:
                print()
                found_fphno=False
                print("~~~ Invalid mobile/phone number of the student's father's has been entered !!! ~~~")
                
        if len(str(s_mphno))==10:
            sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
            found_mphno=True
        else:
            print()
            print("~~~ Invalid mobile/phone number of the student's mother's has been entered !!! ~~~")
            print("--> Please provide the valid mobile/phone number of the student's mother's to store the student's details __/\__")
            print()
            print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
            s_mphno=int(input("Enter the student's Mother's Mobile/Phone Number: +91 "))
            if len(str(s_mphno))==10:
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
                found_mphno=True
            else:
                print()
                found_mphno=False
                print("~~~ Invalid mobile/phone number of the student's mother's has been entered !!! ~~~")
                
        if len(str(s_gcno))==10:
            sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
            found_gcno=True
        else:
            print()
            print("~~~ Invalid contact number of the student's guardian's has been entered !!! ~~~")
            print("--> Please provide the valid contact number of the student's guardian's to store the student's details __/\__")
            print()
            print("// Note:- Contact number must be of 10 digits (without ISD code) //")
            s_gcno=int(input("Enter the student's Guardian's Contact Number: +91 "))
            if len(str(s_gcno))==10:
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
                found_gcno=True
            else:
                print()
                found_gcno=False
                print("~~~ Invalid contact number of the student's guardian's has been entered !!! ~~~")
        
        if s_cls=='LKG' or s_cls=='UKG' or s_cls=='1' or s_cls=='ONE' or s_cls=='I' or s_cls=='2' or s_cls=='TWO' or s_cls=='II' or s_cls=='3' or s_cls=='THREE' or s_cls=='III' or s_cls=='4' or s_cls=='FOUR' or s_cls=='IV' or s_cls=='5' or s_cls=='FIVE' or s_cls=='V' or s_cls=='6' or s_cls=='SIX' or s_cls=='VI' or s_cls=='7' or s_cls=='SEVEN' or s_cls=='VII' or s_cls=='8' or s_cls=='EIGHT' or s_cls=='VIII' or s_cls=='9' or s_cls=='NINE' or s_cls=='IX' or s_cls=='10' or s_cls=='TEN' or s_cls=='X' or s_cls=='11' or s_cls=='ELEVEN' or s_cls=='XI' or s_cls=='12' or s_cls=='TWELEVE' or s_cls=='XII':
            sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
            found_cls=True
        else:
            print()
            print("~~~ Invalid class of the student has been entered !!! ~~~")
            print("--> Please provide the valid class of the student to store the student's details __/\__")
            print()
            s_cls=input("Enter the student's Class: ").upper()
            if s_cls=='LKG' or s_cls=='UKG' or s_cls=='1' or s_cls=='ONE' or s_cls=='I' or s_cls=='2' or s_cls=='TWO' or s_cls=='II' or s_cls=='3' or s_cls=='THREE' or s_cls=='III' or s_cls=='4' or s_cls=='FOUR' or s_cls=='IV' or s_cls=='5' or s_cls=='FIVE' or s_cls=='V' or s_cls=='6' or s_cls=='SIX' or s_cls=='VI' or s_cls=='7' or s_cls=='SEVEN' or s_cls=='VII' or s_cls=='8' or s_cls=='EIGHT' or s_cls=='VIII' or s_cls=='9' or s_cls=='NINE' or s_cls=='IX' or s_cls=='10' or s_cls=='TEN' or s_cls=='X' or s_cls=='11' or s_cls=='ELEVEN' or s_cls=='XI' or s_cls=='12' or s_cls=='TWELEVE' or s_cls=='XII':
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
                found_cls=True
            else:
                print()
                found_cls=False
                print("~~~ Invalid class of the student has been entered !!! ~~~")
                
        if s_sex=='MALE' or s_sex=='FEMALE' or s_sex=='THIRD GENDER' or s_sex=='M' or s_sex=='F' or s_sex=='TG' :
            sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
            found_sex=True
        else:
            print()
            print("~~~ Invalid sex of the student has been entered !!! ~~~")
            print("--> Please provide the valid sex of the student to store the student's details __/\__")
            print()
            s_sex=input("Enter the student's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
            if s_sex=='MALE' or s_sex=='FEMALE' or s_sex=='THIRD GENDER' or s_sex=='M' or s_sex=='F' or s_sex=='TG' :
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
                found_sex=True
            else:
                print()
                found_sex=False
                print("~~~ Invalid sex of the student has been entered !!! ~~~")
                
        if '@' and '.com' in s_email:
            sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
            found_email=True
        else:
            print()
            print("~~~ Student's father's/mother's email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the student's father/mother to store the student's details __/\__")
            print()
            s_email=input("Enter the student's Father's/Mother's Email Address: ")
            if '@' and '.com' in s_email:
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_fphno,s_email,s_add,2021,0,0,0,0,0,0,0,0,0,0,0,0,0,s_bus,s_dist,s_house,s_mphno,s_gn,s_gcno]
                found_email=True
            else:
                print()
                found_email=False
                print("~~~ Student's father's/mother's email address doesn't contain '@' or '.com' !!! ~~~")
                
        if found_cls==True and found_sex==True and found_email==True and found_fphno==True and found_mphno==True and found_gcno==True:
            pickle.dump(sch,f)
            print()
            print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY APPENDED !!! ***")
        else:
            print()
            print("*** STUDENT'S RECORD HAS NOT BEEN APPENDED !!! ***")
            print("--> Something went wrong in provided data, please provide the proper data of the student to store the student's record __/\__")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        print()
        ans=input("Press 'a/A' to append more student's record: ")
        print()
    f.close()
    
    
def SEARCH_STU_REC():
    f=open('SMS_STU.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='s'
    while ans.lower()=='s':
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("############################################################### SEARCH STUDENT'S RECORD ###############################################################")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     ADMNO=int(input("Enter the admission number of the student to search the student's record: "))
     found=False      
     for j in sch:
        if j==ADMNO:
            print("--x--x-- Provided admission number of the student is present in the database ...@ Press 8 to display the Student's FEE DETAILS --x--x--")
            found=True
            break
        
     if found==False:
        print("*** STUDENT'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct admission number of the student to search the student's record __/\__")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
     print()
     ans=input("Press 's/S' to search more student's record: ")
     print()
    f.close()
    
    
def UPDATE_STU_REC():
    f=open('SMS_STU.dat','rb+')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
    ans='u'
    while ans.lower()=='u':
     ADMNO=int(input("Enter the admission number of the student to update the student's record: "))
     found=False
     for j in sch:
        if j==ADMNO:
            
            ans='o'
            while ans.lower()=='o':
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ UPDATE STUDENT'S RECORD $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("--x--x-- STUDENT UPDATE MENU --x--x--")
                print("# Press 'n/N' to update the student's Full Name")
                print("# Press 'f/F' to update the student's Father's Name")
                print("# Press 'm/M' to update the student's Mother's Name")
                print("# Press 'j/J' to update the student's Guardian's Name")
                print("# Press 'g/G' to update the student's Gender")
                print("# Press 'dob/DOB' to update the student's Date Of Birth")
                print("# Press 'fpn/FPN' to update the student's Father's Mobile/Phone Number")
                print("# Press 'mpn/MPN' to update the student's Mother's Mobile/Phone Number")
                print("# Press 'gcn/GCN' to update the student's Guardian's contact Number")
                print("# Press 'e/E' to update the student's Father's/Mother's Email Address")
                print("# Press 'a/A' to update the student's House Address")
                print("# Press 'b/B' to update the student's Bus avail choice, ('Yes/No')")
                print("# Press 'd/D' to update the Distance between student's house address and school")
                print("# Press 'h/H' to update the student's House")
                print("# Press 'c/C' to update the student's Class")
                ch=input("Enter the choice of the student from the STUDENT UPDATE MENU: ").upper()
                
                if ch=='N':
                    print()
                    n=input("Enter the updated Full Name of the student: ")
                    sch[j][0]=n
                    print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='F':
                    print()
                    f=input("Enter the updated Father's Name of the student: ")
                    sch[j][1]=f
                    print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='M':
                    print()
                    m=input("Enter the updated Mother's Name of the student: ")
                    sch[j][2]=m
                    print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='J':
                    print()
                    j=input("Enter the updated Guardian's Name of the student: ")
                    sch[j][27]=j
                    print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='DOB':
                    print()
                    dob=input("Enter the updated Date Of Birth of the student: ")
                    sch[j][5]=dob
                    print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='G':
                    print()
                    g=input("Enter the updated Gender of the student as either MALE or M, FEMALE or F, THIRD GENDER or TG: ")
                    if g=='MALE' or g=='FEMALE' or g=='THIRD GENDER' or g=='M' or g=='F' or g=='TG' :
                        sch[j][4]=g
                        print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STUDENT'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid sex of the student has been entered !!! ~~~")
                        print("--> Please provide the valid sex of the student to update the field of the student's sex __/\__")
                        print()
                        g=input("Enter the updated Gender of the student as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
                        if g=='MALE' or g=='FEMALE' or g=='THIRD GENDER' or g=='M' or g=='F' or g=='TG' :
                            sch[j][4]=g
                            print("*** NOW STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STUDENT'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid sex of the student has been entered !!! ~~~")
                            
                elif ch=='FPN':
                    print()
                    print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
                    fpn=int(input("Enter the updated Mobile/Phone Number of the student's father: +91 "))
                    if len(str(fpn))==10:
                        sch[j][6]=fpn
                        print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STUDENT'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid mobile/phone number of the student's father has been entered !!! ~~~")
                        print("--> Please provide the valid mobile/phone number of the student's father to update the field of the student's father's mobile/phone number __/\__")
                        print()
                        print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
                        fpn=int(input("Enter the updated Mobile/Phone Number of the student's father: +91 "))
                        if len(str(fpn))==10:
                            sch[j][6]=fpn
                            print("*** NOW STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STUDENT'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid mobile/phone number of the student's father has been entered !!! ~~~")
                            
                elif ch=='MPN':
                    print()
                    print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
                    mpn=int(input("Enter the updated Mobile/Phone Number of the student's mother: +91 "))
                    if len(str(mpn))==10:
                        sch[j][26]=mpn
                        print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STUDENT'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid mobile/phone number of the student's mother has been entered !!! ~~~")
                        print("--> Please provide the valid mobile/phone number of the student's mother to update the field of the student's mother's mobile/phone number __/\__")
                        print()
                        print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
                        mpn=int(input("Enter the updated Mobile/Phone Number of the student's mother: +91 "))
                        if len(str(mpn))==10:
                            sch[j][26]=mpn
                            print("*** NOW STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STUDENT'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid mobile/phone number of the student's mother has been entered !!! ~~~")
                            
                elif ch=='GCN':
                    print()
                    print("// Note:- Contact number must be of 10 digits (without ISD code) //")
                    gcn=int(input("Enter the updated Contact Number of the student's guardian: +91 "))
                    if len(str(gcn))==10:
                        sch[j][28]=gcn
                        print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STUDENT'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid contact number of the student's guardian has been entered !!! ~~~")
                        print("--> Please provide the valid contact number of the student's guardian to update the field of the student's guardian's contact number __/\__")
                        print()
                        print("// Note:- Contact number must be of 10 digits (without ISD code) //")
                        gcn=int(input("Enter the updated Contact Number of the student's guardian: +91 "))
                        if len(str(gcn))==10:
                            sch[j][28]=gcn
                            print("*** NOW STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STUDENT'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid contact number of the student's guardian has been entered !!! ~~~")
                    
                elif ch=='E':
                    print()
                    e=input("Enter the updated Email Address of the student's father/mother: ")
                    if '@' and '.com' in s_email:
                        sch[j][7]=e
                        print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STUDENT'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Student's Father's/Mother's Email Address doesn't contain '@' or '.com' !!! ~~~")
                        print("--> Please provide the proper Email Address of the student's father/mother to update the field of the student's father's/mother's email address __/\__")
                        print()
                        s_email=input("Enter the updated Email Address of the student's father/mother: ")
                        if '@' and '.com' in s_email:
                            sch[j][7]=e
                            print("*** NOW STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STUDENT'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Student's Father's/Mother's Email Address doesn't contain '@' or '.com' !!! ~~~")
                            
                elif ch=='A':
                    print()
                    a=input("Enter the updated House Address of the student: ")
                    sch[j][8]=a
                    print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='B':
                    print()
                    b=input("Update, whether the student wants to avail for bus service, Enter 'Yes/No': ").upper()
                    sch[j][23]=b
                    print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='D':
                    print()
                    d=float(input("Enter the updated Distance(in Km) between student's House Address and School: "))
                    sch[j][24]=d
                    print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='H':
                    print()
                    h=input("Enter the updated House of the student: ")
                    sch[j][25]=h
                    print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='C':
                    print()
                    c=input("Enter the updated Class of the student: ").upper()
                    if s_cls=='LKG' or s_cls=='UKG' or s_cls=='1' or s_cls=='ONE' or s_cls=='I' or s_cls=='2' or s_cls=='TWO' or s_cls=='II' or s_cls=='3' or s_cls=='THREE' or s_cls=='III' or s_cls=='4' or s_cls=='FOUR' or s_cls=='IV' or s_cls=='5' or s_cls=='FIVE' or s_cls=='V' or s_cls=='6' or s_cls=='SIX' or s_cls=='VI' or s_cls=='7' or s_cls=='SEVEN' or s_cls=='VII' or s_cls=='8' or s_cls=='EIGHT' or s_cls=='VIII' or s_cls=='9' or s_cls=='NINE' or s_cls=='IX' or s_cls=='10' or s_cls=='TEN' or s_cls=='X' or s_cls=='11' or s_cls=='ELEVEN' or s_cls=='XI' or s_cls=='12' or s_cls=='TWELEVE' or s_cls=='XII':
                        sch[j][3]=c
                        print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STUDENT'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid class of the student has been entered !!! ~~~")
                        print("--> Please provide the valid class of the student to update the field of the student's class __/\__")
                        print()
                        s_cls=input("Enter the updated Class of the student: ").upper()
                        if s_cls=='LKG' or s_cls=='UKG' or s_cls=='1' or s_cls=='ONE' or s_cls=='I' or s_cls=='2' or s_cls=='TWO' or s_cls=='II' or s_cls=='3' or s_cls=='THREE' or s_cls=='III' or s_cls=='4' or s_cls=='FOUR' or s_cls=='IV' or s_cls=='5' or s_cls=='FIVE' or s_cls=='V' or s_cls=='6' or s_cls=='SIX' or s_cls=='VI' or s_cls=='7' or s_cls=='SEVEN' or s_cls=='VII' or s_cls=='8' or s_cls=='EIGHT' or s_cls=='VIII' or s_cls=='9' or s_cls=='NINE' or s_cls=='IX' or s_cls=='10' or s_cls=='TEN' or s_cls=='X' or s_cls=='11' or s_cls=='ELEVEN' or s_cls=='XI' or s_cls=='12' or s_cls=='TWELEVE' or s_cls=='XII':
                            sch[j][3]=c
                            print("*** NOW STUDENT'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STUDENT'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid class of the student has been entered !!! ~~~")
                            
                else:
                    print()
                    print("*** ADMISSION NUMBER OF THE STUDENT HAS BEEN MATCHED BUT YOU HAVE ENTERED WRONG CHOICE FROM THE STUDENT UPDATE MENU !!! ***")
                    print("--> Please provide the appropriate choice to update the student's detail __/\__")
                
                found=True
                pickle.dump(sch,f)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                ans=input("Press 'o/O' to update any other detail of the student: ")
                
     if found==False:
        print("*** STUDENT'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct admission number of the student to update the student's details __/\__")
       
     print()
     ans=input("Press 'u/U' to update more student's record: ")
     print()
    f.close() 
    
    
def DEL_STU_REC():
    SCH={}
    f=open("SMS_STU.dat","rb+")
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='r'
    while ans.lower()=='r':
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("################################################# DELETE TEACHER'S RECORD #################################################")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     ADMNO=int(input("Enter the admission number of the student, to be search and to delete or remove the student's record: "))
     found=False
     for k in sch:
        if k!=ADMNO:
            found=True
            SCH[k]=sch[k]
            pickle.dump(SCH,f)
            
     if found==False:
        print("*** STUDENT'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct admission number of the student to delete or remove the student's record __/\__")
     else:
        print("*** STUDENT'S RECORD HAS BEEN SUCCESSFULLY DELETED !!! ***")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
     print()
     ans=input("Press 'r/R' to delete or remove more student's record: ")
     print()
    f.close()
    
    
def DISP_PART_STU_REC():
    f=open('SMS_STU.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='d'
    while ans.lower()=='d':
     ADMNO=int(input("Enter the admission number of the student to display the Student's FEE SLIP: "))
     print()
     found=False
     for j in sch:
        if j==ADMNO:
            print("-------------------------------------------------------------------")
            print("%%%%%%%%%%%%%%%%%%%%%% STUDENT'S FEE SLIP %%%%%%%%%%%%%%%%%%%%%%")
            print("-------------------------------------------------------------------")
            print("Student's Admission Number: ",j)
            print("Student's Full Name: ",sch[j][0])
            print("Student's Father's Name: ",sch[j][1])
            print("Student's Mother's Name: ",sch[j][2])
            print("Student's Guardian's Name: ",sch[j][27])
            print("Student's Class: ",sch[j][3])
            print("Student's House: ",sch[j][25])
            print("Student's Sex: ",sch[j][4])
            print("Student's DOB: ",sch[j][5])
            print("Student's Age: ",sch[j][10])
            print("Student's Father's Mobile/Phone Number: +91",sch[j][6])
            print("Student's Mother's Mobile/Phone Number: +91",sch[j][26])
            print("Student's Guardian's Contact Number: +91",sch[j][28])
            print("Student's Father's/Mother's Email Address: ",sch[j][7])
            print("Student's House Address: ",sch[j][8])
            print("Student's Tuition Fee: Rs.",sch[j][11])
            print("Student's Hostel Fee: Rs.",sch[j][12])
            print("Student's Mess Fee: Rs.",sch[j][13])
            print("Student's Library Fee: Rs.",sch[j][14])
            print("Student's Laboratory Fee: Rs.",sch[j][15])
            print("Student's Development Fee: Rs.",sch[j][16])
            print("Student's Exam Fee: Rs.",sch[j][17])
            print("Student's Bus Fee: Rs.",sch[j][18])
            print("Student's Peoples fund: Rs.",sch[j][19])
            print("Student's Miscellaneous Fee: Rs.",sch[j][20])
            print("Student's Monthly Fee: Rs.",sch[j][21])
            print("Student's Annual Fee: Rs.",sch[j][22])
            print("Year: ",sch[j][9])
            print("-------------------------------------------------------------------")
            found=True
            
     if found==False:
        print("*** STUDENT'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct admission number of the student to display the Student's FEE SLIP __/\__")
        
     print()
     ans=input("Press 'd/D' to display more Student's FEE SLIP: ")
     print()
    f.close()