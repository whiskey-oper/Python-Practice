# --- THE PASSWORD SECURITY CHECK ---

# Section 1
user_password = "password123"
user_password= input("Enter password here >>> ")
if user_password == "admin123":
    print("Access Granted.")
elif user_password== " ":
    print("Access Denied. Wrong password.")
elif user_password== "admin124":
    print("Please try again.")

# Section 2
login_attempts = 3
user_input= input("Please submit the number of attempts... ")
if login_attempts > 5:
    print("Your account is locked.")
else: login_attempts < 5
print("You have attempts remaining.")


# Section 3
password_length = 5
NEW_passwordlogin: str= input("Create a new password. Make sure it's strong. ")

if password_length < 8:
    print("Password weak. Must be atleast more than 8 characters and not less, idiot.")
elif password_length > 8:
    print("Strong password")
else:
    input("You may leave. Thank you for passing security check.")