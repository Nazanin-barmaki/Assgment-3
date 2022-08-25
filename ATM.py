from itertools import count


passw= 5172
count=0

while count<3:

 passw_user= int(input("Please enter your password:"))
 if 1000<=passw_user<=9999:
        if passw== passw_user:
            print("correct")
            break
        elif passw_user ==2715:
            print("We are reporting to the police. Your account has been blocked")
            break
        else:
            print(" warning Wrong password.")
            count=count+1
 else:
     continue
if count>2:
    print("Too many attempts,Your card was blocked by the bank.")