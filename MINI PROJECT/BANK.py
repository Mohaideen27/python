class Bank:
    bankname='SBI'
    branch='VADA'
    ifsc='SBIN000143'
    def __init__(self, name, account_no, pin, initial_balance):
        self.name=name
        self.__account_no=account_no
        self.__pin=pin
        self.__inital_balance=initial_balance
        self.last_transaction='NO TRANSACTION YET DONE'
        #----------------private methods--------------
    def __authenticate(self):
        account=int(input('enter account_no: '))
        pin=int(input('enter pin: '))
        return self.__account_no==account and self.__pin==pin
    def __generate_receipt(self,type,amount):
        return f'''
                -----------TRANCATION RECEIPT----------
                Bank name           :{Bank.bankname}
                Branch              :{Bank.branch}
                Acc Holder          :{self.name}
                Transaction Type    :{type}
                Amount              :₨. {amount}
                Available balance   :₨. {self.__inital_balance}
        '''
    def __deposit(self, amount):
        self.__inital_balance+=amount
    def __withdraw(self, amount):
        self.__inital_balance-=amount
    def deposit_money(self):
        if self.__authenticate():
            amount=int(input('enter deposit amount: '))
            if amount>0:
                self.__deposit(amount)
                self.last_transaction=self.__generate_receipt('DEPOSIT',amount)
                print('Amount Deposit successful')
            else:
                print('Invalid amount')
         else:
            print('Authentication failed')
    def withdraw_money(self):
        if self.__authenticate():
            amount=int(input('enter withdraw amount: '))
            if amount>0 and amount<=self.__inital_balance:
                self.__withdraw(amount)
                self.last_transaction=self.__generate_receipt('WITHDRAW', amount)
                print('Withdraw successfull')
            else:
                print('Authentication failed')
    def show_balance(self):
        if self.__authenticate():
            print(f'Current Balance        :₨. {self.__inital_balance}')
        else:
            print('Authentication failed')
    def show_details(self):
        print(f'''  Bank name           :{Bank.bankname}
                    Branch              :{Bank.branch}
                    IFSC                :{Bank.ifsc}
                    Acc holder          :{self.name}
                    Available Balance   :₨. {self.__inital_balance}''')
        