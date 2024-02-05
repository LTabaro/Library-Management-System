from tkinter import *
from tkinter import ttk
from datetime import date
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import bookSearch as BS
import bookCheckout as BC
import bookReturn as BR
import bookSelect as BE

global today
current_date = date.today()
today = current_date.strftime('%d/%m/%Y')
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

window = Tk()
window.title("Welcome to Leon's Library Management System")
window.geometry("3000x3000")
window.config(background="PaleVioletRed4")


class LibraryInterface:

    def __init__(self, master):

        # ---------------------------- Creating tabs ------------------------------- #

        self.my_notebook = ttk.Notebook(master)
        self.my_notebook.pack()

        self.search_frame = Frame(self.my_notebook, width=3000, height=3000, bg="white")
        self.book_title_frame = Frame(self.my_notebook, width=3000, height=3000, bg="white")
        self.checkout_frame = Frame(self.my_notebook, width=3000, height=3000, bg="white")
        self.reserve_frame = Frame(self.my_notebook, width=3000, height=3000, bg="white")
        self.return_frame = Frame(self.my_notebook, width=3000, height=3000, bg="white")
        self.select_frame = Frame(self.my_notebook, width=3000, height=3000, bg="white")

        self.search_frame.pack(fill="both", expand=1)
        self.book_title_frame.pack(fill="both", expand=1)
        self.checkout_frame.pack(fill="both", expand=1)
        self.reserve_frame.pack(fill="both", expand=1)
        self.return_frame.pack(fill="both", expand=1)
        self.select_frame.pack(fill="both", expand=1)

        self.my_notebook.add(self.search_frame, text="Search Book Availability")
        self.my_notebook.add(self.book_title_frame, text="List of Book Titles")
        self.my_notebook.add(self.checkout_frame, text="Checkout Books")
        self.my_notebook.add(self.reserve_frame, text="Reserve a book here")
        self.my_notebook.add(self.return_frame, text="Return Books")
        self.my_notebook.add(self.select_frame, text="Recommended Books for Purchase")

        # ---------------------------- Tab for searching book availability ------------------------------- #

        self.search_entry = Entry(self.search_frame, width=40)
        self.search_entry.grid(row=0, column=0)

        self.search_button = Button(self.search_frame, text="Search", command=self.book_search_clicked)
        self.search_button.grid(row=1, column=0, pady=5)

        self.search_status_label = Label(self.search_frame, text=" ", bd=1, relief=SUNKEN, anchor=W)

        # displaying availability dataframe in UI
        self.my_tree = ttk.Treeview(self.search_frame)

        # ---------------------------- Tab for reserving a book ------------------------------- #

        self.reserve_member_entry = Entry(self.reserve_frame, width=10)
        self.reserve_member_entry.grid(row=0, column=1)

        self.reserve_book_entry = Entry(self.reserve_frame, width=10)
        self.reserve_book_entry.grid(row=1, column=1)

        self.reserve_button = Button(self.reserve_frame, text="Reserve", command=self.reserve_clicked)
        self.reserve_button.grid(row=1, column=2)

        self.reserve_member_label = Label(self.reserve_frame, text="Enter Member ID")
        self.reserve_member_label.grid(row=0, column=0)

        self.reserve_book_label = Label(self.reserve_frame, text="Enter Book ID")
        self.reserve_book_label.grid(row=1, column=0)

        self.reserve_status_label = Label(self.reserve_frame, text=" ", bd=1, relief=SUNKEN, anchor=E)

        # ---------------------------- Tab for checking out a book  ------------------------------- #

        self.member_checkout_id = Entry(self.checkout_frame, width=10)
        self.member_checkout_id.grid(row=0, column=1)

        self.book_id_checkout = Entry(self.checkout_frame, width=10)
        self.book_id_checkout.grid(row=1, column=1)

        self.member_checkout_label = Label(self.checkout_frame, text="Enter Member ID")
        self.member_checkout_label.grid(row=0, column=0)

        self.book_id_checkout_label = Label(self.checkout_frame, text="Enter Book ID")
        self.book_id_checkout_label.grid(row=1, column=0)

        self.checkout_button = Button(self.checkout_frame, text="Check out", command=self.checkout_clicked)
        self.checkout_button.grid(row=1, column=2)

        self.checkout_status_label = Label(self.checkout_frame, text=" ", bd=1, relief=SUNKEN, anchor=E)

        # ---------------------------- Tab for returning a book  ------------------------------- #

        self.book_id_return = Entry(self.return_frame, width=10)
        self.book_id_return.grid(row=0, column=0)

        self.return_label = Label(self.return_frame, text="Enter Book ID ")
        self.return_label.grid(row=1, column=0)

        self.return_button = Button(self.return_frame, text="Return", command=self.return_clicked)
        self.return_button.grid(row=0, column=1)

        self.return_status_label = Label(self.return_frame, text=" ", bd=1, relief=SUNKEN, anchor=E)

        # ---------------------------- Tab for recommended books for purchase ------------------------------- #

        self.budget_entry = Entry(self.select_frame)
        self.budget_entry.grid(row=0, column=0)

        self.budget_label = Label(self.select_frame, text="Enter Budget in £")
        self.budget_label.grid(row=1, column=0)

        self.book_recommend_button = Button(self.select_frame, command=self.recommend_clicked, text="Recommend")
        self.book_recommend_button.grid(row=0, column=1)

        self.select_status_label = Label(self.select_frame, text=" ", bd=1, relief=SUNKEN, anchor=E)

        self.select_label1 = Label(self.select_frame, text="")
        self.select_label1.grid(row=3, column=0)
        self.select_label2 = Label(self.select_frame, text="")
        self.select_label2.grid(row=4, column=0)
        self.select_label3 = Label(self.select_frame, text="")
        self.select_label3.grid(row=5, column=0)
        self.select_label4 = Label(self.select_frame, text="")
        self.select_label4.grid(row=6, column=0)
        self.select_label5 = Label(self.select_frame, text="")
        self.select_label5.grid(row=7, column=0)
        self.select_label6 = Label(self.select_frame, text="")
        self.select_label6.grid(row=8, column=0)
        self.select_label7 = Label(self.select_frame, text="")
        self.select_label7.grid(row=9, column=0)

        # ---------------------------- Tab see list of book titles ------------------------------- #

        self.book_titles_button = Button(self.book_title_frame, text="Click here to see list of book titles",
                                         command=self.book_titles_clicked)
        self.book_titles_button.pack()

        self.new_tree = ttk.Treeview(self.book_title_frame, height=12)

        self.treeScroll = ttk.Scrollbar(self.book_title_frame)
        self.treeScroll.configure(command=self.new_tree.yview)
        self.new_tree.configure(yscrollcommand=self.treeScroll.set)
        self.treeScroll.pack(side=RIGHT)
        self.new_tree.pack()

    def clear_search_frame(self):
        self.my_tree.destroy()

    def clear_search_status(self):
        self.search_status_label.config(text=" ", bg="white")

    def clear_reserve_status(self):
        self.reserve_status_label.config(text=" ", bg="white")

    def clear_reserve_entry(self):
        self.reserve_member_entry.delete(0, END)
        self.reserve_book_entry.delete(0, END)

    def clear_member_checkout(self):
        self.member_checkout_id.delete(0, END)

    def clear_book_checkout(self):
        self.book_id_checkout.delete(0, END)

    def clear_checkout_status(self):
        self.checkout_status_label.config(text=" ", bg="white")

    def clear_book_return(self):
        self.book_id_return.delete(0, END)

    def clear_return_status(self):
        self.return_status_label.config(text=" ", bg="white")

    def clear_select_status(self):
        self.select_status_label.config(text=" ", bg="white")

    # ---------------------------- bookSearch module ------------------------------- #
    def book_search_clicked(self):
        book_searched = self.search_entry.get()
        message, book_search_df = BS.book_search_function(book_searched)

        self.clear_search_status()

        self.clear_search_frame()

        if message == "Invalid book title":
            print(message)
            self.search_status_label.config(text=message, bg="red")
            self.search_status_label.grid(row=2, column=0, columnspan=2, sticky=W + E)
        else:

            # displaying book info and availability in UI
            self.my_tree = ttk.Treeview(self.search_frame)

            self.my_tree["column"] = list(book_search_df.columns)
            self.my_tree["show"] = "headings"

            for column in self.my_tree["column"]:
                self.my_tree.heading(column, text=column)
                df_rows = book_search_df.to_numpy().tolist()

            for row in df_rows:
                self.my_tree.insert("", "end", values=row)

            self.my_tree.column("#1", width=30, minwidth=30, stretch=NO)
            self.my_tree.column("#2", width=80, minwidth=80, stretch=NO)
            self.my_tree.column("#3", width=80, stretch=NO)
            self.my_tree.column("#4", width=120, minwidth=120, stretch=NO)
            self.my_tree.column("#5", width=30, minwidth=30, stretch=NO)
            self.my_tree.column("#6", width=100, minwidth=100, stretch=NO)
            self.my_tree.column("#7", width=80, minwidth=80, stretch=NO)

            # Place the treeview in search frame
            self.my_tree.grid(row=2, column=0)

            # Displaying image of searched book
            figure = BS.book_cover_display_function(book_searched)

            canvas = FigureCanvasTkAgg(figure, self.search_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=1)

    def book_titles_clicked(self):

        book_titles_df = BS.book_titles_function()

        # Displaying list of book titles in the UI
        self.new_tree["column"] = list(book_titles_df.columns)
        self.new_tree["show"] = "headings"

        for column in self.my_tree["column"]:
            self.new_tree.heading(column, text=column)

        df_rows = book_titles_df.to_numpy().tolist()

        for row in df_rows:
            self.new_tree.insert("", "end", values=row)

        # Place the treeview in search frame
        self.new_tree.pack()
        self.new_tree.configure(columns="List of Book Titles")
        self.new_tree.column("1", width=40, stretch=NO)
        self.new_tree.column("2", width=0, stretch=NO)
        self.new_tree.column("3", width=0, stretch=NO)

    # ---------------------------- bookCheckout module ------------------------------- #

    def checkout_clicked(self):
        member_id_check_out = self.member_checkout_id.get()
        book_to_checkout = self.book_id_checkout.get()

        message = BC.checkout_function(book_to_checkout, member_id_check_out)
        self.clear_member_checkout()
        self.clear_book_checkout()
        self.clear_checkout_status()
        print(message)
        if message == f"Book {book_to_checkout} successfully checked out":
            self.checkout_status_label.config(text=message, bg="green")
            self.checkout_status_label.grid(row=2, column=0, columnspan=2, sticky=W + E)
        else:
            self.checkout_status_label.config(text=message, bg="red")
            self.checkout_status_label.grid(row=2, column=0, columnspan=2, sticky=W + E)

    # ---------------------------- bookReturn module ------------------------------- #

    def return_clicked(self):
        book_to_return = int(self.book_id_return.get())
        message = BR.return_function(book_to_return)
        self.clear_book_return()
        self.clear_return_status()
        print(message)
        if message == "please enter valid book ID" or message == "This book is already available":

            self.return_status_label.config(text=message, bg="red")
            self.return_status_label.grid(row=2, column=0, columnspan=2, sticky=W + E)
        else:
            self.return_status_label.config(text=message, bg="green")
            self.return_status_label.grid(row=2, column=0, columnspan=2, sticky=W + E)

    # ---------------------------- bookCheckout module ------------------------------- #

    def reserve_clicked(self):
        book_to_reserve = int(self.reserve_book_entry.get())
        reserve_member = self.reserve_member_entry.get()

        message = BC.reserve_function(book_to_reserve, reserve_member)
        self.clear_reserve_status()
        self.clear_reserve_entry()

        print(message)
        if message == "book successfully reserved":
            self.reserve_status_label.config(text=message, bg="green")
            self.reserve_status_label.grid(row=2, column=0, columnspan=2, sticky=W + E)
        else:
            self.reserve_status_label.config(text=message, bg="red")
            self.reserve_status_label.grid(row=2, column=0, columnspan=2, sticky=W + E)

    # ---------------------------- bookSelect module ------------------------------- #

    def recommend_clicked(self):

        user_input = self.budget_entry.get()
        self.clear_select_status()
        pie_chart, ratios = BE.pie_chart()
        bar_chart = BE.bar_chart()

        if not user_input.isnumeric():
            message = "please enter a real number"
            self.select_status_label.config(text=message, bg="red")
            self.select_status_label.grid(row=2, column=0, columnspan=2, sticky=W + E)
        else:
            canvas = FigureCanvasTkAgg(pie_chart, self.select_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=0)

            canvas = FigureCanvasTkAgg(bar_chart, self.select_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=1)

            # calculating budget distribution
            budget = float(user_input)

            self.select_label1.config(text="Based on the given data, it is advisable to spend:")
            self.select_label2.config(text=f"£{round(budget * float(ratios[0]) / 100)} on Fantasy books")
            self.select_label3.config(text=f"£{round(budget * float(ratios[1]) / 100)} on Romance books")
            self.select_label4.config(text=f"£{round(budget * float(ratios[2]) / 100)} on Thriller books")
            self.select_label5.config(text=f"£{round(budget * float(ratios[3]) / 100)} on Sci-Fi books")
            self.select_label6.config(text=f"£{round(budget * float(ratios[4]) / 100)} on Comedy books")
            self.select_label7.config(text=f"£{round(budget * float(ratios[5]) / 100)} on Fairy-Tale books")


gui = LibraryInterface(window)

window.mainloop()
