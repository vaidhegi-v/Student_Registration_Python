detail = {}
login_li = []
review_dict = {}
li = []
term_dict = {}

def signup():
    username = input("Create Your Username: ")
    password = input("Create Your Password: ")
    if username in detail:
        print("Username already exists")
    elif username in term_dict:
        print("You are terminated by the Admin. Pay the fine amount to signup")
    else:
        detail[username] = password
        print("Signup completed successfully")

def login():
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    if username in detail and detail[username] == password and username not in li:
        print("Logged in successfully")
        login_li.append(username)
        li.append(username)
    elif username in term_dict:
        print("You are terminated by the Admin. Pay the fine amount to login")
    elif username in li:
        print("You are already logged in")
    else:
        print("Incorrect login or password")

def logout():
    username = input("Enter Your Username: ")
    if username in login_li:
        print(f"Goodbye, {username}")
        login_li.remove(username)
        li.remove(username)
    else:
        print("Your account is not logged in")

def admin_login():
    admin_id = "vaidhegi"
    password = input("Enter Admin Password: ")
    if password == "uniq" and admin_id not in li:
        li.append(admin_id)
        print("Admin logged in successfully")
    elif admin_id in li:
        print("Admin is already logged in")
    else:
        print("Invalid Admin Password")

def admin_logout():
    password = input("Enter Admin Password: ")
    if password == "uniq" and "vaidhegi" in li:
        li.remove("vaidhegi")
        print("Admin logged out successfully")
    else:
        print("Admin hasn't logged in or invalid password")

def write_review():
    if li and li[-1] != "vaidhegi":
        review = input("Write a review: ")
        review_dict[login_li[-1]] = review
    else:
        print("Only users can write reviews")

def read_review():
    if li and li[-1] == "vaidhegi":
        for user, review in review_dict.items():
            print(f"{user}'s review: {review}")
    else:
        print("Only Admin can read reviews")

def delete_review():
    if li and li[-1] == "vaidhegi":
        user = input("Enter the username to delete review: ")
        if user in review_dict:
            review_dict.pop(user)
            print("Review deleted")
        else:
            print("No such user")
    else:
        print("Only Admin can delete reviews")

def terminate_user():
    if li and li[-1] == "vaidhegi":
        user = input("Enter the username to terminate: ")
        if user in detail:
            term_dict[user] = detail.pop(user)
            login_li.remove(user)
            li.remove(user)
            print(f"User {user} terminated")
        else:
            print("No such user")
    else:
        print("Only Admin can terminate users")

def loggedin_list():
    if li and li[-1] == "vaidhegi":
        print(f"Logged in users: {list(set(li))}")
    else:
        print("Only Admin can see logged-in users")

def pay_fine():
    user = input("Enter your username to pay fine: ")
    password = input("Enter your password: ")
    if user in term_dict and term_dict[user] == password:
        fine = int(input("Enter the fine amount: "))
        if fine >= 500:
            detail[user] = term_dict.pop(user)
            print("Fine paid, account restored")
        else:
            print("Minimum fine amount is Rs.500")
    elif user in detail:
        print("You don't have any fines to pay")
    else:
        print("User not found")

while True:
    print("\n1.Sign Up \n2.Login \n3.Logout \n4.Admin login \n5.Admin logout \n6.Write Review \n7.Read Reviews \n8.Delete Review \n9.Terminate User \n10.List Logged-in Users \n11.Pay Fine \n12.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        signup()
    elif choice == 2:
        login()
    elif choice == 3:
        logout()
    elif choice == 4:
        admin_login()
    elif choice == 5:
        admin_logout()
    elif choice == 6:
        write_review()
    elif choice == 7:
        read_review()
    elif choice == 8:
        delete_review()
    elif choice == 9:
        terminate_user()
    elif choice == 10:
        loggedin_list()
    elif choice == 11:
        pay_fine()
    elif choice == 12:
        print("Thank you! Come again")
        break
    else:
        print("Invalid choice")
