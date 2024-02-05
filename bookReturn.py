"""
Control Layer for return functionalities
"""

import database as DB
from datetime import date


global today
current_date = date.today()
today = current_date.strftime('%d/%m/%Y')


def return_function(book_to_return):
    book_info_df, transactions_df = DB.return_query()

    if book_to_return not in book_info_df['ID'].unique():
        message = "please enter valid book ID"
        return message  # error message for invalid book ID

    elif book_to_return not in transactions_df['Book_ID'].unique():
        message = "This book is already available"
        return message  # book ID is already available error message

    else:
        last_instance_of_book = transactions_df.loc[transactions_df['Book_ID'] == int(book_to_return)].iloc[-1]
        # last instance of book_to_return ID in transactions_df

        if last_instance_of_book['Return'] != '-':  # return date is not blank
            message = "This book is already available"
            return message  # book ID is already available error message

        else:  # return book
            DB.return_book(book_to_return, today)
            message = f"Book {book_to_return} successfully returned"
            return message

# ---------------------------- Testing Return functionalities ------------------------------- #


if __name__ == "__main__":

    error_message1 = return_function(58)
    print(error_message1)
    print('\n Invalid book ID')

    error_message2 = return_function(22)
    print(error_message2)
    print('\n Book already available')

    error_message3 = return_function(11)
    print(error_message3)
    print('\n Book already available')

    # return book
    return_message = return_function(12)
    print(return_message)
    print('\n book successfully returned')

""" ALL TEST CASES PASSED"""