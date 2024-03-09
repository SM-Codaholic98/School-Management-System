import pickle
import random
from datetime import date

sch={}

def calculateAge(birthDate, year):
    today = date.today()
    age = year - birthDate.year - ((today.month, today.day) <(birthDate.month, birthDate.day)) 
    return age


def INSERT_SC_TEACH_REC():
    f=open('SMS_SC_TEACH.dat','wb')
    ans='i'
    while ans.lower()=='i':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& INSERT TEACHER'S RECORD &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        t_id=random.randint(100000,999999)
        t_name=input("Enter the teacher's Full Name: ")
        print("ID Number of",t_name,"is: ",t_id)
        t_fn=input("Enter the teacher's Father's Name: ")
        t_mn=input("Enter the teacher's Mother's Name: ")
        t_sn=input("Enter the teacher's Spouse's Name: ")
        t_gn=input("Enter the teacher's Guardian's Name: ")
        t_sub=input("Enter the teacher's Teaching Subject: ")
        
        print()
        print("// Note:- Do not give dot in between while typing the teacher's degree //")
        t_q=input("Enter the teacher's Qualification(degree) as either B.Sc, BCA or B.Tech for the Bachelor's degree and as either M.Sc, MCA or M.Tech for the Master's degree (Note:- B.Ed is compulsory): ").upper()
        if '.' in t_q:
            t_q=t_q.replace('.','')
        print()
            
        t_g=input("Enter the teacher's Grade as either PRT, TGT or PGT: ").upper()
        t_sex=input("Enter the teacher's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
        t_dob=input("Enter the teacher's Date Of Birth (DD/MM/YYYY): ")
        t_email=input("Enter the teacher's Email Address: ")
        t_add=input("Enter the teacher's House Address: ")        
        
        print()
        print("// Note:- Mobile/Phone number must be of 10 digits of numeric type (without ISD code) //")
        t_phno=int(input("Enter the teacher's Mobile/Phone Number: +91 "))
        print()
        
        print()
        print("// Note:- Aadhaar number must be of 12 digits of numeric type \\")
        t_adhr=int(input("Enter the teacher's Aadhaar Number: "))
        print()
        
        print()
        print("// Note:- Permanent Account Number (PAN) must be of 10 digits of alpha-numeric type \\")
        t_pan=input("Enter the teacher's PAN Number: ")
        print()
        
        print("--x--x-- TEACHER'S BANK DETAILS --x--x--")
        t_cid=int(input("Enter the teacher's Customer ID Number: "))
        print("// Note:- Indian Financial System Code (IFSC Code) must be of 11 digits of alpha-numeric type \\")
        t_ifsc=input("Enter the teacher's IFSC Code: ")
        print("// Note:- Magnetic Ink Character Recognition Code (MICR Code) must be of 9 digits of numeric type \\")
        t_micr=int(input("Enter the teacher's MICR Code: "))
        t_accno=int(input("Enter the teacher's Account Number: "))
        t_br_name=input("Enter the bank's branch Name: ")
        print("// Note:- Telephone number (Toll-Free Number) must be of 10 or 11 digits of numeric type //")
        t_br_tel=int(input("Enter the bank's branch Telephone Number: "))
        t_br_add=input("Enter the bank's branch Address: ")
        t_br_email=input("Enter the bank's branch Email Address: ")
        
        found_grade=False
        found_sex=False
        found_email=False
        found_phno=False
        found_adhr=False
        found_pan=False
        found_ifsc=False
        found_micr=False
        found_tel=False
        found_br_email=False
        
        if '@' and '.com' in t_br_email:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_br_email=True
        else:
            print()
            print("~~~ Bank's branch email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the bank's branch to store the teacher's details __/\__")
            print()
            t_br_email=input("Enter the bank's branch Email Address: ")
            if '@' and '.com' in t_br_email:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_br_email=True
            else:
               print()
               found_br_email=False
               print("~~~ Bank's branch email address doesn't contain '@' or '.com' !!! ~~~")
        
        if len(str(t_br_tel))==10 or len(str(t_br_tel))==11:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_tel=True
        else:
            print()
            print("~~~ Invalid telephone number of the bank's branch has been entered !!! ~~~")
            print("--> Please provide the valid telephone number of the bank's branch to store the teacher's details __/\__")
            print()
            print("// Note:- Telephone number (Toll-Free Number) must be of 10 or 11 digits of numeric type //")
            t_br_tel=int(input("Enter the bank's branch Telephone Number: "))
            if len(str(t_br_tel))==10 or len(str(t_br_tel))==11:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_tel=True
            else:
                print()
                found_tel=False
                print("~~~ Invalid telephone number of the bank's branch has been entered !!! ~~~")
        
        if len(str(t_micr))==9:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_micr=True
        else:
            print()
            print("~~~ Invalid MICR Code of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid MICR Code of the teacher to store the teacher's details __/\__")
            print()
            print("// Note:- Magnetic Ink Character Recognition Code (MICR Code) must be of 9 digits of numeric type \\")
            t_micr=int(input("Enter the teacher's MICR Code: "))
            if len(str(t_micr))==9:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_micr=True
            else:
                print()
                found_micr=False
                print("~~~ Invalid MICR Code of the teacher has been entered !!! ~~~")
        
        if len(t_ifsc)==11:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_ifsc=True
        else:
            print()
            print("~~~ Invalid IFSC Code of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid IFSC Code of the teacher to store the teacher's details __/\__")
            print()
            print("// Note:- Indian Financial System Code (IFSC Code) must be of 11 digits of alpha-numeric type \\")
            t_ifsc=input("Enter the teacher's IFSC Code: ")
            if len(t_ifsc)==11:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_ifsc=True
            else:
                print()
                found_ifsc=False
                print("~~~ Invalid IFSC Code of the teacher has been entered !!! ~~~")
        
        if len(t_pan)==10:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_pan=True
        else:
            print()
            print("~~~ Invalid PAN number of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid PAN number of the teacher to store the teacher's details __/\__")
            print()
            print("// Note:- Permanent Account Number (PAN) must be of 10 digits of alpha-numeric type \\")
            t_pan=input("Enter the teacher's PAN Number: ")
            if len(t_pan)==10:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_pan=True
            else:
                print()
                found_pan=False
                print("~~~ Invalid PAN number of the teacher has been entered !!! ~~~")
        
        if len(str(t_adhr))==12:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_adhr=True
        else:
            print()
            print("~~~ Invalid aadhaar number of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid aadhaar number of the teacher to store the teacher's details __/\__")
            print()
            print("// Note:- Aadhaar number must be of 12 digits of numeric type \\")
            t_adhr=int(input("Enter the teacher's Aadhaar Number: "))
            if len(str(t_adhr))==12:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_adhr=True
            else:
                print()
                found_adhr=False
                print("~~~ Invalid aadhaar number of the teacher has been entered !!! ~~~")
        
        if len(str(t_phno))==10:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_phno=True
        else:
            print()
            print("~~~ Invalid mobile/phone number of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid mobile/phone number of the teacher to store the teacher's details __/\__")
            print()
            print("// Note:- Mobile/Phone number must be of 10 digits of numeric type (without ISD code) //")
            t_phno=int(input("Enter the teacher's Mobile/Phone Number: +91 "))
            if len(str(t_phno))==10:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_phno=True
            else:
                print()
                found_phno=False
                print("~~~ Invalid mobile/phone number of the teacher has been entered !!! ~~~")
        
        if t_g=='PRT' or t_g=='TGT' or t_g=='PGT':
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_grade=True
        else:
            print()
            print("~~~ Invalid grade of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid grade of the teacher to store the teacher's details __/\__")
            print()
            t_g=input("Enter the teacher's Grade as either PRT, TGT or PGT: ").upper()
            if t_g=='PRT' or t_g=='TGT' or t_g=='PGT':
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_grade=True
            else:
                print()
                found_grade=False
                print("~~~ Invalid grade of the teacher has been entered !!! ~~~")
                
        if t_sex=='MALE' or t_sex=='FEMALE' or t_sex=='THIRD GENDER' or t_sex=='M' or t_sex=='F' or t_sex=='TG' :
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_sex=True
        else:
            print()
            print("~~~ Invalid sex of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid sex of the teacher to store the teacher's details __/\__")
            print()
            t_sex=input("Enter the teacher's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
            if t_sex=='MALE' or t_sex=='FEMALE' or t_sex=='THIRD GENDER' or t_sex=='M' or t_sex=='F' or t_sex=='TG' :
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_sex=True
            else:
                print()
                found_sex=False
                print("~~~ Invalid sex of the teacher has been entered !!! ~~~")
                
        if '@' and '.com' in t_email:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_email=True
        else:
            print()
            print("~~~ Teacher's email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the teacher to store the teacher's details __/\__")
            print()
            t_email=input("Enter the teacher's Email Address: ")
            if '@' and '.com' in t_email:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_email=True
            else:
               print()
               found_email=False
               print("~~~ Teacher's email address doesn't contain '@' or '.com' !!! ~~~")
               
        if found_grade==True and found_sex==True and found_email==True and found_phno==True and found_adhr==True and found_pan==True and found_ifsc==True and found_micr==True and found_tel==True and found_br_email==True:
            pickle.dump(sch,f)
            print()
            print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY INSERTED !!! ***")
        else:
            print()
            print("*** TEACHER'S RECORD HAS NOT BEEN INSERTED !!! ***")
            print("--> Something went wrong in provided data, please provide the proper data of the teacher to store the teacher's record __/\__")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        print()
        ans=input("Press 'i/I' to insert more teacher's record: ")
        print()
    f.close()
    
    
percent=0.05
bp1=30000
bp2=35000    
bp3=40000    
def COMPUTE_SC_TEACH_REC():
    
    global percent,bp1,bp2,bp3
    
    f=open('SMS_SC_TEACH.dat','rb+')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='c'
    while ans.lower()=='c':
     ID=int(input("Enter the ID number of the teacher to compute the Teacher's SALARY STRUCTURE: "))
     found=False
     for i in sch:
       if i==ID:
        found=True
        sch[i][8]=sch[i][8]+1
        spl = sch[i][4].split('/')
        t_d = int(spl[0])
        t_m = int(spl[1])
        t_y = int(spl[2])
        t_age = calculateAge(date(t_y, t_m, t_d), sch[i][8])
        sch[i][9] = t_age
        if sch[i][9]>21 and sch[i][9]<61:
            if "BED" in sch[i][2] and ("BSC" in sch[i][2] or "BCA" in sch[i][2] or "BTECH" in sch[i][2]):
                if ("MSC" not in sch[i][2] and "MCA" not in sch[i][2] and "MTECH" not in sch[i][2]) and "PHD" not in sch[i][2]:
                    if sch[i][9]>=22 and sch[i][9]<28:                                                
                        if sch[i][3]=='PRT':
                            bp1=30000
                            da=0.3*bp1
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp1
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp1
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp1+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12
                            sch[i][6]=ai
                            
                        elif sch[i][3]=='TGT':
                            bp2=35000
                            da=0.3*bp2
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp2
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp2
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp2+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12
                            sch[i][6]=ai
                            
                        else:
                            print("~~~ NOTE: Teacher's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],",QUALIFICATION -",sch[i][2],"& GRADE -",sch[i][3],",Invalid grade of the teacher has been entered. --> Teacher's Grade must be 'PRT' ,'TGT' or 'PGT' ~~~")                       
                                
                    elif sch[i][9]>=28 and sch[i][9]<61:
                        if sch[i][3]=='PRT':
                            BP1=bp1*percent
                            bp1=BP1+30000
                            da=0.3*bp1
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp1
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp1
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp1+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12
                            sch[i][6]=ai
                            
                        elif sch[i][3]=='TGT':
                            BP2=bp2*percent
                            bp2=BP2+35000
                            da=0.3*bp2
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp2
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp2
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp2+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12
                            sch[i][6]=ai
                            
                        else:
                             print("~~~ NOTE: Teacher's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],",QUALIFICATION -",sch[i][2],"& GRADE -",sch[i][3],",Invalid grade of the teacher has been entered. --> Teacher's Grade must be 'PRT' ,'TGT' or 'PGT' ~~~")                      
                
                elif "PHD" not in sch[i][2]: 
                    if sch[i][9]>=24 and sch[i][9]<30:
                        if sch[i][3]=='PRT':
                            bp1=30000
                            da=0.3*bp1
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp1
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp1
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp1+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12
                            sch[i][6]=ai
                            
                        elif sch[i][3]=='TGT':
                            bp2=35000
                            da=0.3*bp2
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp2
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp2
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp2+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12
                            sch[i][6]=ai
                            
                        elif sch[i][3]=='PGT':
                            bp3=40000
                            da=0.3*bp3
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp3
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp3
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp3+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12 
                            sch[i][6]=ai
                            
                        else:
                            print("~~~ NOTE: Teacher's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],",QUALIFICATION -",sch[i][2],"& GRADE -",sch[i][3],",Invalid grade of the teacher has been entered. --> Teacher's Grade must be 'PRT' ,'TGT' or 'PGT' ~~~")
                              
                    elif sch[i][9]>=30 and sch[i][9]<61:
                        if sch[i][3]=='PRT':
                            BP1=bp1*percent
                            bp1=BP1+30000
                            da=0.3*bp1
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp1
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp1
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp1+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12
                            sch[i][6]=ai
                            
                        elif sch[i][3]=='TGT':
                            BP2=bp2*percent
                            bp2=BP2+35000
                            da=0.3*bp2
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp2
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp2
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp2+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12
                            sch[i][6]=ai
                            
                        elif sch[i][3]=='PGT':
                            BP3=bp3*percent
                            bp3=BP3+40000
                            da=0.3*bp3
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp3
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp3
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp3+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12 
                            sch[i][6]=ai
                        
                        else:
                            print("~~~ NOTE: Teacher's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],",QUALIFICATION -",sch[i][2],"& GRADE -",sch[i][3],",Invalid grade of the teacher has been entered. --> Teacher's Grade must be 'PRT' ,'TGT' or 'PGT' ~~~")
                
                else:  
                    if sch[i][9]>=27 and sch[i][9]<33:
                        if sch[i][3]=='PRT':
                            bp1=30000
                            da=0.3*bp1
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp1
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp1
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp1+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12
                            sch[i][6]=ai
                            
                        elif sch[i][3]=='TGT':
                            bp2=35000
                            da=0.3*bp2
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp2
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp2
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp2+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12
                            sch[i][6]=ai
                            
                        elif sch[i][3]=='PGT':
                            bp3=40000
                            da=0.3*bp3
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp3
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp3
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp3+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12 
                            sch[i][6]=ai
                                                    
                        else:
                            print("~~~ NOTE: Teacher's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],",QUALIFICATION -",sch[i][2],"& GRADE -",sch[i][3],",Invalid grade of the teacher has been entered. --> Teacher's Grade must be 'PRT' ,'TGT' or 'PGT' ~~~")
                                                
                    elif sch[i][9]>=33 and sch[i][9]<61:
                        if sch[i][3]=='PRT':
                            BP1=bp1*percent
                            bp1=BP1+30000
                            da=0.3*bp1
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp1
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp1
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp1+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12
                            sch[i][6]=ai
                            
                        elif sch[i][3]=='TGT':
                            BP2=bp2*percent
                            bp2=BP2+35000
                            da=0.3*bp2
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp2
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp2
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp2+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12
                            sch[i][6]=ai
                            
                        elif sch[i][3]=='PGT':
                            BP3=bp3*percent
                            bp3=BP3+40000
                            da=0.3*bp3
                            DA=da*12
                            sch[i][12]=da
                            sch[i][16]=DA
                            ma=0.15*bp3
                            MA=ma*12
                            sch[i][13]=ma
                            sch[i][17]=MA
                            hra=10000
                            HRA=hra*12
                            sch[i][14]=hra
                            sch[i][18]=HRA
                            pf=0.28*bp3
                            sch[i][10]=pf
                            PF=pf*12
                            sch[i][15]=PF
                            sch[i][7]=sch[i][7]+PF
                            gp=bp3+da+ma+hra+pf
                            np=gp-pf
                            sch[i][11]=np
                            ai=np*12 
                            sch[i][6]=ai
                            
                        else:
                            print("~~~ NOTE: Teacher's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],",QUALIFICATION -",sch[i][2],"& GRADE -",sch[i][3],",Invalid grade of the teacher has been entered. --> Teacher's Grade must be 'PRT' ,'TGT' or 'PGT' ~~~")
                            
            else:
                print("~~~ NOTE: Teacher's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],"& QUALIFICATION -",sch[i][2],"will be appointed in the school, if the teacher must have B.Ed and (B.Sc or BCA or B.Tech) ~~~")    
        
        else:
            print("~~~ NOTE: Teacher's ID NUMBER -",i,",NAME -",sch[i][0],"& AGE -",sch[i][9],"will be appointed in the school, if the teacher will fall in the age category in between 21 & 61 ~~~")
        
        pickle.dump(sch,f)
     
     if found==False:
        print("*** TEACHER'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the teacher to compute the Teacher's SALARY STRUCTURE __/\__")
     
     print()
     ans=input("Press 'c/C' to compute more Teacher's SALARY STRUCTURE: ")
     print()                 
    f.close()
   
    
def DISP_ALL_SC_TEACH_REC():
    f=open('SMS_SC_TEACH.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
    print("{:<12} {:<12} {:<12} {:<12} {:<12} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("T_ID",
                                                                                                                                                 "T_Name",
                                                                                                                                                 "T_Subject",
                                                                                                                                                 "T_Qualification",
                                                                                                                                                 "T_Grade",
                                                                                                                                                 "T_Age",
                                                                                                                                                 "T_Sex",
                                                                                                                                                 "T_Phno.",
                                                                                                                                                 "T_Email address",
                                                                                                                                                 "T_House address",
                                                                                                                                                 "T_Monthly DA",
                                                                                                                                                 "T_Annual DA",
                                                                                                                                                 "T_Monthly MA",
                                                                                                                                                 "T_Annual MA",
                                                                                                                                                 "T_Monthly HRA",
                                                                                                                                                 "T_Annual HRA",
                                                                                                                                                 "T_Monthly income",
                                                                                                                                                 "T_Annual income",
                                                                                                                                                 "T_Monthly PF",
                                                                                                                                                 "T_Annual PF",
                                                                                                                                                 "T_Total PF",
                                                                                                                                                 "Year"))
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')      
    for j in sch:
        print("{:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(j,
                                                                                                                                                     sch[j][0],
                                                                                                                                                     sch[j][1],
                                                                                                                                                     sch[j][2],
                                                                                                                                                     sch[j][3],
                                                                                                                                                     sch[j][9],
                                                                                                                                                     sch[j][5],
                                                                                                                                                     sch[j][19],
                                                                                                                                                     sch[j][20],
                                                                                                                                                     sch[j][21],
                                                                                                                                                     sch[j][12],
                                                                                                                                                     sch[j][16],
                                                                                                                                                     sch[j][13],
                                                                                                                                                     sch[j][17],
                                                                                                                                                     sch[j][14],
                                                                                                                                                     sch[j][18],
                                                                                                                                                     sch[j][11],
                                                                                                                                                     sch[j][6],
                                                                                                                                                     sch[j][10],
                                                                                                                                                     sch[j][15],
                                                                                                                                                     sch[j][7],
                                                                                                                                                     sch[j][8]))
    f.close()
    
    
def APPEND_SC_TEACH_REC():
    f=open('SMS_SC_TEACH.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
    f.close()
    
    f=open('SMS_SC_TEACH.dat','ab')
    ans='a'
    while ans.lower()=='a':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& APPEND TEACHER'S RECORD &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        t_id=random.randint(100000,999999)
        t_name=input("Enter the teacher's Full Name: ")
        print("ID Number of",t_name,"is: ",t_id)
        t_fn=input("Enter the teacher's Father's Name: ")
        t_mn=input("Enter the teacher's Mother's Name: ")
        t_sn=input("Enter the teacher's Spouse's Name: ")
        t_gn=input("Enter the teacher's Guardian's Name: ")
        t_sub=input("Enter the teacher's Teaching Subject: ")
        
        print()
        print("// Note:- Do not give dot in between while typing the teacher's degree //")
        t_q=input("Enter the teacher's Qualification(degree) as either B.Sc, BCA or B.Tech for the Bachelor's degree and as either M.Sc, MCA or M.Tech for the Master's degree (Note:- B.Ed is compulsory): ").upper()
        if '.' in t_q:
            t_q=t_q.replace('.','')
        print()
            
        t_g=input("Enter the teacher's Grade as either PRT, TGT or PGT: ").upper()
        t_sex=input("Enter the teacher's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
        t_dob=input("Enter the teacher's Date Of Birth (DD/MM/YYYY): ")
        t_email=input("Enter the teacher's Email Address: ")
        t_add=input("Enter the teacher's House Address: ")        
        
        print()
        print("// Note:- Mobile/Phone number must be of 10 digits of numeric type (without ISD code) //")
        t_phno=int(input("Enter the teacher's Mobile/Phone Number: +91 "))
        print()
        
        print()
        print("// Note:- Aadhaar number must be of 12 digits of numeric type \\")
        t_adhr=int(input("Enter the teacher's Aadhaar Number: "))
        print()
        
        print()
        print("// Note:- Permanent Account Number (PAN) must be of 10 digits of alpha-numeric type \\")
        t_pan=input("Enter the teacher's PAN Number: ")
        print()
        
        print("--x--x-- TEACHER'S BANK DETAILS --x--x--")
        t_cid=int(input("Enter the teacher's Customer ID Number: "))
        print("// Note:- Indian Financial System Code (IFSC Code) must be of 11 digits of alpha-numeric type \\")
        t_ifsc=input("Enter the teacher's IFSC Code: ")
        print("// Note:- Magnetic Ink Character Recognition Code (MICR Code) must be of 9 digits of numeric type \\")
        t_micr=int(input("Enter the teacher's MICR Code: "))
        t_accno=int(input("Enter the teacher's Account Number: "))
        t_br_name=input("Enter the bank's branch Name: ")
        print("// Note:- Telephone number (Toll-Free Number) must be of 10 or 11 digits of numeric type //")
        t_br_tel=int(input("Enter the bank's branch Telephone Number: "))
        t_br_add=input("Enter the bank's branch Address: ")
        t_br_email=input("Enter the bank's branch Email Address: ")
        
        found_grade=False
        found_sex=False
        found_email=False
        found_phno=False
        found_adhr=False
        found_pan=False
        found_ifsc=False
        found_micr=False
        found_tel=False
        found_br_email=False
        
        if '@' and '.com' in t_br_email:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_br_email=True
        else:
            print()
            print("~~~ Bank's branch email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the bank's branch to store the teacher's details __/\__")
            print()
            t_br_email=input("Enter the bank's branch Email Address: ")
            if '@' and '.com' in t_br_email:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_br_email=True
            else:
               print()
               found_br_email=False
               print("~~~ Bank's branch email address doesn't contain '@' or '.com' !!! ~~~")
        
        if len(str(t_br_tel))==10 or len(str(t_br_tel))==11:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_tel=True
        else:
            print()
            print("~~~ Invalid telephone number of the bank's branch has been entered !!! ~~~")
            print("--> Please provide the valid telephone number of the bank's branch to store the teacher's details __/\__")
            print()
            print("// Note:- Telephone number (Toll-Free Number) must be of 10 or 11 digits of numeric type //")
            t_br_tel=int(input("Enter the bank's branch Telephone Number: "))
            if len(str(t_br_tel))==10 or len(str(t_br_tel))==11:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_tel=True
            else:
                print()
                found_tel=False
                print("~~~ Invalid telephone number of the bank's branch has been entered !!! ~~~")
        
        if len(str(t_micr))==9:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_micr=True
        else:
            print()
            print("~~~ Invalid MICR Code of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid MICR Code of the teacher to store the teacher's details __/\__")
            print()
            print("// Note:- Magnetic Ink Character Recognition Code (MICR Code) must be of 9 digits of numeric type \\")
            t_micr=int(input("Enter the teacher's MICR Code: "))
            if len(str(t_micr))==9:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_micr=True
            else:
                print()
                found_micr=False
                print("~~~ Invalid MICR Code of the teacher has been entered !!! ~~~")
        
        if len(t_ifsc)==11:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_ifsc=True
        else:
            print()
            print("~~~ Invalid IFSC Code of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid IFSC Code of the teacher to store the teacher's details __/\__")
            print()
            print("// Note:- Indian Financial System Code (IFSC Code) must be of 11 digits of alpha-numeric type \\")
            t_ifsc=input("Enter the teacher's IFSC Code: ")
            if len(t_ifsc)==11:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_ifsc=True
            else:
                print()
                found_ifsc=False
                print("~~~ Invalid IFSC Code of the teacher has been entered !!! ~~~")
        
        if len(t_pan)==10:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_pan=True
        else:
            print()
            print("~~~ Invalid PAN number of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid PAN number of the teacher to store the teacher's details __/\__")
            print()
            print("// Note:- Permanent Account Number (PAN) must be of 10 digits of alpha-numeric type \\")
            t_pan=input("Enter the teacher's PAN Number: ")
            if len(t_pan)==10:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_pan=True
            else:
                print()
                found_pan=False
                print("~~~ Invalid PAN number of the teacher has been entered !!! ~~~")
        
        if len(str(t_adhr))==12:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_adhr=True
        else:
            print()
            print("~~~ Invalid aadhaar number of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid aadhaar number of the teacher to store the teacher's details __/\__")
            print()
            print("// Note:- Aadhaar number must be of 12 digits of numeric type \\")
            t_adhr=int(input("Enter the teacher's Aadhaar Number: "))
            if len(str(t_adhr))==12:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_adhr=True
            else:
                print()
                found_adhr=False
                print("~~~ Invalid aadhaar number of the teacher has been entered !!! ~~~")
        
        if len(str(t_phno))==10:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_phno=True
        else:
            print()
            print("~~~ Invalid mobile/phone number of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid mobile/phone number of the teacher to store the teacher's details __/\__")
            print()
            print("// Note:- Mobile/Phone number must be of 10 digits of numeric type (without ISD code) //")
            t_phno=int(input("Enter the teacher's Mobile/Phone Number: +91 "))
            if len(str(t_phno))==10:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_phno=True
            else:
                print()
                found_phno=False
                print("~~~ Invalid mobile/phone number of the teacher has been entered !!! ~~~")
        
        if t_g=='PRT' or t_g=='TGT' or t_g=='PGT':
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_grade=True
        else:
            print()
            print("~~~ Invalid grade of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid grade of the teacher to store the teacher's details __/\__")
            print()
            t_g=input("Enter the teacher's Grade as either PRT, TGT or PGT: ").upper()
            if t_g=='PRT' or t_g=='TGT' or t_g=='PGT':
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_grade=True
            else:
                print()
                found_grade=False
                print("~~~ Invalid grade of the teacher has been entered !!! ~~~")
                
        if t_sex=='MALE' or t_sex=='FEMALE' or t_sex=='THIRD GENDER' or t_sex=='M' or t_sex=='F' or t_sex=='TG' :
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_sex=True
        else:
            print()
            print("~~~ Invalid sex of the teacher has been entered !!! ~~~")
            print("--> Please provide the valid sex of the teacher to store the teacher's details __/\__")
            print()
            t_sex=input("Enter the teacher's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
            if t_sex=='MALE' or t_sex=='FEMALE' or t_sex=='THIRD GENDER' or t_sex=='M' or t_sex=='F' or t_sex=='TG' :
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_sex=True
            else:
                print()
                found_sex=False
                print("~~~ Invalid sex of the teacher has been entered !!! ~~~")
                
        if '@' and '.com' in t_email:
            sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
            found_email=True
        else:
            print()
            print("~~~ Teacher's email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the teacher to store the teacher's details __/\__")
            print()
            t_email=input("Enter the teacher's Email Address: ")
            if '@' and '.com' in t_email:
                sch[t_id]=[t_name,t_sub,t_q,t_g,t_dob,t_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,t_phno,t_email,t_add,t_adhr,t_pan,t_cid,t_ifsc,t_micr,t_accno,t_br_name,t_br_tel,t_br_add,t_br_email,t_fn,t_mn,t_sn,t_gn]
                found_email=True
            else:
               print()
               found_email=False
               print("~~~ Teacher's email address doesn't contain '@' or '.com' !!! ~~~")
               
        if found_grade==True and found_sex==True and found_email==True and found_phno==True and found_adhr==True and found_pan==True and found_ifsc==True and found_micr==True and found_tel==True and found_br_email==True:
            pickle.dump(sch,f)
            print()
            print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY APPENDED !!! ***")
        else:
            print()
            print("*** TEACHER'S RECORD HAS NOT BEEN APPENDED !!! ***")
            print("--> Something went wrong in provided data, please provide the proper data of the teacher to store the teacher's record __/\__")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        print()
        ans=input("Press 'a/A' to append more teacher's record: ")
        print()
    f.close()
    
    
def SEARCH_SC_TEACH_REC():
    f=open('SMS_SC_TEACH.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='s'
    while ans.lower()=='s':
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("########################################################### SEARCH TEACHER'S RECORD ###########################################################")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     ID=int(input("Enter the ID number of the teacher to search the teacher's record: "))
     found=False      
     for j in sch:
        if j==ID:
            print("--x--x-- Provided ID number of the teacher is present in the database ...@ Press 8 to display the Teacher's SALARY SLIP and Teacher's BANK DETAILS --x--x--")
            found=True
            break
     
     if found==False:
        print("*** TEACHER'S RECORD HAS NOT BEEN FOUND !!! ***") 
        print("--> Please provide the correct ID number of the teacher to search the teacher's record __/\__")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
     print()
     ans=input("Press 's/S' to search more teacher's record: ")
     print()
    f.close()
  
    
def UPDATE_SC_TEACH_REC():
    f=open('SMS_SC_TEACH.dat','rb+')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='u'
    while ans.lower()=='u':
     ID=int(input("Enter the ID number of the teacher to update the teacher's record: "))
     found=False
     for j in sch:
        if j==ID:
            
            ans='o'
            while ans.lower()=='o':
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ UPDATE TEACHER'S RECORD $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("--x--x-- TEACHER UPDATE MENU --x--x--")
                print("# Press 'n/N' to update the teacher's Full Name")
                print("# Press 'h/H' to update the teacher's Father's Name")
                print("# Press 'w/W' to update the teacher's Mother's Name")
                print("# Press 'u/U' to update the teacher's Spouse's Name")
                print("# Press 'j/J' to update the teacher's Guardian's Name")
                print("# Press 't/T' to update the teacher's Teaching Subject")
                print("# Press 's/S' to update the teacher's Gender")
                print("# Press 'd/D' to update the teacher's Date Of Birth")
                print("# Press 'q/Q' to update the teacher's Qualification(degree)")
                print("# Press 'g/G' to update the teacher's Grade")
                print("# Press 'm/M' to update the teacher's Mobile/Phone Number")
                print("# Press 'a/A' to update the teacher's House Address")
                print("# Press 'e/E' to update the teacher's Email Address")
                print("# Press 'r/R' to update the teacher's Aadhaar Number")
                print("# Press 'p/P' to update the teacher's PAN Number")
                print("# Press 'c/C' to update the teacher's Customer ID Number")
                print("# Press 'f/F' to update the teacher's IFSC Code")
                print("# Press 'i/I' to update the teacher's MICR Code")
                print("# Press 'acnt/ACNT' to update the teacher's Account Number")
                print("# Press 'bbn/BBN' to update the bank's branch Name")
                print("# Press 'bbt/BBT' to update the bank's branch Telephone Number")
                print("# Press 'bba/BBA' to update the bank's branch Address")
                print("# Press 'bbe/BBE' to update the bank's branch Email Address")
                ch=input("Enter the choice of the teacher from the TEACHER UPDATE MENU: ").upper()
                
                if ch=='N':
                    print()
                    n=input("Enter the updated Full Name of the teacher: ")
                    sch[j][0]=n
                    print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='H':
                    print()
                    h=input("Enter the updated Father's Name of the teacher: ")
                    sch[j][32]=h
                    print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='W':
                    print()
                    w=input("Enter the updated Mother's Name of the teacher: ")
                    sch[j][33]=w
                    print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='U':
                    print()
                    u=input("Enter the updated Spouse's Name of the teacher: ")
                    sch[j][34]=u
                    print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='J':
                    print()
                    j=input("Enter the updated Guardian's Name of the teacher: ")
                    sch[j][35]=j
                    print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='T':
                    print()
                    t=input("Enter the updated Teaching Subject of the teacher: ")
                    sch[j][1]=t
                    print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='D':
                    print()
                    d=input("Enter the updated Date Of Birth of the teacher: ")
                    sch[j][4]=d
                    print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='S':
                    print()
                    s=input("Enter the updated Gender of the teacher as either MALE or M, FEMALE or F, THIRD GENDER or TG: ")
                    if s=='MALE' or s=='FEMALE' or s=='THIRD GENDER' or s=='M' or s=='F' or s=='TG' :
                        sch[j][5]=s
                        print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid sex of the teacher has been entered !!! ~~~")
                        print("--> Please provide the valid sex of the teacher to update the field of the teacher's sex __/\__")
                        print()
                        s=input("Enter the updated Gender of the teacher as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
                        if s=='MALE' or s=='FEMALE' or s=='THIRD GENDER' or s=='M' or s=='F' or s=='TG' :
                            sch[j][5]=s
                            print("*** NOW TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid sex of the teacher has been entered !!! ~~~")
                
                elif ch=='Q':
                    print()
                    print("// Note:- Do not give dot in between while typing the degree of the teacher //")
                    q=input("Enter the updated Qualification(degree) of the teacher as either B.Sc, BCA or B.Tech for the Bachelor's degree and as either M.Sc, MCA or M.Tech for the Master's degree (Note:- B.Ed is compulsory): ").upper()
                    if '.' in q:
                        q=q.replace('.','')
                    sch[j][2]=q
                    print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='G':
                    print()
                    g=input("Enter the updated Grade of the teacher as either PRT, TGT or PGT: ").upper()
                    if g=='PRT' or g=='TGT' or g=='PGT':
                        sch[j][3]=g
                        print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid grade of the teacher has been entered !!! ~~~")
                        print("--> Please provide the valid grade of the teacher to update the field of the teacher's grade __/\__")
                        print()
                        g=input("Enter the updated Grade of the teacher as either PRT, TGT or PGT: ").upper()
                        if g=='PRT' or g=='TGT' or g=='PGT':
                            sch[j][3]=g
                            print("*** NOW TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid grade of the teacher has been entered !!! ~~~")
                            
                elif ch=='M':
                    print()
                    print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
                    m=int(input("Enter the updated Mobile/Phone Number of the teacher: +91 "))
                    if len(str(m))==10:
                        sch[j][19]=m
                        print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid mobile/phone number of the teacher has been entered !!! ~~~")
                        print("--> Please provide the valid mobile/phone number of the teacher to update the field of the teacher's mobile/phone number __/\__")
                        print()
                        print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) //")
                        m=int(input("Enter the updated Mobile/Phone Number of the teacher: +91 "))
                        if len(str(m))==10:
                            sch[j][19]=m
                            print("*** NOW TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid mobile/phone number of the teacher has been entered !!! ~~~")
                    
                elif ch=='E':
                    print()
                    e=input("Enter the updated Email Address of the teacher: ")
                    if '@' and '.com' in e:
                        sch[j][20]=e
                        print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Teacher's email address doesn't contain '@' or '.com' !!! ~~~")
                        print("--> Please provide the proper email address of the teacher to update the field of the teacher's email address __/\__")
                        print()
                        e=input("Enter the updated Email Address of the teacher: ")
                        if '@' and '.com' in e:
                            sch[j][20]=e
                            print("*** NOW TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Teacher's email address doesn't contain '@' or '.com' !!! ~~~")
                            
                elif ch=='A':
                    print()
                    a=input("Enter the updated House Address of the teacher: ")
                    sch[j][21]=a
                    print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='R':
                    print()
                    print("// Note:- Aadhaar number must be of 12 digits of numeric type \\")
                    r=int(input("Enter the updated Aadhaar Number of the teacher: "))
                    if len(str(r))==12:
                        sch[j][22]=r
                        print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid aadhaar number of the teacher has been entered !!! ~~~")
                        print("--> Please provide the valid aadhaar number of the teacher to update the field of the teacher's aadhaar number __/\__")
                        print()
                        print("// Note:- Aadhaar number must be of 12 digits of numeric type \\")
                        r=int(input("Enter the updated Aadhaar Number of the teacher: "))
                        if len(str(r))==12:
                            sch[j][22]=r
                            print("*** NOW TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid aadhaar number of the teacher has been entered !!! ~~~")
                            
                elif ch=='P':
                    print()
                    print("// Note:- Permanent Account Number (PAN) must be of 10 digits of alpha-numeric type \\")
                    p=input("Enter the updated PAN Number of the teacher: ")
                    if len(p)==10:
                        sch[j][23]=p
                        print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid PAN number of the teacher has been entered !!! ~~~")
                        print("--> Please provide the valid PAN number of the teacher to update the field of the teacher's PAN number __/\__")
                        print()
                        print("// Note:- Permanent Account Number (PAN) must be of 10 digits of alpha-numeric type \\")
                        p=input("Enter the updated PAN Number of the teacher: ")
                        if len(p)==10:
                            sch[j][23]=p
                            print("*** NOW TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid PAN number of the teacher has been entered !!! ~~~")
                            
                elif ch=='C':
                    print()
                    c=input("Enter the updated Customer ID Number of the teacher: ")
                    sch[j][24]=c
                    print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='F':
                    print()
                    print("// Note:- Indian Financial System Code (IFSC Code) must be of 11 digits of alpha-numeric type \\")
                    f=input("Enter the updated IFSC Code of the teacher: ")
                    if len(f)==11:
                        sch[j][25]=f
                        print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid IFSC Code of the teacher has been entered !!! ~~~")
                        print("--> Please provide the valid IFSC Code of the teacher to update the field of the teacher's IFSC Code __/\__")
                        print()
                        print("// Note:- Indian Financial System Code (IFSC Code) must be of 11 digits of alpha-numeric type \\")
                        f=input("Enter the updated IFSC Code of the teacher: ")
                        if len(f)==11:
                            sch[j][25]=f
                            print("*** NOW TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid IFSC Code of the teacher has been entered !!! ~~~")
                            
                elif ch=='I':
                    print()
                    print("// Note:- Magnetic Ink Character Recognition Code (MICR Code) must be of 9 digits of numeric type \\")
                    i=int(input("Enter the updated MICR Code of the teacher: "))
                    if len(str(i))==12:
                        sch[j][26]=i
                        print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid MICR Code of the teacher has been entered !!! ~~~")
                        print("--> Please provide the valid MICR Code of the teacher to update the field of the teacher's MICR Code __/\__")
                        print()
                        print("// Note:- Magnetic Ink Character Recognition Code (MICR Code) must be of 9 digits of numeric type \\")
                        i=int(input("Enter the updated MICR Code of the teacher: "))
                        if len(str(i))==12:
                            sch[j][26]=i
                            print("*** NOW TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid MICR Code of the teacher has been entered !!! ~~~")
                            
                elif ch=='ACNT':
                    print()
                    acnt=input("Enter the updated Account Number of the teacher: ")
                    sch[j][27]=acnt
                    print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='BBN':
                    print()
                    bbn=input("Enter the updated branch Name of the bank: ")
                    sch[j][28]=bbn
                    print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='BBT':
                    print()
                    print("// Note:- Telephone number (Toll-Free Number) must be of 10 or 11 digits of numeric type //")
                    bbt=int(input("Enter the updated branch Telephone Number of the bank: "))
                    if len(str(bbt))==10 or len(str(bbt))==11:
                        sch[j][29]=bbt
                        print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid telephone number of the bank's branch has been entered !!! ~~~")
                        print("--> Please provide the valid telephone number of the bank's branch to update the field of the bank's branch telephone number __/\__")
                        print()
                        print("// Note:- Telephone number (Toll-Free Number) must be of 10 or 11 digits of numeric type //")
                        bbt=int(input("Enter the updated branch Telephone Number of the bank: "))
                        if len(str(bbt))==10 or len(str(bbt))==11:
                            sch[j][29]=bbt
                            print("*** NOW TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid telephone number of the bank's branch has been entered !!! ~~~")
                            
                elif ch=='BBA':
                    print()
                    bba=input("Enter the updated branch Address of the bank: ")
                    sch[j][30]=bba
                    print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='BBE':
                    print()
                    bbe=input("Enter the updated branch Email Address of the bank: ")
                    if '@' and '.com' in e:
                        sch[j][31]=bbe
                        print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Bank's branch email address doesn't contain '@' or '.com' !!! ~~~")
                        print("--> Please provide the proper email address of the bank's branch to update the field of the bank's branch email address __/\__")
                        print()
                        bbe=input("Enter the updated branch Email Address of the bank: ")
                        if '@' and '.com' in bbe:
                            sch[j][31]=bbe
                            print("*** NOW TEACHER'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** TEACHER'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Bank's branch email address doesn't contain '@' or '.com' !!! ~~~")
        
                else:
                    print()
                    print("*** ID NUMBER OF THE TEACHER HAS BEEN MATCHED BUT YOU HAVE ENTERED WRONG CHOICE FROM THE TEACHER UPDATE MENU !!! ***")
                    print("--> Please provide the appropriate choice to update the teacher's detail __/\__")
                
                found=True
                pickle.dump(sch,f)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                ans=input("Press 'o/O' to update any other detail of the teacher: ")
     
     if found==False:
        print("*** TEACHER'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the teacher to update the teacher's details __/\__")
     
     print()
     ans=input("Press 'u/U' to update more teacher's record: ")
     print()
    f.close()
    
    
def DEL_SC_TEACH_REC():
    SCH={}
    f=open("SMS_SC_TEACH.dat","rb+")
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='r'
    while ans.lower()=='r':
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("################################################ DELETE TEACHER'S RECORD ################################################")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     ID=int(input("Enter the ID number of the teacher, to be search and to delete or remove the teacher's record: "))
     found=False
     for k in sch:
        if k!=ID:
            found=True
            SCH[k]=sch[k]
            pickle.dump(SCH,f)
     
     if found==False:
        print("*** TEACHER'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the teacher to delete or remove the teacher's record __/\__")
     else:
        print("*** TEACHER'S RECORD HAS BEEN SUCCESSFULLY DELETED !!! ***")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
     print()
     ans=input("Press 'r/R' to delete or remove more teacher's record: ")
     print()
    f.close()
    
    
def DISP_PART_SC_TEACH_REC():
    f=open('SMS_SC_TEACH.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='d'
    while ans.lower()=='d':
     ID=int(input("Enter the ID number of the teacher to display the Teacher's SALARY SLIP and Teacher's BANK DETAILS: "))
     print()
     found=False
     for j in sch:
        if j==ID:
            print("-------------------------------------------------------------------")
            print("%%%%%%%%%%%%%%%%%%%%%% TEACHER'S SALARY SLIP %%%%%%%%%%%%%%%%%%%%%%")
            print("-------------------------------------------------------------------")
            print("Teacher's Unique ID Number: ",j)
            print("Teacher's Full Name: ",sch[j][0])
            print("Teacher's Father's Name: ",sch[j][32])
            print("Teacher's Mother's Name: ",sch[j][33])
            print("Teacher's Spouse's Name: ",sch[j][34])
            print("Teacher's Guardian's Name: ",sch[j][35])
            print("Teacher's Teaching Subject: ",sch[j][1])
            print("Teacher's Qualification(degree): ",sch[j][2])
            print("Teacher's Grade: ",sch[j][3])
            print("Teacher's Sex: ",sch[j][5])
            print("Teacher's DOB: ",sch[j][4])
            print("Teacher's Age: ",sch[j][9])
            print("Teacher's Mobile/Phone Number: +91",sch[j][19])
            print("Teacher's Aadhaar Number: ",sch[j][22])
            print("Teacher's PAN Number: ",sch[j][23])
            print("Teacher's Email Address: ",sch[j][20])
            print("Teacher's House Address: ",sch[j][21])
            print("Teacher's Monthly DA: Rs.",sch[j][12])
            print("Teacher's Annual DA: Rs.",sch[j][16])
            print("Teacher's Monthly MA: Rs.",sch[j][13])
            print("Teacher's Annual MA: Rs.",sch[j][17])
            print("Teacher's Monthly HRA: Rs.",sch[j][14])
            print("Teacher's Annual HRA: Rs.",sch[j][18])
            print("Teacher's Monthly income: Rs.",sch[j][11])
            print("Teacher's Annual income: Rs.",sch[j][6])
            print("Teacher's Monthly PF: Rs.",sch[j][10])
            print("Teacher's Annual PF: Rs.",sch[j][15])
            print("Teacher's Total PF: Rs.",sch[j][7])
            print("Year: ",sch[j][8])
            print("-------------------------------------------------------------------")
            found=True
     
            print("--------------------------------------------------------------------")
            print("%%%%%%%%%%%%%%%%%%%%%% TEACHER'S BANK DETAILS %%%%%%%%%%%%%%%%%%%%%%")
            print("--------------------------------------------------------------------")
            print("Teacher's Full Name: ",sch[j][0])
            print("Teacher's Customer ID Number: ",sch[j][24])
            print("Teacher's IFSC Code: ",sch[j][25])
            print("Teacher's MICR Code: ",sch[j][26])
            print("Teacher's Account Number: ",sch[j][27])
            print("Bank's Branch Name: ",sch[j][28])
            print("Bank's Branch Telephone Number: ",sch[j][29])
            print("Bank's Branch Address: ",sch[j][30])
            print("Bank's Branch Email Address: ",sch[j][31])
            print("--------------------------------------------------------------------")
            
     if found==False:
        print("*** TEACHER'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the teacher to display the Teacher's SALARY SLIP and Teacher's BANK DETAILS __/\__")
        
     print()
     ans=input("Press 'd/D' to display more Teacher's SALARY SLIP and Teacher's BANK DETAILS: ")
     print()
    f.close()