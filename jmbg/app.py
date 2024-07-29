from cryptography.fernet import Fernet

admin = input("Enter your name: ")
admin_pwd = input("Enter your password: ")
key = Fernet.generate_key()
key = key.decode() + admin_pwd
token = Fernet(key)

def authenticate(username,passwd):
    with open("jmbg/admins.txt","r") as file:
        for line in file.readlines():
            uname,pwd = line.split("|")
            uname = uname.strip()
            pwd = pwd.strip()
            if username.lower() == uname:
                if passwd == pwd:
                    print(f"Welcome, {username.title()}....")
                    return 1
                else:
                    print("Wrong password!")
                    return -1
    print("Unknown user.")
    return 0


def view_jmbgs():
    with open("jmbg/jmbgs.txt","r") as file:
        for line in file.readlines():
            name,jmbg = line.split("|")
            print(f"Name: {name.title()}, Personal ID number: {token.decrypt(jmbg.encode()).decode()}")


def add_jmbg():
    name = input("Enter full name: ").lower()
    jmbg = input("Enter personal number: ")
    if jmbg.isdigit() and len(jmbg) == 13:
        with open("jmbg/jmbgs.txt","a") as file:
            file.write(f"{name} | {token.encrypt(jmbg.encode()).decode()}\n")
        print("Added...")
    else:
        print("JMBG must be completely made out of numbers and have the length of 13.")

            

access = authenticate(admin,admin_pwd)
if not access or access == -1:
    quit()

while True:
    menu = int(input("1. Add\n2. View existing\n3. Quit\n"))
    if menu == 1:
        add_jmbg()
    elif menu == 2:
        view_jmbgs()
    elif menu == 3:
        print("zzz")
        break
    else:
        print("Invalid choice")
        continue

