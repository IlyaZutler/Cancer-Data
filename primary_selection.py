import pandas as pd
import pickle
import os

excel_file_path = r'C:\Users\domashniy\Documents\GitHub\Project_3-Airbnb\Airbnb_Berlin2.xlsx'
cache_file_path = r'C:\Users\domashniy\Documents\GitHub\Project_3-Airbnb\cached_df2.pkl'
def read_excel_with_cache(excel_path, cache_path):

    if os.path.exists(cache_path):
        with open(cache_path, 'rb') as cache_file:
            df = pickle.load(cache_file)
        print("DataFrame загружен из кэша.")
    else:
        df = pd.read_excel(excel_path, engine='openpyxl')
        with open(cache_path, 'wb') as cache_file:
            pickle.dump(df, cache_file)
        print("DataFrame прочитан из Excel и сохранен в кэш.")
    return df

df = read_excel_with_cache(excel_file_path, cache_file_path)

df['Price'] = df['Price'].str.replace('$', '').str.replace(',', '').astype(float)
df['Postal Code'] = df['Postal Code'].str.replace('.0', '').astype(str)
apartments = df.drop(columns=['index', 'Review ID', 'review_date','Reviewer ID', 'Reviewer Name', 'Comments',
                              'Listing URL', 'Listing Name', 'Host ID', 'Host URL', 'Host Name',
                              'Country Code', 'Country', 'Business Travel Ready']).drop_duplicates()

apartments.to_excel(r'C:\Users\domashniy\Documents\GitHub\Project_3-Airbnb\apartments.xlsx', index=False)


