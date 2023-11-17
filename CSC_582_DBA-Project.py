import oracledb

#connect to the Oracle database
username= input("Enter the username\n")
password= input("Enter the password to connect\n")
dsn = "oracle.csep.umflint.edu:1521/csep"
choose = 1

connection = oracledb.connect(username+'/'+password+'@oracle.csep.umflint.edu:1521/csep')
print("Connection with database is successful !!")

#print("Make sure VPN is connected before proceeding further")
    

print("-----------------------------------------------------------")

#To execute sql statements
cursor = connection.cursor()

def create_table():
    try:
        cursor.execute("""
            CREATE TABLE accounts (
                name VARCHAR2(100),
                account_number VARCHAR2(100) PRIMARY KEY,
                balance INT
            )
        """)
        connection.commit()
        create_Account()
        #print("Table Accounts created successfully !!")
    except oracledb.DatabaseError as e:
        error = e.args[0]
        if error.code ==955:
          #print("Accounts table already exists !!")
          create_Account()
          
          

#Account Creation
def create_Account():
    name = input("Enter accountholder's name: ")
    account_number = int(input("Enter account number: "))
    initial_balance = float(input("Enter initial balance to deposit: "))
    try:
       cursor.execute("INSERT INTO accounts (name, account_number, balance) VALUES (:name, :acc_num, :balance)", name=name, acc_num=account_number, balance=initial_balance)
       print("Account created successfully")
    except Exception as e:
       print("Error !!!")
       connection.rollback()
      
    



def check_Balance():
    account_number = int(input("Enter account number: "))
    cursor.execute("SELECT balance FROM accounts WHERE account_number = :acc_num", acc_num = account_number)
    result = cursor.fetchone()
    if result:
        balance = result[0]
        print(f"Balance for account {account_number}: {balance}$")
    else:
        print(f"Account with number {account_number} not found.")
    
def credit():
    account_number = int(input("Enter account number: "))
    amount = float(input("Enter amount to deposit: "))
    cursor.execute("UPDATE accounts SET balance = balance + :amount WHERE account_number = :acc_num",
                    amount=amount, acc_num=account_number)
    print("Amount deposited successfully")

def debit():
    account_number = int(input("Enter account number: "))
    amount = float(input("Enter amount to withdrawl: "))
    cursor.execute("SELECT balance FROM accounts WHERE account_number = :acc_num FOR UPDATE",
                    acc_num=account_number)
    result = cursor.fetchone()
    if result:
        balance = result[0]
        if amount <= balance:
            cursor.execute("UPDATE accounts SET balance = balance - :amount WHERE account_number = :acc_num",
                            amount=amount, acc_num=account_number)
            print("Balance withdrawn successfully")
        else:
            print("Insufficient funds in account")
    else:
        print("Account not found try again")
        

#create_table()
print("Welcome to Banking Application")
#print("-----------------------------------------------------------")
while (choose!=5):
    if (choose <1 or choose >5):
        choose =1
        continue
    print("1. Create Account\n2. Check Balance\n3. Deposit\n4. Withdraw\n5. exit")
    try:
        choose = int(input("Kindly choose the desired action from above: "))
        match choose:
            case 1:
                print("You choose to create account...\n")
                create_table()
            case 2:
                print("You choose to check Balance...\n")
                check_Balance()
            case 3:
                print("You choose to deposit amount...\n")
                credit()
            case 4:
                print("You choose to withdrawl amount...\n")
                debit()
            case 5:
                connection.commit()
                cursor.close()
                connection.close()
                break
    except Exception as e:
          connection.rollback();
          print("Kindly check the inputs provided and try again !!\n")

          
          

print("Thank you.....Have a nice day !!")
        
        
    
        
  
