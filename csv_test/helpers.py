import pandas as pd
import string

def get_alphabet():
    """
Gets list of lowercase letters using string module
    :return: lowercase letters as list of strings
    """
    alphabet = list(string.ascii_lowercase)
    return alphabet

def get_df(url):
    """
Reads csv and converts to DataFrame
    :param url: string, url where csv can be found
    :return: DataFrame based on csv
    """
    df = pd.read_csv(url)
    return df

def get_csv_data(root, url_list):
    """
Loops through csv files, creates DataFrames using get_df, then concatenates into one DataFrame
    :param root: string, root url
    :param url_list: string or list of strings with file name
    :param ext: string, extension
    :return: concatenated DataFrame
    """
    csv_df = []
    ext = '.csv'
    for item in url_list:
        try:
            url = root + str(item) + ext
            csv_df.append(get_df(url))
            print(str(item) + ext + ' downloaded')
        except:
            print(str(item) + ext + ' not found')
    csv_df = pd.concat(csv_df)
    return csv_df

def get_pivot_df(pivot_df, values, index, column, aggfunc):
    """
Converts DataFrame into pivot table
    :param pivot_df: DataFrame
    :param values: column to be aggregated
    :param index: column to be indexed
    :param column: column to be pivoted
    :param aggfunc: aggregate function to be performed on values
    :return: DataFrame converted to pivot table
    """
    pivot_df = pivot_df.pivot_table(values=values, index=index, columns=column, aggfunc=aggfunc).fillna(0)
    print('pivot created')
    return pivot_df


