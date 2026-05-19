import json
import random
import string
from pathlib import Path



class Bank:
    database = 'data.json'
    data = []




    try :
        if Path(database).exists():
           with open(database) as fs:
                data = json.loads(fs.read())
        else : 
            print("no such file exist")        
    except Exception as err:
        print(f"an error occur as {err}")  





    @staticmethod
    def __update ():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))



    @classmethod
    def __accountgenrate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits , k=3 )
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return"".join(id)        






    def createaccount(self):
        info = {
            "name": input ("Tell your name : "),
            "age": int(input ("Tell your age : ")),
            "email": input ("Tell your email : "),
            "pin": int(input ("Tell your 4 number pin : ")),
            "accountNo" : Bank.__accountgenrate(),
            "balance" : 0
        }
        if info['age'] < 18 or len(str(info['pin'])) !=4:
            print ("you you cannot create your account")
        else:
            print ("account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note your account number")

            Bank.data.append(info)

            Bank.__update()







    def depositmoney(self):
        accnumber = input("tell your account number : ")
        pin = int(input("tell your pin : "))

        userdata =[i for i in Bank.data if i['accountNo'] == accnumber and i['pin']==pin]

        if userdata == False:
            print("no data found")

        else:
            amount = int(input("how much you want to deposit : "))
            if amount > 10000 or amount < 0:
                print("sorry the amount is too much, deposit below Rs:10000 and above Rs:0")

            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("AMOUNT DEPOSIT SUCCESSFULLY")





    def withdrawmoney(self):
        accnumber = input("tell your account number : ")
        pin = int(input("tell your pin : "))

        userdata =[i for i in Bank.data if i['accountNo'] == accnumber and i['pin']==pin]

        if userdata == False:
            print("no data found")

        else:
            amount = int(input("how much you want to withdraw : "))
            if amount > userdata[0]['balance'] or amount < 0:
                print("sorry you have umsufficient balance")

            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("AMOUNT WITHDREW SUCCESSFULLY")



       

       

    def showdetails(self):
        accnumber = input("tell your account number : ")
        pin = int(input("tell your pin : "))

        userdata =[i for i in Bank.data if i['accountNo'] == accnumber and i['pin']==pin]
        
        print("\n your imformations are : \n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")






    def updatedetails(self):
        accnumber = input("tell your account number : ")
        pin = int(input("tell your pin : "))

        userdata =[i for i in Bank.data if i['accountNo'] == accnumber and i['pin']==pin]
        
        if userdata == False:
            print("no data found")
        else:
            print("fill the detail for change or leave it empty for no chnage and press enter")

            newdata = {
                "name" : input("enter new name : "),
                "email" : input("enter new email : "),
                "pin" : input("enter new pin : ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]    
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]

            newdata["age"] = userdata[0]["age"]
            newdata["accountNo"] = userdata[0]["accountNo"]
            newdata["balance"] = userdata[0]["balance"]

            if type(newdata["pin"]) == str:
                newdata["pin"] = int(newdata["pin"])

            for i in newdata:
                if newdata [i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i] 

            Bank.__update()
            print("UPDATE INFO SUCCESSFULLY") 







    def delete(self):
        accnumber = input("tell your account number : ")
        pin = int(input("tell your pin : "))

        userdata =[i for i in Bank.data if i['accountNo'] == accnumber and i['pin']==pin]

        if userdata == False:
            print("no such data exist")

        else:
            check = input("press y if you want to delete or press n to cancel")

            if check =="n" or check =="N":
                print("bypass")
            else:
                index =Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print("ACCOUNT DELETE SUCCESSFULLY")        

        
                           




user = Bank()

check = 0
while check !=7:
    print("press 1 for creating account")
    print("press 2 for depositing the money")
    print("press 3 for withdrawing the money")
    print("press 4 for details")
    print("press 5 for updating the details")
    print("press 6 for delete the account")
    print("press 7 to close")

    check = int(input("tell your response: "))

    if check == 1:
        user.createaccount()

    if check == 2:
        user.depositmoney()

    if check == 3:
        user.withdrawmoney()

    if check == 4:
        user.showdetails() 

    if check == 5:
        user.updatedetails()

    if check == 6:
        user.delete()    


        