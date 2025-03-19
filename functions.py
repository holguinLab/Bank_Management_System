import classes
from random import choice,shuffle

list_accounts=[]
banks =[]

def clear():
    import os
    import platform
    
    if platform.system() == "Windows":
        os.system("cls")  
    else:
        os.system("clear")  

def press_key():
    input(' \n\n📢 press key to continue ...')
    clear()

def main_menu():
    menu = '''
    1️⃣ select 1 to go to the creation banks menu 
    2️⃣ select 2 to go to the creation accounts menu
    3️⃣ select 3 to go exit
    '''
    clear()
    print(menu)
    while(True):
        try:
            option= int(input('Here : '))
            if option == 1:
                clear()
                creations_banks()
                break
            elif option == 2:
                clear()
                accounts()
                break
            elif option == 3 :
                print('See you soon 👋')
                break
            else:
                clear()
                print('❌ ERROR : Select 1 or 2 \n',menu)
        except ValueError as e:
            clear()
            print(e,'\n ❌ It must be a number not a string, Select 1 or 2 \n',menu)

def creations_banks():
    ids = 1
    menu = '''
            Menu Banks
    1️⃣ .select 1 to add new bank
    2️⃣ .select 2 to edit bank
    3️⃣ .select 3 to remove bank
    4️⃣ .select 4 to see all banks
    5️⃣ .select 5 to exit menu
    
    '''
    clear()
    while(True):
        try:
            print(menu)
            option = int(input('Here : '))
            if option == 1:
                clear()
                while(True):
                    id = ids
                    bank_name= input('What is the name of the bank? : ')
                    location=input('What is the location of the bank? : ')
                    number_customers = input('How many members the bank has? : ')
                    # add to list
                    if not bank_name == '' and not location == '' and not number_customers == '':
                        new_bank = classes.Banks(id,bank_name,location,number_customers)
                        banks.append(new_bank)
                        ids += 1 
                        clear()
                        print(' ✅ Correctly Aggregated Bank')
                        press_key()
                        break
                    else:
                        clear()
                        print('\n ❌ ERROR : null fields are not allowed\n')
            elif option == 2:
                if banks:
                    clear()
                    for bank in banks:
                        print(f'{bank}\n----------\n')
                    try:
                        consult =  int(input('\nSelect the bank id\nHere:'))
                        for bank in banks :
                            if bank.id == consult:
                                clear()
                                print('✅ Data successfully found\n\n')
                                while(True):
                                    new_bank_name= input('What is the name of the bank? : ')
                                    new_location=input('What is the location of the bank? : ')
                                    new_number_customers = input('How many members the bank has? : ')
                                    if not new_bank_name == '' and not new_location == '' and not new_number_customers == '':
                                        bank.bank_name = new_bank_name
                                        bank.location = new_location
                                        bank.number_customers =new_number_customers
                                        clear()
                                        print('✅ Correctly updated data \n ')
                                        break
                                    else:
                                        clear()
                                        print('\n ❌ ERROR : null fields are not allowed\n')
                            else:
                                clear()
                                print(f' ❌ ERROR: No matching data, select correctly\n')
                    except ValueError as e :
                        clear()
                        print(e,'\n ❌ It must be a number not a string\n' )
                        press_key()
                else:
                    clear()
                    print('❌ no banks added')
                    press_key()
            elif option == 3:
                if banks:
                    clear()
                    for bank in banks:
                        print(f'{bank}\n----------\n')
                    try:
                        consult =  int(input('\nSelect the bank id\nHere:'))
                        for bank in banks :
                            if bank.id == consult:
                                banks.remove(bank)
                                print(' ✅ correctly deleted')
                                break
                        else:
                            clear()
                            print(f' ❌ ERROR: No matching data, select correctly\n')
                    except ValueError as e:
                        clear()
                        print(e,'\n ❌ It must be a number not a string\n' )
                else:
                    clear()
                    print('❌ no banks added')
                    press_key()
            elif option == 4:
                if banks:
                    clear()
                    for bank in banks:
                        print(f'{bank}\n----------\n')
                    press_key()
                else:
                    clear()
                    print('❌ no banks added')
                    press_key()
            elif option == 5:
                main_menu()
                break
            else:
                clear()
                print('\n ❌ select the correct option\n')
                press_key()
        except ValueError as e:
            clear()
            print(e,'\n ❌ It must be a string no a number\n')
            press_key()

def accounts():
    menu = '''
            Menu Accounts
    1️⃣ .select 1 to add new account.
    2️⃣ .select 2 to edit account.
    3️⃣ .select 3 to see all accounts.
    4️⃣ .select 4 to remove account.
    5️⃣ .select 5 to see balance.
    6️⃣ .select 6 to transfer money.
    7️⃣ .select 7 to withdraw money.
    8️⃣ .select 8 to assign bank.
    9️⃣ .select 9 to see complete information.
    🔟 .select 10 to exit menu.
    '''
    ids = 1
    
    while(True):
        try:
            clear()
            print(menu)
            option= int(input('Here : '))

            # Option 1 CREATE ACCOUNTS
            if option == 1 :
                clear()
                id = ids
                name = input('write your name :')
                user = input('write your user :')
                while(name == '' or user == ''):
                    clear()
                    print('\n ❌ ERROR : null fields are not allowed\n')
                    name = input('write your name :')
                    user = input('write your user :')



                run = True
                while(run):
                    clear()
                    pin_generator = input('\nDo you want to use our secure password generator ?\nSelect Y OR N : ').lower()
                    if pin_generator == 'y':
                        pin= pin_generator_security()
                        run=False
                    elif pin_generator == 'n':
                        pin = int(input('\nwrite your pin :'))
                        run=False
                    else:
                        clear()
                        print('\nERROR : Do you want to use our secure password generator ?\nSelect Y OR N ')
                        press_key()


                if not name == '' and not user == '' and not pin == '':
                    clear()
                    new = classes.Bank_Accounts(id,name,pin,user)
                    list_accounts.append(new)
                    print('✅ User successfully added\n')
                    print(f'\nUser :{user}\nPassword genereted : {pin}')
                    press_key()
                    ids += 1
                else:
                    clear()
                    print('\n ❌ ERROR : null fields are not allowed\n')
                    press_key()

            # Option 2 EDIT  ACCOUNTS
            elif option == 2 :
                if list_accounts:
                    clear()
                    for account in list_accounts:
                        print(f'\nList Of Accounts\n\n---------------\n{account}\n---------------')
                    try:
                        consult = int(input('\nSelect account id to edit :'))
                        while(consult == ''):
                            clear()
                            print('❌ No Null')
                            consult = int(input('\nSelect account id to edit :'))
                        for account in list_accounts:
                            if account.id == consult :
                                #data not required 
                                last_name= input('enter your Last name : ')
                                address= input('enter your address : ')
                                tel = input('enter your tel : ')
                                email= input('enter your email : ')
                                
                                #data required
                                user = input('enter your new user : ')
                                name = input('enter your new name : ')
                                
                                while(user == '' or name == ''):
                                    clear()
                                    print('\n ❌ ERROR : null fields are not allowed\n')
                                    user = input('enter your new user : ')
                                    name = input('enter your new name : ')
                                
                                exit = True
                                while(exit):
                                    pin_generator = input('\nWould you like to use our secure password generator to change your pin? ?\nSelect Y OR N : ').lower()
                                    if pin_generator == 'y':
                                        pin = pin_generator_security()
                                        exit = False
                                        
                                    elif pin_generator == 'n':
                                        pin = int(input('\nwrite your new pin :'))
                                        exit = False
                                        
                                    else:
                                        clear()
                                        print('\n ❌ ERROR : Select Y OR N\n')
                                        press_key()
                            else:
                                clear()
                                print(f' ❌ ERROR: No matching data, select correctly\n')
                                press_key()

                            if not name == '' and not user == '' and not pin == '':
                                account.name = name
                                account.user = user
                                account.pin = pin
                                account.last_name = last_name
                                account.address = address
                                account.tel =  tel
                                account.email = email
                                clear()
                                print('✅ Correctly updated data \n ')
                                print(f'\nUser :{user}\nPassword genereted : {pin}')
                                press_key()
                            else:
                                clear()
                                print('\n ❌ ERROR : the pin , user and name fields cannot be empty\n')
                                press_key()
                    except ValueError as e :
                            clear()
                            print(e,'\n ❌ It must be a number not a string\n' )
                            press_key()
                else:
                    clear()
                    print('❌ no accounts added')
                    press_key()
            
            # Option 3 LIST ACCOUNTS
            elif option == 3 :
                if list_accounts:
                    clear()
                    for account in list_accounts:
                        print(f'\n--------------\n{account}\n---------------\n')
                    press_key()
                else:
                    clear()
                    print('❌ no accounts added')
                    press_key()


            # Option 4 REMOVE ACCOUNTS
            elif option == 4 :
                if list_accounts:
                    for account in list_accounts:
                        print(f'\n--------------\n{account}\n---------------\n')
                    try:
                        consult = int(input('Select account id : '))
                        for account in list_accounts:
                            if account.id == consult:
                                list_accounts.remove(account)
                                print(' ✅ correctly deleted')
                                press_key()
                                break # exit for 
                        else:
                            clear()
                            print(f' ❌ ERROR: No matching data, select correctly\n')
                            press_key()
                    except ValueError as e:
                        clear()
                        print(e,'\n ❌ It must be a string no a number\n')
                        press_key()
                else:
                    clear()
                    print('❌ no accounts added')
                    press_key()

            # Option 5 SEE BALANCE
            elif option == 5 :
                if list_accounts:
                    for account in list_accounts:
                        print(f'\n--------------\n{account}\n---------------\n')
                    try:
                        consult = int(input('Select account id : '))
                        for account in list_accounts:
                            if account.id == consult:
                                clear()
                                print(f'Hello {account.name}\nYour current balance is  : $ {account.see_balance()}')
                                press_key()
                                break # exit  for
                        else:
                            clear()
                            print(f' ❌ ERROR: No matching data, select correctly\n')
                            press_key()
                    except ValueError as e:
                        clear()
                        print(e,'\n ❌ It must be a string no a number\n')
                        press_key()
                else:
                    clear()
                    print('❌ no accounts added')
                    press_key()

            # Option 6 TRANSFER MONEY
            elif option == 6 :
                if list_accounts:
                    clear()
                    for account in list_accounts:
                        print(f'\n--------------\n{account}\n---------------\n')
                    try:
                        consult = int(input('Select account id : '))
                        for account in list_accounts:
                            if account.id == consult:
                                clear()
                                print(f'Hello {account.name}\nYour current balance is  : $ {account.see_balance()}')
                                new_balance = int(input('\nType the amount you want to add : '))
                                account.transfer_money(new_balance)
                                print('\n✅ money successfully added Agregado')
                                press_key()
                                break # exit  for
                        else:
                            clear()
                            print(f' ❌ ERROR: No matching data, select correctly\n')
                            press_key()
                    except ValueError as e:
                        clear()
                        print(e,'\n ❌ It must be a string no a number\n')
                        press_key()
                else:
                    clear()
                    print('❌ no accounts added')
                    press_key()
            
            # Option 7 WITHDRAW MONEY 
            elif option == 7 :
                if list_accounts:
                    clear()
                    for account in list_accounts:
                        print(f'\n--------------\n{account}\n---------------\n')
                    try:
                        consult = int(input('Select account id : '))
                        for account in list_accounts:
                            if account.id == consult:
                                clear()
                                print(f'Hello {account.name}\nYour current balance is  : $ {account.see_balance()}')
                                new_balance = int(input('\nEnter the amount to be withdrawn : '))
                                account.withdraw_money(new_balance)
                                print('\n✅ money successfully withdrawn ')
                                press_key()
                                break # exit  for
                        else:
                            clear()
                            print(f' ❌ ERROR: No matching data, select correctly\n')
                            press_key()
                    except ValueError as e:
                        clear()
                        print(e,'\n ❌ It must be a string no a number\n')
                        press_key()
                else:
                    clear()
                    print('❌ no accounts added')
                    press_key()

            # Option 8 ASSIGN BANK
            elif option == 8 :
                if list_accounts:
                    clear()
                    for account in list_accounts:
                        print(f'\n--------------\n{account}\n---------------\n')
                    try:
                        consult = int(input('Select account id : '))
                        clear()
                        if banks:
                            for bank in banks:
                                print(f'\n--------------\n{bank}\n---------------\n')
                            consult2 = int(input('Select bank id :'))
                        else:
                            clear()
                            print('❌ no banks added')
                            press_key()
                        for account in list_accounts:
                            for bank in banks:
                                if account.id == consult and bank.id == consult2:
                                    clear()
                                    account.asing_bank(bank.bank_name)
                                    print(f'Hello {account.name}\nYour  current bank is   : {account.bank_name}')
                                    print('\n✅ Bank Successfully Assigned ')
                                    press_key()
                                    break # exit  for
                            break
                        else:
                            clear()
                            print(f' ❌ ERROR: No matching data, select correctly\n')
                            press_key()
                    except ValueError as e:
                        clear()
                        print(e,'\n ❌ It must be a string no a number\n')
                        press_key()
                else:
                    clear()
                    print('❌ no accounts added')
                    press_key()
            
            # Option 9 COMPLETE INFORMATION
            elif option == 9 :
                if list_accounts:
                    clear()
                    for account in list_accounts:
                        print(f'\n--------------\n{account}\n---------------\n')
                    try:
                        consult = int(input('Select account id : '))
                        for account in list_accounts:
                            if account.id == consult:
                                clear()
                                print(f'Hello {account.name}\nYour Information Complete is :{account.complete_information()}')
                                press_key()
                                break # exit  for
                        else:
                            clear()
                            print(f' ❌ ERROR: No matching data, select correctly\n')
                            press_key()
                    except ValueError as e:
                        clear()
                        print(e,'\n ❌ It must be a string no a number\n')
                        press_key()
                else:
                    clear()
                    print('❌ no accounts added')
                    press_key()
            
            # Option 10 EXIT MENU
            elif option == 10 :
                main_menu()
                break


        except ValueError as e:
            clear()
            print(e,'\n ❌ It must be a number not a string\n' )

def pin_generator_security(): 
    password=[]
    dic = {
        'lowercase ' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        'special' :['!', '@', '#', '$', '%', '*', '-', '_', '=', '+',  '/','?' ],
        'uppercase' : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    }
    while(True):
        try:
            clear()
            lower = int(input('Enter the number of lower case letters : '))
            special = int(input('type the number of special characters: '))
            upper =int(input('Enter the number of upper case letters : '))
            if not lower == '' and not special == '' and not upper == '':
                clear()
                for i in range(lower):
                    password.append(choice(dic['lowercase ']))
                for i in range(special):
                    password.append(choice(dic['special']))
                for i in range(upper):
                    password.append(choice(dic['uppercase']))
                shuffle(password)
                print(f'\nPassword genereted : {"".join(password)}')
                while(True):
                    q = input('\nDo you want to generate a new password ?\nSelect Y OR N : ').lower()
                    if q == 'y':
                        clear()
                        password.clear()
                        for i in range(lower):
                            password.append(choice(dic['lowercase ']))
                        for i in range(special):
                            password.append(choice(dic['special']))
                        for i in range(upper):
                            password.append(choice(dic['uppercase']))
                        shuffle(password)
                        print(f'\nPassword genereted : {"".join(password)}')
                    elif q == 'n':
                        return ''.join(password)
                    else:
                        clear()
                        print('\n ❌ ERROR : Select Y OR N\n')
                        press_key()
            else:
                clear()
                print('\n ❌ ERROR : null fields are not allowed\n')
        except ValueError as e:
            clear()
            print(e,'\n ❌ It must be a number not a string\n' )
            press_key()


