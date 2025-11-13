import time
print("Welcome to our ShoppingWeb!!!")
a = 3
found = False
username = "Medina"
userpassword = "MedinA129"
balance = 500
category = [["0", "T-shirt" , 12.50 ] , ["1","Hoodie" , 45.00 ] , ["2","Jeans" , 50.00]]
B=[] #sebete elave et
F=[] #favorilere elave et
while a > 0:
    enteredusername = input("Please enter your username:   ")
    enteredpassword = input("Please enter your password:  ")
    if userpassword == enteredpassword and username == enteredusername :
        while True:
            print("1-->Catagories")
            print("2-->Basket")
            print("3-->Favorites")
            print("4-->History")
            print("5-->Settings")
            print("6-->Show my balance")
            print("7-->Exit")
            print("---------------------------------------------------------")
            selectednumber = input("Select a number among: 1 2 3 4 5 6 7 ")
            if selectednumber == "1":
                n=0
                print(category)
                choosenId = input("Choose the id you want: ")
                selectedcatagory = input("If you want to add to favorites choose : F\nIf you want to add to basket choose : B  ")
                #if choosenId in category:
                for item in category:
                    if item[0] == choosenId:
                        if selectedcatagory.upper() == "B":
                            B.append(category[n])
                            print("Product added succesfully")
                            print("Your basket: ", B)
                        elif selectedcatagory.upper() == "F":
                            F.append(category[n])
                            print("Product added succesfully")
                            print("All your favorites: ", F)
                            break
                if not found:
                    print("Id was not founded. Please choose the right Id")
                    n = n + 1
            elif selectednumber == "2":
                print("Your basket: ", B)
            elif selectednumber == "3":
                print("All your favorites: ", F)
            if selectednumber == "0":
                print("Goodbye Medina. Your exit is succesfull")
                break  
            if selectednumber == "4":
                print(1)           


    else:
        print("Password or username is incorrect. Please enter again. Don't forget you have only 3 chances")
        a=a-1
    
    if a == 0:
        print("Your account was blocked for 10 seconds be patient and carefull")
        time.sleep(10)