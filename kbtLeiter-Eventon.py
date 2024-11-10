import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data for points of Leicester City and Everton across seasons
data = {
    'Season': ['2014-2015', '2015-2016', '2016-2017', '2017-2018', '2018-2019'],
    'Leicester City': [41, 81, 44, 47, 52],
    'Everton': [47, 47, 61, 49, 54]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Transform data to long format for easier plotting with Seaborn
df_long = df.melt(id_vars=['Season'], value_vars=['Leicester City', 'Everton'],
                  var_name='Club', value_name='Points')

# Plot the points across seasons
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_long, x='Season', y='Points', hue='Club', marker='o')
plt.title("Points of Leicester City and Everton Across Seasons (2014 - 2019)")
plt.xlabel("Season")
plt.ylabel("Points")
plt.grid(True)
plt.show()
