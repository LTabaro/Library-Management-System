"""
Control Layer for searching book title info
"""

import database as DB
import matplotlib.pyplot as plt
YELLOW = "#f7f5dd"


def book_search_function(book_searched):
    """
    :param book_searched: book searched by user
    :return: error message with empty dataframe or empty message with book info and availability dataframe
    """
    book_search_df, transaction_search_df = DB.book_search_query(book_searched)
    # checking availability

    message = " "

    if (" " + book_searched) not in book_search_df['Title'].unique():  # functionality for invalid book titles
        message = "Invalid book title"

    else:

        book_search_df['Availability'] = 'waiting for answer'
        # book ID's not in the transaction database are available by default
        if book_search_df['ID'][0] not in transaction_search_df['Book_ID'].unique():
            book_search_df['Availability'].loc[0] = "AVAILABLE"

        if book_search_df['ID'][1] not in transaction_search_df['Book_ID'].unique():
            book_search_df['Availability'].loc[1] = "AVAILABLE"

        # searching book ID's in the transaction database that are available
        else:
            # the last instance of book id in the transaction_df to check availability for that particular id
            availability_index1 = transaction_search_df.where(  # first ID of Book
                transaction_search_df['Book_ID'] == transaction_search_df['Book_ID'].iloc[0]).last_valid_index()
            availability_index2 = transaction_search_df.where(  # second ID of Book
                transaction_search_df['Book_ID'] == transaction_search_df['Book_ID'].iloc[1]).last_valid_index()

            answer1 = "ON LOAN" if transaction_search_df.loc[availability_index1]['Return'] == '-' else "AVAILABLE"

            answer2 = "ON LOAN" if transaction_search_df.loc[availability_index2]['Return'] == '-' else "AVAILABLE"

            book_search_df['Availability'] = 'waiting for answer'

            book_search_df['Availability'].loc[0] = answer1
            book_search_df['Availability'].loc[1] = answer2

    return message, book_search_df


def book_cover_display_function(book_searched):
    """
    :param book_searched: book searched by user
    :return: image of book cover
    """
    x, book_cover_index = DB.book_cover_display_db(book_searched)
    figure = plt.Figure(figsize=(3, 2), dpi=100, facecolor=YELLOW)
    ax = figure.add_subplot(111)
    figure.subplots_adjust(
        top=1.0,
        bottom=0.0,
        left=0.0,
        right=1.0,
        hspace=0.0,
        wspace=0.0
    )

    ax.imshow(x["Cover"][book_cover_index])
    ax.axis('off')
    # ax.margins(0, 0)
    return figure


def book_titles_function():
    """
    :return: list of unique book titles from the db in a dataframe
    """
    book_titles_df = DB.book_titles_query()
    return book_titles_df


# ---------------------------- Testing bookSearch functionalities ------------------------------- #

if __name__ == "__main__":

    # valid book title
    error_message, search_df = book_search_function("Twilight")
    print(error_message)
    print(search_df)
    print('\n no error message. Dataframe shows book info and availability')

    # Invalid book title
    error_message, search_df = book_search_function("twilight")
    print(error_message)
    print(search_df)  # copy of a slice of a dataframe
    print('\n invalid book title. Dataframe is empty')

    # correct book cover
    fig = book_cover_display_function("Allegiant")
    print('\n Allegiant book cover')

    # list of unique book titles in database
    titles_df = book_titles_function()
    print(titles_df)
    print('\n List of unique book titles in book_info table')


"""ALL TEST CASES PASSED"""
