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
    
    f=open('SMS_STU_EXAM.dat','wb')
    ans='i'
    while ans.lower()=='i':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& INSERT STUDENT'S DETAILS &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s_admno=int(input("Enter the student's Admission Number: "))
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
                s_sec=input("Enter the student's Section: ").upper()
                s_sex=stu[i][4]
                s_dob=stu[i][5]
                s_phno=stu[i][6]
                s_email=stu[i][7]
                s_add=stu[i][8]
                s_ut1=input("Whether the student attended the UNIT_TEST-1, Enter 'Yes-ut1/No': ").lower()
                s_ut2=input("Whether the student attended the UNIT_TEST-2, Enter 'Yes-ut2/No': ").lower()
                s_t1=input("Whether the student attended the TERM-1 examination, Enter 'Yes-t1/No': ").lower()
                s_ut3=input("Whether the student attended the UNIT_TEST-3, Enter 'Yes-ut3/No': ").lower()
                s_ut4=input("Whether the student attended the UNIT_TEST-4, Enter 'Yes-ut4/No': ").lower()
                s_t2=input("Whether the student attended the TERM-2 examination, Enter 'Yes-t2/No': ").lower()
                cls_perf=eval(input("Enter the student's class performance in percentage(out of 5%): "))
                pro_act=eval(input("Enter the student's project and activity percentage(out of 5%): "))
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_phno,s_email,s_add,2021,0,s_house,s_sec,s_ut1,s_ut2,s_t1,s_ut3,s_ut4,s_t2,cls_perf,pro_act,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                
                pickle.dump(sch,f)
                
        if found==False:
            print("*** STUDENT'S RECORD HAS NOT BEEN INSERTED !!! ***")
            print("--> Please provide the correct admission number of the student to store the student's record  __/\__")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
        print()
        ans=input("Press 'i/I' to insert more student's record: ")
        print()
    f.close()
    
    
total_percent_ut1=0
total_percent_ut2=0
total_percent_t1=0
total_percent_ut3=0
total_percent_ut4=0
total_percent_t2=0    
def COMPUTE_STU_RC():
    
    global total_percent_ut1,total_percent_ut2,total_percent_t1,total_percent_ut3,total_percent_ut4,total_percent_t2
    
    f=open('SMS_STU_EXAM.dat','rb+')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='c'
    while ans.lower()=='c':
     ADMNO=int(input("Enter student's admission number to compute the Student's MARK SHEET: "))
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
                u=input("Enter: ")
                if sch[i][13]=='yes-ut1':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-1(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][21]=eng
                    sch[i][22]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][232]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][23]=hin
                        sch[i][24]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][25]=beng
                        sch[i][26]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][27]=sans
                        sch[i][28]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][232]=sec_lang
                        hin=0
                        beng=0
                        sans=0
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][23]=hin
                            sch[i][24]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][25]=beng
                            sch[i][26]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][27]=sans
                            sch[i][28]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][29]=chem
                    sch[i][30]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][31]=phy
                    sch[i][32]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][33]=maths
                    sch[i][34]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][233]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][35]=CS
                        sch[i][36]=csp
                    elif cs=='I':
                        IT=0
                        itp=(IT/40)*100
                        sch[i][37]=IT
                        sch[i][38]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][39]=AI
                        sch[i][40]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][233]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][35]=CS
                            sch[i][36]=csp
                        elif cs=='I':
                            IT=0
                            itp=(IT/40)*100
                            sch[i][37]=IT
                            sch[i][38]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][39]=AI
                            sch[i][40]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][41]=hist
                    sch[i][42]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][43]=geo
                    sch[i][44]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][45]=civ
                    sch[i][46]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][47]=gk
                    sch[i][48]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][49]=msc
                    sch[i][50]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][220]=evs
                    sch[i][221]=evsp
                    total_marks=sch[i][21]+sch[i][23]+sch[i][25]+sch[i][27]+sch[i][29]+sch[i][31]+sch[i][33]+sch[i][35]+sch[i][37]+sch[i][39]+sch[i][41]+sch[i][43]+sch[i][45]+sch[i][47]+sch[i][49]+sch[i][220]
                    sch[i][51]=total_marks
                    total_percent_ut1=(total_marks/240)*100
                    sch[i][52]=total_percent_ut1
                
                v=input("Enter: ")
                if sch[i][14]=='yes-ut2':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-2(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][53]=eng
                    sch[i][54]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][234]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][55]=hin
                        sch[i][56]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][57]=beng
                        sch[i][58]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][59]=sans
                        sch[i][60]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][234]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][55]=hin
                            sch[i][56]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][57]=beng
                            sch[i][58]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][59]=sans
                            sch[i][60]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][61]=chem
                    sch[i][62]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][63]=phy
                    sch[i][64]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][65]=maths
                    sch[i][66]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][235]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][67]=CS
                        sch[i][68]=csp
                    elif cs=='I':
                        IT=0
                        itp=(IT/40)*100
                        sch[i][69]=IT
                        sch[i][70]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][71]=AI
                        sch[i][72]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][235]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][67]=CS
                            sch[i][68]=csp
                        elif cs=='I':
                            IT=0
                            itp=(IT/40)*100
                            sch[i][69]=IT
                            sch[i][70]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][71]=AI
                            sch[i][72]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][73]=hist
                    sch[i][74]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][75]=geo
                    sch[i][76]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][77]=civ
                    sch[i][78]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][79]=gk
                    sch[i][80]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][81]=msc
                    sch[i][82]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][222]=evs
                    sch[i][223]=evsp
                    total_marks=sch[i][53]+sch[i][55]+sch[i][57]+sch[i][59]+sch[i][61]+sch[i][63]+sch[i][65]+sch[i][67]+sch[i][69]+sch[i][71]+sch[i][73]+sch[i][75]+sch[i][77]+sch[i][79]+sch[i][81]+sch[i][222]
                    sch[i][83]=total_marks
                    total_percent_ut2=(total_marks/240)*100
                    sch[i][84]=total_percent_ut2
                
                w=input("Enter: ")           
                if sch[i][15]=='yes-t1':
                    print("MARKS SCORED BY THE STUDENT IN TERM-1(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][85]=eng
                    sch[i][86]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][236]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][87]=hin
                        sch[i][88]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][89]=beng
                        sch[i][90]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][91]=sans
                        sch[i][92]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][236]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][87]=hin
                            sch[i][88]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][89]=beng
                            sch[i][90]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][91]=sans
                            sch[i][92]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/80)*100
                    sch[i][93]=chem
                    sch[i][94]=cp
                    phy=0
                    pp=(phy/80)*100
                    sch[i][95]=phy
                    sch[i][96]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][97]=maths
                    sch[i][98]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][237]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/80)*100
                        sch[i][99]=CS
                        sch[i][100]=csp
                    elif cs=='I':
                        IT=0
                        itp=(IT/80)*100
                        sch[i][101]=IT
                        sch[i][102]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/80)*100
                        sch[i][103]=AI
                        sch[i][104]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][237]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/80)*100
                            sch[i][99]=CS
                            sch[i][100]=csp
                        elif cs=='I':
                            IT=0
                            itp=(IT/80)*100
                            sch[i][101]=IT
                            sch[i][102]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/80)*100
                            sch[i][103]=AI
                            sch[i][104]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/80)*100
                    sch[i][105]=hist
                    sch[i][106]=histp
                    geo=0
                    gp=(geo/80)*100
                    sch[i][107]=geo
                    sch[i][108]=gp
                    civ=0
                    civp=(civ/80)*100
                    sch[i][109]=civ
                    sch[i][110]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][111]=gk
                    sch[i][112]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][113]=msc
                    sch[i][114]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/80)*100
                    sch[i][224]=evs
                    sch[i][225]=evsp
                    total_marks=sch[i][85]+sch[i][87]+sch[i][89]+sch[i][91]+sch[i][93]+sch[i][95]+sch[i][97]+sch[i][99]+sch[i][101]+sch[i][103]+sch[i][105]+sch[i][107]+sch[i][109]+sch[i][111]+sch[i][113]+sch[i][224]
                    sch[i][115]=total_marks
                    total_percent_t1=(total_marks/480)*100
                    sch[i][116]=total_percent_t1
                
                x=input("Enter: ")            
                if sch[i][16]=='yes-ut3':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-3(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][117]=eng
                    sch[i][118]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][238]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][119]=hin
                        sch[i][120]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][121]=beng
                        sch[i][122]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][123]=sans
                        sch[i][124]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][238]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][119]=hin
                            sch[i][120]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][121]=beng
                            sch[i][122]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][123]=sans
                            sch[i][124]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][125]=chem
                    sch[i][126]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][127]=phy
                    sch[i][128]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][129]=maths
                    sch[i][130]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][239]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][131]=CS
                        sch[i][132]=csp
                    elif cs=='I':
                        IT=0
                        itp=(IT/40)*100
                        sch[i][133]=IT
                        sch[i][134]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][135]=AI
                        sch[i][136]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][239]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][131]=CS
                            sch[i][132]=csp
                        elif cs=='I':
                            IT=0
                            itp=(IT/40)*100
                            sch[i][133]=IT
                            sch[i][134]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][135]=AI
                            sch[i][136]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][137]=hist
                    sch[i][138]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][139]=geo
                    sch[i][140]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][141]=civ
                    sch[i][142]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][143]=gk
                    sch[i][144]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][145]=msc
                    sch[i][146]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][226]=evs
                    sch[i][227]=evsp
                    total_marks=sch[i][117]+sch[i][119]+sch[i][121]+sch[i][123]+sch[i][125]+sch[i][127]+sch[i][129]+sch[i][131]+sch[i][133]+sch[i][135]+sch[i][137]+sch[i][139]+sch[i][141]+sch[i][143]+sch[i][145]+sch[i][226]
                    sch[i][147]=total_marks
                    total_percent_ut3=(total_marks/240)*100
                    sch[i][148]=total_percent_ut3
                
                y=input("Enter: ")            
                if sch[i][17]=='yes-ut4':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-4(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][149]=eng
                    sch[i][150]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][240]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][151]=hin
                        sch[i][152]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][153]=beng
                        sch[i][154]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][155]=sans
                        sch[i][156]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][240]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][151]=hin
                            sch[i][152]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][153]=beng
                            sch[i][154]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][155]=sans
                            sch[i][156]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][157]=chem
                    sch[i][158]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][159]=phy
                    sch[i][160]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][161]=maths
                    sch[i][162]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][241]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][163]=CS
                        sch[i][164]=csp
                    elif cs=='I':
                        IT=0
                        itp=(IT/40)*100
                        sch[i][165]=IT
                        sch[i][166]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][167]=AI
                        sch[i][168]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][241]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][163]=CS
                            sch[i][164]=csp
                        elif cs=='I':
                            IT=0
                            itp=(IT/40)*100
                            sch[i][165]=IT
                            sch[i][166]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][167]=AI
                            sch[i][168]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][169]=hist
                    sch[i][170]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][171]=geo
                    sch[i][172]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][173]=civ
                    sch[i][174]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][175]=gk
                    sch[i][176]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][177]=msc
                    sch[i][178]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][228]=evs
                    sch[i][229]=evsp
                    total_marks=sch[i][149]+sch[i][151]+sch[i][153]+sch[i][155]+sch[i][157]+sch[i][159]+sch[i][161]+sch[i][163]+sch[i][165]+sch[i][167]+sch[i][169]+sch[i][171]+sch[i][173]+sch[i][175]+sch[i][177]+sch[i][228]
                    sch[i][179]=total_marks
                    total_percent_ut4=(total_marks/240)*100
                    sch[i][180]=total_percent_ut4
                
                z=input("Enter: ")           
                if sch[i][18]=='yes-t2':
                    print("MARKS SCORED BY THE STUDENT IN TERM-2(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][181]=eng
                    sch[i][182]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][242]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][183]=hin
                        sch[i][184]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][185]=beng
                        sch[i][186]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][187]=sans
                        sch[i][188]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][242]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][183]=hin
                            sch[i][184]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][185]=beng
                            sch[i][186]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/80)*100
                            sch[i][187]=sans
                            sch[i][188]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/80)*100
                    sch[i][189]=chem
                    sch[i][190]=cp
                    phy=0
                    pp=(phy/80)*100
                    sch[i][191]=phy
                    sch[i][192]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][193]=maths
                    sch[i][194]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][243]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/80)*100
                        sch[i][195]=CS
                        sch[i][196]=csp
                    elif cs=='I':
                        IT=0
                        itp=(IT/80)*100
                        sch[i][197]=IT
                        sch[i][198]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/80)*100
                        sch[i][199]=AI
                        sch[i][200]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][243]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/80)*100
                            sch[i][195]=CS
                            sch[i][196]=csp
                        elif cs=='I':
                            IT=0
                            itp=(IT/80)*100
                            sch[i][197]=IT
                            sch[i][198]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/80)*100
                            sch[i][199]=AI
                            sch[i][200]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/80)*100
                    sch[i][201]=hist
                    sch[i][202]=histp
                    geo=0
                    gp=(geo/80)*100
                    sch[i][203]=geo
                    sch[i][204]=gp
                    civ=0
                    civp=(civ/80)*100
                    sch[i][205]=civ
                    sch[i][206]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][207]=gk
                    sch[i][208]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][209]=msc
                    sch[i][210]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/80)*100
                    sch[i][230]=evs
                    sch[i][231]=evsp
                    total_marks=sch[i][181]+sch[i][183]+sch[i][185]+sch[i][187]+sch[i][189]+sch[i][191]+sch[i][193]+sch[i][195]+sch[i][197]+sch[i][199]+sch[i][201]+sch[i][203]+sch[i][205]+sch[i][207]+sch[i][209]+sch[i][230]
                    sch[i][211]=total_marks
                    total_percent_t2=(total_marks/480)*100
                    sch[i][212]=total_percent_t2
                    
            ch=input("Press any key to compute overall student mark sheet: ")
            if total_percent_ut1>=total_percent_ut2:
                best_utI=(5/100)*total_percent_ut1
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            else:
                best_utI=(5/100)*total_percent_ut2
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            a=(20/100)*total_percent_t1
            sch[i][215]=a
            b=(60/100)*total_percent_t2
            sch[i][216]=b
            tp_ut=best_utI+best_utII
            sch[i][217]=tp_ut
            tp_t=a+b
            sch[i][218]=tp_t
            tp_tp=tp_ut+tp_t+sch[i][19]+sch[i][20]
            sch[i][219]=tp_tp
                
                
        elif sch[i][10]==5:
            if sch[i][3]=='UKG':
                u=input("Enter: ")
                if sch[i][13]=='yes-ut1':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-1(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][21]=eng
                    sch[i][22]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][232]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][23]=hin
                        sch[i][24]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][25]=beng
                        sch[i][26]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][27]=sans
                        sch[i][28]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][232]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][23]=hin
                            sch[i][24]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][25]=beng
                            sch[i][26]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][27]=sans
                            sch[i][28]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][29]=chem
                    sch[i][30]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][31]=phy
                    sch[i][32]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][33]=maths
                    sch[i][34]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][233]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][35]=CS
                        sch[i][36]=csp
                    elif cs=='I':
                        IT=0
                        itp=(IT/40)*100
                        sch[i][37]=IT
                        sch[i][38]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][39]=AI
                        sch[i][40]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=eval(input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ")).upper()
                        sch[i][233]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][35]=CS
                            sch[i][36]=csp
                        elif cs=='I':
                            IT=0
                            itp=(IT/40)*100
                            sch[i][37]=IT
                            sch[i][38]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][39]=AI
                            sch[i][40]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][41]=hist
                    sch[i][42]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][43]=geo
                    sch[i][44]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][45]=civ
                    sch[i][46]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][47]=gk
                    sch[i][48]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][49]=msc
                    sch[i][50]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][220]=evs
                    sch[i][221]=evsp
                    total_marks=sch[i][21]+sch[i][23]+sch[i][25]+sch[i][27]+sch[i][29]+sch[i][31]+sch[i][33]+sch[i][35]+sch[i][37]+sch[i][39]+sch[i][41]+sch[i][43]+sch[i][45]+sch[i][47]+sch[i][49]+sch[i][220]
                    sch[i][51]=total_marks
                    total_percent_ut1=(total_marks/240)*100
                    sch[i][52]=total_percent_ut1
                
                v=input("Enter: ")
                if sch[i][14]=='yes-ut2':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-2(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][53]=eng
                    sch[i][54]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][234]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][55]=hin
                        sch[i][56]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][57]=beng
                        sch[i][58]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][59]=sans
                        sch[i][60]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][234]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][55]=hin
                            sch[i][56]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][57]=beng
                            sch[i][58]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][59]=sans
                            sch[i][60]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][61]=chem
                    sch[i][62]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][63]=phy
                    sch[i][64]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][65]=maths
                    sch[i][66]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][235]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][67]=CS
                        sch[i][68]=csp
                    elif cs=='I':
                        IT=0
                        itp=(IT/40)*100
                        sch[i][69]=IT
                        sch[i][70]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][71]=AI
                        sch[i][72]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][235]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][67]=CS
                            sch[i][68]=csp
                        elif cs=='I':
                            IT=0
                            itp=(IT/40)*100
                            sch[i][69]=IT
                            sch[i][70]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][71]=AI
                            sch[i][72]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][73]=hist
                    sch[i][74]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][75]=geo
                    sch[i][76]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][77]=civ
                    sch[i][78]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][79]=gk
                    sch[i][80]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][81]=msc
                    sch[i][82]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][222]=evs
                    sch[i][223]=evsp
                    total_marks=sch[i][53]+sch[i][55]+sch[i][57]+sch[i][59]+sch[i][61]+sch[i][63]+sch[i][65]+sch[i][67]+sch[i][69]+sch[i][71]+sch[i][73]+sch[i][75]+sch[i][77]+sch[i][79]+sch[i][81]+sch[i][222]
                    sch[i][83]=total_marks
                    total_percent_ut2=(total_marks/240)*100
                    sch[i][84]=total_percent_ut2
                           
                w=input("Enter: ")
                if sch[i][15]=='yes-t1':
                    print("MARKS SCORED BY THE STUDENT IN TERM-1(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][85]=eng
                    sch[i][86]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][236]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][87]=hin
                        sch[i][88]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][89]=beng
                        sch[i][90]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][91]=sans
                        sch[i][92]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][236]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][87]=hin
                            sch[i][88]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][89]=beng
                            sch[i][90]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][91]=sans
                            sch[i][92]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/80)*100
                    sch[i][93]=chem
                    sch[i][94]=cp
                    phy=0
                    pp=(phy/80)*100
                    sch[i][95]=phy
                    sch[i][96]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][97]=maths
                    sch[i][98]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][237]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/80)*100
                        sch[i][99]=CS
                        sch[i][100]=csp
                    elif cs=='I':
                        IT=0
                        itp=(IT/80)*100
                        sch[i][101]=IT
                        sch[i][102]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/80)*100
                        sch[i][103]=AI
                        sch[i][104]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][237]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/80)*100
                            sch[i][99]=CS
                            sch[i][100]=csp
                        elif cs=='I':
                            IT=0
                            itp=(IT/80)*100
                            sch[i][101]=IT
                            sch[i][102]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/80)*100
                            sch[i][103]=AI
                            sch[i][104]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/80)*100
                    sch[i][105]=hist
                    sch[i][106]=histp
                    geo=0
                    gp=(geo/80)*100
                    sch[i][107]=geo
                    sch[i][108]=gp
                    civ=0
                    civp=(civ/80)*100
                    sch[i][109]=civ
                    sch[i][110]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][111]=gk
                    sch[i][112]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][113]=msc
                    sch[i][114]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/80)*100
                    sch[i][224]=evs
                    sch[i][225]=evsp
                    total_marks=sch[i][85]+sch[i][87]+sch[i][89]+sch[i][91]+sch[i][93]+sch[i][95]+sch[i][97]+sch[i][99]+sch[i][101]+sch[i][103]+sch[i][105]+sch[i][107]+sch[i][109]+sch[i][111]+sch[i][113]+sch[i][224]
                    sch[i][115]=total_marks
                    total_percent_t1=(total_marks/480)*100
                    sch[i][116]=total_percent_t1
                
                x=input("Enter: ")             
                if sch[i][16]=='yes-ut3':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-3(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][117]=eng
                    sch[i][118]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][238]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][119]=hin
                        sch[i][120]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][121]=beng
                        sch[i][122]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][123]=sans
                        sch[i][124]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][238]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][119]=hin
                            sch[i][120]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][121]=beng
                            sch[i][122]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][123]=sans
                            sch[i][124]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][125]=chem
                    sch[i][126]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][127]=phy
                    sch[i][128]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][129]=maths
                    sch[i][130]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][239]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][131]=CS
                        sch[i][132]=csp
                    elif cs=='I':
                        IT=0
                        itp=(IT/40)*100
                        sch[i][133]=IT
                        sch[i][134]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][135]=AI
                        sch[i][136]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][239]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][131]=CS
                            sch[i][132]=csp
                        elif cs=='I':
                            IT=0
                            itp=(IT/40)*100
                            sch[i][133]=IT
                            sch[i][134]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][135]=AI
                            sch[i][136]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][137]=hist
                    sch[i][138]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][139]=geo
                    sch[i][140]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][141]=civ
                    sch[i][142]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][143]=gk
                    sch[i][144]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][145]=msc
                    sch[i][146]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][226]=evs
                    sch[i][227]=evsp
                    total_marks=sch[i][117]+sch[i][119]+sch[i][121]+sch[i][123]+sch[i][125]+sch[i][127]+sch[i][129]+sch[i][131]+sch[i][133]+sch[i][135]+sch[i][137]+sch[i][139]+sch[i][141]+sch[i][143]+sch[i][145]+sch[i][226]
                    sch[i][147]=total_marks
                    total_percent_ut3=(total_marks/240)*100
                    sch[i][148]=total_percent_ut3
                            
                y=input("Enter: ")
                if sch[i][17]=='yes-ut4':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-4(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][149]=eng
                    sch[i][150]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][240]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][151]=hin
                        sch[i][152]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][153]=beng
                        sch[i][154]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][155]=sans
                        sch[i][156]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][240]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][151]=hin
                            sch[i][152]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][153]=beng
                            sch[i][154]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][155]=sans
                            sch[i][156]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][157]=chem
                    sch[i][158]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][159]=phy
                    sch[i][160]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][161]=maths
                    sch[i][162]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][241]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][163]=CS
                        sch[i][164]=csp
                    elif cs=='I':
                        IT=0
                        itp=(IT/40)*100
                        sch[i][165]=IT
                        sch[i][166]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][167]=AI
                        sch[i][168]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][241]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][163]=CS
                            sch[i][164]=csp
                        elif cs=='I':
                            IT=0
                            itp=(IT/40)*100
                            sch[i][165]=IT
                            sch[i][166]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][167]=AI
                            sch[i][168]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][169]=hist
                    sch[i][170]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][171]=geo
                    sch[i][172]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][173]=civ
                    sch[i][174]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][175]=gk
                    sch[i][176]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][177]=msc
                    sch[i][178]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][228]=evs
                    sch[i][229]=evsp
                    total_marks=sch[i][149]+sch[i][151]+sch[i][153]+sch[i][155]+sch[i][157]+sch[i][159]+sch[i][161]+sch[i][163]+sch[i][165]+sch[i][167]+sch[i][169]+sch[i][171]+sch[i][173]+sch[i][175]+sch[i][177]+sch[i][228]
                    sch[i][179]=total_marks
                    total_percent_ut4=(total_marks/240)*100
                    sch[i][180]=total_percent_ut4
                           
                z=input("Enter: ")
                if sch[i][18]=='yes-t2':
                    print("MARKS SCORED BY THE STUDENT IN TERM-2(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][181]=eng
                    sch[i][182]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][242]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][183]=hin
                        sch[i][184]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][185]=beng
                        sch[i][186]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][187]=sans
                        sch[i][188]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][242]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][183]=hin
                            sch[i][184]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][185]=beng
                            sch[i][186]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/80)*100
                            sch[i][187]=sans
                            sch[i][188]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/80)*100
                    sch[i][189]=chem
                    sch[i][190]=cp
                    phy=0
                    pp=(phy/80)*100
                    sch[i][191]=phy
                    sch[i][192]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][193]=maths
                    sch[i][194]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][243]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/80)*100
                        sch[i][195]=CS
                        sch[i][196]=csp
                    elif cs=='I':
                        IT=0
                        itp=(IT/80)*100
                        sch[i][197]=IT
                        sch[i][198]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/80)*100
                        sch[i][199]=AI
                        sch[i][200]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][243]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/80)*100
                            sch[i][195]=CS
                            sch[i][196]=csp
                        elif cs=='I':
                            IT=0
                            itp=(IT/80)*100
                            sch[i][197]=IT
                            sch[i][198]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/80)*100
                            sch[i][199]=AI
                            sch[i][200]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/80)*100
                    sch[i][201]=hist
                    sch[i][202]=histp
                    geo=0
                    gp=(geo/80)*100
                    sch[i][203]=geo
                    sch[i][204]=gp
                    civ=0
                    civp=(civ/80)*100
                    sch[i][205]=civ
                    sch[i][206]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][207]=gk
                    sch[i][208]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][209]=msc
                    sch[i][210]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/80)*100
                    sch[i][230]=evs
                    sch[i][231]=evsp
                    total_marks=sch[i][181]+sch[i][183]+sch[i][185]+sch[i][187]+sch[i][189]+sch[i][191]+sch[i][193]+sch[i][195]+sch[i][197]+sch[i][199]+sch[i][201]+sch[i][203]+sch[i][205]+sch[i][207]+sch[i][209]+sch[i][230]
                    sch[i][211]=total_marks
                    total_percent_t2=(total_marks/480)*100
                    sch[i][212]=total_percent_t2
                    
            ch=input("Press any key to compute overall student mark sheet: ")
            if total_percent_ut1>=total_percent_ut2:
                best_utI=(5/100)*total_percent_ut1
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            else:
                best_utI=(5/100)*total_percent_ut2
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            a=(20/100)*total_percent_t1
            sch[i][215]=a
            b=(60/100)*total_percent_t2
            sch[i][216]=b
            tp_ut=best_utI+best_utII
            sch[i][217]=tp_ut
            tp_t=a+b
            sch[i][218]=tp_t
            tp_tp=tp_ut+tp_t+sch[i][19]+sch[i][20]
            sch[i][219]=tp_tp
                
        elif sch[i][10]==6:
            if sch[i][3]=='ONE' or sch[i][3]=='1' or sch[i][3]=='I':
                u=input("Enter: ")
                if sch[i][13]=='yes-ut1':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-1(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][21]=eng
                    sch[i][22]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][232]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][23]=hin
                        sch[i][24]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][25]=beng
                        sch[i][26]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][27]=sans
                        sch[i][28]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][232]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][23]=hin
                            sch[i][24]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][25]=beng
                            sch[i][26]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][27]=sans
                            sch[i][28]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][29]=chem
                    sch[i][30]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][31]=phy
                    sch[i][32]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][33]=maths
                    sch[i][34]=mp
                    cs='I'
                    sch[i][233]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][35]=CS
                        sch[i][36]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][37]=IT
                        sch[i][38]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][39]=AI
                        sch[i][40]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][233]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][35]=CS
                            sch[i][36]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][37]=IT
                            sch[i][38]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][39]=AI
                            sch[i][40]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][41]=hist
                    sch[i][42]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][43]=geo
                    sch[i][44]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][45]=civ
                    sch[i][46]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][47]=gk
                    sch[i][48]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][49]=msc
                    sch[i][50]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][220]=evs
                    sch[i][221]=evsp
                    total_marks=sch[i][21]+sch[i][23]+sch[i][25]+sch[i][27]+sch[i][29]+sch[i][31]+sch[i][33]+sch[i][35]+sch[i][37]+sch[i][39]+sch[i][41]+sch[i][43]+sch[i][45]+sch[i][47]+sch[i][49]+sch[i][220]
                    sch[i][51]=total_marks
                    total_percent_ut1=(total_marks/280)*100
                    sch[i][52]=total_percent_ut1
                
                v=input("Enter: ")
                if sch[i][14]=='yes-ut2':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-2(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][53]=eng
                    sch[i][54]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][234]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][55]=hin
                        sch[i][56]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][57]=beng
                        sch[i][58]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][59]=sans
                        sch[i][60]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][234]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][55]=hin
                            sch[i][56]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][57]=beng
                            sch[i][58]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][59]=sans
                            sch[i][60]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][61]=chem
                    sch[i][62]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][63]=phy
                    sch[i][64]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][65]=maths
                    sch[i][66]=mp
                    cs='I'
                    sch[i][235]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][67]=CS
                        sch[i][68]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][69]=IT
                        sch[i][70]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][71]=AI
                        sch[i][72]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][235]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][67]=CS
                            sch[i][68]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][69]=IT
                            sch[i][70]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][71]=AI
                            sch[i][72]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][73]=hist
                    sch[i][74]=histp
                    geo=0
                    sch[i][75]=geo
                    sch[i][76]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][77]=civ
                    sch[i][78]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][79]=gk
                    sch[i][80]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][81]=msc
                    sch[i][82]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][222]=evs
                    sch[i][223]=evsp
                    total_marks=sch[i][53]+sch[i][55]+sch[i][57]+sch[i][59]+sch[i][61]+sch[i][63]+sch[i][65]+sch[i][67]+sch[i][69]+sch[i][71]+sch[i][73]+sch[i][75]+sch[i][77]+sch[i][79]+sch[i][81]+sch[i][222]
                    sch[i][83]=total_marks
                    total_percent_ut2=(total_marks/280)*100
                    sch[i][84]=total_percent_ut2
                           
                w=input("Enter: ")
                if sch[i][15]=='yes-t1':
                    print("MARKS SCORED BY THE STUDENT IN TERM-1(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][85]=eng
                    sch[i][86]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][236]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][87]=hin
                        sch[i][88]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][89]=beng
                        sch[i][90]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][91]=sans
                        sch[i][92]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][236]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][87]=hin
                            sch[i][88]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][89]=beng
                            sch[i][90]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][91]=sans
                            sch[i][92]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/80)*100
                    sch[i][93]=chem
                    sch[i][94]=cp
                    phy=0
                    pp=(phy/80)*100
                    sch[i][95]=phy
                    sch[i][96]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][97]=maths
                    sch[i][98]=mp
                    cs='I'
                    sch[i][237]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/80)*100
                        sch[i][99]=CS
                        sch[i][100]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][101]=IT
                        sch[i][102]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/80)*100
                        sch[i][103]=AI
                        sch[i][104]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][237]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/80)*100
                            sch[i][99]=CS
                            sch[i][100]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][101]=IT
                            sch[i][102]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/80)*100
                            sch[i][103]=AI
                            sch[i][104]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/80)*100
                    sch[i][105]=hist
                    sch[i][106]=histp
                    geo=0
                    gp=(geo/80)*100
                    sch[i][107]=geo
                    sch[i][108]=gp
                    civ=0
                    civp=(civ/80)*100
                    sch[i][109]=civ
                    sch[i][110]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][111]=gk
                    sch[i][112]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][113]=msc
                    sch[i][114]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/80)*100
                    sch[i][224]=evs
                    sch[i][225]=evsp
                    total_marks=sch[i][85]+sch[i][87]+sch[i][89]+sch[i][91]+sch[i][93]+sch[i][95]+sch[i][97]+sch[i][99]+sch[i][101]+sch[i][103]+sch[i][105]+sch[i][107]+sch[i][109]+sch[i][111]+sch[i][113]+sch[i][224]
                    sch[i][115]=total_marks
                    total_percent_t1=(total_marks/560)*100
                    sch[i][116]=total_percent_t1
                            
                x=input("Enter: ")  
                if sch[i][16]=='yes-ut3':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-3(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][117]=eng
                    sch[i][118]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][238]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][119]=hin
                        sch[i][120]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][121]=beng
                        sch[i][122]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][123]=sans
                        sch[i][124]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][238]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][119]=hin
                            sch[i][120]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][121]=beng
                            sch[i][122]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][123]=sans
                            sch[i][124]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][125]=chem
                    sch[i][126]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][127]=phy
                    sch[i][128]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][129]=maths
                    sch[i][130]=mp
                    cs='I'
                    sch[i][239]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][131]=CS
                        sch[i][132]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][133]=IT
                        sch[i][134]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][135]=AI
                        sch[i][136]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][239]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][131]=CS
                            sch[i][132]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][133]=IT
                            sch[i][134]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][135]=AI
                            sch[i][136]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][137]=hist
                    sch[i][138]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][139]=geo
                    sch[i][140]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][141]=civ
                    sch[i][142]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][143]=gk
                    sch[i][144]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][145]=msc
                    sch[i][146]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][226]=evs
                    sch[i][227]=evsp
                    total_marks=sch[i][117]+sch[i][119]+sch[i][121]+sch[i][123]+sch[i][125]+sch[i][127]+sch[i][129]+sch[i][131]+sch[i][133]+sch[i][135]+sch[i][137]+sch[i][139]+sch[i][141]+sch[i][143]+sch[i][145]+sch[i][226]
                    sch[i][147]=total_marks
                    total_percent_ut3=(total_marks/280)*100
                    sch[i][148]=total_percent_ut3
                
                y=input("Enter: ")            
                if sch[i][17]=='yes-ut4':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-4(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][149]=eng
                    sch[i][150]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][240]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][151]=hin
                        sch[i][152]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][153]=beng
                        sch[i][154]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][155]=sans
                        sch[i][156]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][240]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][151]=hin
                            sch[i][152]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][153]=beng
                            sch[i][154]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][155]=sans
                            sch[i][156]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][157]=chem
                    sch[i][158]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][159]=phy
                    sch[i][160]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][161]=maths
                    sch[i][162]=mp
                    cs='I'
                    sch[i][241]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][163]=CS
                        sch[i][164]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][165]=IT
                        sch[i][166]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][167]=AI
                        sch[i][168]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][241]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][163]=CS
                            sch[i][164]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][165]=IT
                            sch[i][166]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][167]=AI
                            sch[i][168]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][169]=hist
                    sch[i][170]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][171]=geo
                    sch[i][172]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][173]=civ
                    sch[i][174]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][175]=gk
                    sch[i][176]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][177]=msc
                    sch[i][178]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][228]=evs
                    sch[i][229]=evsp
                    total_marks=sch[i][149]+sch[i][151]+sch[i][153]+sch[i][155]+sch[i][157]+sch[i][159]+sch[i][161]+sch[i][163]+sch[i][165]+sch[i][167]+sch[i][169]+sch[i][171]+sch[i][173]+sch[i][175]+sch[i][177]+sch[i][228]
                    sch[i][179]=total_marks
                    total_percent_ut4=(total_marks/280)*100
                    sch[i][180]=total_percent_ut4
                           
                z=input("Enter: ")
                if sch[i][18]=='yes-t2':
                    print("MARKS SCORED BY THE STUDENT IN TERM-2(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][181]=eng
                    sch[i][182]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][242]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][183]=hin
                        sch[i][184]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][185]=beng
                        sch[i][186]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][187]=sans
                        sch[i][188]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][242]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][183]=hin
                            sch[i][184]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][185]=beng
                            sch[i][186]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/80)*100
                            sch[i][187]=sans
                            sch[i][188]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/80)*100
                    sch[i][189]=chem
                    sch[i][190]=cp
                    phy=0
                    pp=(phy/80)*100
                    sch[i][191]=phy
                    sch[i][192]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][193]=maths
                    sch[i][194]=mp
                    cs='I'
                    sch[i][243]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/80)*100
                        sch[i][195]=CS
                        sch[i][196]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][197]=IT
                        sch[i][198]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/80)*100
                        sch[i][199]=AI
                        sch[i][200]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][243]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/80)*100
                            sch[i][195]=CS
                            sch[i][196]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][197]=IT
                            sch[i][198]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/80)*100
                            sch[i][199]=AI
                            sch[i][200]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/80)*100
                    sch[i][201]=hist
                    sch[i][202]=histp
                    geo=0
                    gp=(geo/80)*100
                    sch[i][203]=geo
                    sch[i][204]=gp
                    civ=0
                    civp=(civ/80)*100
                    sch[i][205]=civ
                    sch[i][206]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][207]=gk
                    sch[i][208]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][209]=msc
                    sch[i][210]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/80)*100
                    sch[i][230]=evs
                    sch[i][231]=evsp
                    total_marks=sch[i][181]+sch[i][183]+sch[i][185]+sch[i][187]+sch[i][189]+sch[i][191]+sch[i][193]+sch[i][195]+sch[i][197]+sch[i][199]+sch[i][201]+sch[i][203]+sch[i][205]+sch[i][207]+sch[i][209]+sch[i][230]
                    sch[i][211]=total_marks
                    total_percent_t2=(total_marks/560)*100
                    sch[i][212]=total_percent_t2
                    
            ch=input("Press any key to compute overall student mark sheet: ")
            if total_percent_ut1>=total_percent_ut2:
                best_utI=(5/100)*total_percent_ut1
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            else:
                best_utI=(5/100)*total_percent_ut2
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            a=(20/100)*total_percent_t1
            sch[i][215]=a
            b=(60/100)*total_percent_t2
            sch[i][216]=b
            tp_ut=best_utI+best_utII
            sch[i][217]=tp_ut
            tp_t=a+b
            sch[i][218]=tp_t
            tp_tp=tp_ut+tp_t+sch[i][19]+sch[i][20]
            sch[i][219]=tp_tp
                
                
        elif sch[i][10]==7:
            if sch[i][3]=='TWO' or sch[i][3]=='2' or sch[i][3]=='II':
                u=input("Enter: ")
                if sch[i][13]=='yes-ut1':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-1(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][21]=eng
                    sch[i][22]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][232]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][23]=hin
                        sch[i][24]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][25]=beng
                        sch[i][26]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][27]=sans
                        sch[i][28]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][232]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][23]=hin
                            sch[i][24]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][25]=beng
                            sch[i][26]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][27]=sans
                            sch[i][28]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][29]=chem
                    sch[i][30]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][31]=phy
                    sch[i][32]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][33]=maths
                    sch[i][34]=mp
                    cs='I'
                    sch[i][233]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][35]=CS
                        sch[i][36]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][37]=IT
                        sch[i][38]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][39]=AI
                        sch[i][40]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][233]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][35]=CS
                            sch[i][36]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][37]=IT
                            sch[i][38]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][39]=AI
                            sch[i][40]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][41]=hist
                    sch[i][42]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][43]=geo
                    sch[i][44]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][45]=civ
                    sch[i][46]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][47]=gk
                    sch[i][48]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][49]=msc
                    sch[i][50]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][220]=evs
                    sch[i][221]=evsp
                    total_marks=sch[i][21]+sch[i][23]+sch[i][25]+sch[i][27]+sch[i][29]+sch[i][31]+sch[i][33]+sch[i][35]+sch[i][37]+sch[i][39]+sch[i][41]+sch[i][43]+sch[i][45]+sch[i][47]+sch[i][49]+sch[i][220]
                    sch[i][51]=total_marks
                    total_percent_ut1=(total_marks/280)*100
                    sch[i][52]=total_percent_ut1
                
                v=input("Enter: ")
                if sch[i][14]=='yes-ut2':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-2(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][53]=eng
                    sch[i][54]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][234]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][55]=hin
                        sch[i][56]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][57]=beng
                        sch[i][58]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][59]=sans
                        sch[i][60]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][234]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][55]=hin
                            sch[i][56]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][57]=beng
                            sch[i][58]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][59]=sans
                            sch[i][60]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][61]=chem
                    sch[i][62]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][63]=phy
                    sch[i][64]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][65]=maths
                    sch[i][66]=mp
                    cs='I'
                    sch[i][235]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][67]=CS
                        sch[i][68]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][69]=IT
                        sch[i][70]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][71]=AI
                        sch[i][72]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][235]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][67]=CS
                            sch[i][68]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][69]=IT
                            sch[i][70]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][71]=AI
                            sch[i][72]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][73]=hist
                    sch[i][74]=histp
                    geo=0
                    sch[i][75]=geo
                    sch[i][76]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][77]=civ
                    sch[i][78]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][79]=gk
                    sch[i][80]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][81]=msc
                    sch[i][82]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][222]=evs
                    sch[i][223]=evsp
                    total_marks=sch[i][53]+sch[i][55]+sch[i][57]+sch[i][59]+sch[i][61]+sch[i][63]+sch[i][65]+sch[i][67]+sch[i][69]+sch[i][71]+sch[i][73]+sch[i][75]+sch[i][77]+sch[i][79]+sch[i][81]+sch[i][222]
                    sch[i][83]=total_marks
                    total_percent_ut2=(total_marks/280)*100
                    sch[i][84]=total_percent_ut2
                           
                w=input("Enter: ")
                if sch[i][15]=='yes-t1':
                    print("MARKS SCORED BY THE STUDENT IN TERM-1(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][85]=eng
                    sch[i][86]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][236]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][87]=hin
                        sch[i][88]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][89]=beng
                        sch[i][90]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][91]=sans
                        sch[i][92]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][236]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][87]=hin
                            sch[i][88]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][89]=beng
                            sch[i][90]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][91]=sans
                            sch[i][92]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/80)*100
                    sch[i][93]=chem
                    sch[i][94]=cp
                    phy=0
                    pp=(phy/80)*100
                    sch[i][95]=phy
                    sch[i][96]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][97]=maths
                    sch[i][98]=mp
                    cs='I'
                    sch[i][237]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/80)*100
                        sch[i][99]=CS
                        sch[i][100]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][101]=IT
                        sch[i][102]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/80)*100
                        sch[i][103]=AI
                        sch[i][104]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][237]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/80)*100
                            sch[i][99]=CS
                            sch[i][100]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][101]=IT
                            sch[i][102]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/80)*100
                            sch[i][103]=AI
                            sch[i][104]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/80)*100
                    sch[i][105]=hist
                    sch[i][106]=histp
                    geo=0
                    gp=(geo/80)*100
                    sch[i][107]=geo
                    sch[i][108]=gp
                    civ=0
                    civp=(civ/80)*100
                    sch[i][109]=civ
                    sch[i][110]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][111]=gk
                    sch[i][112]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][113]=msc
                    sch[i][114]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/80)*100
                    sch[i][224]=evs
                    sch[i][225]=evsp
                    total_marks=sch[i][85]+sch[i][87]+sch[i][89]+sch[i][91]+sch[i][93]+sch[i][95]+sch[i][97]+sch[i][99]+sch[i][101]+sch[i][103]+sch[i][105]+sch[i][107]+sch[i][109]+sch[i][111]+sch[i][113]+sch[i][224]
                    sch[i][115]=total_marks
                    total_percent_t1=(total_marks/560)*100
                    sch[i][116]=total_percent_t1
                            
                x=input("Enter: ")  
                if sch[i][16]=='yes-ut3':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-3(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][117]=eng
                    sch[i][118]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][238]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][119]=hin
                        sch[i][120]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][121]=beng
                        sch[i][122]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][123]=sans
                        sch[i][124]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][238]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][119]=hin
                            sch[i][120]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][121]=beng
                            sch[i][122]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][123]=sans
                            sch[i][124]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][125]=chem
                    sch[i][126]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][127]=phy
                    sch[i][128]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][129]=maths
                    sch[i][130]=mp
                    cs='I'
                    sch[i][239]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][131]=CS
                        sch[i][132]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][133]=IT
                        sch[i][134]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][135]=AI
                        sch[i][136]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][239]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][131]=CS
                            sch[i][132]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][133]=IT
                            sch[i][134]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][135]=AI
                            sch[i][136]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][137]=hist
                    sch[i][138]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][139]=geo
                    sch[i][140]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][141]=civ
                    sch[i][142]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][143]=gk
                    sch[i][144]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][145]=msc
                    sch[i][146]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][226]=evs
                    sch[i][227]=evsp
                    total_marks=sch[i][117]+sch[i][119]+sch[i][121]+sch[i][123]+sch[i][125]+sch[i][127]+sch[i][129]+sch[i][131]+sch[i][133]+sch[i][135]+sch[i][137]+sch[i][139]+sch[i][141]+sch[i][143]+sch[i][145]+sch[i][226]
                    sch[i][147]=total_marks
                    total_percent_ut3=(total_marks/280)*100
                    sch[i][148]=total_percent_ut3
                
                y=input("Enter: ")            
                if sch[i][17]=='yes-ut4':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-4(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][149]=eng
                    sch[i][150]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][240]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][151]=hin
                        sch[i][152]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][153]=beng
                        sch[i][154]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][155]=sans
                        sch[i][156]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][240]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][151]=hin
                            sch[i][152]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][153]=beng
                            sch[i][154]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][155]=sans
                            sch[i][156]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][157]=chem
                    sch[i][158]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][159]=phy
                    sch[i][160]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][161]=maths
                    sch[i][162]=mp
                    cs='I'
                    sch[i][241]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][163]=CS
                        sch[i][164]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][165]=IT
                        sch[i][166]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][167]=AI
                        sch[i][168]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][241]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][163]=CS
                            sch[i][164]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][165]=IT
                            sch[i][166]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][167]=AI
                            sch[i][168]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][169]=hist
                    sch[i][170]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][171]=geo
                    sch[i][172]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][173]=civ
                    sch[i][174]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][175]=gk
                    sch[i][176]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][177]=msc
                    sch[i][178]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][228]=evs
                    sch[i][229]=evsp
                    total_marks=sch[i][149]+sch[i][151]+sch[i][153]+sch[i][155]+sch[i][157]+sch[i][159]+sch[i][161]+sch[i][163]+sch[i][165]+sch[i][167]+sch[i][169]+sch[i][171]+sch[i][173]+sch[i][175]+sch[i][177]+sch[i][228]
                    sch[i][179]=total_marks
                    total_percent_ut4=(total_marks/280)*100
                    sch[i][180]=total_percent_ut4
                           
                z=input("Enter: ")
                if sch[i][18]=='yes-t2':
                    print("MARKS SCORED BY THE STUDENT IN TERM-2(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][181]=eng
                    sch[i][182]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][242]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][183]=hin
                        sch[i][184]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][185]=beng
                        sch[i][186]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][187]=sans
                        sch[i][188]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][242]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][183]=hin
                            sch[i][184]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][185]=beng
                            sch[i][186]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/80)*100
                            sch[i][187]=sans
                            sch[i][188]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/80)*100
                    sch[i][189]=chem
                    sch[i][190]=cp
                    phy=0
                    pp=(phy/80)*100
                    sch[i][191]=phy
                    sch[i][192]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][193]=maths
                    sch[i][194]=mp
                    cs='I'
                    sch[i][243]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/80)*100
                        sch[i][195]=CS
                        sch[i][196]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][197]=IT
                        sch[i][198]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/80)*100
                        sch[i][199]=AI
                        sch[i][200]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][243]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/80)*100
                            sch[i][195]=CS
                            sch[i][196]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][197]=IT
                            sch[i][198]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/80)*100
                            sch[i][199]=AI
                            sch[i][200]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/80)*100
                    sch[i][201]=hist
                    sch[i][202]=histp
                    geo=0
                    gp=(geo/80)*100
                    sch[i][203]=geo
                    sch[i][204]=gp
                    civ=0
                    civp=(civ/80)*100
                    sch[i][205]=civ
                    sch[i][206]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][207]=gk
                    sch[i][208]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][209]=msc
                    sch[i][210]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/80)*100
                    sch[i][230]=evs
                    sch[i][231]=evsp
                    total_marks=sch[i][181]+sch[i][183]+sch[i][185]+sch[i][187]+sch[i][189]+sch[i][191]+sch[i][193]+sch[i][195]+sch[i][197]+sch[i][199]+sch[i][201]+sch[i][203]+sch[i][205]+sch[i][207]+sch[i][209]+sch[i][230]
                    sch[i][211]=total_marks
                    total_percent_t2=(total_marks/560)*100
                    sch[i][212]=total_percent_t2
                    
            ch=input("Press any key to compute overall student mark sheet: ")
            if total_percent_ut1>=total_percent_ut2:
                best_utI=(5/100)*total_percent_ut1
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            else:
                best_utI=(5/100)*total_percent_ut2
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            a=(20/100)*total_percent_t1
            sch[i][215]=a
            b=(60/100)*total_percent_t2
            sch[i][216]=b
            tp_ut=best_utI+best_utII
            sch[i][217]=tp_ut
            tp_t=a+b
            sch[i][218]=tp_t
            tp_tp=tp_ut+tp_t+sch[i][19]+sch[i][20]
            sch[i][219]=tp_tp
                
                
        elif sch[i][10]==8:
            if sch[i][3]=='THREE' or sch[i][3]=='3' or sch[i][3]=='III':
                u=input("Enter: ")
                if sch[i][13]=='yes-ut1':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-1(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][21]=eng
                    sch[i][22]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][232]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][23]=hin
                        sch[i][24]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][25]=beng
                        sch[i][26]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][27]=sans
                        sch[i][28]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][232]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][23]=hin
                            sch[i][24]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][25]=beng
                            sch[i][26]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][27]=sans
                            sch[i][28]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][29]=chem
                    sch[i][30]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][31]=phy
                    sch[i][32]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][33]=maths
                    sch[i][34]=mp
                    cs='I'
                    sch[i][233]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][35]=CS
                        sch[i][36]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][37]=IT
                        sch[i][38]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][39]=AI
                        sch[i][40]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][233]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][35]=CS
                            sch[i][36]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][37]=IT
                            sch[i][38]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][39]=AI
                            sch[i][40]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][41]=hist
                    sch[i][42]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][43]=geo
                    sch[i][44]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][45]=civ
                    sch[i][46]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][47]=gk
                    sch[i][48]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][49]=msc
                    sch[i][50]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][220]=evs
                    sch[i][221]=evsp
                    total_marks=sch[i][21]+sch[i][23]+sch[i][25]+sch[i][27]+sch[i][29]+sch[i][31]+sch[i][33]+sch[i][35]+sch[i][37]+sch[i][39]+sch[i][41]+sch[i][43]+sch[i][45]+sch[i][47]+sch[i][49]+sch[i][220]
                    sch[i][51]=total_marks
                    total_percent_ut1=(total_marks/280)*100
                    sch[i][52]=total_percent_ut1
                
                v=input("Enter: ")
                if sch[i][14]=='yes-ut2':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-2(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][53]=eng
                    sch[i][54]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][234]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][55]=hin
                        sch[i][56]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][57]=beng
                        sch[i][58]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][59]=sans
                        sch[i][60]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][234]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][55]=hin
                            sch[i][56]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][57]=beng
                            sch[i][58]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][59]=sans
                            sch[i][60]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][61]=chem
                    sch[i][62]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][63]=phy
                    sch[i][64]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][65]=maths
                    sch[i][66]=mp
                    cs='I'
                    sch[i][235]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][67]=CS
                        sch[i][68]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][69]=IT
                        sch[i][70]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][71]=AI
                        sch[i][72]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][235]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][67]=CS
                            sch[i][68]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][69]=IT
                            sch[i][70]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][71]=AI
                            sch[i][72]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][73]=hist
                    sch[i][74]=histp
                    geo=0
                    sch[i][75]=geo
                    sch[i][76]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][77]=civ
                    sch[i][78]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][79]=gk
                    sch[i][80]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][81]=msc
                    sch[i][82]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][222]=evs
                    sch[i][223]=evsp
                    total_marks=sch[i][53]+sch[i][55]+sch[i][57]+sch[i][59]+sch[i][61]+sch[i][63]+sch[i][65]+sch[i][67]+sch[i][69]+sch[i][71]+sch[i][73]+sch[i][75]+sch[i][77]+sch[i][79]+sch[i][81]+sch[i][222]
                    sch[i][83]=total_marks
                    total_percent_ut2=(total_marks/280)*100
                    sch[i][84]=total_percent_ut2
                           
                w=input("Enter: ")
                if sch[i][15]=='yes-t1':
                    print("MARKS SCORED BY THE STUDENT IN TERM-1(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][85]=eng
                    sch[i][86]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][236]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][87]=hin
                        sch[i][88]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][89]=beng
                        sch[i][90]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][91]=sans
                        sch[i][92]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][236]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][87]=hin
                            sch[i][88]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][89]=beng
                            sch[i][90]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][91]=sans
                            sch[i][92]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/80)*100
                    sch[i][93]=chem
                    sch[i][94]=cp
                    phy=0
                    pp=(phy/80)*100
                    sch[i][95]=phy
                    sch[i][96]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][97]=maths
                    sch[i][98]=mp
                    cs='I'
                    sch[i][237]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/80)*100
                        sch[i][99]=CS
                        sch[i][100]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][101]=IT
                        sch[i][102]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/80)*100
                        sch[i][103]=AI
                        sch[i][104]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][237]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/80)*100
                            sch[i][99]=CS
                            sch[i][100]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][101]=IT
                            sch[i][102]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/80)*100
                            sch[i][103]=AI
                            sch[i][104]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/80)*100
                    sch[i][105]=hist
                    sch[i][106]=histp
                    geo=0
                    gp=(geo/80)*100
                    sch[i][107]=geo
                    sch[i][108]=gp
                    civ=0
                    civp=(civ/80)*100
                    sch[i][109]=civ
                    sch[i][110]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][111]=gk
                    sch[i][112]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][113]=msc
                    sch[i][114]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/80)*100
                    sch[i][224]=evs
                    sch[i][225]=evsp
                    total_marks=sch[i][85]+sch[i][87]+sch[i][89]+sch[i][91]+sch[i][93]+sch[i][95]+sch[i][97]+sch[i][99]+sch[i][101]+sch[i][103]+sch[i][105]+sch[i][107]+sch[i][109]+sch[i][111]+sch[i][113]+sch[i][224]
                    sch[i][115]=total_marks
                    total_percent_t1=(total_marks/560)*100
                    sch[i][116]=total_percent_t1
                            
                x=input("Enter: ")  
                if sch[i][16]=='yes-ut3':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-3(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][117]=eng
                    sch[i][118]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][238]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][119]=hin
                        sch[i][120]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][121]=beng
                        sch[i][122]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][123]=sans
                        sch[i][124]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][238]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][119]=hin
                            sch[i][120]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][121]=beng
                            sch[i][122]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][123]=sans
                            sch[i][124]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][125]=chem
                    sch[i][126]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][127]=phy
                    sch[i][128]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][129]=maths
                    sch[i][130]=mp
                    cs='I'
                    sch[i][239]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][131]=CS
                        sch[i][132]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][133]=IT
                        sch[i][134]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][135]=AI
                        sch[i][136]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][239]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][131]=CS
                            sch[i][132]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][133]=IT
                            sch[i][134]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][135]=AI
                            sch[i][136]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][137]=hist
                    sch[i][138]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][139]=geo
                    sch[i][140]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][141]=civ
                    sch[i][142]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][143]=gk
                    sch[i][144]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][145]=msc
                    sch[i][146]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][226]=evs
                    sch[i][227]=evsp
                    total_marks=sch[i][117]+sch[i][119]+sch[i][121]+sch[i][123]+sch[i][125]+sch[i][127]+sch[i][129]+sch[i][131]+sch[i][133]+sch[i][135]+sch[i][137]+sch[i][139]+sch[i][141]+sch[i][143]+sch[i][145]+sch[i][226]
                    sch[i][147]=total_marks
                    total_percent_ut3=(total_marks/280)*100
                    sch[i][148]=total_percent_ut3
                
                y=input("Enter: ")            
                if sch[i][17]=='yes-ut4':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-4(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][149]=eng
                    sch[i][150]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][240]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][151]=hin
                        sch[i][152]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][153]=beng
                        sch[i][154]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][155]=sans
                        sch[i][156]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][240]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][151]=hin
                            sch[i][152]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][153]=beng
                            sch[i][154]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][155]=sans
                            sch[i][156]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][157]=chem
                    sch[i][158]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][159]=phy
                    sch[i][160]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][161]=maths
                    sch[i][162]=mp
                    cs='I'
                    sch[i][241]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][163]=CS
                        sch[i][164]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][165]=IT
                        sch[i][166]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][167]=AI
                        sch[i][168]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][241]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][163]=CS
                            sch[i][164]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][165]=IT
                            sch[i][166]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][167]=AI
                            sch[i][168]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][169]=hist
                    sch[i][170]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][171]=geo
                    sch[i][172]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][173]=civ
                    sch[i][174]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][175]=gk
                    sch[i][176]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][177]=msc
                    sch[i][178]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][228]=evs
                    sch[i][229]=evsp
                    total_marks=sch[i][149]+sch[i][151]+sch[i][153]+sch[i][155]+sch[i][157]+sch[i][159]+sch[i][161]+sch[i][163]+sch[i][165]+sch[i][167]+sch[i][169]+sch[i][171]+sch[i][173]+sch[i][175]+sch[i][177]+sch[i][228]
                    sch[i][179]=total_marks
                    total_percent_ut4=(total_marks/280)*100
                    sch[i][180]=total_percent_ut4
                           
                z=input("Enter: ")
                if sch[i][18]=='yes-t2':
                    print("MARKS SCORED BY THE STUDENT IN TERM-2(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][181]=eng
                    sch[i][182]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][242]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][183]=hin
                        sch[i][184]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][185]=beng
                        sch[i][186]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][187]=sans
                        sch[i][188]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][242]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][183]=hin
                            sch[i][184]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][185]=beng
                            sch[i][186]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/80)*100
                            sch[i][187]=sans
                            sch[i][188]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/80)*100
                    sch[i][189]=chem
                    sch[i][190]=cp
                    phy=0
                    pp=(phy/80)*100
                    sch[i][191]=phy
                    sch[i][192]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][193]=maths
                    sch[i][194]=mp
                    cs='I'
                    sch[i][243]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/80)*100
                        sch[i][195]=CS
                        sch[i][196]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][197]=IT
                        sch[i][198]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/80)*100
                        sch[i][199]=AI
                        sch[i][200]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][243]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/80)*100
                            sch[i][195]=CS
                            sch[i][196]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][197]=IT
                            sch[i][198]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/80)*100
                            sch[i][199]=AI
                            sch[i][200]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/80)*100
                    sch[i][201]=hist
                    sch[i][202]=histp
                    geo=0
                    gp=(geo/80)*100
                    sch[i][203]=geo
                    sch[i][204]=gp
                    civ=0
                    civp=(civ/80)*100
                    sch[i][205]=civ
                    sch[i][206]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][207]=gk
                    sch[i][208]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][209]=msc
                    sch[i][210]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/80)*100
                    sch[i][230]=evs
                    sch[i][231]=evsp
                    total_marks=sch[i][181]+sch[i][183]+sch[i][185]+sch[i][187]+sch[i][189]+sch[i][191]+sch[i][193]+sch[i][195]+sch[i][197]+sch[i][199]+sch[i][201]+sch[i][203]+sch[i][205]+sch[i][207]+sch[i][209]+sch[i][230]
                    sch[i][211]=total_marks
                    total_percent_t2=(total_marks/560)*100
                    sch[i][212]=total_percent_t2
                    
            ch=input("Press any key to compute overall student mark sheet: ")
            if total_percent_ut1>=total_percent_ut2:
                best_utI=(5/100)*total_percent_ut1
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            else:
                best_utI=(5/100)*total_percent_ut2
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            a=(20/100)*total_percent_t1
            sch[i][215]=a
            b=(60/100)*total_percent_t2
            sch[i][216]=b
            tp_ut=best_utI+best_utII
            sch[i][217]=tp_ut
            tp_t=a+b
            sch[i][218]=tp_t
            tp_tp=tp_ut+tp_t+sch[i][19]+sch[i][20]
            sch[i][219]=tp_tp
                
                
        elif sch[i][10]==9:
            if sch[i][3]=='FOUR' or sch[i][3]=='4' or sch[i][3]=='IV':
                u=input("Enter: ")
                if sch[i][13]=='yes-ut1':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-1(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][21]=eng
                    sch[i][22]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][232]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][23]=hin
                        sch[i][24]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][25]=beng
                        sch[i][26]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][27]=sans
                        sch[i][28]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][232]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][23]=hin
                            sch[i][24]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][25]=beng
                            sch[i][26]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][27]=sans
                            sch[i][28]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][29]=chem
                    sch[i][30]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][31]=phy
                    sch[i][32]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][33]=maths
                    sch[i][34]=mp
                    cs='I'
                    sch[i][233]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][35]=CS
                        sch[i][36]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][37]=IT
                        sch[i][38]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][39]=AI
                        sch[i][40]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][233]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][35]=CS
                            sch[i][36]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][37]=IT
                            sch[i][38]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][39]=AI
                            sch[i][40]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][41]=hist
                    sch[i][42]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][43]=geo
                    sch[i][44]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][45]=civ
                    sch[i][46]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][47]=gk
                    sch[i][48]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][49]=msc
                    sch[i][50]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][220]=evs
                    sch[i][221]=evsp
                    total_marks=sch[i][21]+sch[i][23]+sch[i][25]+sch[i][27]+sch[i][29]+sch[i][31]+sch[i][33]+sch[i][35]+sch[i][37]+sch[i][39]+sch[i][41]+sch[i][43]+sch[i][45]+sch[i][47]+sch[i][49]+sch[i][220]
                    sch[i][51]=total_marks
                    total_percent_ut1=(total_marks/280)*100
                    sch[i][52]=total_percent_ut1
                
                v=input("Enter: ")
                if sch[i][14]=='yes-ut2':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-2(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][53]=eng
                    sch[i][54]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][234]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][55]=hin
                        sch[i][56]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][57]=beng
                        sch[i][58]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][59]=sans
                        sch[i][60]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][234]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][55]=hin
                            sch[i][56]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][57]=beng
                            sch[i][58]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][59]=sans
                            sch[i][60]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][61]=chem
                    sch[i][62]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][63]=phy
                    sch[i][64]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][65]=maths
                    sch[i][66]=mp
                    cs='I'
                    sch[i][235]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][67]=CS
                        sch[i][68]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][69]=IT
                        sch[i][70]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][71]=AI
                        sch[i][72]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][235]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][67]=CS
                            sch[i][68]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][69]=IT
                            sch[i][70]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][71]=AI
                            sch[i][72]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][73]=hist
                    sch[i][74]=histp
                    geo=0
                    sch[i][75]=geo
                    sch[i][76]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][77]=civ
                    sch[i][78]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][79]=gk
                    sch[i][80]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][81]=msc
                    sch[i][82]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][222]=evs
                    sch[i][223]=evsp
                    total_marks=sch[i][53]+sch[i][55]+sch[i][57]+sch[i][59]+sch[i][61]+sch[i][63]+sch[i][65]+sch[i][67]+sch[i][69]+sch[i][71]+sch[i][73]+sch[i][75]+sch[i][77]+sch[i][79]+sch[i][81]+sch[i][222]
                    sch[i][83]=total_marks
                    total_percent_ut2=(total_marks/280)*100
                    sch[i][84]=total_percent_ut2
                           
                w=input("Enter: ")
                if sch[i][15]=='yes-t1':
                    print("MARKS SCORED BY THE STUDENT IN TERM-1(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][85]=eng
                    sch[i][86]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][236]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][87]=hin
                        sch[i][88]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][89]=beng
                        sch[i][90]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][91]=sans
                        sch[i][92]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][236]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][87]=hin
                            sch[i][88]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][89]=beng
                            sch[i][90]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][91]=sans
                            sch[i][92]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/80)*100
                    sch[i][93]=chem
                    sch[i][94]=cp
                    phy=0
                    pp=(phy/80)*100
                    sch[i][95]=phy
                    sch[i][96]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][97]=maths
                    sch[i][98]=mp
                    cs='I'
                    sch[i][237]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/80)*100
                        sch[i][99]=CS
                        sch[i][100]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][101]=IT
                        sch[i][102]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/80)*100
                        sch[i][103]=AI
                        sch[i][104]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][237]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/80)*100
                            sch[i][99]=CS
                            sch[i][100]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][101]=IT
                            sch[i][102]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/80)*100
                            sch[i][103]=AI
                            sch[i][104]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/80)*100
                    sch[i][105]=hist
                    sch[i][106]=histp
                    geo=0
                    gp=(geo/80)*100
                    sch[i][107]=geo
                    sch[i][108]=gp
                    civ=0
                    civp=(civ/80)*100
                    sch[i][109]=civ
                    sch[i][110]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][111]=gk
                    sch[i][112]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][113]=msc
                    sch[i][114]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/80)*100
                    sch[i][224]=evs
                    sch[i][225]=evsp
                    total_marks=sch[i][85]+sch[i][87]+sch[i][89]+sch[i][91]+sch[i][93]+sch[i][95]+sch[i][97]+sch[i][99]+sch[i][101]+sch[i][103]+sch[i][105]+sch[i][107]+sch[i][109]+sch[i][111]+sch[i][113]+sch[i][224]
                    sch[i][115]=total_marks
                    total_percent_t1=(total_marks/560)*100
                    sch[i][116]=total_percent_t1
                            
                x=input("Enter: ")  
                if sch[i][16]=='yes-ut3':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-3(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][117]=eng
                    sch[i][118]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][238]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][119]=hin
                        sch[i][120]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][121]=beng
                        sch[i][122]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][123]=sans
                        sch[i][124]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][238]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][119]=hin
                            sch[i][120]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][121]=beng
                            sch[i][122]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][123]=sans
                            sch[i][124]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][125]=chem
                    sch[i][126]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][127]=phy
                    sch[i][128]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][129]=maths
                    sch[i][130]=mp
                    cs='I'
                    sch[i][239]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][131]=CS
                        sch[i][132]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][133]=IT
                        sch[i][134]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][135]=AI
                        sch[i][136]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][239]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][131]=CS
                            sch[i][132]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][133]=IT
                            sch[i][134]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][135]=AI
                            sch[i][136]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][137]=hist
                    sch[i][138]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][139]=geo
                    sch[i][140]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][141]=civ
                    sch[i][142]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][143]=gk
                    sch[i][144]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][145]=msc
                    sch[i][146]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][226]=evs
                    sch[i][227]=evsp
                    total_marks=sch[i][117]+sch[i][119]+sch[i][121]+sch[i][123]+sch[i][125]+sch[i][127]+sch[i][129]+sch[i][131]+sch[i][133]+sch[i][135]+sch[i][137]+sch[i][139]+sch[i][141]+sch[i][143]+sch[i][145]+sch[i][226]
                    sch[i][147]=total_marks
                    total_percent_ut3=(total_marks/280)*100
                    sch[i][148]=total_percent_ut3
                
                y=input("Enter: ")            
                if sch[i][17]=='yes-ut4':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-4(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][149]=eng
                    sch[i][150]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][240]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][151]=hin
                        sch[i][152]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][153]=beng
                        sch[i][154]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][155]=sans
                        sch[i][156]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][240]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][151]=hin
                            sch[i][152]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][153]=beng
                            sch[i][154]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][155]=sans
                            sch[i][156]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/40)*100
                    sch[i][157]=chem
                    sch[i][158]=cp
                    phy=0
                    pp=(phy/40)*100
                    sch[i][159]=phy
                    sch[i][160]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][161]=maths
                    sch[i][162]=mp
                    cs='I'
                    sch[i][241]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/40)*100
                        sch[i][163]=CS
                        sch[i][164]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][165]=IT
                        sch[i][166]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/40)*100
                        sch[i][167]=AI
                        sch[i][168]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][241]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/40)*100
                            sch[i][163]=CS
                            sch[i][164]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][165]=IT
                            sch[i][166]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/40)*100
                            sch[i][167]=AI
                            sch[i][168]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/40)*100
                    sch[i][169]=hist
                    sch[i][170]=histp
                    geo=0
                    gp=(geo/40)*100
                    sch[i][171]=geo
                    sch[i][172]=gp
                    civ=0
                    civp=(civ/40)*100
                    sch[i][173]=civ
                    sch[i][174]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][175]=gk
                    sch[i][176]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][177]=msc
                    sch[i][178]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/40)*100
                    sch[i][228]=evs
                    sch[i][229]=evsp
                    total_marks=sch[i][149]+sch[i][151]+sch[i][153]+sch[i][155]+sch[i][157]+sch[i][159]+sch[i][161]+sch[i][163]+sch[i][165]+sch[i][167]+sch[i][169]+sch[i][171]+sch[i][173]+sch[i][175]+sch[i][177]+sch[i][228]
                    sch[i][179]=total_marks
                    total_percent_ut4=(total_marks/280)*100
                    sch[i][180]=total_percent_ut4
                           
                z=input("Enter: ")
                if sch[i][18]=='yes-t2':
                    print("MARKS SCORED BY THE STUDENT IN TERM-2(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][181]=eng
                    sch[i][182]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][242]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][183]=hin
                        sch[i][184]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][185]=beng
                        sch[i][186]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][187]=sans
                        sch[i][188]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][242]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][183]=hin
                            sch[i][184]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][185]=beng
                            sch[i][186]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/80)*100
                            sch[i][187]=sans
                            sch[i][188]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=0
                    cp=(chem/80)*100
                    sch[i][189]=chem
                    sch[i][190]=cp
                    phy=0
                    pp=(phy/80)*100
                    sch[i][191]=phy
                    sch[i][192]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][193]=maths
                    sch[i][194]=mp
                    cs='I'
                    sch[i][243]=cs
                    if cs=='C':
                        CS=0
                        csp=(CS/80)*100
                        sch[i][195]=CS
                        sch[i][196]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][197]=IT
                        sch[i][198]=itp
                    elif cs=='A':
                        AI=0
                        aip=(AI/80)*100
                        sch[i][199]=AI
                        sch[i][200]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs='I'
                        sch[i][243]=cs
                        if cs=='C':
                            CS=0
                            csp=(CS/80)*100
                            sch[i][195]=CS
                            sch[i][196]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][197]=IT
                            sch[i][198]=itp
                        elif cs=='A':
                            AI=0
                            aip=(AI/80)*100
                            sch[i][199]=AI
                            sch[i][200]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=0
                    histp=(hist/80)*100
                    sch[i][201]=hist
                    sch[i][202]=histp
                    geo=0
                    gp=(geo/80)*100
                    sch[i][203]=geo
                    sch[i][204]=gp
                    civ=0
                    civp=(civ/80)*100
                    sch[i][205]=civ
                    sch[i][206]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][207]=gk
                    sch[i][208]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][209]=msc
                    sch[i][210]=mscp
                    evs=eval(input("Enter the marks scored in ENVIRONMENTAL SCIENCE: "))
                    evsp=(evs/80)*100
                    sch[i][230]=evs
                    sch[i][231]=evsp
                    total_marks=sch[i][181]+sch[i][183]+sch[i][185]+sch[i][187]+sch[i][189]+sch[i][191]+sch[i][193]+sch[i][195]+sch[i][197]+sch[i][199]+sch[i][201]+sch[i][203]+sch[i][205]+sch[i][207]+sch[i][209]+sch[i][230]
                    sch[i][211]=total_marks
                    total_percent_t2=(total_marks/560)*100
                    sch[i][212]=total_percent_t2
                    
            ch=input("Press any key to compute overall student mark sheet: ")
            if total_percent_ut1>=total_percent_ut2:
                best_utI=(5/100)*total_percent_ut1
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            else:
                best_utI=(5/100)*total_percent_ut2
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            a=(20/100)*total_percent_t1
            sch[i][215]=a
            b=(60/100)*total_percent_t2
            sch[i][216]=b
            tp_ut=best_utI+best_utII
            sch[i][217]=tp_ut
            tp_t=a+b
            sch[i][218]=tp_t
            tp_tp=tp_ut+tp_t+sch[i][19]+sch[i][20]
            sch[i][219]=tp_tp
                
                
        elif sch[i][10]==10:
            if sch[i][3]=='FIVE' or sch[i][3]=='5' or sch[i][3]=='V':
                u=input("Enter: ")
                if sch[i][13]=='yes-ut1':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-1(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][21]=eng
                    sch[i][22]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][232]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][23]=hin
                        sch[i][24]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][25]=beng
                        sch[i][26]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][27]=sans
                        sch[i][28]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][232]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][23]=hin
                            sch[i][24]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][25]=beng
                            sch[i][26]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][27]=sans
                            sch[i][28]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][29]=chem
                    sch[i][30]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][31]=phy
                    sch[i][32]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][33]=maths
                    sch[i][34]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][233]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][35]=CS
                        sch[i][36]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][37]=IT
                        sch[i][38]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][39]=AI
                        sch[i][40]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][233]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][35]=CS
                            sch[i][36]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][37]=IT
                            sch[i][38]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][39]=AI
                            sch[i][40]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][41]=hist
                    sch[i][42]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][43]=geo
                    sch[i][44]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][45]=civ
                    sch[i][46]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][47]=gk
                    sch[i][48]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][49]=msc
                    sch[i][50]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][220]=bio
                    sch[i][221]=biop
                    total_marks=sch[i][21]+sch[i][23]+sch[i][25]+sch[i][27]+sch[i][29]+sch[i][31]+sch[i][33]+sch[i][35]+sch[i][37]+sch[i][39]+sch[i][41]+sch[i][43]+sch[i][45]+sch[i][47]+sch[i][49]+sch[i][220]
                    sch[i][51]=total_marks
                    total_percent_ut1=(total_marks/480)*100
                    sch[i][52]=total_percent_ut1
                
                v=input("Enter: ")
                if sch[i][14]=='yes-ut2':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-2(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][53]=eng
                    sch[i][54]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][234]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][55]=hin
                        sch[i][56]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][57]=beng
                        sch[i][58]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][59]=sans
                        sch[i][60]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][234]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][55]=hin
                            sch[i][56]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][57]=beng
                            sch[i][58]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][59]=sans
                            sch[i][60]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][61]=chem
                    sch[i][62]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][63]=phy
                    sch[i][64]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][65]=maths
                    sch[i][66]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][235]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][67]=CS
                        sch[i][68]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][69]=IT
                        sch[i][70]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][71]=AI
                        sch[i][72]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][235]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][67]=CS
                            sch[i][68]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][69]=IT
                            sch[i][70]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][71]=AI
                            sch[i][72]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][73]=hist
                    sch[i][74]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][75]=geo
                    sch[i][76]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][77]=civ
                    sch[i][78]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][79]=gk
                    sch[i][80]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][81]=msc
                    sch[i][82]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][222]=bio
                    sch[i][223]=biop
                    total_marks=sch[i][53]+sch[i][55]+sch[i][57]+sch[i][59]+sch[i][61]+sch[i][63]+sch[i][65]+sch[i][67]+sch[i][69]+sch[i][71]+sch[i][73]+sch[i][75]+sch[i][77]+sch[i][79]+sch[i][81]+sch[i][222]
                    sch[i][83]=total_marks
                    total_percent_ut2=(total_marks/480)*100
                    sch[i][84]=total_percent_ut2
                           
                w=input("Enter: ")
                if sch[i][15]=='yes-t1':
                    print("MARKS SCORED BY THE STUDENT IN TERM-1(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][85]=eng
                    sch[i][86]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][236]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][87]=hin
                        sch[i][88]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][89]=beng
                        sch[i][90]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][91]=sans
                        sch[i][92]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][236]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][87]=hin
                            sch[i][88]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][89]=beng
                            sch[i][90]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][91]=sans
                            sch[i][92]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/80)*100
                    sch[i][93]=chem
                    sch[i][94]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/80)*100
                    sch[i][95]=phy
                    sch[i][96]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][97]=maths
                    sch[i][98]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][237]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/80)*100
                        sch[i][99]=CS
                        sch[i][100]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][101]=IT
                        sch[i][102]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/80)*100
                        sch[i][103]=AI
                        sch[i][104]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][237]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/80)*100
                            sch[i][99]=CS
                            sch[i][100]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][101]=IT
                            sch[i][102]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/80)*100
                            sch[i][103]=AI
                            sch[i][104]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/80)*100
                    sch[i][105]=hist
                    sch[i][106]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/80)*100
                    sch[i][107]=geo
                    sch[i][108]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/80)*100
                    sch[i][109]=civ
                    sch[i][110]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][111]=gk
                    sch[i][112]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][113]=msc
                    sch[i][114]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/80)*100
                    sch[i][224]=bio
                    sch[i][225]=biop
                    total_marks=sch[i][85]+sch[i][87]+sch[i][89]+sch[i][91]+sch[i][93]+sch[i][95]+sch[i][97]+sch[i][99]+sch[i][101]+sch[i][103]+sch[i][105]+sch[i][107]+sch[i][109]+sch[i][111]+sch[i][113]+sch[i][224]
                    sch[i][115]=total_marks
                    total_percent_t1=(total_marks/960)*100
                    sch[i][116]=total_percent_t1
                            
                x=input("Enter: ")
                if sch[i][16]=='yes-ut3':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-3(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][117]=eng
                    sch[i][118]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][238]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][119]=hin
                        sch[i][120]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][121]=beng
                        sch[i][122]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][123]=sans
                        sch[i][124]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][238]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][119]=hin
                            sch[i][120]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][121]=beng
                            sch[i][122]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][123]=sans
                            sch[i][124]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][125]=chem
                    sch[i][126]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][127]=phy
                    sch[i][128]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][129]=maths
                    sch[i][130]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][239]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][131]=CS
                        sch[i][132]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][133]=IT
                        sch[i][134]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][135]=AI
                        sch[i][136]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][239]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][131]=CS
                            sch[i][132]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][133]=IT
                            sch[i][134]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][135]=AI
                            sch[i][136]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][137]=hist
                    sch[i][138]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][139]=geo
                    sch[i][140]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][141]=civ
                    sch[i][142]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][143]=gk
                    sch[i][144]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][145]=msc
                    sch[i][146]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][226]=bio
                    sch[i][227]=biop
                    total_marks=sch[i][117]+sch[i][119]+sch[i][121]+sch[i][123]+sch[i][125]+sch[i][127]+sch[i][129]+sch[i][131]+sch[i][133]+sch[i][135]+sch[i][137]+sch[i][139]+sch[i][141]+sch[i][143]+sch[i][145]+sch[i][226]
                    sch[i][147]=total_marks
                    total_percent_ut3=(total_marks/480)*100
                    sch[i][148]=total_percent_ut3
                            
                y=input("Enter: ")
                if sch[i][17]=='yes-ut4':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-4(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][149]=eng
                    sch[i][150]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][240]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][151]=hin
                        sch[i][152]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][153]=beng
                        sch[i][154]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][155]=sans
                        sch[i][156]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][240]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][151]=hin
                            sch[i][152]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][153]=beng
                            sch[i][154]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][155]=sans
                            sch[i][156]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][157]=chem
                    sch[i][158]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][159]=phy
                    sch[i][160]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][161]=maths
                    sch[i][162]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][241]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][163]=CS
                        sch[i][164]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][165]=IT
                        sch[i][166]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][167]=AI
                        sch[i][168]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][241]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][163]=CS
                            sch[i][164]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][165]=IT
                            sch[i][166]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][167]=AI
                            sch[i][168]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][169]=hist
                    sch[i][170]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][171]=geo
                    sch[i][172]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][173]=civ
                    sch[i][174]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][175]=gk
                    sch[i][176]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][177]=msc
                    sch[i][178]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][228]=bio
                    sch[i][229]=biop
                    total_marks=sch[i][149]+sch[i][151]+sch[i][153]+sch[i][155]+sch[i][157]+sch[i][159]+sch[i][161]+sch[i][163]+sch[i][165]+sch[i][167]+sch[i][169]+sch[i][171]+sch[i][173]+sch[i][175]+sch[i][177]+sch[i][228]
                    sch[i][179]=total_marks
                    total_percent_ut4=(total_marks/480)*100
                    sch[i][180]=total_percent_ut4
                           
                z=input("Enter: ")
                if sch[i][18]=='yes-t2':
                    print("MARKS SCORED BY THE STUDENT IN TERM-2(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][181]=eng
                    sch[i][182]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][242]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][183]=hin
                        sch[i][184]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][185]=beng
                        sch[i][186]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][187]=sans
                        sch[i][188]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][242]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][183]=hin
                            sch[i][184]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][185]=beng
                            sch[i][186]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/80)*100
                            sch[i][187]=sans
                            sch[i][188]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/80)*100
                    sch[i][189]=chem
                    sch[i][190]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/80)*100
                    sch[i][191]=phy
                    sch[i][192]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][193]=maths
                    sch[i][194]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][243]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/80)*100
                        sch[i][195]=CS
                        sch[i][196]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][197]=IT
                        sch[i][198]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/80)*100
                        sch[i][199]=AI
                        sch[i][200]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][243]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/80)*100
                            sch[i][195]=CS
                            sch[i][196]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][197]=IT
                            sch[i][198]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/80)*100
                            sch[i][199]=AI
                            sch[i][200]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/80)*100
                    sch[i][201]=hist
                    sch[i][202]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/80)*100
                    sch[i][203]=geo
                    sch[i][204]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/80)*100
                    sch[i][205]=civ
                    sch[i][206]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][207]=gk
                    sch[i][208]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][209]=msc
                    sch[i][210]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/80)*100
                    sch[i][230]=bio
                    sch[i][231]=biop
                    total_marks=sch[i][181]+sch[i][183]+sch[i][185]+sch[i][187]+sch[i][189]+sch[i][191]+sch[i][193]+sch[i][195]+sch[i][197]+sch[i][199]+sch[i][201]+sch[i][203]+sch[i][205]+sch[i][207]+sch[i][209]+sch[i][230]
                    sch[i][211]=total_marks
                    total_percent_t2=(total_marks/960)*100
                    sch[i][212]=total_percent_t2
                    
            ch=input("Press any key to compute overall student mark sheet: ")
            if total_percent_ut1>=total_percent_ut2:
                best_utI=(5/100)*total_percent_ut1
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            else:
                best_utI=(5/100)*total_percent_ut2
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            a=(20/100)*total_percent_t1
            sch[i][215]=a
            b=(60/100)*total_percent_t2
            sch[i][216]=b
            tp_ut=best_utI+best_utII
            sch[i][217]=tp_ut
            tp_t=a+b
            sch[i][218]=tp_t
            tp_tp=tp_ut+tp_t+sch[i][19]+sch[i][20]
            sch[i][219]=tp_tp
                
                
        elif sch[i][10]==11:
            if sch[i][3]=='SIX' or sch[i][3]=='6' or sch[i][3]=='VI':
                u=input("Enter: ")
                if sch[i][13]=='yes-ut1':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-1(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][21]=eng
                    sch[i][22]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][232]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][23]=hin
                        sch[i][24]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][25]=beng
                        sch[i][26]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][27]=sans
                        sch[i][28]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][232]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][23]=hin
                            sch[i][24]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][25]=beng
                            sch[i][26]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][27]=sans
                            sch[i][28]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][29]=chem
                    sch[i][30]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][31]=phy
                    sch[i][32]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][33]=maths
                    sch[i][34]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][233]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][35]=CS
                        sch[i][36]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][37]=IT
                        sch[i][38]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][39]=AI
                        sch[i][40]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][233]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][35]=CS
                            sch[i][36]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][37]=IT
                            sch[i][38]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][39]=AI
                            sch[i][40]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][41]=hist
                    sch[i][42]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][43]=geo
                    sch[i][44]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][45]=civ
                    sch[i][46]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][47]=gk
                    sch[i][48]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][49]=msc
                    sch[i][50]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][220]=bio
                    sch[i][221]=biop
                    total_marks=sch[i][21]+sch[i][23]+sch[i][25]+sch[i][27]+sch[i][29]+sch[i][31]+sch[i][33]+sch[i][35]+sch[i][37]+sch[i][39]+sch[i][41]+sch[i][43]+sch[i][45]+sch[i][47]+sch[i][49]+sch[i][220]
                    sch[i][51]=total_marks
                    total_percent_ut1=(total_marks/480)*100
                    sch[i][52]=total_percent_ut1
                
                v=input("Enter: ")
                if sch[i][14]=='yes-ut2':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-2(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][53]=eng
                    sch[i][54]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][234]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][55]=hin
                        sch[i][56]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][57]=beng
                        sch[i][58]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][59]=sans
                        sch[i][60]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][234]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][55]=hin
                            sch[i][56]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][57]=beng
                            sch[i][58]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][59]=sans
                            sch[i][60]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][61]=chem
                    sch[i][62]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][63]=phy
                    sch[i][64]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][65]=maths
                    sch[i][66]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][235]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][67]=CS
                        sch[i][68]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][69]=IT
                        sch[i][70]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][71]=AI
                        sch[i][72]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][235]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][67]=CS
                            sch[i][68]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][69]=IT
                            sch[i][70]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][71]=AI
                            sch[i][72]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][73]=hist
                    sch[i][74]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][75]=geo
                    sch[i][76]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][77]=civ
                    sch[i][78]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][79]=gk
                    sch[i][80]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][81]=msc
                    sch[i][82]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][222]=bio
                    sch[i][223]=biop
                    total_marks=sch[i][53]+sch[i][55]+sch[i][57]+sch[i][59]+sch[i][61]+sch[i][63]+sch[i][65]+sch[i][67]+sch[i][69]+sch[i][71]+sch[i][73]+sch[i][75]+sch[i][77]+sch[i][79]+sch[i][81]+sch[i][222]
                    sch[i][83]=total_marks
                    total_percent_ut2=(total_marks/480)*100
                    sch[i][84]=total_percent_ut2
                           
                w=input("Enter: ")
                if sch[i][15]=='yes-t1':
                    print("MARKS SCORED BY THE STUDENT IN TERM-1(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][85]=eng
                    sch[i][86]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][236]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][87]=hin
                        sch[i][88]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][89]=beng
                        sch[i][90]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][91]=sans
                        sch[i][92]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][236]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][87]=hin
                            sch[i][88]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][89]=beng
                            sch[i][90]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][91]=sans
                            sch[i][92]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/80)*100
                    sch[i][93]=chem
                    sch[i][94]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/80)*100
                    sch[i][95]=phy
                    sch[i][96]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][97]=maths
                    sch[i][98]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][237]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/80)*100
                        sch[i][99]=CS
                        sch[i][100]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][101]=IT
                        sch[i][102]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/80)*100
                        sch[i][103]=AI
                        sch[i][104]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][237]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/80)*100
                            sch[i][99]=CS
                            sch[i][100]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][101]=IT
                            sch[i][102]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/80)*100
                            sch[i][103]=AI
                            sch[i][104]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/80)*100
                    sch[i][105]=hist
                    sch[i][106]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/80)*100
                    sch[i][107]=geo
                    sch[i][108]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/80)*100
                    sch[i][109]=civ
                    sch[i][110]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][111]=gk
                    sch[i][112]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][113]=msc
                    sch[i][114]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/80)*100
                    sch[i][224]=bio
                    sch[i][225]=biop
                    total_marks=sch[i][85]+sch[i][87]+sch[i][89]+sch[i][91]+sch[i][93]+sch[i][95]+sch[i][97]+sch[i][99]+sch[i][101]+sch[i][103]+sch[i][105]+sch[i][107]+sch[i][109]+sch[i][111]+sch[i][113]+sch[i][224]
                    sch[i][115]=total_marks
                    total_percent_t1=(total_marks/960)*100
                    sch[i][116]=total_percent_t1
                            
                x=input("Enter: ")
                if sch[i][16]=='yes-ut3':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-3(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][117]=eng
                    sch[i][118]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][238]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][119]=hin
                        sch[i][120]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][121]=beng
                        sch[i][122]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][123]=sans
                        sch[i][124]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][238]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][119]=hin
                            sch[i][120]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][121]=beng
                            sch[i][122]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][123]=sans
                            sch[i][124]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][125]=chem
                    sch[i][126]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][127]=phy
                    sch[i][128]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][129]=maths
                    sch[i][130]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][239]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][131]=CS
                        sch[i][132]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][133]=IT
                        sch[i][134]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][135]=AI
                        sch[i][136]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][239]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][131]=CS
                            sch[i][132]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][133]=IT
                            sch[i][134]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][135]=AI
                            sch[i][136]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][137]=hist
                    sch[i][138]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][139]=geo
                    sch[i][140]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][141]=civ
                    sch[i][142]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][143]=gk
                    sch[i][144]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][145]=msc
                    sch[i][146]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][226]=bio
                    sch[i][227]=biop
                    total_marks=sch[i][117]+sch[i][119]+sch[i][121]+sch[i][123]+sch[i][125]+sch[i][127]+sch[i][129]+sch[i][131]+sch[i][133]+sch[i][135]+sch[i][137]+sch[i][139]+sch[i][141]+sch[i][143]+sch[i][145]+sch[i][226]
                    sch[i][147]=total_marks
                    total_percent_ut3=(total_marks/480)*100
                    sch[i][148]=total_percent_ut3
                            
                y=input("Enter: ")
                if sch[i][17]=='yes-ut4':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-4(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][149]=eng
                    sch[i][150]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][240]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][151]=hin
                        sch[i][152]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][153]=beng
                        sch[i][154]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][155]=sans
                        sch[i][156]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][240]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][151]=hin
                            sch[i][152]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][153]=beng
                            sch[i][154]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][155]=sans
                            sch[i][156]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][157]=chem
                    sch[i][158]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][159]=phy
                    sch[i][160]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][161]=maths
                    sch[i][162]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][241]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][163]=CS
                        sch[i][164]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][165]=IT
                        sch[i][166]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][167]=AI
                        sch[i][168]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][241]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][163]=CS
                            sch[i][164]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][165]=IT
                            sch[i][166]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][167]=AI
                            sch[i][168]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][169]=hist
                    sch[i][170]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][171]=geo
                    sch[i][172]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][173]=civ
                    sch[i][174]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][175]=gk
                    sch[i][176]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][177]=msc
                    sch[i][178]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][228]=bio
                    sch[i][229]=biop
                    total_marks=sch[i][149]+sch[i][151]+sch[i][153]+sch[i][155]+sch[i][157]+sch[i][159]+sch[i][161]+sch[i][163]+sch[i][165]+sch[i][167]+sch[i][169]+sch[i][171]+sch[i][173]+sch[i][175]+sch[i][177]+sch[i][228]
                    sch[i][179]=total_marks
                    total_percent_ut4=(total_marks/480)*100
                    sch[i][180]=total_percent_ut4
                           
                z=input("Enter: ")
                if sch[i][18]=='yes-t2':
                    print("MARKS SCORED BY THE STUDENT IN TERM-2(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][181]=eng
                    sch[i][182]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][242]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][183]=hin
                        sch[i][184]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][185]=beng
                        sch[i][186]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][187]=sans
                        sch[i][188]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][242]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][183]=hin
                            sch[i][184]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][185]=beng
                            sch[i][186]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/80)*100
                            sch[i][187]=sans
                            sch[i][188]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/80)*100
                    sch[i][189]=chem
                    sch[i][190]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/80)*100
                    sch[i][191]=phy
                    sch[i][192]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][193]=maths
                    sch[i][194]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][243]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/80)*100
                        sch[i][195]=CS
                        sch[i][196]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][197]=IT
                        sch[i][198]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/80)*100
                        sch[i][199]=AI
                        sch[i][200]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][243]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/80)*100
                            sch[i][195]=CS
                            sch[i][196]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][197]=IT
                            sch[i][198]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/80)*100
                            sch[i][199]=AI
                            sch[i][200]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/80)*100
                    sch[i][201]=hist
                    sch[i][202]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/80)*100
                    sch[i][203]=geo
                    sch[i][204]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/80)*100
                    sch[i][205]=civ
                    sch[i][206]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][207]=gk
                    sch[i][208]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][209]=msc
                    sch[i][210]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/80)*100
                    sch[i][230]=bio
                    sch[i][231]=biop
                    total_marks=sch[i][181]+sch[i][183]+sch[i][185]+sch[i][187]+sch[i][189]+sch[i][191]+sch[i][193]+sch[i][195]+sch[i][197]+sch[i][199]+sch[i][201]+sch[i][203]+sch[i][205]+sch[i][207]+sch[i][209]+sch[i][230]
                    sch[i][211]=total_marks
                    total_percent_t2=(total_marks/960)*100
                    sch[i][212]=total_percent_t2
                    
            ch=input("Press any key to compute overall student mark sheet: ")
            if total_percent_ut1>=total_percent_ut2:
                best_utI=(5/100)*total_percent_ut1
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            else:
                best_utI=(5/100)*total_percent_ut2
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            a=(20/100)*total_percent_t1
            sch[i][215]=a
            b=(60/100)*total_percent_t2
            sch[i][216]=b
            tp_ut=best_utI+best_utII
            sch[i][217]=tp_ut
            tp_t=a+b
            sch[i][218]=tp_t
            tp_tp=tp_ut+tp_t+sch[i][19]+sch[i][20]
            sch[i][219]=tp_tp
                
                
        elif sch[i][10]==12:
            if sch[i][3]=='SEVEN' or sch[i][3]=='7' or sch[i][3]=='VII':
                u=input("Enter: ")
                if sch[i][13]=='yes-ut1':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-1(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][21]=eng
                    sch[i][22]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][232]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][23]=hin
                        sch[i][24]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][25]=beng
                        sch[i][26]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][27]=sans
                        sch[i][28]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][232]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][23]=hin
                            sch[i][24]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][25]=beng
                            sch[i][26]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][27]=sans
                            sch[i][28]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][29]=chem
                    sch[i][30]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][31]=phy
                    sch[i][32]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][33]=maths
                    sch[i][34]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][233]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][35]=CS
                        sch[i][36]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][37]=IT
                        sch[i][38]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][39]=AI
                        sch[i][40]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][233]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][35]=CS
                            sch[i][36]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][37]=IT
                            sch[i][38]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][39]=AI
                            sch[i][40]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][41]=hist
                    sch[i][42]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][43]=geo
                    sch[i][44]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][45]=civ
                    sch[i][46]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][47]=gk
                    sch[i][48]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][49]=msc
                    sch[i][50]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][220]=bio
                    sch[i][221]=biop
                    total_marks=sch[i][21]+sch[i][23]+sch[i][25]+sch[i][27]+sch[i][29]+sch[i][31]+sch[i][33]+sch[i][35]+sch[i][37]+sch[i][39]+sch[i][41]+sch[i][43]+sch[i][45]+sch[i][47]+sch[i][49]+sch[i][220]
                    sch[i][51]=total_marks
                    total_percent_ut1=(total_marks/480)*100
                    sch[i][52]=total_percent_ut1
                
                v=input("Enter: ")
                if sch[i][14]=='yes-ut2':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-2(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][53]=eng
                    sch[i][54]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][234]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][55]=hin
                        sch[i][56]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][57]=beng
                        sch[i][58]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][59]=sans
                        sch[i][60]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][234]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][55]=hin
                            sch[i][56]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][57]=beng
                            sch[i][58]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][59]=sans
                            sch[i][60]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][61]=chem
                    sch[i][62]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][63]=phy
                    sch[i][64]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][65]=maths
                    sch[i][66]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][235]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][67]=CS
                        sch[i][68]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][69]=IT
                        sch[i][70]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][71]=AI
                        sch[i][72]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][235]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][67]=CS
                            sch[i][68]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][69]=IT
                            sch[i][70]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][71]=AI
                            sch[i][72]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][73]=hist
                    sch[i][74]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][75]=geo
                    sch[i][76]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][77]=civ
                    sch[i][78]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][79]=gk
                    sch[i][80]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][81]=msc
                    sch[i][82]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][222]=bio
                    sch[i][223]=biop
                    total_marks=sch[i][53]+sch[i][55]+sch[i][57]+sch[i][59]+sch[i][61]+sch[i][63]+sch[i][65]+sch[i][67]+sch[i][69]+sch[i][71]+sch[i][73]+sch[i][75]+sch[i][77]+sch[i][79]+sch[i][81]+sch[i][222]
                    sch[i][83]=total_marks
                    total_percent_ut2=(total_marks/480)*100
                    sch[i][84]=total_percent_ut2
                           
                w=input("Enter: ")
                if sch[i][15]=='yes-t1':
                    print("MARKS SCORED BY THE STUDENT IN TERM-1(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][85]=eng
                    sch[i][86]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][236]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][87]=hin
                        sch[i][88]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][89]=beng
                        sch[i][90]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][91]=sans
                        sch[i][92]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][236]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][87]=hin
                            sch[i][88]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][89]=beng
                            sch[i][90]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][91]=sans
                            sch[i][92]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/80)*100
                    sch[i][93]=chem
                    sch[i][94]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/80)*100
                    sch[i][95]=phy
                    sch[i][96]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][97]=maths
                    sch[i][98]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][237]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/80)*100
                        sch[i][99]=CS
                        sch[i][100]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][101]=IT
                        sch[i][102]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/80)*100
                        sch[i][103]=AI
                        sch[i][104]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][237]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/80)*100
                            sch[i][99]=CS
                            sch[i][100]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][101]=IT
                            sch[i][102]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/80)*100
                            sch[i][103]=AI
                            sch[i][104]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/80)*100
                    sch[i][105]=hist
                    sch[i][106]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/80)*100
                    sch[i][107]=geo
                    sch[i][108]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/80)*100
                    sch[i][109]=civ
                    sch[i][110]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][111]=gk
                    sch[i][112]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][113]=msc
                    sch[i][114]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/80)*100
                    sch[i][224]=bio
                    sch[i][225]=biop
                    total_marks=sch[i][85]+sch[i][87]+sch[i][89]+sch[i][91]+sch[i][93]+sch[i][95]+sch[i][97]+sch[i][99]+sch[i][101]+sch[i][103]+sch[i][105]+sch[i][107]+sch[i][109]+sch[i][111]+sch[i][113]+sch[i][224]
                    sch[i][115]=total_marks
                    total_percent_t1=(total_marks/960)*100
                    sch[i][116]=total_percent_t1
                            
                x=input("Enter: ")
                if sch[i][16]=='yes-ut3':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-3(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][117]=eng
                    sch[i][118]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][238]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][119]=hin
                        sch[i][120]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][121]=beng
                        sch[i][122]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][123]=sans
                        sch[i][124]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][238]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][119]=hin
                            sch[i][120]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][121]=beng
                            sch[i][122]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][123]=sans
                            sch[i][124]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][125]=chem
                    sch[i][126]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][127]=phy
                    sch[i][128]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][129]=maths
                    sch[i][130]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][239]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][131]=CS
                        sch[i][132]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][133]=IT
                        sch[i][134]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][135]=AI
                        sch[i][136]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][239]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][131]=CS
                            sch[i][132]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][133]=IT
                            sch[i][134]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][135]=AI
                            sch[i][136]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][137]=hist
                    sch[i][138]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][139]=geo
                    sch[i][140]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][141]=civ
                    sch[i][142]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][143]=gk
                    sch[i][144]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][145]=msc
                    sch[i][146]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][226]=bio
                    sch[i][227]=biop
                    total_marks=sch[i][117]+sch[i][119]+sch[i][121]+sch[i][123]+sch[i][125]+sch[i][127]+sch[i][129]+sch[i][131]+sch[i][133]+sch[i][135]+sch[i][137]+sch[i][139]+sch[i][141]+sch[i][143]+sch[i][145]+sch[i][226]
                    sch[i][147]=total_marks
                    total_percent_ut3=(total_marks/480)*100
                    sch[i][148]=total_percent_ut3
                            
                y=input("Enter: ")
                if sch[i][17]=='yes-ut4':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-4(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][149]=eng
                    sch[i][150]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][240]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][151]=hin
                        sch[i][152]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][153]=beng
                        sch[i][154]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][155]=sans
                        sch[i][156]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][240]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][151]=hin
                            sch[i][152]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][153]=beng
                            sch[i][154]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][155]=sans
                            sch[i][156]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][157]=chem
                    sch[i][158]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][159]=phy
                    sch[i][160]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][161]=maths
                    sch[i][162]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][241]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][163]=CS
                        sch[i][164]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][165]=IT
                        sch[i][166]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][167]=AI
                        sch[i][168]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][241]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][163]=CS
                            sch[i][164]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][165]=IT
                            sch[i][166]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][167]=AI
                            sch[i][168]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][169]=hist
                    sch[i][170]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][171]=geo
                    sch[i][172]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][173]=civ
                    sch[i][174]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][175]=gk
                    sch[i][176]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][177]=msc
                    sch[i][178]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][228]=bio
                    sch[i][229]=biop
                    total_marks=sch[i][149]+sch[i][151]+sch[i][153]+sch[i][155]+sch[i][157]+sch[i][159]+sch[i][161]+sch[i][163]+sch[i][165]+sch[i][167]+sch[i][169]+sch[i][171]+sch[i][173]+sch[i][175]+sch[i][177]+sch[i][228]
                    sch[i][179]=total_marks
                    total_percent_ut4=(total_marks/480)*100
                    sch[i][180]=total_percent_ut4
                           
                z=input("Enter: ")
                if sch[i][18]=='yes-t2':
                    print("MARKS SCORED BY THE STUDENT IN TERM-2(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][181]=eng
                    sch[i][182]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][242]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][183]=hin
                        sch[i][184]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][185]=beng
                        sch[i][186]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][187]=sans
                        sch[i][188]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][242]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][183]=hin
                            sch[i][184]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][185]=beng
                            sch[i][186]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/80)*100
                            sch[i][187]=sans
                            sch[i][188]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/80)*100
                    sch[i][189]=chem
                    sch[i][190]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/80)*100
                    sch[i][191]=phy
                    sch[i][192]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][193]=maths
                    sch[i][194]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][243]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/80)*100
                        sch[i][195]=CS
                        sch[i][196]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][197]=IT
                        sch[i][198]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/80)*100
                        sch[i][199]=AI
                        sch[i][200]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=eval(input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ")).upper()
                        sch[i][243]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/80)*100
                            sch[i][195]=CS
                            sch[i][196]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][197]=IT
                            sch[i][198]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/80)*100
                            sch[i][199]=AI
                            sch[i][200]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/80)*100
                    sch[i][201]=hist
                    sch[i][202]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/80)*100
                    sch[i][203]=geo
                    sch[i][204]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/80)*100
                    sch[i][205]=civ
                    sch[i][206]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][207]=gk
                    sch[i][208]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][209]=msc
                    sch[i][210]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/80)*100
                    sch[i][230]=bio
                    sch[i][231]=biop
                    total_marks=sch[i][181]+sch[i][183]+sch[i][185]+sch[i][187]+sch[i][189]+sch[i][191]+sch[i][193]+sch[i][195]+sch[i][197]+sch[i][199]+sch[i][201]+sch[i][203]+sch[i][205]+sch[i][207]+sch[i][209]+sch[i][230]
                    sch[i][211]=total_marks
                    total_percent_t2=(total_marks/960)*100
                    sch[i][212]=total_percent_t2
                    
            ch=input("Press any key to compute overall student mark sheet: ")
            if total_percent_ut1>=total_percent_ut2:
                best_utI=(5/100)*total_percent_ut1
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            else:
                best_utI=(5/100)*total_percent_ut2
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            a=(20/100)*total_percent_t1
            sch[i][215]=a
            b=(60/100)*total_percent_t2
            sch[i][216]=b
            tp_ut=best_utI+best_utII
            sch[i][217]=tp_ut
            tp_t=a+b
            sch[i][218]=tp_t
            tp_tp=tp_ut+tp_t+sch[i][19]+sch[i][20]
            sch[i][219]=tp_tp
                
        elif sch[i][10]==13:
            if sch[i][3]=='EIGHT' or sch[i][3]=='8' or sch[i][3]=='VIII':
                u=input("Enter: ")
                if sch[i][13]=='yes-ut1':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-1(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][21]=eng
                    sch[i][22]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][232]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][23]=hin
                        sch[i][24]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][25]=beng
                        sch[i][26]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][27]=sans
                        sch[i][28]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][232]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][23]=hin
                            sch[i][24]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][25]=beng
                            sch[i][26]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][27]=sans
                            sch[i][28]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][29]=chem
                    sch[i][30]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][31]=phy
                    sch[i][32]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][33]=maths
                    sch[i][34]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][233]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][35]=CS
                        sch[i][36]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][37]=IT
                        sch[i][38]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][39]=AI
                        sch[i][40]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][233]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][35]=CS
                            sch[i][36]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][37]=IT
                            sch[i][38]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][39]=AI
                            sch[i][40]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][41]=hist
                    sch[i][42]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][43]=geo
                    sch[i][44]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][45]=civ
                    sch[i][46]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][47]=gk
                    sch[i][48]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][49]=msc
                    sch[i][50]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][220]=bio
                    sch[i][221]=biop
                    total_marks=sch[i][21]+sch[i][23]+sch[i][25]+sch[i][27]+sch[i][29]+sch[i][31]+sch[i][33]+sch[i][35]+sch[i][37]+sch[i][39]+sch[i][41]+sch[i][43]+sch[i][45]+sch[i][47]+sch[i][49]+sch[i][220]
                    sch[i][51]=total_marks
                    total_percent_ut1=(total_marks/480)*100
                    sch[i][52]=total_percent_ut1
                
                v=input("Enter: ")
                if sch[i][14]=='yes-ut2':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-2(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][53]=eng
                    sch[i][54]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][234]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][55]=hin
                        sch[i][56]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][57]=beng
                        sch[i][58]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][59]=sans
                        sch[i][60]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][234]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][55]=hin
                            sch[i][56]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][57]=beng
                            sch[i][58]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][59]=sans
                            sch[i][60]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][61]=chem
                    sch[i][62]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][63]=phy
                    sch[i][64]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][65]=maths
                    sch[i][66]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][235]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][67]=CS
                        sch[i][68]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][69]=IT
                        sch[i][70]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][71]=AI
                        sch[i][72]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][235]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][67]=CS
                            sch[i][68]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][69]=IT
                            sch[i][70]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][71]=AI
                            sch[i][72]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][73]=hist
                    sch[i][74]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][75]=geo
                    sch[i][76]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][77]=civ
                    sch[i][78]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][79]=gk
                    sch[i][80]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][81]=msc
                    sch[i][82]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][222]=bio
                    sch[i][223]=biop
                    total_marks=sch[i][53]+sch[i][55]+sch[i][57]+sch[i][59]+sch[i][61]+sch[i][63]+sch[i][65]+sch[i][67]+sch[i][69]+sch[i][71]+sch[i][73]+sch[i][75]+sch[i][77]+sch[i][79]+sch[i][81]+sch[i][222]
                    sch[i][83]=total_marks
                    total_percent_ut2=(total_marks/480)*100
                    sch[i][84]=total_percent_ut2
                           
                w=input("Enter: ")
                if sch[i][15]=='yes-t1':
                    print("MARKS SCORED BY THE STUDENT IN TERM-1(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][85]=eng
                    sch[i][86]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][236]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][87]=hin
                        sch[i][88]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][89]=beng
                        sch[i][90]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][91]=sans
                        sch[i][92]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][236]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][87]=hin
                            sch[i][88]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][89]=beng
                            sch[i][90]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][91]=sans
                            sch[i][92]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/80)*100
                    sch[i][93]=chem
                    sch[i][94]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/80)*100
                    sch[i][95]=phy
                    sch[i][96]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][97]=maths
                    sch[i][98]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][237]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/80)*100
                        sch[i][99]=CS
                        sch[i][100]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][101]=IT
                        sch[i][102]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/80)*100
                        sch[i][103]=AI
                        sch[i][104]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][237]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/80)*100
                            sch[i][99]=CS
                            sch[i][100]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][101]=IT
                            sch[i][102]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/80)*100
                            sch[i][103]=AI
                            sch[i][104]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/80)*100
                    sch[i][105]=hist
                    sch[i][106]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/80)*100
                    sch[i][107]=geo
                    sch[i][108]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/80)*100
                    sch[i][109]=civ
                    sch[i][110]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][111]=gk
                    sch[i][112]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][113]=msc
                    sch[i][114]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/80)*100
                    sch[i][224]=bio
                    sch[i][225]=biop
                    total_marks=sch[i][85]+sch[i][87]+sch[i][89]+sch[i][91]+sch[i][93]+sch[i][95]+sch[i][97]+sch[i][99]+sch[i][101]+sch[i][103]+sch[i][105]+sch[i][107]+sch[i][109]+sch[i][111]+sch[i][113]+sch[i][224]
                    sch[i][115]=total_marks
                    total_percent_t1=(total_marks/960)*100
                    sch[i][116]=total_percent_t1
                            
                x=input("Enter: ")
                if sch[i][16]=='yes-ut3':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-3(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][117]=eng
                    sch[i][118]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][238]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][119]=hin
                        sch[i][120]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][121]=beng
                        sch[i][122]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][123]=sans
                        sch[i][124]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][238]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][119]=hin
                            sch[i][120]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][121]=beng
                            sch[i][122]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][123]=sans
                            sch[i][124]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][125]=chem
                    sch[i][126]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][127]=phy
                    sch[i][128]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][129]=maths
                    sch[i][130]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][239]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][131]=CS
                        sch[i][132]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][133]=IT
                        sch[i][134]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][135]=AI
                        sch[i][136]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][239]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][131]=CS
                            sch[i][132]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][133]=IT
                            sch[i][134]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][135]=AI
                            sch[i][136]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][137]=hist
                    sch[i][138]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][139]=geo
                    sch[i][140]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][141]=civ
                    sch[i][142]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][143]=gk
                    sch[i][144]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][145]=msc
                    sch[i][146]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][226]=bio
                    sch[i][227]=biop
                    total_marks=sch[i][117]+sch[i][119]+sch[i][121]+sch[i][123]+sch[i][125]+sch[i][127]+sch[i][129]+sch[i][131]+sch[i][133]+sch[i][135]+sch[i][137]+sch[i][139]+sch[i][141]+sch[i][143]+sch[i][145]+sch[i][226]
                    sch[i][147]=total_marks
                    total_percent_ut3=(total_marks/480)*100
                    sch[i][148]=total_percent_ut3
                            
                y=input("Enter: ")
                if sch[i][17]=='yes-ut4':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-4(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][149]=eng
                    sch[i][150]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][240]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][151]=hin
                        sch[i][152]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][153]=beng
                        sch[i][154]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][155]=sans
                        sch[i][156]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][240]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][151]=hin
                            sch[i][152]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][153]=beng
                            sch[i][154]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][155]=sans
                            sch[i][156]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][157]=chem
                    sch[i][158]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][159]=phy
                    sch[i][160]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][161]=maths
                    sch[i][162]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][241]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][163]=CS
                        sch[i][164]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][165]=IT
                        sch[i][166]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][167]=AI
                        sch[i][168]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][241]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][163]=CS
                            sch[i][164]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][165]=IT
                            sch[i][166]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][167]=AI
                            sch[i][168]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][169]=hist
                    sch[i][170]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][171]=geo
                    sch[i][172]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][173]=civ
                    sch[i][174]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][175]=gk
                    sch[i][176]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][177]=msc
                    sch[i][178]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][228]=bio
                    sch[i][229]=biop
                    total_marks=sch[i][149]+sch[i][151]+sch[i][153]+sch[i][155]+sch[i][157]+sch[i][159]+sch[i][161]+sch[i][163]+sch[i][165]+sch[i][167]+sch[i][169]+sch[i][171]+sch[i][173]+sch[i][175]+sch[i][177]+sch[i][228]
                    sch[i][179]=total_marks
                    total_percent_ut4=(total_marks/480)*100
                    sch[i][180]=total_percent_ut4
                           
                z=input("Enter: ")
                if sch[i][18]=='yes-t2':
                    print("MARKS SCORED BY THE STUDENT IN TERM-2(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][181]=eng
                    sch[i][182]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][242]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][183]=hin
                        sch[i][184]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][185]=beng
                        sch[i][186]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][187]=sans
                        sch[i][188]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][242]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][183]=hin
                            sch[i][184]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][185]=beng
                            sch[i][186]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/80)*100
                            sch[i][187]=sans
                            sch[i][188]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/80)*100
                    sch[i][189]=chem
                    sch[i][190]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/80)*100
                    sch[i][191]=phy
                    sch[i][192]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][193]=maths
                    sch[i][194]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][243]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/80)*100
                        sch[i][195]=CS
                        sch[i][196]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][197]=IT
                        sch[i][198]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/80)*100
                        sch[i][199]=AI
                        sch[i][200]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][243]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/80)*100
                            sch[i][195]=CS
                            sch[i][196]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][197]=IT
                            sch[i][198]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/80)*100
                            sch[i][199]=AI
                            sch[i][200]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/80)*100
                    sch[i][201]=hist
                    sch[i][202]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/80)*100
                    sch[i][203]=geo
                    sch[i][204]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/80)*100
                    sch[i][205]=civ
                    sch[i][206]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][207]=gk
                    sch[i][208]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][209]=msc
                    sch[i][210]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/80)*100
                    sch[i][230]=bio
                    sch[i][231]=biop
                    total_marks=sch[i][181]+sch[i][183]+sch[i][185]+sch[i][187]+sch[i][189]+sch[i][191]+sch[i][193]+sch[i][195]+sch[i][197]+sch[i][199]+sch[i][201]+sch[i][203]+sch[i][205]+sch[i][207]+sch[i][209]+sch[i][230]
                    sch[i][211]=total_marks
                    total_percent_t2=(total_marks/960)*100
                    sch[i][212]=total_percent_t2
                    
            ch=input("Press any key to compute overall student mark sheet: ")
            if total_percent_ut1>=total_percent_ut2:
                best_utI=(5/100)*total_percent_ut1
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            else:
                best_utI=(5/100)*total_percent_ut2
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            a=(20/100)*total_percent_t1
            sch[i][215]=a
            b=(60/100)*total_percent_t2
            sch[i][216]=b
            tp_ut=best_utI+best_utII
            sch[i][217]=tp_ut
            tp_t=a+b
            sch[i][218]=tp_t
            tp_tp=tp_ut+tp_t+sch[i][19]+sch[i][20]
            sch[i][219]=tp_tp
               
                
        elif sch[i][10]==14:
            if sch[i][3]=='NINE' or sch[i][3]=='9' or sch[i][3]=='IX':
                u=input("Enter: ")
                if sch[i][13]=='yes-ut1':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-1(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][21]=eng
                    sch[i][22]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][232]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][23]=hin
                        sch[i][24]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][25]=beng
                        sch[i][26]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][27]=sans
                        sch[i][28]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][232]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][23]=hin
                            sch[i][24]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][25]=beng
                            sch[i][26]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][27]=sans
                            sch[i][28]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][29]=chem
                    sch[i][30]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][31]=phy
                    sch[i][32]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][33]=maths
                    sch[i][34]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][233]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][35]=CS
                        sch[i][36]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][37]=IT
                        sch[i][38]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][39]=AI
                        sch[i][40]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][233]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][35]=CS
                            sch[i][36]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][37]=IT
                            sch[i][38]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][39]=AI
                            sch[i][40]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][41]=hist
                    sch[i][42]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][43]=geo
                    sch[i][44]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][45]=civ
                    sch[i][46]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][47]=gk
                    sch[i][48]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][49]=msc
                    sch[i][50]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][220]=bio
                    sch[i][221]=biop
                    total_marks=sch[i][21]+sch[i][23]+sch[i][25]+sch[i][27]+sch[i][29]+sch[i][31]+sch[i][33]+sch[i][35]+sch[i][37]+sch[i][39]+sch[i][41]+sch[i][43]+sch[i][45]+sch[i][47]+sch[i][49]+sch[i][220]
                    sch[i][51]=total_marks
                    total_percent_ut1=(total_marks/480)*100
                    sch[i][52]=total_percent_ut1
                
                v=input("Enter: ")
                if sch[i][14]=='yes-ut2':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-2(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][53]=eng
                    sch[i][54]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][234]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][55]=hin
                        sch[i][56]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][57]=beng
                        sch[i][58]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][59]=sans
                        sch[i][60]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][234]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][55]=hin
                            sch[i][56]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][57]=beng
                            sch[i][58]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][59]=sans
                            sch[i][60]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][61]=chem
                    sch[i][62]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][63]=phy
                    sch[i][64]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][65]=maths
                    sch[i][66]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][235]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][67]=CS
                        sch[i][68]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][69]=IT
                        sch[i][70]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][71]=AI
                        sch[i][72]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][235]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][67]=CS
                            sch[i][68]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][69]=IT
                            sch[i][70]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][71]=AI
                            sch[i][72]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][73]=hist
                    sch[i][74]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][75]=geo
                    sch[i][76]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][77]=civ
                    sch[i][78]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][79]=gk
                    sch[i][80]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][81]=msc
                    sch[i][82]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][222]=bio
                    sch[i][223]=biop
                    total_marks=sch[i][53]+sch[i][55]+sch[i][57]+sch[i][59]+sch[i][61]+sch[i][63]+sch[i][65]+sch[i][67]+sch[i][69]+sch[i][71]+sch[i][73]+sch[i][75]+sch[i][77]+sch[i][79]+sch[i][81]+sch[i][222]
                    sch[i][83]=total_marks
                    total_percent_ut2=(total_marks/480)*100
                    sch[i][84]=total_percent_ut2
                           
                w=input("Enter: ")
                if sch[i][15]=='yes-t1':
                    print("MARKS SCORED BY THE STUDENT IN TERM-1(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][85]=eng
                    sch[i][86]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][236]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][87]=hin
                        sch[i][88]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][89]=beng
                        sch[i][90]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][91]=sans
                        sch[i][92]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][236]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][87]=hin
                            sch[i][88]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][89]=beng
                            sch[i][90]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][91]=sans
                            sch[i][92]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/80)*100
                    sch[i][93]=chem
                    sch[i][94]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/80)*100
                    sch[i][95]=phy
                    sch[i][96]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][97]=maths
                    sch[i][98]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][237]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/80)*100
                        sch[i][99]=CS
                        sch[i][100]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][101]=IT
                        sch[i][102]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/80)*100
                        sch[i][103]=AI
                        sch[i][104]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][237]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/80)*100
                            sch[i][99]=CS
                            sch[i][100]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][101]=IT
                            sch[i][102]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/80)*100
                            sch[i][103]=AI
                            sch[i][104]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/80)*100
                    sch[i][105]=hist
                    sch[i][106]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/80)*100
                    sch[i][107]=geo
                    sch[i][108]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/80)*100
                    sch[i][109]=civ
                    sch[i][110]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][111]=gk
                    sch[i][112]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][113]=msc
                    sch[i][114]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/80)*100
                    sch[i][224]=bio
                    sch[i][225]=biop
                    total_marks=sch[i][85]+sch[i][87]+sch[i][89]+sch[i][91]+sch[i][93]+sch[i][95]+sch[i][97]+sch[i][99]+sch[i][101]+sch[i][103]+sch[i][105]+sch[i][107]+sch[i][109]+sch[i][111]+sch[i][113]+sch[i][224]
                    sch[i][115]=total_marks
                    total_percent_t1=(total_marks/960)*100
                    sch[i][116]=total_percent_t1
                            
                x=input("Enter: ")
                if sch[i][16]=='yes-ut3':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-3(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][117]=eng
                    sch[i][118]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][238]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][119]=hin
                        sch[i][120]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][121]=beng
                        sch[i][122]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][123]=sans
                        sch[i][124]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][238]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][119]=hin
                            sch[i][120]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][121]=beng
                            sch[i][122]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][123]=sans
                            sch[i][124]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][125]=chem
                    sch[i][126]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][127]=phy
                    sch[i][128]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][129]=maths
                    sch[i][130]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][239]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][131]=CS
                        sch[i][132]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][133]=IT
                        sch[i][134]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][135]=AI
                        sch[i][136]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][239]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][131]=CS
                            sch[i][132]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][133]=IT
                            sch[i][134]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][135]=AI
                            sch[i][136]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][137]=hist
                    sch[i][138]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][139]=geo
                    sch[i][140]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][141]=civ
                    sch[i][142]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][143]=gk
                    sch[i][144]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][145]=msc
                    sch[i][146]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][226]=bio
                    sch[i][227]=biop
                    total_marks=sch[i][117]+sch[i][119]+sch[i][121]+sch[i][123]+sch[i][125]+sch[i][127]+sch[i][129]+sch[i][131]+sch[i][133]+sch[i][135]+sch[i][137]+sch[i][139]+sch[i][141]+sch[i][143]+sch[i][145]+sch[i][226]
                    sch[i][147]=total_marks
                    total_percent_ut3=(total_marks/480)*100
                    sch[i][148]=total_percent_ut3
                            
                y=input("Enter: ")
                if sch[i][17]=='yes-ut4':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-4(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][149]=eng
                    sch[i][150]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][240]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][151]=hin
                        sch[i][152]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][153]=beng
                        sch[i][154]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][155]=sans
                        sch[i][156]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][240]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][151]=hin
                            sch[i][152]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][153]=beng
                            sch[i][154]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][155]=sans
                            sch[i][156]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][157]=chem
                    sch[i][158]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][159]=phy
                    sch[i][160]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][161]=maths
                    sch[i][162]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][241]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][163]=CS
                        sch[i][164]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][165]=IT
                        sch[i][166]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][167]=AI
                        sch[i][168]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][241]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][163]=CS
                            sch[i][164]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][165]=IT
                            sch[i][166]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][167]=AI
                            sch[i][168]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][169]=hist
                    sch[i][170]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][171]=geo
                    sch[i][172]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][173]=civ
                    sch[i][174]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][175]=gk
                    sch[i][176]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][177]=msc
                    sch[i][178]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][228]=bio
                    sch[i][229]=biop
                    total_marks=sch[i][149]+sch[i][151]+sch[i][153]+sch[i][155]+sch[i][157]+sch[i][159]+sch[i][161]+sch[i][163]+sch[i][165]+sch[i][167]+sch[i][169]+sch[i][171]+sch[i][173]+sch[i][175]+sch[i][177]+sch[i][228]
                    sch[i][179]=total_marks
                    total_percent_ut4=(total_marks/480)*100
                    sch[i][180]=total_percent_ut4
                           
                z=input("Enter: ")
                if sch[i][18]=='yes-t2':
                    print("MARKS SCORED BY THE STUDENT IN TERM-2(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][181]=eng
                    sch[i][182]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][242]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][183]=hin
                        sch[i][184]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][185]=beng
                        sch[i][186]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][187]=sans
                        sch[i][188]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][242]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][183]=hin
                            sch[i][184]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][185]=beng
                            sch[i][186]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/80)*100
                            sch[i][187]=sans
                            sch[i][188]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/80)*100
                    sch[i][189]=chem
                    sch[i][190]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/80)*100
                    sch[i][191]=phy
                    sch[i][192]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][193]=maths
                    sch[i][194]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][243]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/80)*100
                        sch[i][195]=CS
                        sch[i][196]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][197]=IT
                        sch[i][198]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/80)*100
                        sch[i][199]=AI
                        sch[i][200]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][243]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/80)*100
                            sch[i][195]=CS
                            sch[i][196]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][197]=IT
                            sch[i][198]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/80)*100
                            sch[i][199]=AI
                            sch[i][200]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/80)*100
                    sch[i][201]=hist
                    sch[i][202]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/80)*100
                    sch[i][203]=geo
                    sch[i][204]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/80)*100
                    sch[i][205]=civ
                    sch[i][206]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][207]=gk
                    sch[i][208]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][209]=msc
                    sch[i][210]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/80)*100
                    sch[i][230]=bio
                    sch[i][231]=biop
                    total_marks=sch[i][181]+sch[i][183]+sch[i][185]+sch[i][187]+sch[i][189]+sch[i][191]+sch[i][193]+sch[i][195]+sch[i][197]+sch[i][199]+sch[i][201]+sch[i][203]+sch[i][205]+sch[i][207]+sch[i][209]+sch[i][230]
                    sch[i][211]=total_marks
                    total_percent_t2=(total_marks/960)*100
                    sch[i][212]=total_percent_t2
                    
            ch=input("Press any key to compute overall student mark sheet: ")
            if total_percent_ut1>=total_percent_ut2:
                best_utI=(5/100)*total_percent_ut1
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            else:
                best_utI=(5/100)*total_percent_ut2
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            a=(20/100)*total_percent_t1
            sch[i][215]=a
            b=(60/100)*total_percent_t2
            sch[i][216]=b
            tp_ut=best_utI+best_utII
            sch[i][217]=tp_ut
            tp_t=a+b
            sch[i][218]=tp_t
            tp_tp=tp_ut+tp_t+sch[i][19]+sch[i][20]
            sch[i][219]=tp_tp
                
                
        elif sch[i][10]==15:
            if sch[i][3]=='TEN' or sch[i][3]=='10' or sch[i][3]=='X':
                u=input("Enter: ")
                if sch[i][13]=='yes-ut1':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-1(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][21]=eng
                    sch[i][22]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][232]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][23]=hin
                        sch[i][24]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][25]=beng
                        sch[i][26]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][27]=sans
                        sch[i][28]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][232]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][23]=hin
                            sch[i][24]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][25]=beng
                            sch[i][26]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][27]=sans
                            sch[i][28]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][29]=chem
                    sch[i][30]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][31]=phy
                    sch[i][32]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][33]=maths
                    sch[i][34]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][233]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][35]=CS
                        sch[i][36]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][37]=IT
                        sch[i][38]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][39]=AI
                        sch[i][40]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][233]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][35]=CS
                            sch[i][36]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][37]=IT
                            sch[i][38]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][39]=AI
                            sch[i][40]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][41]=hist
                    sch[i][42]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][43]=geo
                    sch[i][44]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][45]=civ
                    sch[i][46]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][47]=gk
                    sch[i][48]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][49]=msc
                    sch[i][50]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][220]=bio
                    sch[i][221]=biop
                    total_marks=sch[i][21]+sch[i][23]+sch[i][25]+sch[i][27]+sch[i][29]+sch[i][31]+sch[i][33]+sch[i][35]+sch[i][37]+sch[i][39]+sch[i][41]+sch[i][43]+sch[i][45]+sch[i][47]+sch[i][49]+sch[i][220]
                    sch[i][51]=total_marks
                    total_percent_ut1=(total_marks/480)*100
                    sch[i][52]=total_percent_ut1
                
                v=input("Enter: ")
                if sch[i][14]=='yes-ut2':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-2(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][53]=eng
                    sch[i][54]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][234]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][55]=hin
                        sch[i][56]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][57]=beng
                        sch[i][58]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][59]=sans
                        sch[i][60]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][234]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][55]=hin
                            sch[i][56]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][57]=beng
                            sch[i][58]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][59]=sans
                            sch[i][60]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][61]=chem
                    sch[i][62]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][63]=phy
                    sch[i][64]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][65]=maths
                    sch[i][66]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][235]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][67]=CS
                        sch[i][68]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][69]=IT
                        sch[i][70]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][71]=AI
                        sch[i][72]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][235]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][67]=CS
                            sch[i][68]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][69]=IT
                            sch[i][70]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][71]=AI
                            sch[i][72]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][73]=hist
                    sch[i][74]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][75]=geo
                    sch[i][76]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][77]=civ
                    sch[i][78]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][79]=gk
                    sch[i][80]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][81]=msc
                    sch[i][82]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][222]=bio
                    sch[i][223]=biop
                    total_marks=sch[i][53]+sch[i][55]+sch[i][57]+sch[i][59]+sch[i][61]+sch[i][63]+sch[i][65]+sch[i][67]+sch[i][69]+sch[i][71]+sch[i][73]+sch[i][75]+sch[i][77]+sch[i][79]+sch[i][81]+sch[i][222]
                    sch[i][83]=total_marks
                    total_percent_ut2=(total_marks/480)*100
                    sch[i][84]=total_percent_ut2
                           
                w=input("Enter: ")
                if sch[i][15]=='yes-t1':
                    print("MARKS SCORED BY THE STUDENT IN TERM-1(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][85]=eng
                    sch[i][86]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][236]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][87]=hin
                        sch[i][88]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][89]=beng
                        sch[i][90]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][91]=sans
                        sch[i][92]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][236]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][87]=hin
                            sch[i][88]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][89]=beng
                            sch[i][90]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][91]=sans
                            sch[i][92]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/80)*100
                    sch[i][93]=chem
                    sch[i][94]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/80)*100
                    sch[i][95]=phy
                    sch[i][96]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][97]=maths
                    sch[i][98]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][237]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/80)*100
                        sch[i][99]=CS
                        sch[i][100]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][101]=IT
                        sch[i][102]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/80)*100
                        sch[i][103]=AI
                        sch[i][104]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][237]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/80)*100
                            sch[i][99]=CS
                            sch[i][100]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][101]=IT
                            sch[i][102]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/80)*100
                            sch[i][103]=AI
                            sch[i][104]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/80)*100
                    sch[i][105]=hist
                    sch[i][106]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/80)*100
                    sch[i][107]=geo
                    sch[i][108]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/80)*100
                    sch[i][109]=civ
                    sch[i][110]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][111]=gk
                    sch[i][112]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][113]=msc
                    sch[i][114]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/80)*100
                    sch[i][224]=bio
                    sch[i][225]=biop
                    total_marks=sch[i][85]+sch[i][87]+sch[i][89]+sch[i][91]+sch[i][93]+sch[i][95]+sch[i][97]+sch[i][99]+sch[i][101]+sch[i][103]+sch[i][105]+sch[i][107]+sch[i][109]+sch[i][111]+sch[i][113]+sch[i][224]
                    sch[i][115]=total_marks
                    total_percent_t1=(total_marks/960)*100
                    sch[i][116]=total_percent_t1
                            
                x=input("Enter: ")
                if sch[i][16]=='yes-ut3':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-3(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][117]=eng
                    sch[i][118]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][238]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][119]=hin
                        sch[i][120]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][121]=beng
                        sch[i][122]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][123]=sans
                        sch[i][124]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][238]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][119]=hin
                            sch[i][120]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][121]=beng
                            sch[i][122]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][123]=sans
                            sch[i][124]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][125]=chem
                    sch[i][126]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][127]=phy
                    sch[i][128]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][129]=maths
                    sch[i][130]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][239]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][131]=CS
                        sch[i][132]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][133]=IT
                        sch[i][134]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][135]=AI
                        sch[i][136]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][239]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][131]=CS
                            sch[i][132]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][133]=IT
                            sch[i][134]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][135]=AI
                            sch[i][136]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][137]=hist
                    sch[i][138]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][139]=geo
                    sch[i][140]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][141]=civ
                    sch[i][142]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][143]=gk
                    sch[i][144]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][145]=msc
                    sch[i][146]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][226]=bio
                    sch[i][227]=biop
                    total_marks=sch[i][117]+sch[i][119]+sch[i][121]+sch[i][123]+sch[i][125]+sch[i][127]+sch[i][129]+sch[i][131]+sch[i][133]+sch[i][135]+sch[i][137]+sch[i][139]+sch[i][141]+sch[i][143]+sch[i][145]+sch[i][226]
                    sch[i][147]=total_marks
                    total_percent_ut3=(total_marks/480)*100
                    sch[i][148]=total_percent_ut3
                            
                y=input("Enter: ")
                if sch[i][17]=='yes-ut4':
                    print("MARKS SCORED BY THE STUDENT IN UNIT_TEST-4(F.M=40)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/40)*100
                    sch[i][149]=eng
                    sch[i][150]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][240]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/40)*100
                        sch[i][151]=hin
                        sch[i][152]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/40)*100
                        sch[i][153]=beng
                        sch[i][154]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/40)*100
                        sch[i][155]=sans
                        sch[i][156]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][240]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/40)*100
                            sch[i][151]=hin
                            sch[i][152]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/40)*100
                            sch[i][153]=beng
                            sch[i][154]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/40)*100
                            sch[i][155]=sans
                            sch[i][156]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/40)*100
                    sch[i][157]=chem
                    sch[i][158]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/40)*100
                    sch[i][159]=phy
                    sch[i][160]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/40)*100
                    sch[i][161]=maths
                    sch[i][162]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][241]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/40)*100
                        sch[i][163]=CS
                        sch[i][164]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/40)*100
                        sch[i][165]=IT
                        sch[i][166]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/40)*100
                        sch[i][167]=AI
                        sch[i][168]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][241]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/40)*100
                            sch[i][163]=CS
                            sch[i][164]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/40)*100
                            sch[i][165]=IT
                            sch[i][166]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/40)*100
                            sch[i][167]=AI
                            sch[i][168]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/40)*100
                    sch[i][169]=hist
                    sch[i][170]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/40)*100
                    sch[i][171]=geo
                    sch[i][172]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/40)*100
                    sch[i][173]=civ
                    sch[i][174]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/40)*100
                    sch[i][175]=gk
                    sch[i][176]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/40)*100
                    sch[i][177]=msc
                    sch[i][178]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/40)*100
                    sch[i][228]=bio
                    sch[i][229]=biop
                    total_marks=sch[i][149]+sch[i][151]+sch[i][153]+sch[i][155]+sch[i][157]+sch[i][159]+sch[i][161]+sch[i][163]+sch[i][165]+sch[i][167]+sch[i][169]+sch[i][171]+sch[i][173]+sch[i][175]+sch[i][177]+sch[i][228]
                    sch[i][179]=total_marks
                    total_percent_ut4=(total_marks/480)*100
                    sch[i][180]=total_percent_ut4
                           
                z=input("Enter: ")
                if sch[i][18]=='yes-t2':
                    print("MARKS SCORED BY THE STUDENT IN TERM-2(F.M=80)")
                    print("Admission number of",sch[i][0],"is: ",i)
                    eng=eval(input("Enter the marks scored in ENGLISH: "))
                    ep=(eng/80)*100
                    sch[i][181]=eng
                    sch[i][182]=ep
                    sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                    sch[i][242]=sec_lang
                    if sec_lang=='H':
                        hin=eval(input("Enter the marks scored in HINDI: "))
                        hp=(hin/80)*100
                        sch[i][183]=hin
                        sch[i][184]=hp
                    elif sec_lang=='B':
                        beng=eval(input("Enter the marks scored in BENGALI: "))
                        bp=(beng/80)*100
                        sch[i][185]=beng
                        sch[i][186]=bp
                    elif sec_lang=='S':
                        sans=eval(input("Enter the marks scored in SANSKRIT: "))
                        sp=(sans/80)*100
                        sch[i][187]=sans
                        sch[i][188]=sp
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        sec_lang=input("Whether he/she has 2nd language as Hindi(H)/Bengali(B)/Sanskrit(S), Enter 'h/b/s': ").upper()
                        sch[i][242]=sec_lang
                        if sec_lang=='H':
                            hin=eval(input("Enter the marks scored in HINDI: "))
                            hp=(hin/80)*100
                            sch[i][183]=hin
                            sch[i][184]=hp
                        elif sec_lang=='B':
                            beng=eval(input("Enter the marks scored in BENGALI: "))
                            bp=(beng/80)*100
                            sch[i][185]=beng
                            sch[i][186]=bp
                        elif sec_lang=='S':
                            sans=eval(input("Enter the marks scored in SANSKRIT: "))
                            sp=(sans/80)*100
                            sch[i][187]=sans
                            sch[i][188]=sp
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    chem=eval(input("Enter the marks scored in CHEMISTRY: "))
                    cp=(chem/80)*100
                    sch[i][189]=chem
                    sch[i][190]=cp
                    phy=eval(input("Enter the marks scored in PHYSICS: "))
                    pp=(phy/80)*100
                    sch[i][191]=phy
                    sch[i][192]=pp
                    maths=eval(input("Enter the marks scored in MATHS: "))
                    mp=(maths/80)*100
                    sch[i][193]=maths
                    sch[i][194]=mp
                    cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                    sch[i][243]=cs
                    if cs=='C':
                        CS=eval(input("Enter the marks scored in CS: "))
                        csp=(CS/80)*100
                        sch[i][195]=CS
                        sch[i][196]=csp
                    elif cs=='I':
                        IT=eval(input("Enter the marks scored in IT: "))
                        itp=(IT/80)*100
                        sch[i][197]=IT
                        sch[i][198]=itp
                    elif cs=='A':
                        AI=eval(input("Enter the marks scored in AI: "))
                        aip=(AI/80)*100
                        sch[i][199]=AI
                        sch[i][200]=aip
                    else:
                        print("YOU HAVE ENTERED WRONG CHOICE !!! , # Please enter the correct choice #")
                        cs=input("Whether he/she has COMPUTER SCIENCE as CS(c)/IT(i)/AI(a), Enter 'c/i/a': ").upper()
                        sch[i][243]=cs
                        if cs=='C':
                            CS=eval(input("Enter the marks scored in CS: "))
                            csp=(CS/80)*100
                            sch[i][195]=CS
                            sch[i][196]=csp
                        elif cs=='I':
                            IT=eval(input("Enter the marks scored in IT: "))
                            itp=(IT/80)*100
                            sch[i][197]=IT
                            sch[i][198]=itp
                        elif cs=='A':
                            AI=eval(input("Enter the marks scored in AI: "))
                            aip=(AI/80)*100
                            sch[i][199]=AI
                            sch[i][200]=aip
                        else:
                            print("AGAIN YOU HAVE ENTERED WRONG CHOICE !!!")
                    hist=eval(input("Enter the marks scored in HISTORY: "))
                    histp=(hist/80)*100
                    sch[i][201]=hist
                    sch[i][202]=histp
                    geo=eval(input("Enter the marks scored in GEOGRAPHY: "))
                    gp=(geo/80)*100
                    sch[i][203]=geo
                    sch[i][204]=gp
                    civ=eval(input("Enter the marks scored in CIVICS: "))
                    civp=(civ/80)*100
                    sch[i][205]=civ
                    sch[i][206]=civp
                    gk=eval(input("Enter the marks scored in GENERAL KNOWLEDGE: "))
                    gkp=(gk/80)*100
                    sch[i][207]=gk
                    sch[i][208]=gkp
                    msc=eval(input("Enter the marks scored in MORAL SCIENCE: "))
                    mscp=(msc/80)*100
                    sch[i][209]=msc
                    sch[i][210]=mscp
                    bio=eval(input("Enter the marks scored in BIOLOGY: "))
                    biop=(bio/80)*100
                    sch[i][230]=bio
                    sch[i][231]=biop
                    total_marks=sch[i][181]+sch[i][183]+sch[i][185]+sch[i][187]+sch[i][189]+sch[i][191]+sch[i][193]+sch[i][195]+sch[i][197]+sch[i][199]+sch[i][201]+sch[i][203]+sch[i][205]+sch[i][207]+sch[i][209]+sch[i][230]
                    sch[i][211]=total_marks
                    total_percent_t2=(total_marks/960)*100
                    sch[i][212]=total_percent_t2
                    
            ch=input("Press any key to compute overall student mark sheet: ")
            if total_percent_ut1>=total_percent_ut2:
                best_utI=(5/100)*total_percent_ut1
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            else:
                best_utI=(5/100)*total_percent_ut2
                sch[i][213]=best_utI
                if total_percent_ut3>=total_percent_ut4:
                    best_utII=(5/100)*total_percent_ut3
                    sch[i][214]=best_utII
                else:
                    best_utII=(5/100)*total_percent_ut4
                    sch[i][214]=best_utII
            a=(20/100)*total_percent_t1
            sch[i][215]=a
            b=(60/100)*total_percent_t2
            sch[i][216]=b
            tp_ut=best_utI+best_utII
            sch[i][217]=tp_ut
            tp_t=a+b
            sch[i][218]=tp_t
            tp_tp=tp_ut+tp_t+sch[i][19]+sch[i][20]
            sch[i][219]=tp_tp           
                      
        else:
            print("-->",sch[i][0],"---> Incorrect age input, so he/she can't be admitted to the school __/\__")
            
        pickle.dump(sch,f)
        
     if found==False:
        print("*** STUDENT'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct admission number of the student to compute the Student's MARK SHEET __/\__")
     print()
     ans=input("Press 'c/C' to compute more Student's MARK SHEET: ")
     print()
    f.close()
    
    
def APPEND_STU_REC():
    f=open('SMS_STU.dat','rb')
    stu={}
    while True:
        try:
            stu=pickle.load(f)
        except EOFError:
            break  
    f.close()
    
    print(stu)
    
    f=open('SMS_STU_EXAM.dat','ab')
    ans='a'
    while ans.lower()=='a':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& APPEND STUDENT'S DETAILS &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s_admno=int(input("Enter the student's Admission Number: "))
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
                s_sec=input("Enter the student's Section: ").upper()
                s_sex=stu[i][4]
                s_dob=stu[i][5]
                s_phno=stu[i][6]
                s_email=stu[i][7]
                s_add=stu[i][8]
                s_ut1=input("Whether the student attended the UNIT_TEST-1, Enter 'Yes-ut1/No': ").lower()
                s_ut2=input("Whether the student attended the UNIT_TEST-2, Enter 'Yes-ut2/No': ").lower()
                s_t1=input("Whether the student attended the TERM-1 examination, Enter 'Yes-t1/No': ").lower()
                s_ut3=input("Whether the student attended the UNIT_TEST-3, Enter 'Yes-ut3/No': ").lower()
                s_ut4=input("Whether the student attended the UNIT_TEST-4, Enter 'Yes-ut4/No': ").lower()
                s_t2=input("Whether the student attended the TERM-2 examination, Enter 'Yes-t2/No': ").lower()
                cls_perf=eval(input("Enter the student's class perfomance in percentage(out of 5%): "))
                pro_act=eval(input("Enter the student's project and activity percentage(out of 5%): "))
                sch[s_admno]=[s_name,s_fn,s_mn,s_cls,s_sex,s_dob,s_phno,s_email,s_add,2021,0,s_house,s_sec,s_ut1,s_ut2,s_t1,s_ut3,s_ut4,s_t2,cls_perf,pro_act,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                
                pickle.dump(sch,f)
                
        if found==False:
            print("*** STUDENT'S RECORD HAS NOT BEEN APPENDED !!! ***")
            print("--> Please provide the correct admission number of the student to store the student's record  __/\__")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
        print()
        ans=input("Press 'a/A' to append more student's record: ")
        print()
    f.close()
    
    
def SEARCH_STU_REC():
    f=open('SMS_STU_EXAM.dat','rb')
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
            print("--x--x-- Provided admission number of the student is present in the database ...@ Press 7 to display the Student's MARK SHEET --x--x--")
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
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ UPDATE STUDENT'S DETAIL $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
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
                    print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='F':
                    print()
                    f=input("Enter the updated Father's Name of the student: ")
                    sch[j][1]=f
                    print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='M':
                    print()
                    m=input("Enter the updated Mother's Name of the student: ")
                    sch[j][2]=m
                    print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='J':
                    print()
                    j=input("Enter the updated Guardian's Name of the student: ")
                    sch[j][27]=j
                    print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='DOB':
                    print()
                    dob=input("Enter the updated Date Of Birth of the student: ")
                    sch[j][5]=dob
                    print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='G':
                    print()
                    g=input("Enter the updated Gender of the student as either MALE or M, FEMALE or F, THIRD GENDER or TG: ")
                    if g=='MALE' or g=='FEMALE' or g=='THIRD GENDER' or g=='M' or g=='F' or g=='TG' :
                        sch[j][4]=g
                        print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STUDENT'S DETAIL HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid sex of the student has been entered !!! ~~~")
                        print("--> Please provide the valid sex of the student to update the field of the student's sex __/\__")
                        print()
                        g=input("Enter the updated Gender of the student as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
                        if g=='MALE' or g=='FEMALE' or g=='THIRD GENDER' or g=='M' or g=='F' or g=='TG' :
                            sch[j][4]=g
                            print("*** NOW STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STUDENT'S DETAIL HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid sex of the student has been entered !!! ~~~")
                            
                elif ch=='FPN':
                    print()
                    print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
                    fpn=int(input("Enter the updated Mobile/Phone Number of the student's father: +91 "))
                    if len(str(fpn))==10:
                        sch[j][6]=fpn
                        print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STUDENT'S DETAIL HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid mobile/phone number of the student's father has been entered !!! ~~~")
                        print("--> Please provide the valid mobile/phone number of the student's father to update the field of the student's father's mobile/phone number __/\__")
                        print()
                        print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
                        fpn=int(input("Enter the updated Mobile/Phone Number of the student's father: +91 "))
                        if len(str(fpn))==10:
                            sch[j][6]=fpn
                            print("*** NOW STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STUDENT'S DETAIL HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid mobile/phone number of the student's father has been entered !!! ~~~")
                            
                elif ch=='MPN':
                    print()
                    print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
                    mpn=int(input("Enter the updated Mobile/Phone Number of the student's mother: +91 "))
                    if len(str(mpn))==10:
                        sch[j][26]=mpn
                        print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STUDENT'S DETAIL HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid mobile/phone number of the student's mother has been entered !!! ~~~")
                        print("--> Please provide the valid mobile/phone number of the student's mother to update the field of the student's mother's mobile/phone number __/\__")
                        print()
                        print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
                        mpn=int(input("Enter the updated Mobile/Phone Number of the student's mother: +91 "))
                        if len(str(mpn))==10:
                            sch[j][26]=mpn
                            print("*** NOW STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STUDENT'S DETAIL HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid mobile/phone number of the student's mother has been entered !!! ~~~")
                            
                elif ch=='GCN':
                    print()
                    print("// Note:- Contact number must be of 10 digits (without ISD code) //")
                    gcn=int(input("Enter the updated Contact Number of the student's guardian: +91 "))
                    if len(str(gcn))==10:
                        sch[j][28]=gcn
                        print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STUDENT'S DETAIL HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid contact number of the student's guardian has been entered !!! ~~~")
                        print("--> Please provide the valid contact number of the student's guardian to update the field of the student's guardian's contact number __/\__")
                        print()
                        print("// Note:- Contact number must be of 10 digits (without ISD code) //")
                        gcn=int(input("Enter the updated Contact Number of the student's guardian: +91 "))
                        if len(str(gcn))==10:
                            sch[j][28]=gcn
                            print("*** NOW STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STUDENT'S DETAIL HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid contact number of the student's guardian has been entered !!! ~~~")
                    
                elif ch=='E':
                    print()
                    e=input("Enter the updated Email Address of the student's father/mother: ")
                    if '@' and '.com' in s_email:
                        sch[j][7]=e
                        print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STUDENT'S DETAIL HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Student's Father's/Mother's Email Address doesn't contain '@' or '.com' !!! ~~~")
                        print("--> Please provide the proper Email Address of the student's father/mother to update the field of the student's father's/mother's email address __/\__")
                        print()
                        s_email=input("Enter the updated Email Address of the student's father/mother: ")
                        if '@' and '.com' in s_email:
                            sch[j][7]=e
                            print("*** NOW STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STUDENT'S DETAIL HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Student's Father's/Mother's Email Address doesn't contain '@' or '.com' !!! ~~~")
                            
                elif ch=='A':
                    print()
                    a=input("Enter the updated House Address of the student: ")
                    sch[j][8]=a
                    print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='B':
                    print()
                    b=input("Update, whether the student wants to avail for bus service, Enter 'Yes/No': ").upper()
                    sch[j][23]=b
                    print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='D':
                    print()
                    d=float(input("Enter the updated Distance(in Km) between student's House Address and School: "))
                    sch[j][24]=d
                    print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='H':
                    print()
                    h=input("Enter the updated House of the student: ")
                    sch[j][25]=h
                    print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='C':
                    print()
                    c=input("Enter the updated Class of the student: ").upper()
                    if s_cls=='LKG' or s_cls=='UKG' or s_cls=='1' or s_cls=='ONE' or s_cls=='I' or s_cls=='2' or s_cls=='TWO' or s_cls=='II' or s_cls=='3' or s_cls=='THREE' or s_cls=='III' or s_cls=='4' or s_cls=='FOUR' or s_cls=='IV' or s_cls=='5' or s_cls=='FIVE' or s_cls=='V' or s_cls=='6' or s_cls=='SIX' or s_cls=='VI' or s_cls=='7' or s_cls=='SEVEN' or s_cls=='VII' or s_cls=='8' or s_cls=='EIGHT' or s_cls=='VIII' or s_cls=='9' or s_cls=='NINE' or s_cls=='IX' or s_cls=='10' or s_cls=='TEN' or s_cls=='X' or s_cls=='11' or s_cls=='ELEVEN' or s_cls=='XI' or s_cls=='12' or s_cls=='TWELEVE' or s_cls=='XII':
                        sch[j][3]=c
                        print("*** STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STUDENT'S DETAIL HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid class of the student has been entered !!! ~~~")
                        print("--> Please provide the valid class of the student to update the field of the student's class __/\__")
                        print()
                        s_cls=input("Enter the updated Class of the student: ").upper()
                        if s_cls=='LKG' or s_cls=='UKG' or s_cls=='1' or s_cls=='ONE' or s_cls=='I' or s_cls=='2' or s_cls=='TWO' or s_cls=='II' or s_cls=='3' or s_cls=='THREE' or s_cls=='III' or s_cls=='4' or s_cls=='FOUR' or s_cls=='IV' or s_cls=='5' or s_cls=='FIVE' or s_cls=='V' or s_cls=='6' or s_cls=='SIX' or s_cls=='VI' or s_cls=='7' or s_cls=='SEVEN' or s_cls=='VII' or s_cls=='8' or s_cls=='EIGHT' or s_cls=='VIII' or s_cls=='9' or s_cls=='NINE' or s_cls=='IX' or s_cls=='10' or s_cls=='TEN' or s_cls=='X' or s_cls=='11' or s_cls=='ELEVEN' or s_cls=='XI' or s_cls=='12' or s_cls=='TWELEVE' or s_cls=='XII':
                            sch[j][3]=c
                            print("*** NOW STUDENT'S DETAIL HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STUDENT'S DETAIL HAS NOT BEEN UPDATED !!! ***")
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
    f=open("SMS_STU_EXAM.dat","rb+")
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
    stu={}
    while True:
        try:
            stu=pickle.load(f)
        except EOFError:
            break
    f.close()
    
    f=open('SMS_STU_EXAM.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='d'
    while ans.lower()=='d':
     ADMNO=int(input("Enter the admission number of the student to display the Student's MARK SHEET: "))
     print()
     found=False
     for i in sch:
        if i==ADMNO:
            print("--------------------------------------------------------------------------------------")
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% STUDENT'S MARK SHEET %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print("--------------------------------------------------------------------------------------")
            print("Student's Admission Number: ",i)
            print("Student's Full Name: ",stu[i][0])
            print("Student's Father's Name: ",stu[i][1])
            print("Student's Mother's Name: ",stu[i][2])
            print("Student's Guardian's Name: ",stu[i][27])
            print("Student's Class: ",stu[i][3])
            print("Student's House: ",stu[i][25])
            print("Student's Sex: ",stu[i][4])
            print("Student's DOB: ",stu[i][5])
            print("Student's Age: ",stu[i][10])
            print("Student's Father's Mobile/Phone Number: +91",stu[i][6])
            print("Student's Mother's Mobile/Phone Number: +91",stu[i][26])
            print("Student's Guardian's Contact Number: +91",stu[i][28])
            print("Student's Father's/Mother's Email Address: ",stu[i][7])
            print("Student's House Address: ",stu[i][8])
            print("Year: ",stu[i][9])
            
            print()
            
            print("*** MARKS SCORED BY THE STUDENT IN UNIT_TEST-1(F.M=40) ***")
            print("Marks scored in ENGLISH: ",sch[i][21])
            print("Percentage of marks scored in ENGLISH: ",sch[i][22],"%")
            if sch[i][232]=='H':
                print("Marks scored in HINDI: ",sch[i][23])
                print("Percentage of marks scored in HINDI: ",sch[i][24],"%")
            elif sch[i][232]=='B':
                print("Marks scored in BENGALI: ",sch[i][25])
                print("Percentage of marks scored in BENGALI: ",sch[i][26],"%")
            elif sch[i][232]=='S':
                print("Marks scored in SANSKRIT: ",sch[i][27])
                print("Percentage of marks scored in SANSKRIT: ",sch[i][28],"%")
            print("Marks scored in CHEMISTRY: ",sch[i][29])
            print("Percentage of marks scored in CHEMISTRY: ",sch[i][30],"%")
            print("Marks scored in PHYSICS: ",sch[i][31])
            print("Percentage of marks scored in PHYSICS: ",sch[i][32],"%")
            print("Marks scored in MATHS: ",sch[i][33])
            print("Percentage of marks scored in MATHS: ",sch[i][34],"%")
            if sch[i][233]=='C':
                print("Marks scored in COMPUTER SCIENCE: ",sch[i][35])
                print("Percentage of marks scored in COMPUTER SCIENCE: ",sch[i][36],"%")
            elif sch[i][233]=='I':
                print("Marks scored in INFORMATION TECHNOLOGY: ",sch[i][37])
                print("Percentage of marks scored in INFORMATION TECHNOLOGY: ",sch[i][38],"%")
            elif sch[i][233]=='A':
                print("Marks scored in ARTIFICIAL INTELLIGENCE: ",sch[i][39])
                print("Percentage of marks scored in ARTIFICAL INTELLIGENCE: ",sch[i][40],"%")
            print("Marks scored in HISTORY: ",sch[i][41])
            print("Percentage of marks scored in HISTORY: ",sch[i][42],"%")
            print("Marks scored in GEOGRAPHY: ",sch[i][43])
            print("Percentage of marks scored in GEOGRAPHY: ",sch[i][44],"%")
            print("Marks scored in CIVICS: ",sch[i][45])
            print("Percentage of marks scored in CIVICS: ",sch[i][46]),"%"
            print("Marks scored in GENERAL KNOWLEDGE: ",sch[i][47])
            print("Percentage of marks scored in GENERAL KNOWLEDGE: ",sch[i][48],"%")
            print("Marks scored in MORAL SCIENCE: ",sch[i][49])
            print("Percentage of marks scored in MORAL SCIENCE: ",sch[i][50],"%")
            print("Marks scored in BIOLOGY: ",sch[i][220])
            print("Percentage of marks scored in BIOLOGY: ",sch[i][221],"%")
            print("Total Marks gained by the student: ",sch[i][51])
            print("Total percentage gained by the student: ",sch[i][52],"%")
            
            print()
            
            print("*** MARKS SCORED BY THE STUDENT IN UNIT_TEST-2(F.M=40) ***")
            print("Marks scored in ENGLISH: ",sch[i][53])
            print("Percentage of marks scored in ENGLISH: ",sch[i][54],"%")
            if sch[i][234]=='H':
                print("Marks scored in HINDI: ",sch[i][55])
                print("Percentage of marks scored in HINDI: ",sch[i][56],"%")
            elif sch[i][234]=='B':
                print("Marks scored in BENGALI: ",sch[i][57])
                print("Percentage of marks scored in BENGALI: ",sch[i][58],"%")
            elif sch[i][234]=='S':
                print("Marks scored in SANSKRIT: ",sch[i][59])
                print("Percentage of marks scored in SANSKRIT: ",sch[i][60],"%")
            print("Marks scored in CHEMISTRY: ",sch[i][61])
            print("Percentage of marks scored in CHEMISTRY: ",sch[i][62],"%")
            print("Marks scored in PHYSICS: ",sch[i][63])
            print("Percentage of marks scored in PHYSICS: ",sch[i][64],"%")
            print("Marks scored in MATHS: ",sch[i][65])
            print("Percentage of marks scored in MATHS: ",sch[i][66],"%")
            if sch[i][235]=='C':
                print("Marks scored in COMPUTER SCIENCE: ",sch[i][67])
                print("Percentage of marks scored in COMPUTER SCIENCE: ",sch[i][68],"%")
            elif sch[i][235]=='I':
                print("Marks scored in INFORMATION TECHNOLOGY: ",sch[i][69])
                print("Percentage of marks scored in INFORMATION TECHNOLOGY: ",sch[i][70],"%")
            elif sch[i][235]=='A':
                print("Marks scored in ARTIFICIAL INTELLIGENCE: ",sch[i][71])
                print("Percentage of marks scored in ARTIFICAL INTELLIGENCE: ",sch[i][72],"%")
            print("Marks scored in HISTORY: ",sch[i][73])
            print("Percentage of marks scored in HISTORY: ",sch[i][74],"%")
            print("Marks scored in GEOGRAPHY: ",sch[i][75])
            print("Percentage of marks scored in GEOGRAPHY: ",sch[i][76],"%")
            print("Marks scored in CIVICS: ",sch[i][77])
            print("Percentage of marks scored in CIVICS: ",sch[i][78],"%")
            print("Marks scored in GENERAL KNOWLEDGE: ",sch[i][79])
            print("Percentage of marks scored in GENERAL KNOWLEDGE: ",sch[i][80],"%")
            print("Marks scored in MORAL SCIENCE: ",sch[i][81])
            print("Percentage of marks scored in MORAL SCIENCE: ",sch[i][82],"%")
            print("Marks scored in BIOLOGY: ",sch[i][222])
            print("Percentage of marks scored in BIOLOGY: ",sch[i][223],"%")
            print("Total Marks gained by the student: ",sch[i][83])
            print("Total percentage gained by the student: ",sch[i][84],"%")
            
            print()
            
            print("*** MARKS SCORED BY THE STUDENT IN TERM-1(F.M=80) ***")
            print("Marks scored in ENGLISH: ",sch[i][85])
            print("Percentage of marks scored in ENGLISH: ",sch[i][86],"%")
            if sch[i][236]=='H':
                print("Marks scored in HINDI: ",sch[i][87])
                print("Percentage of marks scored in HINDI: ",sch[i][88],"%")
            elif sch[i][236]=='B':
                print("Marks scored in BENGALI: ",sch[i][89])
                print("Percentage of marks scored in BENGALI: ",sch[i][90],"%")
            elif sch[i][236]=='S':
                print("Marks scored in SANSKRIT: ",sch[i][91])
                print("Percentage of marks scored in SANSKRIT: ",sch[i][92,"%"])
            print("Marks scored in CHEMISTRY: ",sch[i][93])
            print("Percentage of marks scored in CHEMISTRY: ",sch[i][94],"%")
            print("Marks scored in PHYSICS: ",sch[i][95])
            print("Percentage of marks scored in PHYSICS: ",sch[i][96],"%")
            print("Marks scored in MATHS: ",sch[i][97])
            print("Percentage of marks scored in MATHS: ",sch[i][98],"%")
            if sch[i][237]=='C':
                print("Marks scored in COMPUTER SCIENCE: ",sch[i][99])
                print("Percentage of marks scored in COMPUTER SCIENCE: ",sch[i][100],"%")
            elif sch[i][237]=='I':
                print("Marks scored in INFORMATION TECHNOLOGY: ",sch[i][101])
                print("Percentage of marks scored in INFORMATION TECHNOLOGY: ",sch[i][102],"%")
            elif sch[i][237]=='A':
                print("Marks scored in ARTIFICIAL INTELLIGENCE: ",sch[i][103])
                print("Percentage of marks scored in ARTIFICAL INTELLIGENCE: ",sch[i][104],"%")
            print("Marks scored in HISTORY: ",sch[i][105])
            print("Percentage of marks scored in HISTORY: ",sch[i][106],"%")
            print("Marks scored in GEOGRAPHY: ",sch[i][107])
            print("Percentage of marks scored in GEOGRAPHY: ",sch[i][108],"%")
            print("Marks scored in CIVICS: ",sch[i][109])
            print("Percentage of marks scored in CIVICS: ",sch[i][110],"%")
            print("Marks scored in GENERAL KNOWLEDGE: ",sch[i][111])
            print("Percentage of marks scored in GENERAL KNOWLEDGE: ",sch[i][112],"%")
            print("Marks scored in MORAL SCIENCE: ",sch[i][113])
            print("Percentage of marks scored in MORAL SCIENCE: ",sch[i][114],"%")
            print("Marks scored in BIOLOGY: ",sch[i][224])
            print("Percentage of marks scored in BIOLOGY: ",sch[i][225],"%")
            print("Total Marks gained by the student: ",sch[i][115])
            print("Total percentage gained by the student: ",sch[i][116],"%")
            
            print()
            
            print("*** MARKS SCORED BY THE STUDENT IN UNIT_TEST-3(F.M=40) ***")
            print("Marks scored in ENGLISH: ",sch[i][117])
            print("Percentage of marks scored in ENGLISH: ",sch[i][118],"%")
            if sch[i][238]=='H':
                print("Marks scored in HINDI: ",sch[i][119])
                print("Percentage of marks scored in HINDI: ",sch[i][120],"%")
            elif sch[i][238]=='B':
                print("Marks scored in BENGALI: ",sch[i][121])
                print("Percentage of marks scored in BENGALI: ",sch[i][122],"%")
            elif sch[i][238]=='S':
                print("Marks scored in SANSKRIT: ",sch[i][123])
                print("Percentage of marks scored in SANSKRIT: ",sch[i][124],"%")
            print("Marks scored in CHEMISTRY: ",sch[i][125])
            print("Percentage of marks scored in CHEMISTRY: ",sch[i][126],"%")
            print("Marks scored in PHYSICS: ",sch[i][127])
            print("Percentage of marks scored in PHYSICS: ",sch[i][128],"%")
            print("Marks scored in MATHS: ",sch[i][129])
            print("Percentage of marks scored in MATHS: ",sch[i][130],"%")
            if sch[i][239]=='C':
                print("Marks scored in COMPUTER SCIENCE: ",sch[i][131])
                print("Percentage of marks scored in COMPUTER SCIENCE: ",sch[i][132],"%")
            elif sch[i][239]=='I':
                print("Marks scored in INFORMATION TECHNOLOGY: ",sch[i][133])
                print("Percentage of marks scored in INFORMATION TECHNOLOGY: ",sch[i][134],"%")
            elif sch[i][239]=='A':
                print("Marks scored in ARTIFICIAL INTELLIGENCE: ",sch[i][135])
                print("Percentage of marks scored in ARTIFICAL INTELLIGENCE: ",sch[i][136],"%")
            print("Marks scored in HISTORY: ",sch[i][137])
            print("Percentage of marks scored in HISTORY: ",sch[i][138],"%")
            print("Marks scored in GEOGRAPHY: ",sch[i][139])
            print("Percentage of marks scored in GEOGRAPHY: ",sch[i][140],"%")
            print("Marks scored in CIVICS: ",sch[i][141])
            print("Percentage of marks scored in CIVICS: ",sch[i][142],"%")
            print("Marks scored in GENERAL KNOWLEDGE: ",sch[i][143])
            print("Percentage of marks scored in GENERAL KNOWLEDGE: ",sch[i][144],"%")
            print("Marks scored in MORAL SCIENCE: ",sch[i][145])
            print("Percentage of marks scored in MORAL SCIENCE: ",sch[i][146],"%")
            print("Marks scored in BIOLOGY: ",sch[i][226])
            print("Percentage of marks scored in BIOLOGY: ",sch[i][227],"%")
            print("Total Marks gained by the student: ",sch[i][147])
            print("Total percentage gained by the student: ",sch[i][148],"%")
            
            print()
            
            print("*** MARKS SCORED BY THE STUDENT IN UNIT_TEST-4(F.M=40) ***")
            print("Marks scored in ENGLISH: ",sch[i][149])
            print("Percentage of marks scored in ENGLISH: ",sch[i][150],"%")
            if sch[i][240]=='H':
                print("Marks scored in HINDI: ",sch[i][151])
                print("Percentage of marks scored in HINDI: ",sch[i][152],"%")
            elif sch[i][240]=='B':
                print("Marks scored in BENGALI: ",sch[i][153])
                print("Percentage of marks scored in BENGALI: ",sch[i][154],"%")
            elif sch[i][240]=='S':
                print("Marks scored in SANSKRIT: ",sch[i][155])
                print("Percentage of marks scored in SANSKRIT: ",sch[i][156],"%")
            print("Marks scored in CHEMISTRY: ",sch[i][157])
            print("Percentage of marks scored in CHEMISTRY: ",sch[i][158],"%")
            print("Marks scored in PHYSICS: ",sch[i][159])
            print("Percentage of marks scored in PHYSICS: ",sch[i][160],"%")
            print("Marks scored in MATHS: ",sch[i][161])
            print("Percentage of marks scored in MATHS: ",sch[i][162],"%")
            if sch[i][241]=='C':
                print("Marks scored in COMPUTER SCIENCE: ",sch[i][163])
                print("Percentage of marks scored in COMPUTER SCIENCE: ",sch[i][164],"%")
            elif sch[i][241]=='I':
                print("Marks scored in INFORMATION TECHNOLOGY: ",sch[i][165])
                print("Percentage of marks scored in INFORMATION TECHNOLOGY: ",sch[i][166],"%")
            elif sch[i][241]=='A':
                print("Marks scored in ARTIFICIAL INTELLIGENCE: ",sch[i][167])
                print("Percentage of marks scored in ARTIFICAL INTELLIGENCE: ",sch[i][168],"%")
            print("Marks scored in HISTORY: ",sch[i][169])
            print("Percentage of marks scored in HISTORY: ",sch[i][170],"%")
            print("Marks scored in GEOGRAPHY: ",sch[i][171])
            print("Percentage of marks scored in GEOGRAPHY: ",sch[i][172],"%")
            print("Marks scored in CIVICS: ",sch[i][173])
            print("Percentage of marks scored in CIVICS: ",sch[i][174],"%")
            print("Marks scored in GENERAL KNOWLEDGE: ",sch[i][175])
            print("Percentage of marks scored in GENERAL KNOWLEDGE: ",sch[i][176],"%")
            print("Marks scored in MORAL SCIENCE: ",sch[i][177])
            print("Percentage of marks scored in MORAL SCIENCE: ",sch[i][178],"%")
            print("Marks scored in BIOLOGY: ",sch[i][228])
            print("Percentage of marks scored in BIOLOGY: ",sch[i][229],"%")
            print("Total Marks gained by the student: ",sch[i][179])
            print("Total percentage gained by the student: ",sch[i][180],"%")
            
            print()
            
            print("*** MARKS SCORED BY THE STUDENT IN TERM-2(F.M=80) ***")
            print("Marks scored in ENGLISH: ",sch[i][181])
            print("Percentage of marks scored in ENGLISH: ",sch[i][182],"%")
            if sch[i][242]=='H':
                print("Marks scored in HINDI: ",sch[i][183])
                print("Percentage of marks scored in HINDI: ",sch[i][184],"%")
            elif sch[i][242]=='B':
                print("Marks scored in BENGALI: ",sch[i][185])
                print("Percentage of marks scored in BENGALI: ",sch[i][186],"%")
            elif sch[i][242]=='S':
                print("Marks scored in SANSKRIT: ",sch[i][187])
                print("Percentage of marks scored in SANSKRIT: ",sch[i][188],"%")
            print("Marks scored in CHEMISTRY: ",sch[i][189])
            print("Percentage of marks scored in CHEMISTRY: ",sch[i][190],"%")
            print("Marks scored in PHYSICS: ",sch[i][191])
            print("Percentage of marks scored in PHYSICS: ",sch[i][192],"%")
            print("Marks scored in MATHS: ",sch[i][193])
            print("Percentage of marks scored in MATHS: ",sch[i][194],"%")
            if sch[i][243]=='C':
                print("Marks scored in COMPUTER SCIENCE: ",sch[i][195])
                print("Percentage of marks scored in COMPUTER SCIENCE: ",sch[i][196],"%")
            elif sch[i][243]=='I':
                print("Marks scored in INFORMATION TECHNOLOGY: ",sch[i][197])
                print("Percentage of marks scored in INFORMATION TECHNOLOGY: ",sch[i][198],"%")
            elif sch[i][243]=='A':
                print("Marks scored in ARTIFICIAL INTELLIGENCE: ",sch[i][199])
                print("Percentage of marks scored in ARTIFICAL INTELLIGENCE: ",sch[i][200],"%")
            print("Marks scored in HISTORY: ",sch[i][201])
            print("Percentage of marks scored in HISTORY: ",sch[i][202],"%")
            print("Marks scored in GEOGRAPHY: ",sch[i][203])
            print("Percentage of marks scored in GEOGRAPHY: ",sch[i][204],"%")
            print("Marks scored in CIVICS: ",sch[i][205])
            print("Percentage of marks scored in CIVICS: ",sch[i][206],"%")
            print("Marks scored in GENERAL KNOWLEDGE: ",sch[i][207])
            print("Percentage of marks scored in GENERAL KNOWLEDGE: ",sch[i][208],"%")
            print("Marks scored in MORAL SCIENCE: ",sch[i][209])
            print("Percentage of marks scored in MORAL SCIENCE: ",sch[i][210],"%")
            print("Marks scored in BIOLOGY: ",sch[i][230])
            print("Percentage of marks scored in BIOLOGY: ",sch[i][231],"%")
            print("Total Marks gained by the student: ",sch[i][211])
            print("Total percentage gained by the student: ",sch[i][212],"%")
            
            print()
            
            print("Best of UNIT_TEST's under TERM-1(out of 5): ",sch[i][213])
            print("Best of UNIT_TEST's under TERM-2(out of 5): ",sch[i][214])
            print("Best of overall UNIT_TEST(out of 10): ",sch[i][217])
            print("Total Marks scored in TERM-1(out of 20): ",sch[i][215])
            print("Total Marks scored in TERM-2(out of 60): ",sch[i][216])
            print("Overall TERM examination(out of 80): ",sch[i][218])
            print("Percentage gained by the student in CLASS PERFORMANCE(out of 5): ",sch[i][19],"%")
            print("Percentage gained by the student in PROJECT & ACTIVITY(out of 5): ",sch[i][20],"%")
            print("Total percentage gained by the student(out of 100): ",sch[i][219],"%")
            
            print()
            
            if sch[i][219]>=33:
                print("# --PASS-- Promoted to next class #")
            else:
                print("# --FAIL-- Not promoted to next class #")
                
            print("--------------------------------------------------------------------------------------")
                
            found=True
            
     if found==False:
        print("*** STUDENT'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct admission number of the student to display the Student's MARK SHEET __/\__")
        
     print()
     ans=input("Press 'd/D' to display more Student's MARK SHEET: ")
     print()
    f.close()