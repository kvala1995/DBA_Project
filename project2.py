import oracledb

# Connect #connect to the Oracle database
username= input("Enter the username\n")
password= input("Enter the password to connect\n")
dsn = "oracle.csep.umflint.edu:1521/csep"
try:
   connection = oracledb.connect(username+'/'+password+'@oracle.csep.umflint.edu:1521/csep')
except:
    print("Make sure VPN is connected before proceeding further")
    
print("Connection with database is successful !!")
print("-----------------------------------------------------------")

#To execute sql statements
cursor = connection.cursor()

def create_table():
    try:
        cursor.execute("""
            CREATE TABLE accounts (
                name VARCHAR2(100),
                account_number VARCHAR2(100),
                balance INT
            )
        """)
        connection.commit()
        print("Table Accounts created successfully !!")
    except:
        print("Accounts table already exists !!")

#Account Creation
def create_Account():
    name = input("Enter accountholder's name: ")
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance to deposit: "))
    cursor.execute("INSERT INTO accounts (name, account_number, balance) VALUES (:name, :acc_num, :balance)", name=name, acc_num=account_number, balance=initial_balance)
    print("Account created successfully")

def check_Balance():
    
    cursor.execute("SELECT balance FROM accounts WHERE account_number = :acc_num", acc_num = account_number)
        

#create_table()
print("Welcome to Banking Application")
#print("-----------------------------------------------------------")
print("1. Create Account\n2. Check Balance\n3. Deposit\n4. Withdraw\n")
try:
    choose = input("Kindly choose the desired action from above: ")
    match choose:
        case "1":
            print("You choose to create account...\n")
            create_Account()
        case "2":
            print("You choose to check Balance...\n")
            check_Balance()
except:
    print("Kindly check the inputs provided and try again !!")
        
        
    
        
  
