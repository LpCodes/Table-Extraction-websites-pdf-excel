import pandas as pd

def fetch_table():
    """ fetches tables from a given website """
    
    # enter the website returns lists of tables
    get_all_tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
    
    # get length of how many tables r present 
    # print(len(get_all_tables))
    
    # pull the required table
    firsttable = get_all_tables[0]

    # create a DF
    dataframe1 = pd.DataFrame(firsttable)
    
    # send data tp excel if req
    dataframe1.to_excel("lp1.xlsx")
    print('DataFrame is written to Excel File successfully now dance')
    
    
fetch_table()