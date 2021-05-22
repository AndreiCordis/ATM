import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, NewAccountPage, MenuPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#b3d9ff")
        self.controller = controller
        self.controller.title("ATM")
        self.controller.state("zoomed")
        self.controller.iconphoto(False,
                        tk.PhotoImage(file="img/atm-machine.png"))

        self.users = {}  # empty dictionary
        self.loadUsers()

        headingLabel1 = tk.Label(self,
                                 text="IETI BANK",
                                 font=("Helvetica", 45, "bold"),
                                 foreground="white",
                                 background="#b3d9ff")

        headingLabel1.pack(pady=25)

        space_label = tk.Label(self, height=4, bg="#b3d9ff")
        space_label.pack()

        username_label = tk.Label(self,
                                  text="Enter your username",
                                  font=("Helvetica", 13),
                                  bg="#b3d9ff",
                                  fg="white")
        username_label.pack(pady=10)

        my_username = tk.StringVar()
        username_entry_box = tk.Entry(self,
                                      textvariable=my_username,
                                      font=("Helvetica",12),
                                      width=22)
        username_entry_box.pack(ipady=7)

        password_label = tk.Label(self,
                                  text="Enter your PIN",
                                  font=("Helvetica", 13),
                                  bg="#b3d9ff",
                                  fg="white")
        password_label.pack(pady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self,
                                      textvariable=my_password,
                                      font=("Helvetica",12),
                                      width=22)
        password_entry_box.pack(ipady=7)

        def make_stars(_):
            password_entry_box.configure(fg="black", show="*")
        password_entry_box.bind("<FocusIn>", make_stars)



        enter_button = tk.Button(self,
                                 text='Enter',
                                 command=lambda: self.checkValidUsernamePassword(),
                                 relief="raised",
                                 borderwidth=4,
                                 width=25,
                                 height=3,
                                 bg="#6495ED")
        enter_button.pack(pady=15)

        new_account_button = tk.Button(self,
                                 text='Create new account',
                                 command=lambda: controller.show_frame("NewAccountPage"),
                                 relief="raised",
                                 borderwidth=4,
                                 width=25,
                                 height=3,
                                 bg="#87CEEB")
        new_account_button.pack(pady=15)

        incorrect_password_label = tk.Label(self,
                                            text="",
                                            font=("Helvetica", 13),
                                            fg="white",
                                            bg="#99ccff",
                                            anchor="n")
        incorrect_password_label.pack(fill="both", expand=True)

        def checkValidUserPass(self):
            user = self.userNameVar.get()
            attemptPassword = self.passwordVar.get()
            try:
                realPassword = self.users[user]
                if attemptPassword == realPassword:
                     controller.show_frame("MenuPage")  # They are good - do something

            except KeyError:  # That user name is not in our dictionary of users
                self.invalidUser()

        def invalidUser():
            incorrect_password_label["text"]="Incorrect Password"

    def loadUsers(self):
    # Loadup all of the usernames and passwords into a dictionary
        with open("LoginDetails.txt", 'r') as f:
            for row in f:
                user, password = row.split(" ")
                self.users[user] = password

class NewAccountPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.controller = controller



class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="green")
        self.controller = controller



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
