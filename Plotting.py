import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function


def plotting(df, x, title, jpg):
    fig, ax = plt.subplots(figsize=(15, 5))
    palette = sns.color_palette('colorblind')  # so everyone can see it
    sns.histplot(data=filtered_df, x=x, hue=x, legend=False, palette=palette)
    sns.set_style('darkgrid')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel(x)
    plt.ylabel('No. of Farms Overlapping Indigenous Land')
    plt.title(title)
    plt.tight_layout()
    plt.savefig(jpg, dpi=400)


# Data Import & Filtering
df = pd.read_csv('invaders.csv')
# There are a lot of Indigenous Groups, so I am filtering out the groups
# with the fewest documented invaders:
filtered_df = df.groupby('Name of Indigenous People').filter(lambda x: x[
    'Name of Indigenous People'].shape[0] >= 10)

# Plotting (to Find Patterns)
plotting(filtered_df, 'Name of Indigenous People', 'Number of Non-Indigenous '
         'Farms Overlapping Brazilian Indigenous Land per Indigenous '
         'Group\nFor Groups with Over 10 Overlapping Lands (2023)',
         'invasions_by people.jpg')

plotting(df, 'Phase of Demarcation', 'Number of Non-Indigenous Farms '
         'Overlapping Brazilian Indigenous Land per Phase of Legal Demarcation'
         '\n (2023)', 'invasions_by demarcation.jpg')
