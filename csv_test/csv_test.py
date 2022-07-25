from helpers import get_csv_data, get_pivot_df
import string

alphabet = list(string.ascii_lowercase)
root_url = 'https://public.wiwdata.com/engineering-challenge/data/'
ext = '.csv'

df = get_pivot_df(get_csv_data(root_url, alphabet, ext))

df.to_csv('wheniwork.csv')