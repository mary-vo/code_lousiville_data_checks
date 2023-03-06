import pandas as pd
import os
import matplotlib.pyplot as plt

file = os.path.join('..','assets','IMDB_Top_250_Movies.csv')
df = pd.read_csv(file)
print(df.head())

# Occurrences by rating
occurrences = df['rating'].value_counts()
print(occurrences)

# Map the couhnt/occurrences for each group of rating
plt.scatter(occurrences.index,occurrences.values, marker="s", c='red')
plt.title('Occurrences by Rating')
plt.xlabel('Rating')
plt.ylabel('Occurrences')
plt.show()