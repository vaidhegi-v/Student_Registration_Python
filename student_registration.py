detail={}
login_li=[]
review_dict={}
li=[]
term_dict={}
def signup():
    username=input("Create Your Username: ")
    password=input("Create Your Password: ")
    if username in detail:
        print("Username is already exist")
    elif username in term_dict:
        print("You are terminated by the Admin..Pay the fine amount to signup")
    else:
        detail.setdefault(username,password)
        print("You are signup successfully completed")
def login():
    global login_id
    login_id = input("Enter Your Username: ")
    login_password = input("Enter Your Password: ")
    if login_id in detail and detail[login_id] == login_password and login_id not in li:
        print("You are successfully logged in")
        login_li.append(login_id)
        li.append(login_id)
    elif login_id not in login_li:
        print("You are terminated by the Admin..Pay the fine amount to login")
    elif login_id in li:
        li.append(login_id)
        print("You are already in") 
    else:
        print("Incorrect login or password")           
def logout():
    logout_id=input("Enter Your Username: ")
    if logout_id in login_li:
        print("successfully loged out, Goodbye",logout_id)
        login_li.remove(logout_id)
        li.remove(logout_id)
    else:
        print("Your account is not loged in")
def admin_login():
    admin_id="vaidhegi"
    admin_password=input("Enter Password: ")
    if admin_password=="uniq" and admin_password not in li:
        li.append(admin_id)
        print("Admin logged in successfully")
    elif admin_password in li:
        li.append(admin_id)
        print("Already Admin is logged-in")
    else:
        print("Invalid Admin Password")
def admin_logout():
    admin_password=input("Enter Password: ")
    if admin_password in li:
        print("Admin logged out successfully")
        li.remove(admin_id)
    elif admin_password=="uniq" and admin_password not in li:
        print("Admin hasn't logged in")
    else:
        print("Invalid Admin Password")
def write_review():
    if li[-1]!="vaidhegi":
        review=input("Write a review: ")
        review_dict.setdefault(login_id,review)
    else:
        print("Only user can write review")
def read_review():
    if li[-1]=="vaidhegi":
        for i in review_dict:
            print(i,"'s review is",review_dict[i])
    else:
        print("Only Admin can read reviews")
def delete_review():
    if li[-1]=="vaidhegi":
        del_review_id=input("Enter the user name for delete review: ")
        if del_review_id in detail:
            review_dict.pop(del_review_id)
        else:
            print("No user in this name")
    else:
        print("Only Admin can delete reviews")
def terminate_user():
    if li[-1]=="vaidhegi":
        terminat_user=input("Enter the user name to terminate review: ")
        if terminat_user in detail:
            login_li.remove(terminat_user)
            li.remove(terminat_user)
            x=detail.pop(terminat_user)
            term_dict.setdefault(terminat_user,x)
        else:
            print("No user in this username")   
    else:
        print("Only Admin can terminate user")
def loggedin_list():
    if li[-1]=="vaidhegi":
        lo_li=set(li)
        print(list(lo_li))
    else:
        print("Only Admin can see logged-in user names")
def fine_amount():
    fine_id=input("Enter the user name to pay fine: ")
    fine_password=input("Enter the password: ")
    if fine_id in term_dict and fine_password==term_dict[fine_id]:
        fine=int(input("Enter the fine amount: "))
        if fine>=500:
            detail.setdefault(fine_id,fine_password)
        else:
            print("The minimum fine amount is Rs.500")
    elif fine_id not in term_dict and fine_id in detail:
        print("You don't have any fine to pay")
    else:
        print("User is unidentified")
           
while True:
    print("\n 1.Sign Up \n 2.Login \n 3.Logout \n 4.Admin login \n 5.Admin logout \n 6.Write Review \n 7.Read User Reviws \n 8.Delete User Reviws \n 9.Terminate User \n 10.List Logged-in Users \n 11.Pay Fine \n 12.Exit")
    a=int(input("Enter your choice: "))
    
    if a==1:      
        signup()
    elif a==2:
        login()
    elif a==3:
        logout()
    elif a==4:
        admin_login()
    elif a==5:
        admin_logout()
    elif a==6:
        write_review()
    elif a==7:
        read_review()
    elif a==8:
        delete_review()
    elif a==9:
        terminate_user()
    elif a==10:
        loggedin_list()
    elif a==11:
        fine_amount()
    elif a==12:
        print("Thank you for coming our site, come soon")
        break
    else:
        print("Invalid process")
