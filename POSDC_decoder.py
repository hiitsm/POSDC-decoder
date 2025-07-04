import tkinter as tk
from tkinter import messagebox
import json
import datetime
import os

credentials_file = "credentials.json"
log_file = "logs.json"

if os.path.exists(credentials_file):
    with open(credentials_file, 'r') as f:
        credentials = json.load(f)
else:
    credentials = {'User1': 'Pass123',
                   'User2': 'password',
                   'admin': 'adminpass'}


def save_credentials():
    with open(credentials_file, 'w') as f:
        json.dump(credentials, f)

def save_log(event, user=""):
    log_entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user": user,
        "event": event
        }
    
    logs = []
    
    if os.path.exists(log_file):
        try:
            with open(log_file, 'r') as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    else:
        with open(log_file, 'w') as f:
            json.dump([], f)
    logs.append(log_entry)
    
    with open(log_file, 'w') as f:
        json.dump(logs, f, indent=4)

def open_admin_panel():
    admin = tk.Tk()
    admin.title("Admin Panel")

    tk.Label(admin, text="New Username:").grid(row=0, column=0)
    new_user_entry = tk.Entry(admin)
    new_user_entry.grid(row=0, column=1)

    tk.Label(admin, text="New Password:").grid(row=1, column=0)
    new_pass_entry = tk.Entry(admin, show="*")
    new_pass_entry.grid(row=1, column=1)

    def add_user():
        new_user = new_user_entry.get()
        new_pass = new_pass_entry.get()
        if new_user and new_pass:
            credentials[new_user] = new_pass
            save_credentials()
            messagebox.showinfo("Success", "User added.")
        else:
            messagebox.showerror("Error", "Username and password cannot be empty.")

    tk.Button(admin, text="Add User", command=add_user).grid(row=2, column=0)

    tk.Label(admin, text="Username to Delete:").grid(row=3, column=0)
    delete_user_entry = tk.Entry(admin)
    delete_user_entry.grid(row=3, column=1)

    def delete_user():
        del_user = delete_user_entry.get()
        if del_user in credentials and del_user != "admin":
            del credentials[del_user]
            save_credentials()
            messagebox.showinfo("Success", "User deleted.")
        else:
            messagebox.showerror("Error", "User not found")

    tk.Button(admin, text="Delete User", command=delete_user).grid(row=4, column=0)


def open_decoder():
    root = tk.Tk() 
    root.title("POSDC decoder")
    root.geometry("805x600+550+200")
    
    enter = tk.Label(root, text = "Kindly enter POSDC below:")
    enter.grid(row=0, column=0)
    
    user_enter = tk.Entry(root)
    user_enter.grid(row=1, column=0)
    
    result = tk.Label(root, text = "Results")
    result.grid(row=2, column=0)
    
    text = tk.Text(root, width=100, height=30)
    text.grid(row=3, column=0)
    
    thanks = tk.Label(root, text = "Thanks for using me:)")
    thanks.grid(row=4, column=0)
    
    def decoder(event=None):
        code = user_enter.get()
        if len(code) < 12:
            save_log("Error: Invalid Input (Less than 12 chars.)", user="")
            messagebox.showerror("Error","Please enter at least 12 values")
        else:
            save_log("Decode Request", user="")
            card_input_capability ={
                '0':"Unknown\n",
                '1':"Manual, no terminal\n",
                '2':"Magnetic stripe read\n", 
                '3':"Optical Code\n", 
                '4':"Optical Character Recognition\n",
                '5':"Integrated Circuit Card\n",
                '6':"Key entered\n",
                }
            
            cardmember_auth_capability ={
                '0':'No electronic authentication\n',
                '1':'PIN\n',
                '2':'Electronic signature analysis\n',
                '3':'Biometrics\n',
                '4':'Biographic\n',
                '5':'Electronic authentication inoperative\n',
                '6':'Other\n',
                }
            
            card_capture ={
                '0':'None\n',
                '1':'Capture\n',
                }
            
            operating_environment ={
                '0':'No terminal used\n',
                '1':'On premise of Card Acceptor, attended\n',
                '2':'On premise of Card Acceptor, unattended\n',
                '3':'Off premise of Card Acceptor, attended\n',
                '4':'Off premise of Card Acceptor, unattended\n',
                '5':'On premise of Cardmember, unattended\n',
                '9':'Delivery mode unkown, unspecified\n',
                'S':'Electronic delivery of product\n',
                'T':'Physical delivery of product\n',
                'X':'Mobile remote\n',
                'Z':'Transit Access Terminal\n',
                }
            
            cardmember_present ={
                '0':'Cardmember present\n',
                '1':'Cardmember not present, unspecified\n',
                '2':'Cardmember not present, mail order\n',
                '3':'Cardmember not present, telephone\n',
                '4':'Cardmember not present, standing authorization\n',
                '9':'Cardmember not present, recurring billing\n',
                'S':'Cardmember not present, Internet transaction\n',
                'T':'Cardmember present at Participants bank\n',
                }
            
            card_present ={
                '0':'Card not present\n',
                '1':'Card present\n',
                '8':'Issuer Originated Payments\n',
                'X':'Contactless Transaction\n',
                'Y':'Digital Wallet - Contactless Initiated\n',
                'Z':'Digital Wallet - Application Initiated\n',
                }
            
            card_data_input ={
                '0':'Unspecified\n',
                '1':'Manual, no terminal\n',
                '2':'Magnetic stripe read\n',
                '3':'Optical Code\n',
                '4':'Optical Charater Recognition\n',
                '5':'Integrated Circuit Card\n',
                '6':'Key entered\n',
                '9':'Chipcard Fallback, Chip cannot be read\n',
                'A':'Credentials on file\n',
                'S':'Keyed Card Account Number and Keypad PCSC key entered at Point of Sale\n',
                'V':'VOice authorization Network to Issuer Only\n',
                'W':'Magnetic stripe read and PCSC key-entered at Point of Sale\n',
                }
            
            cardmember_auth ={
                '0':'Not authenticated\n',
                '1':'PIN\n',
                '2':'Electronic signature analysis\n',
                '3':'Biometric\n',
                '4':'Biographic\n',
                '5':'Manual signature verification\n',
                '6':'Other manual verification\n',
                'S':'Electronic ticket Environment\n',
                }
            
            cardmember_auth_entity ={
                '0':'Not authenticated\n',
                '1':'Integrated Circuit Card\n',
                '2':'Card Acceptor Device\n',
                '3':'Authorizing agent\n',
                '4':'By merchant\n',
                '5':'Other\n',
                }
            
            card_data_output ={
                '0':'Unknown\n',
                '1':'None\n',
                '2':'Magnetic stripe write\n',
                '3':'Integrated Circuit Card\n',
                }
            
            terminal_output ={
                '0':'Unknown\n',
                '1':'None\n',
                '2':'Printing\n',
                '3':'Display\n',
                '4':'Printing and display\n',
                }
            
            PIN_capture ={
                '0':'No PIN capture capability\n',
                '1':'Device PIN capture capability unknown\n',
                '4':'Four characters\n',
                '5':'Five characters\n',
                '6':'Six characters\n',
                '7':'Seven characters\n',
                '8':'Eight characters\n',
                '9':'Nine characters\n',
                'A':'Ten characters\n',
                'B':'Eleven characters\n',
                'C':'Twelve characters\n',
                }
    
            if code[0] in card_input_capability:
                text.insert('end-1c', 'Card Data Input Capability = ' + card_input_capability[code[0]])
            else:
                text.insert('end-1c', "Card Data Input Capability = Usage reserved\n")
            if code[1] in cardmember_auth_capability:
                text.insert('end-1c', 'Cardmember Authentication Capability = '+ cardmember_auth_capability[code[1]])
            else:
                text.insert('end-1c', "Cardmember Authentication Capability = Usage reserved\n")
            if code[2] in card_capture:
                text.insert('end-1c', 'Card Capture Capability = ' + card_capture[code[2]]) 
            else:
                text.insert('end-1c', "Card Capture Capability = Usage reserved\n")
            if code[3] in operating_environment:
                text.insert('end-1c', 'Operating environment = ' + operating_environment[code[3]])
            else:
                text.insert('end-1c', "Operating environment = Usage reserved\n")
            if code[4] in cardmember_present:
                text.insert('end-1c', 'Cardmember Present = ' + cardmember_present[code[4]])
            else:
                text.insert('end-1c', "Cardmember Present = Usage reserved\n")
            if code[5] in card_present:
                text.insert('end-1c', 'Card Present = ' + card_present[code[5]])
            else:
                text.insert('end-1c',"Card Present = Usage reserved\n")
            if code[6] in card_data_input:
                text.insert('end-1c', 'Card Data Input Mode = ' + card_data_input[code[6]])
            else:
                text.insert('end-1c', "Card Data Input Mode = Usage reserved\n")
            if code[7] in cardmember_auth:
                text.insert('end-1c', 'Cardmember Authentication = ' + cardmember_auth[code[7]])
            else:
                text.insert('end-1c', "Cardmember Authentication = Usage reserved\n")
            if code[8] in cardmember_auth_entity:
                text.insert('end-1c', 'Cardmember Authentication Entity = ' + cardmember_auth_entity[code[8]])
            else:
                text.insert('end-1c', "Cardmember Authentication Entity = Usage reserved\n")
            if code[9] in card_data_output:
                text.insert('end-1c', 'Card Data Output Capability = ' + card_data_output[code[9]])
            else:
                text.insert('end-1c', "Card Data Output Capability = Usage reserved\n")
            if code[10] in terminal_output:
                text.insert('end-1c', 'Terminal Output Capability = ' + terminal_output[code[10]])
            else:
                text.insert('end-1c', "Terminal Output Capability = Usage reserved\n")
            if code[11] in PIN_capture:
                text.insert('end-1c', 'PIN Capture Capability = ' + PIN_capture[code[11]])
                text.insert('end', '\n'+'\n')
            else:
                text.insert('end-1c', "PIN Capture Capability = Usage reserved\n")
                text.insert('end', '\n'+'\n')
    user_enter.bind('<Return>', decoder)
def login():
    user = userenter.get()
    password = passenter.get()

    if user in credentials and credentials[user] == password:
        save_log("Login Succesful", user=user)
        if user == "admin":
            open_admin_panel()
        else:
            messagebox.showinfo("Login succesful", "Access Granted")
            main.destroy()
            open_decoder()
    else:
        save_log("Login Failed", user=user)
        messagebox.showerror("Login unsuccseful", "Invalid username or password")
        


main = tk.Tk()
main.title("Login Form")
main.geometry('250x150+800+400')

userlabel = tk.Label(main, text="UserID")
userlabel.pack()

userenter = tk.Entry(main)
userenter.pack()

passlabel = tk.Label(main, text="Password:")
passlabel.pack()

passenter = tk.Entry(main, show="*")
passenter.pack()

button = tk.Button(main, text="Login", command=login)
button.pack()

main.mainloop()

