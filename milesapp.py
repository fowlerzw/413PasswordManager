import pandas as pd
import csv
import rsa


def main():  # put application's code here
    publicKey, privateKey = rsa.newkeys(512)
    filename = "DataSet.csv"
    key = input("Enter Master Key: ")
    if(key == "miles"):
        menu = input("Hello Welcome to your password Manager\nPress A To add a password\nPress V to View List of Passwords")
    else:
        print("Wrong Password")
        quit()
    if(menu == "A"):
        site = input("Enter Site Name: ")
        user = input("Enter Username: ")
        password = input("Enter Password: ")
        encMessage = rsa.encrypt(message.encode(),
                         publicKey)
        rows = [str(site),str(user),str(encMessage)]
        with open(filename, 'a') as csvfile: 
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow(rows)
    elif(menu == "V"):
        df = pd.read_csv(filename, names=["site","user","pass"])
        
    for passwords in df["pass"]:
        namespace = fernet.decrypt(passwords).decode()
        print(namespace)
    print(df)
    

    
    #returnpass = 
    #decMessage = fernet.decrypt(returnpass).decode()

if __name__ == '__main__':
    main()
