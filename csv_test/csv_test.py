from helpers import get_csv_data, get_pivot_df, get_alphabet


list_url = get_alphabet()
root_url = 'https://public.wiwdata.com/engineering-challenge/data/'


df = get_pivot_df(get_csv_data(root_url, list_url), 'length',
                  'user_id', 'path', 'sum')

try:
    df.to_csv('csv_test.csv')
    print('csv created')
except:
    print('csv not created')