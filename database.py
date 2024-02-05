"""
Database access layer for CRUD operations
"""

import config
import sqlite3
import matplotlib.image as mpimg
import pickle
import pandas as pd
from datetime import date

current_date = date.today()
today = current_date.strftime('%d/%m/%Y')


conn = sqlite3.connect('library.db')

c = conn.cursor()

table_1 = """CREATE TABLE books ( 
ID INT PRIMARY KEY,
Genre VARCHAR(10),
Title VARCHAR(10),
Author VARCHAR(10),
Price INT,
Purchase_Date DATE
)"""
table_2 = """CREATE TABLE transactions (
Book_ID INT,
Reservation DATE,
Checkout DATE, 
Return DATE,
Member_ID INT 
)"""
table_3 = """ 
CREATE TABLE covers(Title VARCHAR(50) PRIMARY KEY, Cover BLOB)
"""

list_of_book_titles = ["Allegiant",
                       "Breaking Dawn",
                       "Charlie and the Chocolate Factory",
                       "Diary of a Wimpy Kid",
                       "Divergent",
                       "Eclipse",
                       "Harry Potter and the Chamber of Secrets",
                       "Harry Potter and the Deathly Hallows",
                       "Harry Potter and the Goblet of Fire",
                       "Harry Potter and the Half-Blood Prince",
                       "Harry Potter and the Order of the Phoenix",
                       "Harry Potter and the Philosopher's Stone",
                       "Harry Potter and the Prisoner of Azkaban",
                       "Insurgent",
                       "Life and Death",
                       "Matilda",
                       "Midnight Sun",
                       "New moon",
                       "Percy Jackson & the Olympians",
                       "The Last Apprentice",
                       "The Spook's Apprentice",
                       "The Spook's Curse",
                       "The Spook's Mistake",
                       "The Spook's Secret",
                       "Twilight"]


def create_tables():
    c.execute(table_1)  # Book_info table
    c.execute(table_2)  # Loan_Reservation_History table
    c.execute(table_3)  # table for book covers
    conn.commit()


def initialize_books():
    with open('Book_info.txt', encoding='utf-16') as Book_info:
        next(Book_info)  # to skip header
        book_list = [tuple(line.split(',')) for line in Book_info]
        print(book_list)
    c.executemany("INSERT INTO books values (?,?,?,?,?,?)", book_list)
    conn.commit()


def initialize_transactions():
    with open('Loan_Reservation_History.txt', encoding='utf-16') as Loan_Reservation_History:
        next(Loan_Reservation_History)  # to skip header
        loan_list = [tuple(line.split(' ')) for line in Loan_Reservation_History]
    c.executemany("INSERT INTO transactions values (?,?,?,?,?)", loan_list)
    conn.commit()


def insertBLOB(Title, cover):
    try:
        sqliteConnection = sqlite3.connect('library.db')
        cursor = sqliteConnection.cursor()

        sqlite_insert_blob_query = """ INSERT INTO covers
                                  (Title, cover) VALUES (?, ?)"""

        img = mpimg.imread(cover)
        empPhoto = pickle.dumps(img)  # packing imagedata

        # Convert data into tuple format
        data_tuple = (Title, empPhoto)

        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")


def populating_book_cover_table():
    insertBLOB(list_of_book_titles[0], config.BOOK_DIR + "/Allegiant.png")
    insertBLOB(list_of_book_titles[1], config.BOOK_DIR + "/Breaking Dawn.png")
    insertBLOB(list_of_book_titles[2], config.BOOK_DIR + "/Charlie and the Chocolate Factory.png")
    insertBLOB(list_of_book_titles[3], config.BOOK_DIR + "/Diary of a Wimpy Kid.png")
    insertBLOB(list_of_book_titles[4], config.BOOK_DIR + "/Divergent.png")
    insertBLOB(list_of_book_titles[5], config.BOOK_DIR + "/Eclipse.png")
    insertBLOB(list_of_book_titles[6], config.BOOK_DIR + "/Harry Potter and the Chamber of Secrets.png")
    insertBLOB(list_of_book_titles[7], config.BOOK_DIR + "/Harry Potter and the Deathly Hallows.png")
    insertBLOB(list_of_book_titles[8], config.BOOK_DIR + "/Harry Potter and the Goblet of Fire.png")
    insertBLOB(list_of_book_titles[9], config.BOOK_DIR + "/Harry Potter and the Half-Blood Prince.png")
    insertBLOB(list_of_book_titles[10], config.BOOK_DIR + "/Harry Potter and the Order of the Phoenix.png")
    insertBLOB(list_of_book_titles[11], config.BOOK_DIR + "/Harry Potter and the Philosopher's Stone.png")
    insertBLOB(list_of_book_titles[12], config.BOOK_DIR + "/Harry Potter and the Prisoner of Azkaban.png")
    insertBLOB(list_of_book_titles[13], config.BOOK_DIR + "/Insurgent.png")
    insertBLOB(list_of_book_titles[14], config.BOOK_DIR + "/Life and Death.png")
    insertBLOB(list_of_book_titles[15], config.BOOK_DIR + "/Matilda.png")
    insertBLOB(list_of_book_titles[16], config.BOOK_DIR + "/Midnight Sun.png")
    insertBLOB(list_of_book_titles[17], config.BOOK_DIR + "/New moon.png")
    insertBLOB(list_of_book_titles[18], config.BOOK_DIR + "/Percy Jackson & the Olympians.png")
    insertBLOB(list_of_book_titles[19], config.BOOK_DIR + "/The Last Apprentice.png")
    insertBLOB(list_of_book_titles[20], config.BOOK_DIR + "/The Spook's Apprentice.png")
    insertBLOB(list_of_book_titles[21], config.BOOK_DIR + "/The Spook's Curse.png")
    insertBLOB(list_of_book_titles[22], config.BOOK_DIR + "/The Spook's Mistake.png")
    insertBLOB(list_of_book_titles[23], config.BOOK_DIR + "/The Spook's Secret.png")
    insertBLOB(list_of_book_titles[24], config.BOOK_DIR + "/Twilight.png")


def book_search_query(book_searched):  # returns dataframe of book info for the searched book
    book_query = pd.read_sql_query(f'SELECT * FROM books WHERE Title = " {book_searched}"', conn)
    transactions_query = pd.read_sql_query(
        f'SELECT * FROM transactions INNER JOIN books ON books.ID = transactions.Book_ID '
        f'WHERE Title = " {book_searched}"', conn)

    book_search_df = pd.DataFrame(book_query, columns=['ID', 'Genre', 'Title', 'Author', 'Price', 'Purchase_Date'])
    transaction_search_df = pd.DataFrame(transactions_query,
                                         columns=['Book_ID', 'Reservation', 'Checkout', 'Return', 'Member_ID'])
    return book_search_df, transaction_search_df


def book_cover_display_db(book_searched):  # returns the book cover of the searched book
    df = pd.read_sql('SELECT * FROM covers', conn)
    book_cover_index = df.where(df['Title'] == book_searched).last_valid_index()
    x = df[["Cover"]].applymap(lambda x: pickle.loads(x))
    return x, book_cover_index


def book_titles_query():  # returns a dataframe of the unique book titles in the db
    book_query = pd.read_sql_query(f"SELECT * FROM books", conn)
    book_info_df = pd.DataFrame(book_query, columns=['ID', 'Genre', 'Title', 'Author', 'Price', 'Purchase_Date'])

    book_titles_list = book_info_df['Title'].unique()
    book_titles_df = pd.DataFrame(book_titles_list, columns=['List of Book Titles'])
    return book_titles_df


def checkout_query():  # returns books and transactions tables in a dataframe for the checkout function
    book_query2 = pd.read_sql_query(f"SELECT * FROM books", conn)
    transactions_query2 = pd.read_sql_query(f"SELECT * FROM transactions", conn)

    book_info_df = pd.DataFrame(book_query2, columns=['ID', 'Genre', 'Title', 'Author', 'Price', 'Purchase_Date'])
    transactions_df = pd.DataFrame(transactions_query2,
                                   columns=['Book_ID', 'Reservation', 'Checkout', 'Return', 'Member_ID'])
    return book_info_df, transactions_df


def checkout_book(book_to_checkout, today, member_id_check_out):  # adds bock checkout to db
    checkout_tuple = [(int(book_to_checkout), '-', today, '-', int(member_id_check_out))]
    c.executemany("INSERT INTO transactions values (?,?,?,?,?)", checkout_tuple)
    conn.commit()


def reservation_query():  # returns books and transactions tables in a dataframe for the reserve function
    book_query4 = pd.read_sql_query(f"SELECT * FROM books", conn)
    transactions_query4 = pd.read_sql_query(f"SELECT * FROM transactions", conn)

    book_info_df = pd.DataFrame(book_query4, columns=['ID', 'Genre', 'Title', 'Author', 'Price', 'Purchase_Date'])
    transactions_df = pd.DataFrame(transactions_query4,
                                   columns=['Book_ID', 'Reservation', 'Checkout', 'Return', 'Member_ID'])
    return book_info_df, transactions_df


def reserve_book(book_to_reserve, today, reserve_member):  # adds book reservation to db
    reserve_tuple = [(int(book_to_reserve), today, '-', '-', int(reserve_member))]
    c.executemany("INSERT INTO transactions values (?,?,?,?,?)", reserve_tuple)
    conn.commit()


def return_query():  # returns books and transactions tables in a dataframe for the return function
    book_query3 = pd.read_sql_query(f"SELECT * FROM books", conn)
    transactions_query3 = pd.read_sql_query(f"SELECT * FROM transactions", conn)

    book_info_df = pd.DataFrame(book_query3, columns=['ID', 'Genre', 'Title', 'Author', 'Price', 'Purchase_Date'])
    transactions_df = pd.DataFrame(transactions_query3,
                                   columns=['Book_ID', 'Reservation', 'Checkout', 'Return', 'Member_ID'])
    return book_info_df, transactions_df


def return_book(book_to_return, today):  # adds book return to db
    return_tuple = [(int(book_to_return), '-', '-', today, '-')]
    c.executemany("INSERT INTO transactions values (?,?,?,?,?)", return_tuple)
    conn.commit()


if __name__ == "__main__":

    # testing book checkout function
    checkout_book(11, today, 5555)
    book_info_df1, transactions_df1 = checkout_query()
    print(transactions_df1.tail())
    print('\n book checkout has been added to the database')

    # testing book reserve function
    reserve_book(11, today, 5555)
    book_info_df2, transactions_df2 = reservation_query()
    print(transactions_df2.tail())
    print('\n book reservation has been added to the database')

    # testing book return function
    return_book(11, today)
    book_info_df3, transactions_df3 = checkout_query()
    print(transactions_df3.tail())
    print('\n book return has been added to the database')

