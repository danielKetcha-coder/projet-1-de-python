import time
import os

print("\n ###############################################################################\n")
print("\n                   WELCOME TO SKAW'S INVENTORY SYSTEM \n")
print("\n ################################################################################\n") 

users = { }

def load_user():
    global users
    if not os.path.exists("users.txt"):
        open('users.txt', "w").close()
    with open("users.txt", "r") as f:
        for line in f:
            if not line:
                continue
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue
            email = parts[0].lower()
            username = parts[1].upper()
            pw = parts[2]
           
            users[email] = {"Username" : username, "Password" : pw}
    return users
users = load_user()
    


def regis():
    print('\t\n == "REGISTRATION" ==')
    print("___________________________")
    user_name = input("Enter your user_name : ").capitalize()
    while True:
        email = input("\n Enter your E-mail ----> [xxx@gmail.com] : ").lower()
        Valid_emails = ["@gmail.com", "@yahoo.com"]
        while (email[0].isdecimal()) or (email[-10:] not in Valid_emails) or (len(email) < 11):
            email = input("\n Enter a valid e-mail ----> [xxx@gmail.com] : ").lower()
        user_password = input("\n Enter your password ----> ")
        while len(user_password) < 8:
             user_password = input("\n Enter at least a 8-digit/character password ----> ")

        if email in users:
            print(f'"{email}" already registered ! Pls enter a valid E-mail...\n')
            continue
        users[email] = {"Username" : user_name, "Password" : user_password}
        with open("users.txt", "a") as f:
            f.write(f"{email},{user_name},{user_password}\n")
       
        print(f"\t Registration Successful for '{user_name.capitalize()}' !")
        break
    main_menu()

current_user = None
def save_users():
    with open("users.txt", "w") as f:
        for email, info in users.items():
            f.write(f"{email},{info['Username']},{info['Password']}\n")

    


def login():
    print("\t\n    == LOGIN ==")
    print("   ______________    \n")
    print("\n\t GLAD TO HAVE YOU BACK ! \n")
    email = input("\n Enter your E-mail : ").lower()
    password = input("Enter your password : ")
    # while email == " " or password == " ":
    #     email = input("\n Enter your E-mail : ").lower()
    #     password = input("Enter your password : ")

    print(f"\n Login...")
    time.sleep(3)
    # with open("users.txt", "r") as f:
    #     for line in f:
    #         line = line.strip() 
    #         if line == email and line == users[email]['Password']:
    if email in users:
        if users[email]['Password'] == password:
            global current_user
            current_user = email

            print(f"\n\t Login successful !\n \t WELCOME {users[email]['Username'].upper()} !")
            main_menu()
        else:
            print("Wrong Password !")
            print("\n Login Session failed !")
    else:
        print("\n Login Session failed !")    


def Change_Password():
    global users, current_user
    print("\n\t --- ACCOUNT SETTINGS ---\n")
    if current_user is None:
        print("No Login Session...")
        return
    old_pw = input("Enter the old password : ")
    if old_pw != users[current_user]['Password']:
        print("Incorrect Password !")
        return
    new_pw = input("Enter your new password : ")
    while len(new_pw) < 8:
        print("Invalid password !")
        new_pw = input("Enter a password of atleast 8 characters : ")
    while old_pw == new_pw:
        print("\n New password can't be the same as your old password.")
        new_pw = input("Enter a different password  : ")
    users[current_user]["Password"] = new_pw
    save_users()
    print("\n Password Successfully Changed")



def Auth_menu():
    while True:
        print("                  **************************************")
        print("                  *       AUTHENTIFICATION MENU        *")
        print("                  **************************************\n")

        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        print("\t\n 1. Register \n 2. Login \n 3. EXIT")

        choice = input(" Option =>: ")
        match choice:
            case "1":
                regis()
            case "2":
                login()
            case "3":
                print("BYE ! SEE YOU SOON.\n")
                print("Exiting...")
                time.sleep(3)
                break
            case _:
                print("Invalid input...Please try again !")


            
products = {
    "item001": {"name" : "Ledger Book", "price" : 3000, "qty" : 50, "sold" : 0},
    "item002": {"name" : "Pen", "price" : 200, "qty" : 9, "sold" : 0},
    "item003": {"name" : "School bag", "price" : 10000, "qty" : 30, "sold" : 0}
}


def view():
    print("\n\t --- ITEM LIST ---")
    for key, info in products.items():
        print(f'{key}  :    {info["name"]:<10}    {info["price"]:<10}    {info["qty"]:<10} \n')
        if low_stock(key):
            break

       

def ID():
        Id = list(products.keys())
        last_id = Id[-1]
        last_id_digit = int(last_id[4:])
        upd_id_digit = last_id_digit + 1
        new_id = f"item{upd_id_digit:03}"
        return new_id

def add():
    new_item_name = input("\n Enter the New item : ").capitalize()
    if new_item_name in products:
        print(f"{new_item_name} already exists...")
    else:
        new_item_qty = int(input("Enter the item's qty : "))
        new_item_price = int(input("Enter the item's unit price : "))
        new_id = ID()
        products[new_id] = {"name" : new_item_name, "price" : new_item_price, "qty": new_item_qty}
        print(f'\n "{new_item_name.lower()}" successfully added.')



def dlt():
    dlt_item = input("Enter the item's name / ID — to be deleted : ").capitalize()
    item_key = None
    if dlt_item in products:
        item_key = dlt_item
    else:
        for key, info in products.items():
                if info['name'].lower() == dlt_item.lower():
                    item_key = key
                    del products[key]
                    print(f'\t "{dlt_item.capitalize()}" has successfully been deleted !')
                    break
        if item_key == None:
            print(f"'{dlt_item}' do not exist !")
            # dlt_item = input("Please Re-enter the item's name to be deleted : ").capitalize()


# def upd():
#     upd_item = input("Enter the item to be updated : ").capitalize()
#     upd_qty = int(input("Enter the new "))
#     for key, info in products.items():
#         if info['name'] == upd_item:
#             products[upd_item] =



def sale():
    global products
    num_of_items_sold = int(input("Input the N° if items sold : "))   
    for i in range(1, (num_of_items_sold) + 1):
        print(f"\t\n == Item {i} Sold ==\n")
        item = input("Enter The Item's Name/ID => ")
        Item_key = None
        if item in products:
            Item_key = item
        else:
            for key, info in products.items():
                if info['name'].lower() == item.lower():
                    Item_key = key
                    break
        if Item_key == None:
            print(f'"{item.capitalize()}" not found...')
            continue

        Info = products[Item_key]
        Qty = int(input("Enter the qty sold => "))
        if Qty <= 0:
            time.sleep(2)
            print("× Invalid qty !!\n Skipping..")
            time.sleep(2)
            continue
        if Qty > Info['qty']:
            print(f'Unenough stock ("{Info['name']}" Available Stock : {Info['qty']})')
            continue
        if (Qty > Info['qty']) and (Info['qty'] <= 10):
            low_stock(Item_key)
            continue

        unit_price = Info['price']
        total_amt_sold = (unit_price) * (Qty)
        Info["qty"] -= Qty
        log_hist("Sale", Item_key, Qty)
        Info["sold"] = Info.get("sold", 0) + Qty
        print("\n\t ___SALES___\n")
        print(f"{Info['name']} : {Qty} x {Info['price']} = {total_amt_sold} FCFA \n") 
        low_stock(Item_key)
        # Une alerte doit stay ici
        
# log_transaction("SALE", item_id, Qty)
# low_stock()


def restock(item_id):
   qty = int(input("\n Enter the restock qty : "))
   products[item_id]['qty'] += qty
   log_hist("Restock", item_id, qty)
   print(f'"{products[item_id]['name']}" restocked to {products[item_id]['qty']} units !\n')
   low_stock(item_id)

def restock_menu():
    print("\n\t --- ITEM RESTOCK MENU ---\n")
    item = input("Enter the item's name/ID to be restocked : ")
    item_ID = None
    if item in products:
        item_ID = item
    else:
        for key, info in products.items():
            if info['name'].lower() == item.lower():
               item_ID = key
               break

        if item_ID is None:
            print(f"'{item.capitalize()}' do not exist !")
            return
        
    qty = int(input("Enter the restock qty : "))
    if qty <= 0:
        print("Invalid Quantity !")
        return
    products[item_ID]['qty'] += qty
    log_hist("Restock", item_ID, qty )
    print(f'"{products[item_ID]['name']}" restocked to {products[item_ID]['qty']} units !\n')
    low_stock(item_ID)



#    if item_restock in products:
#            item_id = item_restock
#    else:
#         for key, info in products.items():
#             if info['name'].lower() == item_restock.lower():
#                 item_id = key
#                 break
#         if item_id is None:
#             print(f'"{item_restock}" not found.')
    
#         info = products[item_id]
#         print(f"     {info['name']} found with {info['qty']} units  \n")

#         qty_restock = int(input("Enter the restock : "))
#         info['qty'] += qty_restock
#         print(f'"{info['name']}" restocked to {info['qty']} units !')


def low_stock(item_id):    
    info = products[item_id]
    Low_stock_qty = 10
    qty = info['qty']
    name = info['name']
    # for item_id, info in products.items():
    if qty == 0:
        print(f'STOCK ALERT : "{name}" Completely Out Of Stock...!')
    elif qty <= Low_stock_qty:
        print(f'     STOCK ALERT : "{name}" left with {qty} units...\n Please may restock !\n')
    else:
        return
    restock_qtn = input("\t\n Do you want to restock ?! \n 1. Yes (Y) ? \n 2. No (N) \n Enter your choice : ").lower()
    if restock_qtn.lower() == "y" or restock_qtn.lower() == "yes" :
         #or restock_qtn.capitalize() == "Yes" or restock_qtn.upper() == "YES" : # Probleme
        restock(item_id)
        print(f'{item_id} : {info["name"]} | New_Qty: {info["qty"]}')
        return True    
    elif restock_qtn.lower() == "n" and restock_qtn.lower() == "no":
       print("\t\n Returning to Main Menu...")
       time.sleep(2)
       

    return False
        # while (restock_qtn != "y") or (restock_qtn != "n") or (restock_qtn != "yes") or (restock_qtn != "no"):
        #     restock_qtn = input("\n Please enter a valid choice [Yes(Y)/No (n)]: ")
       
           

def search():
    print("\n\t--- ITEM SEARCH ENGINE ---")
    search_item = input(("\n Either enter the item's ID ⇔ item's Name : "))
    item_id = None
    if search_item in products:
        item_id = search_item

    else:
        for key, info in products.items():
            if info['name'].lower() == search_item.lower(): 
                item_id = key
                break
    if item_id == None:
        print(f"'{search_item}' not Found !")
        return

    info = products[item_id]
    print(f"\n\t Searching '{search_item}'.... ")
    time.sleep(1)
    print(f"\n Item_name : {info['name']}     Price : {info['price']}     Qty : {info['qty']}\n")
    low_stock(item_id) # Se declenche ni'importe comment mais qd la quatite n'est pas <= 10
# products = {
#     "item001": {"name" : "Ledger Book", "price" : 3000, "qty" : 50, "sold" : 0},
#     "item002": {"name" : "Pen", "price" : 200, "qty" : 9, "sold" : 0},
#     "item003": {"name" : "School bag", "price" : 10000, "qty" : 30, "sold" : 0}
# }

transactions = []

def log_hist(action, item_id, qty):
    transactions.append({
    "Type": action,
    "Item_id": item_id,
    "item_name": products[item_id]['name'],
    "Qty": qty,
    "Time": time.strftime("%Y-%m-%d %H:%M:%S")
    })


def hist():
    print("\t\n ==== TRANSACTION HISTORY ==== \n")
    if not transactions:
        print("No Transactions have been performed yet...")
    else:
         print("ITEM    |    ACTION    |    QTY    |    TIME \n")
         for s in transactions:
            print(f"{s["item_name"]}    |    {s["Type"]}     |    {s["Qty"]}     |    {s["Time"]}")


def report():
    print("\t\n ---=== ITEM REPORT ===--- \n")
    if not (products and transactions):
        print("No Available Report List...")
    else:
        for item_id, info in products.items():
            sold = 0
            restock = 0
            total_amount = 0
            for t in transactions:
                if t['Item_id'] == item_id:
                    if t["Type"] == "Sale":
                        sold += t["Qty"]
                        total_amount += t['Qty'] * info['price']
                elif t['Type'] == "Restock":
                    restock += t['Qty']
            Qty = info['qty']
            if Qty == 0:
                Status = "Empty_Stock !"
            elif Qty <= 10:
                Status = "Low_Stock !"
            else:
                Status = "OK."
            
            print(f"Item : {info['name']}")
            print(f"Qty_Sold : {sold} ")
            print(f"Qty_Restocked : {restock} ")
            print(f"Qty_Left: {Qty} ")
            print(f"Status : {Status}")   
            print(f"Revenue : {total_amount} FCFA ")
            print("_" * 40)
           

def main_menu():
    while True:
        print("\n\t === SMART INVENTORY MANAGEMENT SYSTEM ===")
        print("\n Menu Options :\n ")
        print("1. Add New Item")
        print("2. Remove Item")
        # print("3. Update Item")
        print("3. Sell Item")
        print("4. Restock Item")
        print("5. View Item List")
        print("6. Item Search")
        print("7. Transaction History")
        print("8. Item Report")
        print("9. Change Password")
        print("0. Save & EXIT")
        choice = input("\t Choice : ")
        match choice:
            case "1":
                add()
            case "2":
                dlt()
            # case "3":
            #     upd()
            case "3":
                sale()
            case "4":
                restock_menu()
            case "8":
                report()
            case "7":
                hist()
            case "5":
                view()
            case "6":
                search()
            case "9":
                Change_Password()
            
            case "0":
                print("Do you want to Logout ?\n - Yes (Y)\n - No (N)\n")
                qtn = input("Choice (Y/N)=> ")
                if qtn == "Y" or "y":   
                    print("Saving Overall Changes...\n")
                    time.sleep(2)
                    print("All Changes Successfully saved.")
                    break
                if qtn == "N" or "n":
                    main_menu()
                else:
                    print("{qtn} is an invalid input !\n Please enter something valid.\n")
                    qtn = input("Choice (Y/N)=> ")
            case _:
                print("Invalid input !")
Auth_menu()
# main_menu()

                
