import school01,school02,school03,school04,school05,school06,school07,school08,stdiomask,pyttsx3,ascii_magic

ans='c'
while ans.lower()=='c':
 print()
 un=input("Enter the Username: ").upper()
 pw=stdiomask.getpass("Enter the Password: ")
 if un=='PC_INT_SCHOOL' and pw=='pcintschlms2023':
  print()
  print('''                    *************************        
                  *         WELCOME TO        *     
                *  PYCODE INTERNATIONAL SCHOOL  *
              *                                   *
            *---------------        ----------------*
            [\ ############{\      /}#############/]
            [+\:::::/\:::::{%\    /%}:::::/\:::::/+] 
            [++\___/OO\____{%%\==/%%}____/OO\___/++]
            [++/((((((((((({%%/==\%%})))))))))))\++]
            [+/::::::::::::{%/    \%}::::::::::::\+]
            [/#############{/      \}#############\]
            ----------------        ----------------''')
  print()
  text_speech=pyttsx3.init()
  a="welcome to school management system of piecode international school"
  text_speech.setProperty("rate",110)
  text_speech.say(a)
  text_speech.runAndWait()
  print()
  output=ascii_magic.from_image_file("images (1).jpg",columns=120,char='@')
  ascii_magic.to_terminal(output)
  print()
  
  ANS='H'
  while ANS.upper()=='H':
    print()
    output=ascii_magic.from_image_file("images.jpg",columns=90,char='@')
    ascii_magic.to_terminal(output)
    print()
    output=ascii_magic.from_image_file("home tab.png",columns=200,char='@')
    ascii_magic.to_terminal(output)
    print()
    print("~~~ HOME PAGE --> MENU ~~~")
    print("# Press 1 to go to the SCIENCE TEACHERS PAGE") 
    print("# Press 2 to go to the COMMERCE TEACHERS PAGE") 
    print("# Press 3 to go to the ARTS TEACHERS PAGE") 
    print("# Press 4 to go to the GROUP-A STAFFS PAGE ") 
    print("# Press 5 to go to the GROUP-B STAFFS PAGE ") 
    print("# Press 6 to go to the STUDENTS FEE PAGE") 
    print("# Press 7 to go to the STUDENTS REPORT CARD PAGE") 
    print("# Press 8 to go to the STUDENTS CCA PAGE ") 
    ch=int(input("Enter your choice from the MENU of HOME PAGE: "))
    
    if ch==1:
        print()
        ANS='Y'
        while ANS.upper()=='Y':
         output=ascii_magic.from_image_file("science teacher tab.png",columns=200,char='@')
         ascii_magic.to_terminal(output)
         print()
         print("~~~ SCIENCE TEACHERS PAGE --> MENU ~~~")
         print("# Press 1 to insert the details of the science teachers")
         print("# Press 2 to compute the salary structure of the science teachers")
         print("# Press 3 to display the record of all science teachers") 
         print("# Press 4 to append the details of the science teachers")
         print("# Press 5 to search the record of the science teachers")
         print("# Press 6 to update the details of the science teachers")
         print("# Press 7 to delete the record of the science teachers")
         print("# Press 8 to display the salary slip and bank details of the particular science teacher")  
         ch=int(input("Enter your choice from the MENU of SCIENCE TEACHERS PAGE: "))
         if ch==1:
            print()
            school01.INSERT_SC_TEACH_REC()  
            print()
         elif ch==2:
            print()
            school01.COMPUTE_SC_TEACH_REC()
            print()
         elif ch==3:
            print()
            school01.DISP_ALL_SC_TEACH_REC()
            print()
         elif ch==4:
            print()
            school01.APPEND_SC_TEACH_REC()
            print()
         elif ch==5:
            print()
            school01.SEARCH_SC_TEACH_REC()
            print()
         elif ch==6:
            print()
            school01.UPDATE_SC_TEACH_REC()
            print()
         elif ch==7:
            print()
            school01.DEL_SC_TEACH_REC()   
            print()
         elif ch==8:
            print()
            school01.DISP_PART_SC_TEACH_REC()
            print()
         else:
            print()
            print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
            print("--> Please provide the appropriate choice to access the MENU of SCIENCE TEACHERS PAGE __/\__")
            print()
         ANS=input("Press 'y/Y' to go to the SCIENCE TEACHERS PAGE or Press 'q/Q' to quit: ")
         print()
         
    elif ch==2:
        print()
        ANS='Y'
        while ANS.upper()=='Y':
         output=ascii_magic.from_image_file("commerce teacher tab.png",columns=200,char='@')
         ascii_magic.to_terminal(output)
         print()
         print("~~~ COMMERCE TEACHERS PAGE --> MENU ~~~")
         print("# Press 1 to insert the details of the commerce teachers")
         print("# Press 2 to compute the salary structure of the commerce teachers")
         print("# Press 3 to display the record of all commerce teachers")
         print("# Press 4 to append the details of the commerce teachers")
         print("# Press 5 to search the record of the commerce teachers")
         print("# Press 6 to update the details of the commerce teachers")
         print("# Press 7 to delete the record of the commerce teachers")
         print("# Press 8 to display the salary slip and bank details of the particular commerce teacher")
         ch=int(input("Enter your choice from the MENU of COMMERCE TEACHERS PAGE: "))
         if ch==1:
           print()
           school02.INSERT_COMM_TEACH_REC()
           print()
         elif ch==2:
           print()
           school02.COMPUTE_COMM_TEACH_REC()
           print()
         elif ch==3:
           print()
           school02.DISP_ALL_COMM_TEACH_REC()
           print()
         elif ch==4:
           print()
           school02.APPEND_COMM_TEACH_REC()
           print()
         elif ch==5:
           print()
           school02.SEARCH_COMM_TEACH_REC()
           print()
         elif ch==6:
           print()
           school02.UPDATE_COMM_TEACH_REC()
           print()
         elif ch==7:
           print()
           school02.DEL_COMM_TEACH_REC()   
           print()
         elif ch==8:
           print()
           school02.DISP_PART_COMM_TEACH_REC()
           print()
         else:
           print()
           print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
           print("--> Please provide the appropriate choice to access the MENU of COMMERCE TEACHERS PAGE __/\__")
           print()
         ANS=input("Press 'y/Y' to go to the COMMERCE TEACHERS PAGE or Press 'q/Q' to quit: ")
         print()
         
    elif ch==3:
        print()
        ANS='Y'
        while ANS.upper()=='Y':
         output=ascii_magic.from_image_file("arts teacher tab.png",columns=200,char='@')
         ascii_magic.to_terminal(output)
         print()
         print("~~~ ARTS TEACHERS PAGE --> MENU ~~~")
         print("# Press 1 to insert the details of the arts teachers")
         print("# Press 2 to compute the salary structure of the arts teachers")
         print("# Press 3 to display the record of all arts teachers")
         print("# Press 4 to append the details of the arts teachers")
         print("# Press 5 to search the record of the arts teachers")
         print("# Press 6 to update the details of the arts teachers")
         print("# Press 7 to delete the record of the arts teachers")
         print("# Press 8 to display the salary slip and bank details of the particular arts teacher")
         ch=int(input("Enter your choice from the MENU of ARTS TEACHERS PAGE: "))
         if ch==1:
           print()
           school03.INSERT_ARTS_TEACH_REC()
           print()
         elif ch==2:
           print()
           school03.COMPUTE_ARTS_TEACH_REC()
           print()
         elif ch==3:
           print()
           school03.DISP_ALL_ARTS_TEACH_REC()
           print()
         elif ch==4:
           print()
           school03.APPEND_ARTS_TEACH_REC()
           print()
         elif ch==5:
           print()
           school03.SEARCH_ARTS_TEACH_REC()
           print()
         elif ch==6:
           print()
           school03.UPDATE_ARTS_TEACH_REC()
           print()
         elif ch==7:
           print()
           school03.DEL_ARTS_TEACH_REC()   
           print()
         elif ch==8:
           print()
           school03.DISP_PART_ARTS_TEACH_REC()
           print()
         else:
           print()
           print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
           print("--> Please provide the appropriate choice to access the MENU of ARTS TEACHERS PAGE __/\__")
           print()
         ANS=input("Press 'y/Y' to go to the ARTS TEACHERS PAGE or Press 'q/Q' to quit: ")
         print()
         
    elif ch==4:
        print()
        ANS='Y'
        while ANS.upper()=='Y':
         output=ascii_magic.from_image_file("group-a staff tab.png",columns=200,char='@')
         ascii_magic.to_terminal(output)
         print()
         print("~~~ GROUP-A STAFFS PAGE --> MENU ~~~")
         print("# Press 1 to insert the details of the group-A staffs")
         print("# Press 2 to compute the salary structure of the group-A staffs")
         print("# Press 3 to display the record of all group-A staffs")
         print("# Press 4 to append the details of the group-A staffs")
         print("# Press 5 to search the record of the group-A staffs")
         print("# Press 6 to update the details of the group-A staffs")
         print("# Press 7 to delete the record of the group-A staffs")
         print("# Press 8 to display the salary slip and bank details of the particular group-A staff")
         ch=int(input("Enter your choice from the MENU of GROUP-A STAFFS PAGE: "))
         if ch==1:
           print()
           school04.INSERT_GROUP_A_STAFF_REC()
           print()
         elif ch==2:
           print()
           school04.COMPUTE_GROUP_A_STAFF_REC()
           print()
         elif ch==3:
           print()
           school04.DISP_ALL_GROUP_A_STAFF_REC()
           print()
         elif ch==4:
           print()
           school04.APPEND_GROUP_A_STAFF_REC()
           print()
         elif ch==5:
           print()
           school04.SEARCH_GROUP_A_STAFF_REC()
           print()
         elif ch==6:
           print()
           school04.UPDATE_GROUP_A_STAFF_REC()
           print()
         elif ch==7:
           print()
           school04.DEL_GROUP_A_STAFF_REC()   
           print()
         elif ch==8:
           print()
           school04.DISP_PART_GROUP_A_STAFF_REC()
           print()
         else:
           print()
           print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
           print("--> Please provide the appropriate choice to access the MENU of GROUP-A STAFFS PAGE __/\__")
           print()
         ANS=input("Press 'y/Y' to go to the GROUP-A STAFFS PAGE or Press 'q/Q' to quit: ")
         print()
         
    elif ch==5:
        print()
        ANS='Y'
        while ANS.upper()=='Y':
         output=ascii_magic.from_image_file("group-b staff tab.png",columns=200,char='@')
         ascii_magic.to_terminal(output)
         print()
         print("~~~ GROUP-B STAFFS PAGE --> MENU ~~~")
         print("# Press 1 to insert the details of the group-B staffs")
         print("# Press 2 to compute the salary structure of the group-B staffs")
         print("# Press 3 to display the record of all group-B staffs")
         print("# Press 4 to append the details of the group-B staffs")
         print("# Press 5 to search the record of the group-B staffs")
         print("# Press 6 to update the details of the group-B staffs")
         print("# Press 7 to delete the record of the group-B staffs")
         print("# Press 8 to display the salary slip and bank details of the particular group-B staff")
         ch=int(input("Enter your choice from the MENU of GROUP-B STAFFS PAGE: "))
         if ch==1:
           print()
           school05.INSERT_GROUP_B_STAFF_REC()
           print()
         elif ch==2:
           print()
           school05.COMPUTE_GROUP_B_STAFF_REC()
           print()
         elif ch==3:
           print()
           school05.DISP_ALL_GROUP_B_STAFF_REC()
           print()
         elif ch==4:
           print()
           school05.APPEND_GROUP_B_STAFF_REC()
           print()
         elif ch==5:
           print()
           school05.SEARCH_GROUP_B_STAFF_REC()
           print()
         elif ch==6:
           print()
           school05.UPDATE_GROUP_B_STAFF_REC()
           print()
         elif ch==7:
           print()
           school05.DEL_GROUP_B_STAFF_REC()   
           print()
         elif ch==8:
           print()
           school05.DISP_PART_GROUP_B_STAFF_REC()
           print()
         else:
           print()
           print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
           print("--> Please provide the appropriate choice to access the MENU of GROUP-B STAFFS PAGE __/\__")
           print()
         ANS=input("Press 'y/Y' to go to the GROUP-B STAFFS PAGE or Press 'q/Q' to quit: ")
         print()
         
    elif ch==6:
        print()
        ANS='Y'
        while ANS.upper()=='Y':
         output=ascii_magic.from_image_file("student fees tab.png",columns=200,char='@')
         ascii_magic.to_terminal(output)
         print() 
         print("~~~ STUDENTS FEE PAGE --> MENU ~~~")
         print("# Press 1 to insert the details of the students")
         print("# Press 2 to compute the fee structure of the students")
         print("# Press 3 to display the record of all students")
         print("# Press 4 to append the details of the students")
         print("# Press 5 to search the record of the students")
         print("# Press 6 to update the details of the students")
         print("# Press 7 to delete the record of the students")
         print("# Press 8 to display the fee slip of the particular student")
         ch=int(input("Enter your choice from the MENU of STUDENTS FEE PAGE: "))
         if ch==1:
            print()
            school06.INSERT_STU_REC()
            print()
         elif ch==2:
            print()
            school06.COMPUTE_STU_FEE()
            print()
         elif ch==3:
            print()
            school06.DISP_ALL_STU_REC()
            print()
         elif ch==4:
            print()
            school06.APPEND_STU_REC()
            print()
         elif ch==5:
            print()
            school06.SEARCH_STU_REC()
            print()
         elif ch==6:
            print()
            school06.UPDATE_STU_REC()
            print()
         elif ch==7:
            print()
            school06.DEL_STU_REC()   
            print()
         elif ch==8:
            print()
            school06.DISP_PART_STU_REC()
            print()
         else:
           print()
           print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
           print("--> Please provide the appropriate choice to access the MENU of STUDENTS FEE PAGE __/\__")
           print()
         ANS=input("Press 'y/Y' to go to the STUDENTS FEE PAGE or Press 'q/Q' to quit: ")
         print()
         
    elif ch==7:
        print()
        ANS='Y'
        while ANS.upper()=='Y':
         output=ascii_magic.from_image_file("student report card tab.png",columns=200,char='@')
         ascii_magic.to_terminal(output)
         print() 
         print("~~~ STUDENTS REPORT CARD PAGE --> MENU ~~~")
         print("# Press 1 to insert the details of the students")
         print("# Press 2 to compute the Report Card of the students")
         print("# Press 3 to append the details of the students")
         print("# Press 4 to search the record of the students")
         print("# Press 5 to update the details of the students")
         print("# Press 6 to delete the record of the students")
         print("# Press 7 to display the report card of the particular student")
         ch=int(input("Enter your choice from the MENU of STUDENTS REPORT CARD PAGE: "))
         if ch==1:
          print()
          school07.INSERT_STU_REC()
          print()
         elif ch==2:
          print()
          school07.COMPUTE_STU_RC()
          print()
         elif ch==3:
          print()
          school07.APPEND_STU_REC()
          print()
         elif ch==4:
          print()
          school07.SEARCH_STU_REC()
          print()
         elif ch==5:
          print()
          school07.UPDATE_STU_REC()
          print()
         elif ch==6:
          print()
          school07.DEL_STU_REC()   
          print()
         elif ch==7:
          print()
          school07.DISP_PART_STU_REC()
          print()
         else:
           print()
           print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
           print("--> Please provide the appropriate choice to access the MENU of STUDENTS REPORT CARD PAGE __/\__")
           print()
         ANS=input("Press 'y/Y' to go to the STUDENTS REPORT CARD PAGE or Press 'q/Q' to quit: ")
         print()
         
    elif ch==8:
        print()
        ANS='Y'
        while ANS.upper()=='Y':
         output=ascii_magic.from_image_file("student cca tab.png",columns=200,char='@')
         ascii_magic.to_terminal(output)
         print()
         print("~~~ STUDENTS CCA PAGE --> MENU ~~~")
         print("# Press 1 to insert the details of the students")
         print("# Press 2 to display the result of the students in co-curicular activites, self awarness and in health status")
         ch=int(input("Enter your choice from the MENU of STUDENTS CCA PAGE: "))
         if ch==1:
          print()
          school08.INSERT_STU_REC()
          print()
         elif ch==2:
          print()
          school08.DISPLAY_co_curi()
          print()
         else:
           print()
           print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
           print("--> Please provide the appropriate choice to access the MENU of STUDENTS CCA PAGE __/\__")
           print()
         ANS=input("Press 'y/Y' to go to the STUDENTS CCA PAGE or Press 'q/Q' to quit: ")
         print()   
          
    else:
        print()
        print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
        print("--> Please provide the appropriate choice to access the MENU of HOME PAGE __/\__")
        print()
        
    print()
    output=ascii_magic.from_image_file("school-icon.png",columns=120,char='@')
    ascii_magic.to_terminal(output)
    print()
    ANS=input("Press 'h/H' to go to the HOME PAGE or Press 'q/Q' to quit: ")
    print()
    if ANS.lower()=='q':
      print()
      print('****************************************************************************************************************')
      print('''                                    THANK YOU FOR USING PYCODE INTERNATIONAL SCHOOL MANAGEMENT SYSTEM _/\_,
                                                                    PLEASE VISIT AGAIN....''')
      print('****************************************************************************************************************')
      text_speech=pyttsx3.init()
      a="Thank you for using school management system of piecode international school, please visit again"
      text_speech.setProperty("rate",110)
      text_speech.say(a)
      text_speech.runAndWait()
      print()
      output=ascii_magic.from_image_file("how-to-respond-to-thank-you.webp",columns=150,char='@')
      ascii_magic.to_terminal(output)
      print()
 
 elif un=='PC_INT_SCHOOL' and pw!='pcintschlms2023':
    print("~~ Access denied !!! ,invalid password has been entered ~~")
    text_speech=pyttsx3.init()
    a="Access denied, invalid password has been entered, please provide the valid and correct authorised credentials to access the account"
    text_speech.setProperty("rate",110)
    text_speech.say(a)
    text_speech.runAndWait()
    print()
 
 elif un!='PC_INT_SCHOOL' and pw=='pcintschlms2023':
    print("~~ Access denied !!! ,invalid username has been entered ~~")
    text_speech=pyttsx3.init()
    a="Access denied, invalid username has been entered, please provide the valid and correct authorised credentials to access the account"
    text_speech.setProperty("rate",110)
    text_speech.say(a)
    text_speech.runAndWait()
    print()
 
 else:
    print("~~ Access denied !!! ,invalid username and password has been entered ~~")
    text_speech=pyttsx3.init()
    a="Access denied, invalid username and password has been entered, please provide the valid and correct authorised credentials to access the account"
    text_speech.setProperty("rate",110)
    text_speech.say(a)
    text_speech.runAndWait()
    print()
    
 ans=input("Press 'c/C' to continue to run the SMS or Press 'e/E' to exit: ")
 print()
