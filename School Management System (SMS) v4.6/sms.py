import stdiomask

un=input("Enter Username: ").upper()
pw=stdiomask.getpass("Enter Password: ")
if un=='SV_INT_SCHOOL' and pw=='svintschlms2021':
    print('''                         ************************        
                       *        WELCOME TO        *     
                     *    SV INTERNATIONAL SCHOOL    *
                   *                                    *
                   ---------------        ----------------
                   |\             \      /              /|
                   | \     /\      \    /      /\      / | 
                   |  \___/oo\______\  /______/oo\____/  |
                   |  /             /  \              \  | 
                   | /             /    \              \ |
                   |/             /      \              \|
                   ---------------        ----------------''')
else:
    print("Invalid username and password !!!")                                        