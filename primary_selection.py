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

#apartments.to_excel(r'C:\Users\domashniy\Documents\GitHub\Project_3-Airbnb\apartments.xlsx', index=False)

def remove_host_name_from_comments(row):
    comment = row['Comments']
    host_name = row['Host Name']

    # Обрабатываем случаи, когда значение может быть None или NaN
    if pd.isna(comment) or pd.isna(host_name):
        return comment

    # Удаляем слово хоста из комментария
    updated_comment = comment.replace(str(host_name), '').strip()
    return updated_comment

# Создаем новый датафрейм с результатом
df_с = pd.DataFrame()
df_с['Comments'] = df.apply(remove_host_name_from_comments, axis=1)

# Удаляем строки, где 'Comments1' пустой или состоит только из пробелов
df_с = df_с[df_с['Comments'].str.strip() != '']
df_с.dropna(inplace=True)

df_с.to_excel(r'C:\Users\domashniy\Documents\GitHub\Project_3-Airbnb\Comments.xlsx', index=False)