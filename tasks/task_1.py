import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_csv('vgsale_1.csv')

# 1. Анализ популярных жанров до и после 2000 года
до_2000 = df[df['Year'] < 2000].groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
после_2000 = df[df['Year'] >= 2000].groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
до_2000.plot(kind='bar')
plt.title('Популярные жанры до 2000 года')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
после_2000.plot(kind='bar')
plt.title('Популярные жанры после 2000 года')
plt.xticks(rotation=45)
plt.tight_layout()

# 2. Анализ по количеству игр и объему продаж
количество_игр = df['Genre'].value_counts()
объем_продаж = df.groupby('Genre')['Global_Sales'].sum()

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
количество_игр.plot(kind='bar')
plt.title('Количество игр по жанрам')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
объем_продаж.plot(kind='bar')
plt.title('Объем продаж по жанрам')
plt.xticks(rotation=45)
plt.tight_layout()

# 3. Количество игр по годам
игры_по_годам = df['Year'].value_counts().sort_index()
plt.figure(figsize=(15, 5))
игры_по_годам.plot(kind='line')
plt.title('Количество выпущенных игр по годам')
plt.xlabel('Год')
plt.ylabel('Количество игр')

# 4. Топ-3 издателя
топ_издатели = df['Publisher'].value_counts().head(3).index
издатели_платформы = df[df['Publisher'].isin(топ_издатели)].groupby(['Publisher', 'Platform']).size().unstack()
издатели_платформы.plot(kind='bar', stacked=True, figsize=(15, 6))
plt.title('Распределение игр по платформам для топ-3 издателей')
plt.xticks(rotation=45)

# 5. Круговые диаграммы продаж
def построить_круговую(данные, заголовок):
    продажи = данные[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
    plt.figure(figsize=(8, 8))
    plt.pie(продажи, labels=['Северная Америка', 'Европа', 'Япония', 'Другие'], autopct='%1.1f%%')
    plt.title(заголовок)

построить_круговую(df[df['Year'] < 2000], 'Продажи до 2000 года')
построить_круговую(df[df['Year'] >= 2000], 'Продажи после 2000 года')

plt.show()
