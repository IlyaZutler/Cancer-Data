import pandas as pd
import pickle
import os

# Путь к вашему Excel-файлу
excel_file_path = r'C:\Users\domashniy\Documents\GitHub\Project_3-Airbnb\Airbnb_Berlin2.xlsx'
# Путь к файлу для кэширования
cache_file_path = r'C:\Users\domashniy\Documents\GitHub\Project_3-Airbnb\cached_df2.pkl'

# Функция для чтения Excel-файла и кэширования DataFrame
def read_excel_with_cache(excel_path, cache_path):

    if os.path.exists(cache_path):
        # Если кэш-файл существует, загружаем DataFrame из кэша
        with open(cache_path, 'rb') as cache_file:
            df = pickle.load(cache_file)
        print("DataFrame загружен из кэша.")
    else:

        # Если кэш-файл не существует, читаем Excel-файл и сохраняем в кэш
        df = pd.read_excel(excel_path, engine='openpyxl')
        # Если ваш файл в формате .xls, используйте engine='openpyxl'
        with open(cache_path, 'wb') as cache_file:
            pickle.dump(df, cache_file)
        print("DataFrame прочитан из Excel и сохранен в кэш.")
    return df

# Чтение DataFrame с использованием кэша
df = read_excel_with_cache(excel_file_path, cache_file_path)

# Вывод первых нескольких строк DataFrame для проверки
print(df.head(1))
print(df.shape)
print(df.info())
print(df.isna().sum())
print(df.describe())

apartments = df.drop(columns=['index', 'Review ID', 'review_date','Reviewer ID', 'Reviewer Name','Comments' ]).drop_duplicates()

apartments.to_excel(r'C:\Users\domashniy\Documents\GitHub\Project_3-Airbnb\apartments.xlsx', index=False)

print(apartments.head(1))
print(apartments.shape)

