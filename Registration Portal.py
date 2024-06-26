from tkinter import *
from tkinter import messagebox

class Person:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f"{self.username}({self.role})"

    def printDetails(self):
        print(self.username, self.role)

class Teacher(Person):
    def __init__(self, username, password, role, department):
        super().__init__(username, password, role)
        self.department = department
        self.consecutive_wrong_attempts = 0

    def printDetails(self):
        print(self.username, self.role, self.department)

class UGStudent(Person):
    def __init__(self, username, password, role, department, year_of_graduation):
        super().__init__(username, password, role)
        self.department = department
        self.year_of_graduation = year_of_graduation
        self.consecutive_wrong_attempts = 0

    def printDetails(self):
        print(self.username, self.role, self.department, self.year_of_graduation)

class PGStudent(Person):
    def __init__(self, username, password, role, department):
        super().__init__(username, password, role)
        self.department = department
        self.consecutive_wrong_attempts = 0

    def printDetails(self):
        print(self.username, self.role, self.department)

def loadDetails():
    try:
        with open("user_details.txt", "r") as file:
            lines = file.readlines()
            details = []
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    if parts[2] == "Teacher":
                        x = Teacher(parts[0], parts[1], parts[2], parts[3])
                        details.append(x)
                    elif parts[2] == "UG Student" and len(parts) == 5:
                        x = UGStudent(parts[0], parts[1], parts[2], parts[3], int(parts[4]))
                        details.append(x)
                    elif parts[2] == "PG Student":
                        x = PGStudent(parts[0], parts[1], parts[2], parts[3])
                        details.append(x)
            return details
    except FileNotFoundError:
        return []

def saveDetails(details):
    with open("user_details.txt", "w") as file:
        for user in details:
            file.write(f"{user.username},{user.password},{user.role},{user.department}\n")
            if isinstance(user, UGStudent):
                file.write(f"{user.username},{user.password},{user.role},{user.department},{user.year_of_graduation}\n")

listOfDetails = loadDetails()

def signUp():
    userSignUp()

def signIn():
    userSignIn()

def userSignUp():
    signupWindow = Tk()
    signupWindow.geometry("500x500")
    signupWindow.title("Sign Up")
    signupWindow.configure(bg="#FF5733")

    frame1 = Frame(signupWindow, bg="#FF5733")
    frame1.pack(side=TOP, pady=10)

    frame2 = Frame(signupWindow, bg="#FF5733")
    frame2.pack(side=TOP, pady=10)

    frame3 = Frame(signupWindow, bg="#FF5733")
    frame3.pack(side=TOP, pady=10)

    label_user = Label(frame1, text="Enter your email ID:", font=('Arial', 10, 'bold'), fg='black', bg = "#FF5733")
    label_user.pack(side=TOP)

    entry_user = Entry(frame1, font=("Helvetica", 10))
    entry_user.pack(side=TOP)

    label_pass = Label(frame2, text="Enter your password:", font=('Arial', 10, 'bold'), fg='black', bg = "#FF5733")
    label_pass.pack(side=TOP)

    entry_pass = Entry(frame2, font=("Helvetica", 10), show="*")
    entry_pass.pack(side=TOP)

    roles = ["UG Student", "Teacher", "PG Student"]
    selected_role = StringVar()
    selected_role.set(roles[0])

    label_role = Label(frame3, text="Select your role:", font=('Arial', 10, 'bold'), fg='black', bg="#FF5733")
    label_role.pack(side=TOP)

    option_menu = OptionMenu(frame3, selected_role, *roles)
    option_menu.config(font=("Helvetica", 10), bg="#FF5733")
    option_menu.pack(side=TOP)

    additional_details_frame = Frame(signupWindow, bg="#FF5733")
    additional_details_frame.pack(side=TOP)

    def displayAdditionalDetails():
        role = selected_role.get()
        clearAdditionalDetailsFrame()

        if role == "Teacher":
            label_department = Label(additional_details_frame, text="Enter your department:",
                                      font=('Arial', 10, 'bold'), fg='black', bg = "#FF5733")
            label_department.pack(side=TOP)

            entry_department = Entry(additional_details_frame, font=("Helvetica", 10))
            entry_department.pack(side=TOP)

        elif role == "UG Student":
            label_department = Label(additional_details_frame, text="Enter your department:",
                                      font=('Arial', 10, 'bold'), fg='black', bg = "#FF5733")
            label_department.pack(side=TOP)

            entry_department = Entry(additional_details_frame, font=("Helvetica", 10))
            entry_department.pack(side=TOP)

            label_year_of_graduation = Label(additional_details_frame, text="Enter your year of graduation:",
                                             font=('Arial', 10, 'bold'), fg='black', bg = "#FF5733")
            label_year_of_graduation.pack(side=TOP)

            entry_year_of_graduation = Entry(additional_details_frame, font=("Helvetica", 10))
            entry_year_of_graduation.pack(side=TOP)

        elif role == "PG Student":
            label_department = Label(additional_details_frame, text="Enter your department:",
                                      font=('Arial', 10, 'bold'), fg='black', bg = "#FF5733")
            label_department.pack(side=TOP)

            entry_department = Entry(additional_details_frame, font=("Helvetica", 10))
            entry_department.pack(side=TOP)

        submit_details = Button(additional_details_frame, text="Submit",
                                command=lambda: submitSignUp(role, entry_user.get(), entry_pass.get(),
                                                             entry_department.get(),
                                                             entry_year_of_graduation.get() if role == "UG Student" else ""),
                                font=("Helvetica", 10))
        submit_details.pack(side=TOP)

    def clearAdditionalDetailsFrame():
        for widget in additional_details_frame.winfo_children():
            widget.destroy()

    def submitSignUp(role, username, password, department, year_of_graduation):
        def checkUserId():
            flag = 0
            for i, char in enumerate(username):
                if char == '@':
                    x = username[i:]
                    if x in ['@gmail.com', '@outlook.com', '@gmail.cc', '@kgpian.iitkgp.ac.in']:
                        print("User ID valid.")
                        flag = 1
            if flag == 0:
                messagebox.showinfo("Can't use this", "Email ID Invalid.")
                return False
            return True

        def checkPassword():
            if len(password) < 8:
                messagebox.showinfo("Password is bad", "Password is too weak.")
                return False
            elif len(password) > 12:
                messagebox.showinfo("Password is bad", "Password is too long.")
                return False
            else:
                a = b = c = 0
                for x in password:
                    if 'A' <= x <= 'Z':
                        a = 1
                    elif 'a' <= x <= 'z':
                        b = 1
                    elif x == ' ':
                        messagebox.showinfo("Password is bad", "Password can't have spaces.")
                        return False
                    else:
                        c = 1
                if a == 0:
                    messagebox.showinfo("Password is bad", "Password needs to have at least one upper case letter.")
                    return False
                elif b == 0:
                    messagebox.showinfo("Password is bad", "Password needs to have at least one lower case letter.")
                    return False
                elif c == 0:
                    messagebox.showinfo("Password is bad", "Password needs to have at least one symbol.")
                    return False
                else:
                    print("Password accepted")
                    return True

        if not checkUserId() or not checkPassword():
            return

        if role == "Teacher":
            user_instance = Teacher(username, password, role, department)
        elif role == "UG Student":
            user_instance = UGStudent(username, password, role, department, year_of_graduation)
        elif role == "PG Student":
            user_instance = PGStudent(username, password, role, department)

        global listOfDetails
        listOfDetails.append(user_instance)
        saveDetails(listOfDetails)
        signupWindow.destroy()

    submit_role_button = Button(frame3, text="Submit Role", command=displayAdditionalDetails,
                                font=("Helvetica", 10))
    submit_role_button.pack(side=TOP)

    signupWindow.mainloop()


def userSignIn():
    loginWindow = Tk()

    loginWindow.geometry("500x300")
    loginWindow.title("Login Portal")
    loginWindow.configure(bg="#FF5733")

    frame1 = Frame(loginWindow, bg = "#FF5733")
    frame1.pack(side=TOP, pady=10)

    frame2 = Frame(loginWindow, bg = "#FF5733")
    frame2.pack(side=TOP, pady=10)

    frame3 = Frame(loginWindow, bg = "#FF5733")
    frame3.pack(side=TOP, pady=10)

    label_user = Label(frame1, text="Enter your email ID:", font=('Arial', 10, 'bold'), fg='black', bg = "#FF5733")
    label_user.pack(side=TOP)

    entry_user = Entry(frame1, font=("Helvetica", 10))
    entry_user.pack(side=TOP)

    label_pass = Label(frame2, text="Enter your password:", font=('Arial', 10, 'bold'), fg='black', bg = "#FF5733")
    label_pass.pack(side=TOP)

    entry_pass = Entry(frame2, font=("Helvetica", 10), show="*")
    entry_pass.pack(side=TOP)

    def submitLogin():
        user = entry_user.get()
        password = entry_pass.get()

        def checkIfUserExists():
            flag = 0
            for x in listOfDetails:
                if x.username == user:
                    flag = 1
                    if x.role == "Teacher" and x.password == password:
                        print("Signed In.")
                        loginWindow.destroy()
                        showProfile(x)
                    elif x.role != "Teacher" and x.password == password:
                        print("Signed In.")
                        loginWindow.destroy()
                        showProfile(x)
                    else:
                        x.consecutive_wrong_attempts += 1
                        messagebox.showinfo("Incorrect Password", f"Wrong password. Attempt {x.consecutive_wrong_attempts} of 3")
                        if x.consecutive_wrong_attempts == 3:
                            messagebox.showinfo("Too many attempts", "You have reached the maximum number of wrong attempts. Account deleted.")
                            listOfDetails.remove(x)
                            loginWindow.destroy()
                            mainPage()

            if flag == 0:
                messagebox.showinfo("User Not Found", "User doesn't exist")

        checkIfUserExists()

    def showProfile(user_instance):
        profileWindow = Tk()
        profileWindow.geometry("500x300")
        profileWindow.title("Profile")
        profileWindow.configure(bg="#FF5733")

        label_user = Label(profileWindow, text=f"Welcome, {user_instance.username}!", font=('Arial', 14, 'bold'),
                       fg='black', bg="lightgreen")
        label_user.pack(side=TOP, pady=10)
        
        def showDetails():
            detailsWindow = Tk()
            detailsWindow.geometry("300x200")
            detailsWindow.title("User Details")
            detailsWindow.configure(bg="#FF5733")

            label_username = Label(detailsWindow, text=f"Username: {user_instance.username}", font=('Arial', 10),
                                   fg='black', bg = "#FF5733")
            label_username.pack(side=TOP)

            label_role = Label(detailsWindow, text=f"Role: {user_instance.role}", font=('Arial', 10),
                              fg='black', bg = "#FF5733")
            label_role.pack(side=TOP)

            label_department = Label(detailsWindow, text=f"Department: {user_instance.department}",
                                         font=('Arial', 10), fg='black', bg = "#FF5733")
            label_department.pack(side=TOP)

            if user_instance.role == "UG Student":
                label_year_of_graduation = Label(detailsWindow,
                                                 text=f"Year of Graduation: {user_instance.year_of_graduation}",
                                                 font=('Arial', 10), fg='black', bg = "#FF5733")
                label_year_of_graduation.pack(side=TOP)

            detailsWindow.mainloop()

        def updateDetails():
            profileWindow.destroy()
            rootUpdateDetails = Tk()
            rootUpdateDetails.geometry("500x300")
            rootUpdateDetails.title("Update Details")
            rootUpdateDetails.configure(bg="#FF5733")

            frame1 = Frame(rootUpdateDetails, bg = "#FF5733")
            frame1.pack(side=TOP)

            label_password = Label(frame1, text="Enter your password:", font=('Arial', 10, 'bold'), fg='black',
                                   bg = "#FF5733")
            label_password.pack(side=TOP)

            entry_password = Entry(frame1, font=("Helvetica", 12), show="*")
            entry_password.pack(side=TOP)

            frame2 = Frame(rootUpdateDetails, bg = "#FF5733")
            frame2.pack(side=TOP)

            label_details = Label(frame2, text="Select detail to update:", font=('Arial', 10, 'bold'), fg='black',
                                  bg = "#FF5733")
            label_details.pack(side=TOP)

            details_options_teacher = ["Email", "Password", "Department"]
            details_options_student = ["Email", "Password", "Department"]

            selected_detail = StringVar()
            if user_instance.role == "Teacher":
                selected_detail.set(details_options_teacher[0])
                option_menu = OptionMenu(frame2, selected_detail, *details_options_teacher)
            elif user_instance.role == "UG Student" or user_instance.role == "PG Student":
                selected_detail.set(details_options_student[0])
                option_menu = OptionMenu(frame2, selected_detail, *details_options_student)

            option_menu.config(font=("Helvetica", 10), bg = "#FF5733")
            option_menu.pack(side=TOP)

            frame3 = Frame(rootUpdateDetails, bg = "#FF5733")
            frame3.pack(side=TOP)

            label_new_value = Label(frame3, text="Enter new value:", font=('Arial', 10, 'bold'), fg='black',
                                    bg = "#FF5733")
            label_new_value.pack(side=TOP)

            entry_new_value = Entry(frame3, font=("Helvetica", 10))
            entry_new_value.pack(side=TOP)

            def updateAndClose():
                entered_password = entry_password.get()
                if entered_password == user_instance.password:
                    detail_to_update = selected_detail.get()
                    new_value = entry_new_value.get()

                    if detail_to_update == "Email":
                        user_instance.username = new_value
                    elif detail_to_update == "Password":
                        user_instance.password = new_value
                    elif detail_to_update == "Department" and (
                            user_instance.role == "Teacher" or user_instance.role == "UG Student"):
                        user_instance.department = new_value

                    saveDetails(listOfDetails)
                    rootUpdateDetails.destroy()
                    showProfile(user_instance)
                else:
                    label_error = Label(rootUpdateDetails, text="Incorrect password!", font=("Helvetica", 10),
                                        bg = "#FF5733")
                    label_error.pack(side=TOP)

            submit_details = Button(frame3, text="Update", command=updateAndClose, font=("Helvetica", 10))
            submit_details.pack(side=TOP)

            rootUpdateDetails.mainloop()

        def deRegister():
            for x in listOfDetails:
                if x.username == user_instance.username:
                    listOfDetails.remove(x)
                    saveDetails(listOfDetails)
                    profileWindow.destroy()

        def logOut():
            saveDetails(listOfDetails)
            profileWindow.destroy()

        submit_details = Button(profileWindow, text="View Profile", command=showDetails, font=("Helvetica", 10))
        submit_details.pack(side=TOP, pady=5)

        submit_details = Button(profileWindow, text="Update Details", command=updateDetails,
                                font=("Helvetica", 10))
        submit_details.pack(side=TOP, pady=5)

        submit_details = Button(profileWindow, text="Delete Account", command=deRegister,
                                font=("Helvetica", 10))
        submit_details.pack(side=TOP, pady=5)

        submit_details = Button(profileWindow, text="Log Out", command=logOut, font=("Helvetica", 10))
        submit_details.pack(side=TOP, pady=5)

        profileWindow.mainloop()

    submit_details = Button(frame3, text="Submit", command=submitLogin, font=("Helvetica", 10))
    submit_details.pack(side=TOP)

    loginWindow.mainloop()

def mainPage():
    window = Tk()

    window.geometry("500x300")
    window.title("Login Portal")
    window.configure(bg="#FF5733")  # Flashy Orange Background

    label1 = Label(window, text="Welcome!", font=('Arial', 16, 'bold'), fg='white', bg="#FF5733")  # White text on flashy orange background
    label1.pack(side=TOP, pady=20)

    frame1 = Frame(window, bg="#FF5733")  # Flashy Orange Background
    frame1.pack(side=TOP, pady=10)

    signin = Button(window, text="Sign In", command=signIn, font=("Arial", 12), bg="#3498db", fg="white")  # Green button
    signin.pack(side=TOP, pady=10)

    signup = Button(window, text="Sign Up", command=signUp, font=("Arial", 12), bg="#3498db", fg="white")  # Blue button
    signup.pack(side=BOTTOM, pady=10)

    label1 = Label(window, text="Don't have an account?", font=('Arial', 12, 'bold'), fg='white', bg="#FF5733")  # White text on flashy orange background
    label1.pack(side=BOTTOM, pady=10)

    window.mainloop()

saveDetails(listOfDetails)

mainPage()
