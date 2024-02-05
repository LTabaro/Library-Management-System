"""
Control Layer for checking out and reserving books
"""

import database as DB
from datetime import date

global today
current_date = date.today()
today = current_date.strftime('%d/%m/%Y')


def checkout_function(book_to_checkout, member_id_check_out):
    """
    :param book_to_checkout: book ID to check out
    :param member_id_check_out: member that wants to check out a book
    :return: message to say book has been checked out or an error message
    """

    book_info_df, transactions_df = DB.checkout_query()

    if int(book_to_checkout) not in book_info_df['ID'].unique():
        message = "please enter valid book ID"
        return message  # invalid book ID error

    elif not member_id_check_out.isdigit() or len(member_id_check_out) != 4:
        message = "please enter 4 digit member ID number"
        return message  # invalid member ID error

    elif int(book_to_checkout) not in transactions_df['Book_ID'].unique():
        DB.checkout_book(book_to_checkout, today, member_id_check_out)
        message = f"Book {book_to_checkout} successfully checked out"
        return message  # checkout book

    else:
        last_instance_of_book = transactions_df.loc[transactions_df['Book_ID'] == int(book_to_checkout)].iloc[-1]

        if last_instance_of_book['Return'] == '-':
            message = "This book ID is currently on loan."
            return message  # book ID on loan error

        else:  # checkout book
            DB.checkout_book(book_to_checkout, today, member_id_check_out)
            message = f"Book {book_to_checkout} successfully checked out"
            return message  # book ID on loan error


def reserve_function(book_to_reserve, reserve_member):
    """

    :param book_to_reserve: book ID reserve
    :param reserve_member: member that wants to reserve a book
    :return: message to say book has been reserved or an error message
    """

    book_info_df, transactions_df = DB.reservation_query()

    if book_to_reserve not in book_info_df['ID'].unique():
        message = "please enter valid book ID"
        return message  # invalid book ID error

    elif not reserve_member.isdigit() or len(reserve_member) != 4:
        message = "please enter 4 digit member ID number"
        return message  # invalid member ID error

    elif book_to_reserve not in transactions_df['Book_ID'].unique():
        message = "This book is already available."
        return message  # book ID is already available error

    else:

        last_instance_of_book = transactions_df.loc[transactions_df['Book_ID'] == int(book_to_reserve)].iloc[-1]

        if last_instance_of_book['Return'] != '-':
            message = "This book ID is already available."
            return message  # book ID is already available error

        elif last_instance_of_book['Reservation'] != '-':
            message = "This book is already reserved. Please come back later"
            return message  # book ID is already reserved

        else:  # reserve book
            DB.reserve_book(book_to_reserve, today, reserve_member)
            message = "book successfully reserved"
            return message  # reserve book


if __name__ == "__main__":
    # ---------------------------- Testing Checkout functionalities ------------------------------- #

    # Invalid book ID error
    error_message1 = checkout_function(58, "1111")
    print(error_message1)
    print('\n Invalid book ID')
    
    # Invalid member ID error
    error_message2 = checkout_function(22, "111")
    print(error_message2)
    print('\n Member ID is not a 4 digit number')
    error_message3 = checkout_function(22, "123p")
    print(error_message3)
    print('\n Member ID is not a 4 digit number')
    
    # Book ID on loan error
    error_message4 = checkout_function(3, "2222")
    print(error_message4)
    print('\n This book is already on loan')
    error_message5 = checkout_function(5, "2222")
    print(error_message5)
    print('\n This book is already on loan')
    error_message6 = checkout_function(7, "2222")
    print(error_message6)
    print('\n This book is already on loan')
    error_message7 = checkout_function(9, "2222")
    print(error_message7)
    print('\n This book is already on loan')
    error_message8 = checkout_function(10, "2222")
    print(error_message8)
    print('\n This book is already on loan')
 
    # checkout book
    checkout_message = checkout_function(12, "4444")
    print(checkout_message)
    print('\n book successfully checked out')

    # ---------------------------- Testing Reserve functionalities ------------------------------- #

    # Invalid book ID error
    error_message1 = reserve_function(58, "1111")
    print(error_message1)

    # Invalid member ID error
    print('\n Invalid book ID')
    error_message2 = reserve_function(22, "111")
    print(error_message2)
    print('\n Member ID is not a 4 digit number')
    error_message3 = reserve_function(22, "123p")
    print(error_message3)
    print('\n Member ID is not a 4 digit number')

    # book ID is already available error
    error_message4 = reserve_function(18, "2222")
    print(error_message4)
    print('\n This book is already available')
    error_message5 = reserve_function(20, "2222")
    print(error_message5)
    print('\n This book is already available')
    error_message6 = reserve_function(6, "2222")
    print(error_message6)
    print('\n This book is already available')

    # book ID already reserved error
    error_message4 = reserve_function(8, "2222")
    print(error_message4)
    print('\n This book is already reserved')

    # reserve book
    reserve_message = reserve_function(12, "4444")
    print(reserve_message)
    print('\n book successfully reserved')
