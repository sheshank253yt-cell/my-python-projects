import json


def start():
    print("------welcome to password manager------")
    mas_user = input("Enter master password to access password manager:")
    with open("mas_pass.json","r") as f:
        
        data = json.load(f)
        
    if data["password"] ==mas_user:
        print("---------login successful!---------")
        return True
    else:
        print("invalid password!") 
        
           



def view():
    with open("passwords.json","r") as file:
        data = json.load(file)
        
        for i in data:
            
            print(f"Username:{i["username"]};password:{i["password"]}")
    
    
    
def add():
    user_us = input("Enter username:")
    user_pwd = input("Enter password:") 
    
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError :
        data = []

    data.append({"username": user_us, "password": user_pwd})
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)
    print("------details saved!------")    
    
    
    
    
def main():
    while True:
        if start():
            

            while True:
                print("------COMMANDS------")
                print("1.view exiting passwords\n2.add new password\n3.exit")
                user = input("choose (1 or 2 or 3):")
                if user =="1":
                    view()
                elif user =="2":
                    view()
                elif user =="3":
                    print("Thankyou.")
                    break
                else:
                    print("invalid choice!.")
                    continue    
        
            
        else:
            continue 
        
        
        
        
        
        
        
              
if __name__ =="__main__" :
    main()        


