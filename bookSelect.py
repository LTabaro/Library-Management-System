"""
Control Layer for book recommendations
"""
import matplotlib.pyplot as plt


def pie_chart():
    """
    Returns a pie chart of the ratio of books sold in 2021 per genre
    """
    a = int(95)  # number of Fantasy books sold in 2021 (millions)
    b = int(68)  # number of Romance books sold in 2021 (millions)
    c = int(25)  # number of Thriller books sold in 2021 (millions)
    d = int(42)  # number of Sci-Fi books sold in 2021 (millions)
    e = int(5)  # number of Comedy books sold in 2021 (millions)
    f = int(59)  # number of Fairy-Tale books sold in 2021 (millions)

    total = a + b + c + d + e + f

    ratios = [a/total, b/total, c/total, d/total, e/total, f/total]  # used to calculate number of books to purchase

    genres = ['Fantasy', 'Romance', 'Thriller', 'Sci-Fi', 'Comedy', 'Fairy-Tale']

    pie = plt.Figure(figsize=(5, 4), dpi=100)

    explode = (0, 0, 0, .2, .3, .1)

    ax = pie.add_subplot(111)
    ax.pie([a, b, c, d, e, f], labels=genres, autopct='%.2f %%', explode=explode)

    return pie, ratios


def bar_chart():
    """
    Returns a bar chart of the total number of books sold in 2021 per genre
    """
    genres = ['Fantasy', 'Romance', 'Thriller', 'Sci-Fi', 'Comedy', 'Fairy-Tale']

    bar = plt.figure(figsize=(6, 4))
    plt.title("Number of Books Sold per Genre 2021")
    plt.axis('off')
    ax = bar.add_subplot(111)

    a = int(95)  # number of Fantasy books sold in 2021 (millions)
    b = int(68)  # number of Romance books sold in 2021 (millions)
    c = int(25)  # number of Thriller books sold in 2021 (millions)
    d = int(42)  # number of Sci-Fi books sold in 2021 (millions)
    e = int(5)  # number of Comedy books sold in 2021 (millions)
    f = int(59)  # number of Fairy-Tale books sold in 2021 (millions)
    values = [a, b, c, d, e, f]

    ax.bar(genres, values)

    return bar


if __name__ == "__main__":
    pie1, ratios1 = pie_chart()  # pie chart
    print('\n Ratio of Books Sold per Genre')
    bar1 = bar_chart()  # bar chart
    print('\n Number of Books Sold per Genre 2021')
