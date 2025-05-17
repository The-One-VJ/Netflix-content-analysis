import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from collections import Counter

# Load the data
df = pd.read_csv("D:\\VJ\\BI file\\OTT\\netflix_titles.csv")
print(df.head())

# Show missing values
print("\nMissing Values:\n", df.isnull().sum())

# Drop rows with nulls in critical columns
df = df.dropna(subset=[
    'show_id', 'type', 'title', 'director', 'cast', 'country',
    'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'
])

# Show value counts for content type
print("\nContent Type Counts:\n", df['type'].value_counts())

# >>>>>>>>>>>>>>>>>> VISUALIZATION: Content Type Distribution <<<<<<<<<<<<<<<<<<<
plt.figure(figsize=(6, 4))
sb.countplot(data=df, x='type', hue='type', palette='Set2', legend=False)
plt.title("Content Distribution")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
# >>>>>>>>>>>>>>>>>> VISUALIZATION: Content Over the Years <<<<<<<<<<<<<<<<<<<<<

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')

# Drop rows where date conversion failed
df = df.dropna(subset=['date_added'])

# Extract year
df['year_added'] = df['date_added'].dt.year

# Count titles by year
yearly_counts = df['year_added'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
yearly_counts.plot(kind='bar', color='red')
plt.title("Netflix Titles Added Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")
plt.xticks(rotation=45)
plt.tight_layout()

# >>>>>>>>>>>>>>>>>> VISUALIZATION: Top 10 Countries by Content <<<<<<<<<<<<<<<<<<<

top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sb.barplot(x=top_countries.values, y=top_countries.index, palette='Set3')
plt.title("Top 10 Countries by Netflix Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()

# >>>>>>>>>>>>>>>>>> VISUALIZATION: Top 10 Genres <<<<<<<<<<<<<<<<<<<<<<

all_genres = []
for genres in df['listed_in'].dropna():
    all_genres.extend([g.strip() for g in genres.split(',')])

top_genres = pd.Series(Counter(all_genres)).sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_genres.plot(kind='barh', color='salmon')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()
