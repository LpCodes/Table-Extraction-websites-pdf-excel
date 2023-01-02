import pandas as pd


def fetch_table():
    """fetches tables from a given website"""

    # enter the website returns lists of tables
    get_all_tables = pd.read_html(
        "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    )

    # get length of how many tables r present
    # print(len(get_all_tables))

    # pull the required table
    firsttable = get_all_tables[0]

    # create a DF
    dataframe1 = pd.DataFrame(firsttable)

    # send data tp excel if req
    dataframe1.to_excel("lp1.xlsx")
    print("DataFrame is written to Excel File successfully now dance")


def fetch_table_2():
    """fetches tables from a given website"""

    # enter the website returns lists of tables
    get_all_tables = pd.read_html(r"https://en.wikipedia.org/wiki/FIFA_World_Cup")

    # get length of how many tables r present
    print(len(get_all_tables))
    # With 38 tables, it can be challenging to find the one you need. To make the table selection easier, use the match parameter to select a subset of tables. We can use the caption “tablename” to select the table
    # with atrrubutes if required
    # dfs = pd.read_html(html_string, attrs={'id': 'report'})

    table_MN = pd.read_html(
        r"https://en.wikipedia.org/wiki/FIFA_World_Cup",
        match="Teams reaching the top four",
    )
    print(len(table_MN))

    # pull the required table
    firsttable = table_MN[0]

    # create a DF
    dataframe1 = pd.DataFrame(firsttable)

    # send data tp excel if req
    dataframe1.to_excel("lp2.xlsx")
    print("DataFrame is written to Excel File successfully now dance")


# fetch_table_2()
