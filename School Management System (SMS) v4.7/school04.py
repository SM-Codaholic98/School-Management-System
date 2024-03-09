import pickle
import random
from datetime import date

sch={}

def calculateAge(birthDate, year):
    today = date.today()
    age = year - birthDate.year - ((today.month, today.day) <(birthDate.month, birthDate.day)) 
    return age


def INSERT_GROUP_A_STAFF_REC():
    f=open('SMS_GROUP_A_STAFF.dat','wb')
    ans='i'
    while ans.lower()=='i':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& INSERT STAFF'S RECORD &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s_id=random.randint(100000,999999)
        s_name=input("Enter the staff's Full Name: ")
        print("ID Number of",s_name,"is: ",s_id)
        s_fn=input("Enter the staff's Father's Name: ")
        s_mn=input("Enter the staff's Mother's Name: ")
        s_sn=input("Enter the staff's Spouse's Name: ")
        s_gn=input("Enter the staff's Guardian's Name: ")
        s_rwg=input("Enter the staff's relation with the guardian of the staff: ")
        s_sub=input("Enter the staff's Working Subject: ")
        
        print()
        print("// Note:- Do not give dot in between while typing the staff's degree //")
        s_q=input("Enter the staff's Qualification(degree) (Note:- Bachelor's degree is compulsory): ").upper()
        if '.' in s_q:
            s_q=s_q.replace('.','')
        print()
            
        s_g=input("Enter the staff's Grade as either RECEPTIONIST, CLERK, HEAD CLERK, OFFICE SUPERINTENDENT or OFFICE ASSISTANT: ").upper()
        s_sex=input("Enter the staff's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
        s_dob=input("Enter the staff's Date Of Birth (DD/MM/YYYY): ")
        s_email=input("Enter the staff's Email Address: ")
        s_add=input("Enter the staff's House Address: ")        
        
        print()
        print("// Note:- Mobile/Phone number must be of 10 digits of numeric type (without ISD code) //")
        s_phno=int(input("Enter the staff's Mobile/Phone Number: +91 "))
        print()
        
        print()
        print("// Note:- Aadhaar number must be of 12 digits of numeric type \\")
        s_adhr=int(input("Enter the staff's Aadhaar Number: "))
        print()
        
        print()
        print("// Note:- Permanent Account Number (PAN) must be of 10 digits of alpha-numeric type \\")
        s_pan=input("Enter the staff's PAN Number: ")
        print()
        
        print("--x--x-- STAFF'S BANK DETAILS --x--x--")
        s_cid=int(input("Enter the staff's Customer ID Number: "))
        print("// Note:- Indian Financial System Code (IFSC Code) must be of 11 digits of alpha-numeric type \\")
        s_ifsc=input("Enter the staff's IFSC Code: ")
        print("// Note:- Magnetic Ink Character Recognition Code (MICR Code) must be of 9 digits of numeric type \\")
        s_micr=int(input("Enter the staff's MICR Code: "))
        s_accno=int(input("Enter the staff's Account Number: "))
        s_br_name=input("Enter the bank's branch Name: ")
        print("// Note:- Telephone number (Toll-Free Number) must be of 10 or 11 digits of numeric type //")
        s_br_tel=int(input("Enter the bank's branch Telephone Number: "))
        s_br_add=input("Enter the bank's branch Address: ")
        s_br_email=input("Enter the bank's branch Email Address: ")
        
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
        
        if '@' and '.com' in s_br_email:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_br_email=True
        else:
            print()
            print("~~~ Bank's branch email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the bank's branch to store the staff's details __/\__")
            print()
            s_br_email=input("Enter the bank's branch Email Address: ")
            if '@' and '.com' in s_br_email:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_br_email=True
            else:
               print()
               found_br_email=False
               print("~~~ Bank's branch email address doesn't contain '@' or '.com' !!! ~~~")
        
        if len(str(s_br_tel))==10 or len(str(s_br_tel))==11:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_tel=True
        else:
            print()
            print("~~~ Invalid telephone number of the bank's branch has been entered !!! ~~~")
            print("--> Please provide the valid telephone number of the bank's branch to store the staff's details __/\__")
            print()
            print("// Note:- Telephone number (Toll-Free Number) must be of 10 or 11 digits of numeric type //")
            s_br_tel=int(input("Enter the bank's branch Telephone Number: "))
            if len(str(s_br_tel))==10 or len(str(s_br_tel))==11:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_tel=True
            else:
                print()
                found_tel=False
                print("~~~ Invalid telephone number of the bank's branch has been entered !!! ~~~")
        
        if len(str(s_micr))==9:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_micr=True
        else:
            print()
            print("~~~ Invalid MICR Code of the staff has been entered !!! ~~~")
            print("--> Please provide the valid MICR Code of the staff to store the staff's details __/\__")
            print()
            print("// Note:- Magnetic Ink Character Recognition Code (MICR Code) must be of 9 digits of numeric type \\")
            s_micr=int(input("Enter the staff's MICR Code: "))
            if len(str(s_micr))==9:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_micr=True
            else:
                print()
                found_micr=False
                print("~~~ Invalid MICR Code of the staff has been entered !!! ~~~")
        
        if len(s_ifsc)==11:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_ifsc=True
        else:
            print()
            print("~~~ Invalid IFSC Code of the staff has been entered !!! ~~~")
            print("--> Please provide the valid IFSC Code of the staff to store the staff's details __/\__")
            print()
            print("// Note:- Indian Financial System Code (IFSC Code) must be of 11 digits of alpha-numeric type \\")
            s_ifsc=input("Enter the staff's IFSC Code: ")
            if len(s_ifsc)==11:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_ifsc=True
            else:
                print()
                found_ifsc=False
                print("~~~ Invalid IFSC Code of the staff has been entered !!! ~~~")
        
        if len(s_pan)==10:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_pan=True
        else:
            print()
            print("~~~ Invalid PAN number of the staff has been entered !!! ~~~")
            print("--> Please provide the valid PAN number of the staff to store the staff's details __/\__")
            print()
            print("// Note:- Permanent Account Number (PAN) must be of 10 digits of alpha-numeric type \\")
            s_pan=input("Enter the staff's PAN Number: ")
            if len(s_pan)==10:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_pan=True
            else:
                print()
                found_pan=False
                print("~~~ Invalid PAN number of the staff has been entered !!! ~~~")
        
        if len(str(s_adhr))==12:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_adhr=True
        else:
            print()
            print("~~~ Invalid aadhaar number of the staff has been entered !!! ~~~")
            print("--> Please provide the valid aadhaar number of the staff to store the staff's details __/\__")
            print()
            print("// Note:- Aadhaar number must be of 12 digits of numeric type \\")
            s_adhr=int(input("Enter the staff's Aadhaar Number: "))
            if len(str(s_adhr))==12:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_adhr=True
            else:
                print()
                found_adhr=False
                print("~~~ Invalid aadhaar number of the staff has been entered !!! ~~~")
        
        if len(str(s_phno))==10:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_phno=True
        else:
            print()
            print("~~~ Invalid mobile/phone number of the staff has been entered !!! ~~~")
            print("--> Please provide the valid mobile/phone number of the staff to store the staff's details __/\__")
            print()
            print("// Note:- Mobile/Phone number must be of 10 digits of numeric type (without ISD code) //")
            s_phno=int(input("Enter the staff's Mobile/Phone Number: +91 "))
            if len(str(s_phno))==10:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_phno=True
            else:
                print()
                found_phno=False
                print("~~~ Invalid mobile/phone number of the staff has been entered !!! ~~~")
        
        if s_g=='RECEPTIONIST' or s_g=='CLERK' or s_g=='HEAD CLERK' or s_g=='OFFICE SUPERINTENDENT' or s_g=='OFFICE ASSISTANT':
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_grade=True
        else:
            print()
            print("~~~ Invalid grade of the staff has been entered !!! ~~~")
            print("--> Please provide the valid grade of the staff to store the staff's details __/\__")
            print()
            s_g=input("Enter the staff's Grade as either RECEPTIONIST, CLERK, HEAD CLERK, OFFICE SUPERINTENDENT or OFFICE ASSISTANT: ").upper()
            if s_g=='RECEPTIONIST' or s_g=='CLERK' or s_g=='HEAD CLERK' or s_g=='OFFICE SUPERINTENDENT' or s_g=='OFFICE ASSISTANT':
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_grade=True
            else:
                print()
                found_grade=False
                print("~~~ Invalid grade of the staff has been entered !!! ~~~")
                
        if s_sex=='MALE' or s_sex=='FEMALE' or s_sex=='THIRD GENDER' or s_sex=='M' or s_sex=='F' or s_sex=='TG' :
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_sex=True
        else:
            print()
            print("~~~ Invalid sex of the staff has been entered !!! ~~~")
            print("--> Please provide the valid sex of the staff to store the staff's details __/\__")
            print()
            s_sex=input("Enter the staff's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
            if s_sex=='MALE' or s_sex=='FEMALE' or s_sex=='THIRD GENDER' or s_sex=='M' or s_sex=='F' or s_sex=='TG' :
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_sex=True
            else:
                print()
                found_sex=False
                print("~~~ Invalid sex of the staff has been entered !!! ~~~")
                
        if '@' and '.com' in s_email:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_email=True
        else:
            print()
            print("~~~ Staff's email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the staff to store the staff's details __/\__")
            print()
            s_email=input("Enter the staff's Email Address: ")
            if '@' and '.com' in s_email:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_email=True
            else:
               print()
               found_email=False
               print("~~~ Staff's email address doesn't contain '@' or '.com' !!! ~~~")
               
        if found_grade==True and found_sex==True and found_email==True and found_phno==True and found_adhr==True and found_pan==True and found_ifsc==True and found_micr==True and found_tel==True and found_br_email==True:
            pickle.dump(sch,f)
            print()
            print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY INSERTED !!! ***")
        else:
            print()
            print("*** STAFF'S RECORD HAS NOT BEEN INSERTED !!! ***")
            print("--> Something went wrong in provided data, please provide proper data of the staff to store the staff's record __/\__")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        print()
        ans=input("Press 'i/I' to insert more staff's record: ")
        print()
    f.close()
    
    
percent=0.05  
bp1=25000
bp2=27000   
def COMPUTE_GROUP_A_STAFF_REC():
    
    global percent,bp1,bp2
    
    f=open('SMS_GROUP_A_STAFF.dat','rb+')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='c'
    while ans.lower()=='c':
     ID=int(input("Enter the ID number of the staff to compute the Staff's SALARY STRUCTURE: "))
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
        if sch[i][9]>19 and sch[i][9]<61:
            if "BA" in sch[i][2] or "BSC" in sch[i][2] or "BCA" in sch[i][2] or "BTECH" in sch[i][2] or "BCOM" in sch[i][2] or "BBA" in sch[i][2] or "BFA" in sch[i][2]:
                if ("MA" not in sch[i][2] and "MSC" not in sch[i][2] and "MCOM" not in sch[i][2] and "MBA" not in sch[i][2] and "MFA" not in sch[i][2] and "MTECH" not in sch[i][2] and "MCA" not in sch[i][2]) and "PHD" not in sch[i][2]:
                    if sch[i][9]>=20 and sch[i][9]<25:                                                
                        if sch[i][3]=='RECEPTIONIST':
                            bp1=25000
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
                            
                        elif sch[i][3]=='CLERK':
                            bp1=25000
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
                            
                        elif sch[i][3]=='OFFICE ASSISTANT':
                            bp1=25000
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
                            
                        elif sch[i][3]=='HEAD CLERK':
                            bp2=27000
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
                            
                        elif sch[i][3]=='OFFICE SUPERINTENDENT':
                            bp2=27000
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
                            print("~~~ NOTE: Staff's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],",QUALIFICATION -",sch[i][2],"& GRADE -",sch[i][3],",Invalid grade of the staff has been entered. --> Staff's Grade must be 'RECEPTIONIST' ,'CLERK', 'OFFICE ASSISTANT', 'HEAD CLERK' or 'OFFICE SUPERINTENDENT' ~~~")                 
                                
                    elif sch[i][9]>=25 and sch[i][9]<61:
                        if sch[i][3]=='RECEPTIONIST':
                            BP1=bp1*percent
                            bp1=BP1+25000
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
                            
                        elif sch[i][3]=='CLERK':
                            BP1=bp1*percent
                            bp1=BP1+25000
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
                            
                        elif sch[i][3]=='OFFICE ASSISTANT':
                            BP1=bp1*percent
                            bp1=BP1+25000
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
                            
                        elif sch[i][3]=='HEAD CLERK':
                            BP2=bp2*percent
                            bp2=BP2+27000
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
                            
                        elif sch[i][3]=='OFFICE SUPERINTENDENT':
                            BP2=bp2*percent
                            bp2=BP2+27000
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
                            print("~~~ NOTE: Staff's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],",QUALIFICATION -",sch[i][2],"& GRADE -",sch[i][3],",Invalid grade of the staff has been entered. --> Staff's Grade must be 'RECEPTIONIST' ,'CLERK', 'OFFICE ASSISTANT', 'HEAD CLERK' or 'OFFICE SUPERINTENDENT' ~~~")                          
                
                elif "PHD" not in sch[i][2]: 
                    if sch[i][9]>=22 and sch[i][9]<27:
                        if sch[i][3]=='RECEPTIONIST':
                            bp1=25000
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
                            
                        elif sch[i][3]=='CLERK':
                            bp1=25000
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
                            
                        elif sch[i][3]=='OFFICE ASSISTANT':
                            bp1=25000
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
                            
                        elif sch[i][3]=='HEAD CLERK':
                            bp2=27000
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
                            
                        elif sch[i][3]=='OFFICE SUPERINTENDENT':
                            bp2=27000
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
                            print("~~~ NOTE: Staff's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],",QUALIFICATION -",sch[i][2],"& GRADE -",sch[i][3],",Invalid grade of the staff has been entered. --> Staff's Grade must be 'RECEPTIONIST' ,'CLERK', 'OFFICE ASSISTANT', 'HEAD CLERK' or 'OFFICE SUPERINTENDENT' ~~~")
                              
                    elif sch[i][9]>=27 and sch[i][9]<61:
                        if sch[i][3]=='RECEPTIONIST':
                            BP1=bp1*percent
                            bp1=BP1+25000
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
                            
                        elif sch[i][3]=='CLERK':
                            BP1=bp1*percent
                            bp1=BP1+25000
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
                            
                        elif sch[i][3]=='OFFICE ASSISTANT':
                            BP1=bp1*percent
                            bp1=BP1+25000
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
                            
                        elif sch[i][3]=='HEAD CLERK':
                            BP2=bp2*percent
                            bp2=BP2+27000
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
                            
                        elif sch[i][3]=='OFFICE SUPERINTENDENT':
                            BP2=bp2*percent
                            bp2=BP2+27000
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
                            print("~~~ NOTE: Staff's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],",QUALIFICATION -",sch[i][2],"& GRADE -",sch[i][3],",Invalid grade of the staff has been entered. --> Staff's Grade must be 'RECEPTIONIST' ,'CLERK', 'OFFICE ASSISTANT', 'HEAD CLERK' or 'OFFICE SUPERINTENDENT' ~~~")
                
                else:  
                    if sch[i][9]>=25 and sch[i][9]<30:
                        if sch[i][3]=='RECEPTIONIST':
                            bp1=25000
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
                            
                        elif sch[i][3]=='CLERK':
                            bp1=25000
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
                            
                        elif sch[i][3]=='OFFICE ASSISTANT':
                            bp1=25000
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
                            
                        elif sch[i][3]=='HEAD CLERK':
                            bp2=27000
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
                            
                        elif sch[i][3]=='OFFICE SUPERINTENDENT':
                            bp2=27000
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
                            print("~~~ NOTE: Staff's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],",QUALIFICATION -",sch[i][2],"& GRADE -",sch[i][3],",Invalid grade of the staff has been entered. --> Staff's Grade must be 'RECEPTIONIST' ,'CLERK', 'OFFICE ASSISTANT', 'HEAD CLERK' or 'OFFICE SUPERINTENDENT' ~~~")
                                                
                    elif sch[i][9]>=30 and sch[i][9]<61:
                        if sch[i][3]=='RECEPTIONIST':
                            BP1=bp1*percent
                            bp1=BP1+25000
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
                            
                        elif sch[i][3]=='CLERK':
                            BP1=bp1*percent
                            bp1=BP1+25000
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
                            
                        elif sch[i][3]=='OFFICE ASSISTANT':
                            BP1=bp1*percent
                            bp1=BP1+25000
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
                            
                        elif sch[i][3]=='HEAD CLERK':
                            BP2=bp2*percent
                            bp2=BP2+27000
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
                            
                        elif sch[i][3]=='OFFICE SUPERINTENDENT':
                            BP2=bp2*percent
                            bp2=BP2+27000
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
                            print("~~~ NOTE: Staff's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],",QUALIFICATION -",sch[i][2],"& GRADE -",sch[i][3],",Invalid grade of the staff has been entered. --> Staff's Grade must be 'RECEPTIONIST' ,'CLERK', 'OFFICE ASSISTANT', 'HEAD CLERK' or 'OFFICE SUPERINTENDENT' ~~~")
                            
            else:
                print("~~~ NOTE: Staff's ID NUMBER -",i,",NAME -",sch[i][0],",AGE -",sch[i][9],"& QUALIFICATION -",sch[i][2],"will be appointed in the school, if the staff must have Bachelor's Degree ~~~")
                    
        else:
            print("~~~ NOTE: Staff's ID NUMBER -",i,",NAME -",sch[i][0],"& AGE -",sch[i][9],"will be appointed in the school, if the staff will fall in the age category in between 19 & 61 ~~~")    
                         
        pickle.dump(sch,f)
        
     if found==False:
        print("*** STAFF'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the staff to compute the Staff's SALARY STRUCTURE __/\__")
        
     print()
     ans=input("Press 'c/C' to compute more Staff's SALARY STRUCTURE: ")
     print()
    f.close()
    
    
def DISP_ALL_GROUP_A_STAFF_REC():
    f=open('SMS_GROUP_A_STAFF.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
    print("{:<12} {:<12} {:<12} {:<12} {:<12} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("S_ID",
                                                                                                                                                 "S_Name",
                                                                                                                                                 "S_Subject",
                                                                                                                                                 "S_Qualification",
                                                                                                                                                 "S_Grade",
                                                                                                                                                 "S_Age",
                                                                                                                                                 "S_Sex",
                                                                                                                                                 "S_Phno.",
                                                                                                                                                 "S_Email address",
                                                                                                                                                 "S_House address",
                                                                                                                                                 "S_Monthly DA",
                                                                                                                                                 "S_Annual DA",
                                                                                                                                                 "S_Monthly MA",
                                                                                                                                                 "S_Annual MA",
                                                                                                                                                 "S_Monthly HRA",
                                                                                                                                                 "S_Annual HRA",
                                                                                                                                                 "S_Monthly income",
                                                                                                                                                 "S_Annual income",
                                                                                                                                                 "S_Monthly PF",
                                                                                                                                                 "S_Annual PF",
                                                                                                                                                 "S_Total PF",
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
    
    
def APPEND_GROUP_A_STAFF_REC():
    f=open('SMS_GROUP_A_STAFF.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
    f.close()
    
    f=open('SMS_GROUP_A_STAFF.dat','ab')
    ans='a'
    while ans.lower()=='a':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& APPEND STAFF'S RECORD &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s_id=random.randint(100000,999999)
        s_name=input("Enter the staff's Full Name: ")
        print("ID Number of",s_name,"is: ",s_id)
        s_fn=input("Enter the staff's Father's Name: ")
        s_mn=input("Enter the staff's Mother's Name: ")
        s_sn=input("Enter the staff's Spouse's Name: ")
        s_gn=input("Enter the staff's Guardian's Name: ")
        s_rwg=input("Enter the staff's relation with the guardian of the staff: ")
        s_sub=input("Enter the staff's Working Subject: ")
        
        print()
        print("// Note:- Do not give dot in between while typing the staff's degree //")
        s_q=input("Enter the staff's Qualification(degree) (Note:- Bachelor's degree is compulsory): ").upper()
        if '.' in s_q:
            s_q=s_q.replace('.','')
        print()
            
        s_g=input("Enter the staff's Grade as either RECEPTIONIST, CLERK, HEAD CLERK, OFFICE SUPERINTENDENT or OFFICE ASSISTANT: ").upper()
        s_sex=input("Enter the staff's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
        s_dob=input("Enter the staff's Date Of Birth (DD/MM/YYYY): ")
        s_email=input("Enter the staff's Email Address: ")
        s_add=input("Enter the staff's House Address: ")        
        
        print()
        print("// Note:- Mobile/Phone number must be of 10 digits of numeric type (without ISD code) //")
        s_phno=int(input("Enter the staff's Mobile/Phone Number: +91 "))
        print()
        
        print()
        print("// Note:- Aadhaar number must be of 12 digits of numeric type \\")
        s_adhr=int(input("Enter the staff's Aadhaar Number: "))
        print()
        
        print()
        print("// Note:- Permanent Account Number (PAN) must be of 10 digits of alpha-numeric type \\")
        s_pan=input("Enter the staff's PAN Number: ")
        print()
        
        print("--x--x-- STAFF'S BANK DETAILS --x--x--")
        s_cid=int(input("Enter the staff's Customer ID Number: "))
        print("// Note:- Indian Financial System Code (IFSC Code) must be of 11 digits of alpha-numeric type \\")
        s_ifsc=input("Enter the staff's IFSC Code: ")
        print("// Note:- Magnetic Ink Character Recognition Code (MICR Code) must be of 9 digits of numeric type \\")
        s_micr=int(input("Enter the staff's MICR Code: "))
        s_accno=int(input("Enter the staff's Account Number: "))
        s_br_name=input("Enter the bank's branch Name: ")
        print("// Note:- Telephone number (Toll-Free Number) must be of 10 or 11 digits of numeric type //")
        s_br_tel=int(input("Enter the bank's branch Telephone Number: "))
        s_br_add=input("Enter the bank's branch Address: ")
        s_br_email=input("Enter the bank's branch Email Address: ")
        
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
        
        if '@' and '.com' in s_br_email:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_br_email=True
        else:
            print()
            print("~~~ Bank's branch email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the bank's branch to store the staff's details __/\__")
            print()
            s_br_email=input("Enter the bank's branch Email Address: ")
            if '@' and '.com' in s_br_email:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_br_email=True
            else:
               print()
               found_br_email=False
               print("~~~ Bank's branch email address doesn't contain '@' or '.com' !!! ~~~")
        
        if len(str(s_br_tel))==10 or len(str(s_br_tel))==11:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_tel=True
        else:
            print()
            print("~~~ Invalid telephone number of the bank's branch has been entered !!! ~~~")
            print("--> Please provide the valid telephone number of the bank's branch to store the staff's details __/\__")
            print()
            print("// Note:- Telephone number (Toll-Free Number) must be of 10 or 11 digits of numeric type //")
            s_br_tel=int(input("Enter the bank's branch Telephone Number: "))
            if len(str(s_br_tel))==10 or len(str(s_br_tel))==11:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_tel=True
            else:
                print()
                found_tel=False
                print("~~~ Invalid telephone number of the bank's branch has been entered !!! ~~~")
        
        if len(str(s_micr))==9:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_micr=True
        else:
            print()
            print("~~~ Invalid MICR Code of the staff has been entered !!! ~~~")
            print("--> Please provide the valid MICR Code of the staff to store the staff's details __/\__")
            print()
            print("// Note:- Magnetic Ink Character Recognition Code (MICR Code) must be of 9 digits of numeric type \\")
            s_micr=int(input("Enter the staff's MICR Code: "))
            if len(str(s_micr))==9:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_micr=True
            else:
                print()
                found_micr=False
                print("~~~ Invalid MICR Code of the staff has been entered !!! ~~~")
        
        if len(s_ifsc)==11:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_ifsc=True
        else:
            print()
            print("~~~ Invalid IFSC Code of the staff has been entered !!! ~~~")
            print("--> Please provide the valid IFSC Code of the staff to store the staff's details __/\__")
            print()
            print("// Note:- Indian Financial System Code (IFSC Code) must be of 11 digits of alpha-numeric type \\")
            s_ifsc=input("Enter the staff's IFSC Code: ")
            if len(s_ifsc)==11:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_ifsc=True
            else:
                print()
                found_ifsc=False
                print("~~~ Invalid IFSC Code of the staff has been entered !!! ~~~")
        
        if len(s_pan)==10:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_pan=True
        else:
            print()
            print("~~~ Invalid PAN number of the staff has been entered !!! ~~~")
            print("--> Please provide the valid PAN number of the staff to store the staff's details __/\__")
            print()
            print("// Note:- Permanent Account Number (PAN) must be of 10 digits of alpha-numeric type \\")
            s_pan=input("Enter the staff's PAN Number: ")
            if len(s_pan)==10:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_pan=True
            else:
                print()
                found_pan=False
                print("~~~ Invalid PAN number of the staff has been entered !!! ~~~")
        
        if len(str(s_adhr))==12:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_adhr=True
        else:
            print()
            print("~~~ Invalid aadhaar number of the staff has been entered !!! ~~~")
            print("--> Please provide the valid aadhaar number of the staff to store the staff's details __/\__")
            print()
            print("// Note:- Aadhaar number must be of 12 digits of numeric type \\")
            s_adhr=int(input("Enter the staff's Aadhaar Number: "))
            if len(str(s_adhr))==12:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_adhr=True
            else:
                print()
                found_adhr=False
                print("~~~ Invalid aadhaar number of the staff has been entered !!! ~~~")
        
        if len(str(s_phno))==10:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_phno=True
        else:
            print()
            print("~~~ Invalid mobile/phone number of the staff has been entered !!! ~~~")
            print("--> Please provide the valid mobile/phone number of the staff to store the staff's details __/\__")
            print()
            print("// Note:- Mobile/Phone number must be of 10 digits of numeric type (without ISD code) //")
            s_phno=int(input("Enter the staff's Mobile/Phone Number: +91 "))
            if len(str(s_phno))==10:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_phno=True
            else:
                print()
                found_phno=False
                print("~~~ Invalid mobile/phone number of the staff has been entered !!! ~~~")
        
        if s_g=='RECEPTIONIST' or s_g=='CLERK' or s_g=='HEAD CLERK' or s_g=='OFFICE SUPERINTENDENT' or s_g=='OFFICE ASSISTANT':
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_grade=True
        else:
            print()
            print("~~~ Invalid grade of the staff has been entered !!! ~~~")
            print("--> Please provide the valid grade of the staff to store the staff's details __/\__")
            print()
            s_g=input("Enter the staff's Grade as either RECEPTIONIST, CLERK, HEAD CLERK, OFFICE SUPERINTENDENT or OFFICE ASSISTANT: ").upper()
            if s_g=='RECEPTIONIST' or s_g=='CLERK' or s_g=='HEAD CLERK' or s_g=='OFFICE SUPERINTENDENT' or s_g=='OFFICE ASSISTANT':
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_grade=True
            else:
                print()
                found_grade=False
                print("~~~ Invalid grade of the staff has been entered !!! ~~~")
                
        if s_sex=='MALE' or s_sex=='FEMALE' or s_sex=='THIRD GENDER' or s_sex=='M' or s_sex=='F' or s_sex=='TG' :
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_sex=True
        else:
            print()
            print("~~~ Invalid sex of the staff has been entered !!! ~~~")
            print("--> Please provide the valid sex of the staff to store the staff's details __/\__")
            print()
            s_sex=input("Enter the staff's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
            if s_sex=='MALE' or s_sex=='FEMALE' or s_sex=='THIRD GENDER' or s_sex=='M' or s_sex=='F' or s_sex=='TG' :
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_sex=True
            else:
                print()
                found_sex=False
                print("~~~ Invalid sex of the staff has been entered !!! ~~~")
                
        if '@' and '.com' in s_email:
            sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
            found_email=True
        else:
            print()
            print("~~~ Staff's email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the staff to store the staff's details __/\__")
            print()
            s_email=input("Enter the staff's Email Address: ")
            if '@' and '.com' in s_email:
                sch[s_id]=[s_name,s_sub,s_q,s_g,s_dob,s_sex,0,0,2021,0,0,0,0,0,0,0,0,0,0,s_phno,s_email,s_add,s_adhr,s_pan,s_cid,s_ifsc,s_micr,s_accno,s_br_name,s_br_tel,s_br_add,s_br_email,s_fn,s_mn,s_sn,s_gn,s_rwg]
                found_email=True
            else:
               print()
               found_email=False
               print("~~~ Staff's email address doesn't contain '@' or '.com' !!! ~~~")
               
        if found_grade==True and found_sex==True and found_email==True and found_phno==True and found_adhr==True and found_pan==True and found_ifsc==True and found_micr==True and found_tel==True and found_br_email==True:
            pickle.dump(sch,f)
            print()
            print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY APPENDED !!! ***")
        else:
            print()
            print("*** STAFF'S RECORD HAS NOT BEEN APPENDED !!! ***")
            print("--> Something went wrong in provided data, please provide the proper data of the staff to store the staff's record __/\__")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        print()
        ans=input("Press 'a/A' to append more staff's record: ")
        print()
    f.close()
    
    
def SEARCH_GROUP_A_STAFF_REC():
    f=open('SMS_GROUP_A_STAFF.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='s'
    while ans.lower()=='s':
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("####################################################### SEARCH STAFF'S RECORD #########################################################")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     ID=int(input("Enter the ID number of the staff to search the staff's record: "))
     found=False      
     for j in sch:
        if j==ID:
            print("--x--x-- Provided ID number of the staff is present in the database ...@ Press 8 to display the Staff's SALARY SLIP and Staff's BANK DETAILS --x--x--")
            found=True
            break
        
     if found==False:
        print("*** STAFF'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the staff to search the staff's record __/\__")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
     print()
     ans=input("Press 's/S' to search more staff's record: ")
     print()
    f.close()
  
    
def UPDATE_GROUP_A_STAFF_REC():
    f=open('SMS_GROUP_A_STAFF.dat','rb+')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='u'
    while ans.lower()=='u':
     ID=int(input("Enter the ID number of the staff to update the staff's record: "))
     found=False
     for j in sch:
        if j==ID:
            
            ans='o'
            while ans.lower()=='o':
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ UPDATE STAFF'S RECORD $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("--x--x-- STAFF UPDATE MENU --x--x--")
                print("# Press 'n/N' to update the staff's Full Name")
                print("# Press 'h/H' to update the staff's Father's Name")
                print("# Press 'b/B' to update the staff's Mother's Name")
                print("# Press 'u/U' to update the staff's Spouse's Name")
                print("# Press 'j/J' to update the staff's Guardian's Name")
                print("# Press 'w/W' to update the staff's Working Subject")
                print("# Press 'd/D' to update the staff's Date Of Birth")
                print("# Press 's/S' to update the staff's Gender")
                print("# Press 'q/Q' to update the staff's Qualification(degree)")
                print("# Press 'g/G' to update the staff's Grade")
                print("# Press 'm/M' to update the staff's Mobile/Phone Number")
                print("# Press 'e/E' to update the staff's Email Address")
                print("# Press 'a/A' to update the staff's House Address")
                print("# Press 'r/R' to update the staff's Aadhaar Number")
                print("# Press 'p/P' to update the staff's PAN Number")
                print("# Press 'c/C' to update the staff's Customer ID Number")
                print("# Press 'f/F' to update the staff's IFSC Code")
                print("# Press 'i/I' to update the staff's MICR Code")
                print("# Press 'acnt/ACNT' to update the staff's Account Number")
                print("# Press 'bbn/BBN' to update the bank's branch Name")
                print("# Press 'bbt/BBT' to update the bank's branch Telephone Number")
                print("# Press 'bba/BBA' to update the bank's branch Address")
                print("# Press 'bbe/BBE' to update the bank's branch Email Address")
                ch=input("Enter the choice of the staff from the STAFF UPDATE MENU: ").upper()
                
                if ch=='N':
                    print()
                    n=input("Enter the updated Full Name of the staff: ")
                    sch[j][0]=n
                    print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='H':
                    print()
                    h=input("Enter the updated Father's Name of the staff: ")
                    sch[j][32]=h
                    print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='B':
                    print()
                    b=input("Enter the updated Mother's Name of the staff: ")
                    sch[j][33]=b
                    print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='U':
                    print()
                    u=input("Enter the updated Spouse's Name of the staff: ")
                    sch[j][34]=u
                    print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='J':
                    print()
                    j=input("Enter the updated Guardian's Name of the staff: ")
                    sch[j][35]=j
                    k=input("Enter the staff's updated relation with the guardian of the staff: ")
                    sch[j][36]=k
                    print()
                    print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='W':
                    print()
                    w=input("Enter the updated Working Subject of the staff: ")
                    sch[j][1]=w
                    print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='D':
                    print()
                    d=input("Enter the updated Date Of Birth of the staff: ")
                    sch[j][4]=d
                    print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='S':
                    print()
                    s=input("Enter the updated Gender of the staff as either MALE or M, FEMALE or F, THIRD GENDER or TG: ")
                    if s=='MALE' or s=='FEMALE' or s=='THIRD GENDER' or s=='M' or s=='F' or s=='TG' :
                        sch[j][5]=s
                        print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid sex of the staff has been entered !!! ~~~")
                        print("--> Please provide the valid sex of the staff to update the field of the staff's sex __/\__")
                        print()
                        s=input("Enter the updated Gender of the staff as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
                        if s=='MALE' or s=='FEMALE' or s=='THIRD GENDER' or s=='M' or s=='F' or s=='TG' :
                            sch[j][5]=s
                            print("*** NOW STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid sex of the staff has been entered !!! ~~~")
                                    
                elif ch=='Q':
                    print()
                    print("// Note:- Do not give dot in between while typing the degree of the staff //")
                    q=input("Enter the updated Qualification of the staff (Note:- Bachelor's degree is compulsory): ").upper()
                    if '.' in q:
                        q=q.replace('.','')
                    sch[j][2]=q
                    print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='G':
                    print()
                    g=input("Enter the updated Grade of the staff as either RECEPTIONIST, CLERK, HEAD CLERK, OFFICE SUPERINTENDENT or OFFICE ASSISTANT: ").upper()
                    if g=='RECEPTIONIST' or g=='CLERK' or g=='HEAD CLERK' or g=='OFFICE SUPERINTENDENT' or g=='OFFICE ASSISTANT':
                        sch[j][3]=g
                        print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid grade of the staff has been entered !!! ~~~")
                        print("--> Please provide the valid grade of the staff to update the field of the staff's grade __/\__")
                        print()
                        g=input("Enter the updated Grade of the staff as either RECEPTIONIST, CLERK, HEAD CLERK, OFFICE SUPERINTENDENT or OFFICE ASSISTANT: ").upper()
                        if g=='RECEPTIONIST' or g=='CLERK' or g=='HEAD CLERK' or g=='OFFICE SUPERINTENDENT' or g=='OFFICE ASSISTANT':
                            sch[j][3]=g
                            print("*** NOW STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid grade of the staff has been entered !!! ~~~")
                            
                elif ch=='M':
                    print()
                    print("// Note:- Mobile/Phone number must be of 10 digits of numeric type (without ISD code) //")
                    m=int(input("Enter the updated Mobile/Phone Number of the staff: +91 "))
                    if len(str(m))==10:
                        sch[j][19]=m
                        print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid mobile/phone number of the staff has been entered !!! ~~~")
                        print("--> Please provide the valid mobile/phone number of the staff to update the field of the staff's mobile/phone number __/\__")
                        print()
                        print("// Note:- Mobile/Phone number must be of 10 digits of numeric type (without ISD code) //")
                        m=int(input("Enter the updated Mobile/Phone Number of the staff: +91 "))
                        if len(str(m))==10:
                            sch[j][19]=m
                            print("*** NOW STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid mobile/phone number of the staff has been entered !!! ~~~")
                    
                elif ch=='E':
                    print()
                    e=input("Enter the updated Email Address of the staff: ")
                    if '@' and '.com' in e:
                        sch[j][20]=e
                        print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Staff's email address doesn't contain '@' or '.com' !!! ~~~")
                        print("--> Please provide the proper email address of the staff to update the field of the staff's email address __/\__")
                        print()
                        e=input("Enter the updated Email Address of the staff: ")
                        if '@' and '.com' in e:
                            sch[j][20]=e
                            print("*** NOW STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Staff's email address doesn't contain '@' or '.com' !!! ~~~")
                            
                elif ch=='A':
                    print()
                    a=input("Enter the updated House Address of the staff: ")
                    sch[j][21]=a
                    print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='R':
                    print()
                    print("// Note:- Aadhaar number must be of 12 digits of numeric type \\")
                    r=int(input("Enter the updated Aadhaar Number of the staff: "))
                    if len(str(r))==12:
                        sch[j][22]=r
                        print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid aadhaar number of the staff has been entered !!! ~~~")
                        print("--> Please provide the valid aadhaar number of the staff to update the field of the staff's aadhaar number __/\__")
                        print()
                        print("// Note:- Aadhaar number must be of 12 digits of numeric type \\")
                        r=int(input("Enter the updated Aadhaar Number of the staff: "))
                        if len(str(r))==12:
                            sch[j][22]=r
                            print("*** NOW STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid aadhaar number of the staff has been entered !!! ~~~")
                            
                elif ch=='P':
                    print()
                    print("// Note:- Permanent Account Number (PAN) must be of 10 digits of alpha-numeric type \\")
                    p=input("Enter the updated PAN Number of the staff: ")
                    if len(p)==10:
                        sch[j][23]=p
                        print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid PAN number of the staff has been entered !!! ~~~")
                        print("--> Please provide the valid PAN number of the staff to update the field of the staff's PAN number __/\__")
                        print()
                        print("// Note:- Permanent Account Number (PAN) must be of 10 digits of alpha-numeric type \\")
                        p=input("Enter the updated PAN Number of the staff: ")
                        if len(p)==10:
                            sch[j][23]=p
                            print("*** NOW STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid PAN number of the staff has been entered !!! ~~~")
                            
                elif ch=='C':
                    print()
                    c=input("Enter the updated Customer ID Number of the staff: ")
                    sch[j][24]=c
                    print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='F':
                    print()
                    print("// Note:- Indian Financial System Code (IFSC Code) must be of 11 digits of alpha-numeric type \\")
                    f=input("Enter the updated IFSC Code of the staff: ")
                    if len(f)==11:
                        sch[j][25]=f
                        print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid IFSC Code of the staff has been entered !!! ~~~")
                        print("--> Please provide the valid IFSC Code of the staff to update the field of the staff's IFSC Code __/\__")
                        print()
                        print("// Note:- Indian Financial System Code (IFSC Code) must be of 11 digits of alpha-numeric type \\")
                        f=input("Enter the updated IFSC Code of the staff: ")
                        if len(f)==11:
                            sch[j][25]=f
                            print("*** NOW STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid IFSC Code of the staff has been entered !!! ~~~")
                            
                elif ch=='I':
                    print()
                    print("// Note:- Magnetic Ink Character Recognition Code (MICR Code) must be of 9 digits of numeric type \\")
                    i=int(input("Enter the updated MICR Code of the staff: "))
                    if len(str(i))==12:
                        sch[j][26]=i
                        print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid MICR Code of the staff has been entered !!! ~~~")
                        print("--> Please provide the valid MICR Code of the staff to update the field of the staff's MICR Code __/\__")
                        print()
                        print("// Note:- Magnetic Ink Character Recognition Code (MICR Code) must be of 9 digits of numeric type \\")
                        i=int(input("Enter the updated MICR Code of the staff: "))
                        if len(str(i))==12:
                            sch[j][26]=i
                            print("*** NOW STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid MICR Code of the staff has been entered !!! ~~~")
                            
                elif ch=='ACNT':
                    print()
                    acnt=input("Enter the updated Account Number of the staff: ")
                    sch[j][27]=acnt
                    print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='BBN':
                    print()
                    bbn=input("Enter the updated branch Name of the bank: ")
                    sch[j][28]=bbn
                    print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='BBT':
                    print()
                    print("// Note:- Telephone number (Toll-Free Number) must be of 10 or 11 digits of numeric type //")
                    bbt=int(input("Enter the updated branch Telephone Number of the bank: "))
                    if len(str(bbt))==10 or len(str(bbt))==11:
                        sch[j][29]=bbt
                        print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid telephone number of the bank's branch has been entered !!! ~~~")
                        print("--> Please provide the valid telephone number of the bank's branch to update the field of the bank's branch telephone number __/\__")
                        print()
                        print("// Note:- Telephone number (Toll-Free Number) must be of 10 or 11 digits of numeric type //")
                        bbt=int(input("Enter the updated branch Telephone Number of the bank: "))
                        if len(str(bbt))==10 or len(str(bbt))==11:
                            sch[j][29]=bbt
                            print("*** NOW STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid telephone number of the bank's branch has been entered !!! ~~~")
                            
                elif ch=='BBA':
                    print()
                    bba=input("Enter the updated branch Address of the bank: ")
                    sch[j][30]=bba
                    print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='BBE':
                    print()
                    bbe=input("Enter the updated branch Email Address: ")
                    if '@' and '.com' in e:
                        sch[j][31]=bbe
                        print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Bank's branch email address doesn't contain '@' or '.com' !!! ~~~")
                        print("--> Please provide the proper email address of the bank's branch to update the field of the bank's branch email address __/\__")
                        print()
                        bbe=input("Enter the updated branch Email Address of the bank: ")
                        if '@' and '.com' in bbe:
                            sch[j][31]=bbe
                            print("*** NOW STAFF'S RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** STAFF'S RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Bank's branch email address doesn't contain '@' or '.com' !!! ~~~")
                    
                else:
                    print()
                    print("*** ID NUMBER OF THE STAFF HAS BEEN MATCHED BUT YOU HAVE ENTERED WRONG CHOICE FROM THE STAFF UPDATE MENU !!! ***")
                    print("--> Please provide the appropriate choice to update the staff's detail __/\__")
                
                found=True
                pickle.dump(sch,f)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                ans=input("Press 'o/O' to update any other detail of the staff: ")
                
     if found==False:
        print("*** STAFF'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the staff to update the staff's details __/\__")
     
     print()
     ans=input("Press 'u/U' to update more staff's record: ")
     print()
    f.close()
    
    
def DEL_GROUP_A_STAFF_REC():
    SCH={}
    f=open("SMS_GROUP_A_STAFF.dat","rb+")
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
    ans='r'
    while ans.lower()=='r':
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("############################################# DELETE STAFF'S RECORD #############################################")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     ID=int(input("Enter the ID number of the staff, to be search and to delete or remove the staff's record: "))
     found=False
     for k in sch:
        if k!=ID:
            found=True
            SCH[k]=sch[k]
            pickle.dump(SCH,f)
     
     if found==False:
        print("*** STAFF'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the staff to delete or remove the staff's record __/\__")
     else:
        print("*** STAFF'S RECORD HAS BEEN SUCCESSFULLY DELETED !!! ***")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
     print()
     ans=input("Press 'r/R' to delete or remove more staff's record: ")
     print()
    f.close()
    
    
def DISP_PART_GROUP_A_STAFF_REC():
    f=open('SMS_GROUP_A_STAFF.dat','rb')
    sch={}
    while True:
        try:
            sch=pickle.load(f)
        except EOFError:
            break
        
    ans='d'
    while ans.lower()=='d':
     ID=int(input("Enter the ID number of the staff to display the Staff's SALARY SLIP and Staff's BANK DETAILS: "))
     print()
     found=False
     for j in sch:
        if j==ID:
            print("-------------------------------------------------------------------")
            print("%%%%%%%%%%%%%%%%%%%%%%% STAFF'S SALARY SLIP %%%%%%%%%%%%%%%%%%%%%%%")
            print("-------------------------------------------------------------------")
            print("Staff's Unique ID Number: ",j)
            print("Staff's Full Name: ",sch[j][0])
            print("Staff's Father's Name: ",sch[j][32])
            print("Staff's Mother's Name: ",sch[j][33])
            print("Staff's Spouse's Name: ",sch[j][34])
            print("Staff's Guardian's Name: ",sch[j][35])
            print("Staff's relation with the guardian of the staff: ",sch[j][36])
            print("Staff's Working Subject: ",sch[j][1])
            print("Staff's Qualification(degree): ",sch[j][2])
            print("Staff's Grade: ",sch[j][3])
            print("Staff's Sex: ",sch[j][5])
            print("Staff's DOB: ",sch[j][4])
            print("Staff's Age: ",sch[j][9])
            print("Staff's Mobile/Phone Number: +91",sch[j][19])
            print("Staff's Aadhaar Number: ",sch[j][22])
            print("Staff's PAN Number: ",sch[j][23])
            print("Staff's Email Address: ",sch[j][20])
            print("Staff's House Address: ",sch[j][21])
            print("Staff's Monthly DA: Rs.",sch[j][12])
            print("Staff's Annual DA: Rs.",sch[j][16])
            print("Staff's Monthly MA: Rs.",sch[j][13])
            print("Staff's Annual MA: Rs.",sch[j][17])
            print("Staff's Monthly HRA: Rs.",sch[j][14])
            print("Staff's Annual HRA: Rs.",sch[j][18])
            print("Staff's Monthly income: Rs.",sch[j][11])
            print("Staff's Annual income: Rs.",sch[j][6])
            print("Staff's Monthly PF: Rs.",sch[j][10])
            print("Staff's Annual PF: Rs.",sch[j][15])
            print("Staff's Total PF: Rs.",sch[j][7])
            print("Year: ",sch[j][8])
            print("-------------------------------------------------------------------")
            found=True
            
            print("------------------------------------------------------------------")
            print("%%%%%%%%%%%%%%%%%%%%%% STAFF'S BANK DETAILS %%%%%%%%%%%%%%%%%%%%%%")
            print("------------------------------------------------------------------")
            print("Staff's Full Name: ",sch[j][0])
            print("Staff's Customer ID Number: ",sch[j][24])
            print("Staff's IFSC Code: ",sch[j][25])
            print("Staff's MICR Code: ",sch[j][26])
            print("Staff's Account Number: ",sch[j][27])
            print("Bank's Branch Name: ",sch[j][28])
            print("Bank's Branch Telephone Number: ",sch[j][29])
            print("Bank's Branch Address: ",sch[j][30])
            print("Bank's Branch Email Address: ",sch[j][31])
            print("------------------------------------------------------------------")
     
     if found==False:
        print("*** STAFF'S RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the staff to display the Staff's SALARY SLIP and Staff's BANK DETAILS __/\__")
        
     print()
     ans=input("Press 'd/D' to display more Staff's SALARY SLIP and Staff's BANK DETAILS: ")
     print()
    f.close()