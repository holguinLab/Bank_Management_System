class Banks:
    def __init__(self,id='',bank_name="No Bank Assigned", location="Unknown", number_customers=0):
        self.id =id
        self.bank_name = bank_name
        self.location = location
        self.numbers_customers=number_customers
    def __str__(self):
        return f'Code : {self.id}\nName : {self.bank_name}\nLocation: {self.location}\nCustomers :{self.numbers_customers}'

class Bank_Accounts(Banks):
    def __init__(self,id:int,name:str,pin:int,user:str,):
        super().__init__()
        self.id = id
        self.user = user
        self.pin = pin
        self.id = id
        self.name =name
        self.last_name=''
        self.address=''
        self.tel = ''
        self.email= ''
        self.balance = 0
    def __str__(self):
        return f'Code : {self.id}\nName : {self.name}\nUser :{self.user}\nPin : {self.pin}\nbank : {self.bank_name}'
    
    def see_balance(self):
        return self.balance

    def transfer_money(self,c):
        self.balance = self.balance + c
    
    def withdraw_money(self,c):
        self.balance = self.balance - c
    
    def asing_bank(self,bank:object):
        self.bank_name = bank

    def complete_information(self):
        return f'''
    \n
    Codigo : {self.id}
    Username : {self.user}
    Pin : {self.pin}
    Name : {self.name}
    Last Name : {self.last_name}
    Address : {self.address}
    Tel : {self.tel}
    Email : {self.email}
    Current Balance : {self.balance}
    Partner Bank  : {self.bank_name}
    '''

