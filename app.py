import tkMessageBox
from Tkinter import *

import os
from PIL import Image, ImageTk
from spider_account import *
from spider_tweet import *


class Application(Frame):
    DARK_BG = '#313131'
    LIGHT_BG = '#646464'

    def create_widgets(self):
        # Menus
        menubar = Menu(self.master, tearoff=False)
        self.master.config(menu=menubar)

        menu_file = Menu(menubar)
        menu_file.add_command(label="New Twitter Account", command=self.new)
        menu_file.add_separator()
        menu_file.add_command(label='Quit', command=self.quit_app)
        menubar.add_cascade(label='File', menu=menu_file)

        menu_help = Menu(menubar)
        menu_help.add_command(label='about', command=self.help)
        menubar.add_cascade(label='Help', menu=menu_help)

        # Header
        frame_top = Frame(self.master, height=100, width=800, relief=GROOVE, background=self.DARK_BG)
        frame_top.pack(side=TOP, fill=X)

        # Logo
        logo_img = ImageTk.PhotoImage(Image.open(os.path.dirname(__file__) + "/128.ico"))
        logo = Button(frame_top, compound=LEFT, image=logo_img, text="Squid", bg=self.DARK_BG,
                      activebackground=self.LIGHT_BG, height=50, bd=0, padx=0, pady=0, relief=FLAT)
        logo.img = logo_img
        logo.grid(row=0, column=0)
        # Header Buttons
        btn_img = ImageTk.PhotoImage(Image.open(os.path.dirname(__file__) + "/squid.gif"))
        conf_btn = Button(frame_top, compound=LEFT, image=btn_img, text='Configuration', bg=self.DARK_BG,
                          activebackground=self.LIGHT_BG)
        conf_btn.img = btn_img
        conf_btn.grid(row=0, column=1)
        publish_btn = Button(frame_top, compound=LEFT, image=btn_img, text='Pubishing')
        publish_btn.grid(row=0, column=2)
        report_btn = Button(frame_top, compound=LEFT, image=btn_img, text='Reports')
        report_btn.grid(row=0, column=3)

        # Frame Left
        self.frame_left = Frame(self.master, width=200, height=500, borderwidth=1, relief=GROOVE,
                                background=self.LIGHT_BG)
        self.frame_left.pack(side=LEFT, fill=Y, expand=False)

        # Frame Middle
        self.frame_middle = Frame(self.master, borderwidth=1, relief=GROOVE, width=600, height=500)
        self.frame_middle.pack(side=RIGHT, fill=BOTH)

        # Frame Right
        # self.frame_right = Frame(self.master, width=200, borderwidth=1, relief=GROOVE, background='#646464')
        # self.frame_right.pack(side=LEFT, fill=Y, expand=False)

        # Twitter accounts
        self.listbox_accounts = Listbox(self.frame_left, fg="#FFFFFF", bg="#313131")
        self.listbox_accounts.pack(fill=X)

    def quit_app(self):
        self.quit()

    def new(self):
        print 'New ....'
        self.account_id_label = Label(self.frame_middle, text="Account ID or Screen Name")
        self.account_id_label.pack()
        self.account_id = Entry(self.frame_middle)
        self.account_id.pack()
        self.account_insert = Button(self.frame_middle, text="Create", command=self.insert_account)
        self.account_insert.pack()

    def insert_account(self):
        name = self.account_id.get()
        self.spider_account.mining_account(name)
        self.update_accounts()

    def update_accounts(self):
        self.listbox_accounts.delete(0, END)
        total_accounts = self.spider_account.get_total_accounts()
        text = "Total Accounts : %d" % total_accounts
        self.listbox_accounts.insert(END, text)
        for account in session.query(Account).order_by(Account.name):
            self.listbox_accounts.insert(END, account.name)
        self.account_view = Button(self.frame_left, text="view account", command=self.view_account)
        self.account_view.pack()

    def view_account(self):
        name = self.listbox_accounts.curselection()
        account_name = Label(self.frame_middle, text=name)
        self.pack = account_name.pack()

    def help(self):
        tkMessageBox.showinfo("About", "bla bla")

    def feed_initial_data(self):
        self.update_accounts()

    def __init__(self, master=None):
        self.spider_account = SpiderAccount()
        self.spider_tweet = SpiderTweet()
        Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.feed_initial_data()


root = Tk()
root.minsize(width=800, height=600)
root.wm_iconbitmap("128.exr")
root.title('Squid')
root.minsize(width=800, height=600)
app = Application(master=root)
app.mainloop()
