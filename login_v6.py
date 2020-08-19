import random
import smtplib
#from captcha.image import ImageCaptcha
import sqlite3
import tkinter.messagebox as tkMessageBox
from tkinter import *
import re
from tkinter import ttk,messagebox
import base64
import tkinter.messagebox
from captcha.image import ImageCaptcha
import string
import random
from PIL import ImageTk,Image
import cv2

root = Tk()
root.title("Our DB Project is Here !!!")


width = 1250
height = 750
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


# =======================================VARIABLES=====================================
USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
image_captcha = ""
ans_captcha = StringVar()
# =======================================METHODS=======================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("db_member.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")


def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def show1():
    root.configure(background = "blue")
    print("THANKS FOR USING OUR SERVICE ")

#=======================================Encrypt & Decrypt================================
def encrypt(message1):
    message_bytes = message1.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def decrypt(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message


# =======================================Login Screen=======================================

# ============================================CAPTCHA FUNCTION ==================================


def generate_captcha():
	data_set = list(string.ascii_letters+string.digits)
	s = ""
	for i in range(6):
		a = random.choice(data_set)
		s = s+a
		data_set.remove(a)

	global image_captcha
	image_captcha = s
	return s

def get_image():
	return image_captcha


def LoginForm():
    
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=80)
    
    lbl_username = Label(LoginFrame, text="Username* ", font=('times new roman', 22), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password* ", font=('times new roman', 22), bd=18)
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('times new roman', 18),fg="red")
    lbl_result1.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, font=('times new roman', 20), textvariable=USERNAME,bg="lavender", width=20)
    username.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('times new roman', 20), textvariable=PASSWORD,bg="lavender", width=20, show="*")
    password.grid(row=2, column=1)
    captcha = Label(LoginFrame, text="CapTcha* ", font=('times new roman', 22), bd=18)
    captcha.grid(row=4)
    generate_first_image_login()
    password = Entry(LoginFrame, font=('times new roman', 20),bg="lavender", textvariable=ans_captcha, width=20, show="*")
    password.grid(row=5, column=1)
    #==================================Creating a photoimage object to use image===========================
    photo = PhotoImage(Image.open("regenerate.jpeg"))
    # Resizing image to fit on button 
    photoimage = photo.subsample(3, 3)
    # here, image option is used to
    # set image on button
    # compound option is used to align
    # image on LEFT side of button
    Button(LoginFrame, text = 'Click Me !', image = photoimage ,compound = LEFT, command = regenerate_image_captcha_login).grid(row = 4, column = 4)
    btn_login = Button(LoginFrame, text="LOGIN", font=('times new roman', 18),bg="green",fg="white",bd=5,activebackground="green1",cursor="hand2", width=35, command=Login)
    btn_login.grid(row=6, columnspan=2, pady=20)

    lbl_register = Label(LoginFrame, text="REGISTER", fg="brown4", font=('algerian', 13,"bold underline"),cursor="hand2")
    lbl_register.grid(row=0, sticky=SW)
    lbl_register.bind('<Button-1>', Toggle_FromLogin_ToRegister)
    lbl_forgetpassword = Label(LoginFrame, text="Forgot Password?", fg="Blue4", font=('algerian', 12),cursor="hand2")
    lbl_forgetpassword.grid(row=6,columnspan=2, pady=4)
    lbl_forgetpassword.bind('<Button-1>', Toggle_FromLogin_ToForgetPass)
    USERNAME.set("")
    PASSWORD.set("")
   

def generate_first_image_login():
    global img,im,imgtk,Show_image
    img = ImageCaptcha()
    s = generate_captcha()
    value = img.generate(s)
    img.write(s,"cap.png")
    img = cv2.imread("cap.png")
    im = Image.fromarray(img)
    imgtk = ImageTk
    imgtk = ImageTk.PhotoImage(image = im)
    Show_image = tkinter.Label(LoginFrame, image = imgtk).grid(row = 4, column = 1)

	#=========================================================================================
	

def regenerate_image_captcha_login():
    global img,im,imgtk,Show_image
    img = ImageCaptcha()
    s = generate_captcha()
    value = img.generate(s)
    img.write(s,"cap.png")
    img = cv2.imread("cap.png")
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image = im)
    Show_image = tkinter.Label(LoginFrame, image = imgtk).grid(row = 4, column = 1)




# def check_image_captcha():
#     global ans
# 	if ans.get() == get_image():
# 		tkinter.messagebox.showinfo("Success!","CAPTCHA code Matched.")
# 		ans.set("")
# 	else:
# 		tkinter.messagebox.showinfo("Wrong!","CAPTCHA code does not Match.")
# 		ans.set("")


def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=40)
    lbl = Label(RegisterFrame, text="")
    lbl.grid(row=1)
    lbl1 = Label(RegisterFrame, text="")
    lbl1.grid(row=2)
    lbl2 = Label(RegisterFrame, text="")
    lbl2.grid(row=3)
    lbl_username = Label(RegisterFrame, text="Username* ", font=('times new roman', 22), bd=25)
    lbl_username.grid(row=4)
    lbl_password = Label(RegisterFrame, text="Password* ", font=('times new roman', 22), bd=25)
    lbl_password.grid(row=5)
    lbl_firstname = Label(RegisterFrame, text="Firstname* ", font=('times new roman', 22), bd=25)
    lbl_firstname.grid(row=6)
    lbl_lastname = Label(RegisterFrame, text="Lastname* ", font=('times new roman', 22), bd=25)
    lbl_lastname.grid(row=7)
    lbl_result2 = Label(RegisterFrame, text="", font=('times new roman', 18))
    lbl_result2.grid(row=9, columnspan=2)
    lbl_lastnam = Label(RegisterFrame, text="CaPTcHa* ", font=('times new roman', 22), bd=25)
    lbl_lastnam.grid(row=8)
    username = Entry(RegisterFrame,text="Email-ID*", font=('times new roman', 20),bg="lavender", textvariable=USERNAME, width=20)
    username.grid(row=4, column=1)
    password = Entry(RegisterFrame, font=('times new roman', 20),bg="lavender", textvariable=PASSWORD, width=20, show="*")
    password.grid(row=5, column=1)
    firstname = Entry(RegisterFrame, font=('times new roman', 20),bg="lavender", textvariable=FIRSTNAME, width=20)
    firstname.grid(row=6, column=1)
    lastname = Entry(RegisterFrame, font=('times new roman', 20),bg="lavender", textvariable=LASTNAME, width=20)
    lastname.grid(row=7, column=1)
    #chk = Checkbutton(root,text="I Agree terms for saving my detalis in your database",font=("arial",12))
    #ckk.grid(row=9)
    generate_first_image()
    captcha_entry = Entry(RegisterFrame, font=('times new roman', 20),bg="lavender", textvariable=ans_captcha, width=20, show="*")
    captcha_entry.grid(row = 9, column = 1)
    #==================================Creating a photoimage object to use image===========================
    photo = PhotoImage(file = r"circle.png")
    # Resizing image to fit on button 
    photoimage = photo.subsample(3, 3)
    # here, image option is used to
    # set image on button
    # compound option is used to align
    # image on LEFT side of button
    Button(root, text = 'Click Me !', image = photoimage ,compound = LEFT, command = regenerate_image_captcha).grid(row = 8, column = 6)
    btn_login = Button(RegisterFrame, text="REGISTER", font=('times new roman', 18),bg="green",fg="white",bd=5,activebackground="seagreen1",cursor="hand2", width=35, command=Register)
    btn_login.grid(row=9, columnspan=2, pady=85)
    lbl_login = Label(RegisterFrame, text="LOGIN PAGE",cursor="hand2", fg="Brown4", font=('algerian ', 12,"bold underline"))
    lbl_login.grid(row=3, sticky=W)
    lbl_login.bind('<Button-1>', Toggle_FromRegister_ToLogin)
    USERNAME.set("")
    PASSWORD.set("")

    #===============================Captcha==================================================
def generate_first_image():
    global img,im,imgtk,Show_image
    img = ImageCaptcha()
    s = generate_captcha()
    value = img.generate(s)
    img.write(s,"cap.png")
    img = cv2.imread("cap.png")
    im = Image.fromarray(img)
    imgtk = ImageTk
    imgtk = ImageTk.PhotoImage(image = im)
    Show_image = tkinter.Label(RegisterFrame, image = imgtk).grid(row = 8, column = 1)
		
	#=========================================================================================
def regenerate_image_captcha():
    global img,im,imgtk,Show_image
    img = ImageCaptcha()
    s = generate_captcha()
    value = img.generate(s)
    img.write(s,"cap.png")
    img = cv2.imread("cap.png")
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image = im)
    Show_image = tkinter.Label(RegisterFrame, image = imgtk).grid(row = 8, column = 1)
	

# =======================================Forget Password Screen=======================================
def ForgetPasswordForm():
    global ForgetPasswordFrame, lbl_result3
    ForgetPasswordFrame = Frame(root)
    ForgetPasswordFrame.pack(side=TOP, pady=80)
    lbl_username = Label(ForgetPasswordFrame, text="Username* ", font=('times new roman', 23), bd=18)
    lbl_username.grid(row=2)
    lbl_result3 = Label(ForgetPasswordFrame, text="", font=('times new roman', 18))
    lbl_result3.grid(row=4, columnspan=2)
    username = Entry(ForgetPasswordFrame, font=('times new roman', 20),bg="lavender", textvariable=USERNAME, width=23)
    username.grid(row=2, column=1)
    btn_ForgetPassword = Button(ForgetPasswordFrame, text="SEND E-MAIL",font=("times new roman",18),bg="green",fg="white",bd=5,activebackground="seagreen1",cursor="hand2", width=35,
                                command=ForgetPassword)
    btn_ForgetPassword.grid(row=5, columnspan=2, pady=20)
    lbl_login1 = Label(ForgetPasswordFrame, text="LOGIN", fg="brown4",cursor="hand2", font=('algerian', 12,"bold underline"))
    lbl_login1.grid(row=0, sticky=W)
    lbl_login1.bind('<Button-1>', Toggle_FromForgetPass_ToLogin)
    USERNAME.set("")

# =======================================Toggling(Routing) Of Screens=======================================
def Toggle_FromRegister_ToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()


def Toggle_FromLogin_ToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()


def Toggle_FromLogin_ToForgetPass(event=None):
    LoginFrame.destroy()
    ForgetPasswordForm()


def Toggle_FromForgetPass_ToLogin(event=None):
    ForgetPasswordFrame.destroy()
    LoginForm()


# =======================================Register Method=======================================
def Register():
    username_demo = USERNAME.get()
    password_demo = PASSWORD.get()
    firstname = FIRSTNAME.get()
    lastname = LASTNAME.get()
    username = encrypt(username_demo)
    password = encrypt(password_demo)
 
    Database()
    if username == "" or password == "" or firstname == "" or lastname == "":
        lbl_result2.config(text="Please complete the required field!", fg="red")
  
    else:
        if not check_mail(username_demo):
            lbl_result2.config(text="Invalid E-mail !", fg="red")

        elif not check_password(password_demo):
            lbl_result2.config(text="-Ivalid Password[A-Z,a-z,0-9,!@#$%^&*]", fg="red")
        

        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (username,))
            if cursor.fetchone() is not None:
                lbl_result2.config(text="Username is already taken", fg="red")
            else:
                cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)",
                               (str(username), str(password), str(firstname), str(lastname)))
                conn.commit()
                USERNAME.set("")
                PASSWORD.set("")
                FIRSTNAME.set("")
                LASTNAME.set("")
                lbl_result2.config(text="Successfully Created!", fg="black")
            cursor.close()
            conn.close()
       


# =======================================Login Method=======================================
def Login():
    username_demo = USERNAME.get()
    password_demo = PASSWORD.get()
    username = encrypt(username_demo)
    password = encrypt(password_demo)
    Database()
    if username == "" or password == "":
        lbl_result1.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?",
                       (username, password))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="You Successfully Login", fg="blue")
            USERNAME.set("")
            PASSWORD.set("")
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
        conn.commit()
        cursor.close()
        conn.close()


# =======================================Forget Password Method=======================================
def ForgetPassword():
    username_demo = USERNAME.get()
    username_info = encrypt(username_demo)
    Database()
    if username_info == "":
        lbl_result3.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? ", (username_info,))

        if cursor.fetchone() is not None:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("databaseproject2000@gmail.com", "database@2000")
            password = get_random_password_string(8)
            message = '''
            Hello,
            We wanted to let you know that your OurSQL password was reset.
            Please do not reply to this email with your password. We will never ask for your password, and we strongly discourage you from sharing it with anyone.
            Your Password Is : '''
            final_msg = message + password
            server.sendmail("databaseproject2000@gmail.com", username_demo, final_msg)
            server.quit()
            password_updater(username_info, password)
            lbl_result3.config(text="Email Sent Successfully", fg="blue")

        else:
            lbl_result3.config(text="Invalid Username or password", fg="red")

        USERNAME.set("")
        cursor.close()
        conn.commit()
        conn.close()
        

def password_updater(username_info, password_info):
    Database()
    password_demo = encrypt(password_info)
    cursor.execute("UPDATE `member` SET `password` = ? WHERE `username` = ? ",
                   (password_demo, username_info))


def get_random_password_string(length):
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password


# =======================================Validating Methods=======================================
def check_mail(email_info):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    var = True if (re.search(regex, email_info)) else False
    return var


def check_password(password_info):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pattern = re.compile(reg)
    match = re.search(pattern, password_info)
    var = True if match else False
    return var


LoginForm()

# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", font=("ALGERIAN",20),menu=filemenu)
root.config(menu=menubar)

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
