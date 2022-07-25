import pandas as pd


def get_df(url):
    df = pd.read_csv(url)
    return df

def get_csv_data(root, url_list, ext):
    csv_df = []
    for item in url_list:
        url = root + str(item) + ext
        csv_df.append(get_df(url))
    csv_df = pd.concat(csv_df)
    return csv_df

def get_pivot_df(pivot_df):
    pivot_df = pivot_df.pivot_table(values='length', index='user_id', columns='path', aggfunc='sum').fillna(0)
    return pivot_df


