"""
Functions needed: 

# 1. load_data(filename)
#    → loads the CSV file and returns a dataframe

# 2. top_songs(df, n=10)
#    → returns the top n most streamed songs

# 3. top_artists(df, n=10)
#    → returns the top n most popular artists

# 4. plot_top_songs(df)
#    → creates a bar chart of top 10 songs

# 5. plot_top_artists(df)
#    → creates a bar chart of top 10 artists

# 6. plot_energy_vs_popularity(df)
#    → creates a scatter plot

# 7. main()
#    → menu to tie everything together

"""

# libraries needed: 

import pandas as pd
import matplotlib.pyplot as plt


# step 1

def load_data(filename):
    df = pd.read_csv(filename, encoding='latin-1')
    return df

# ////// testing ///////
df = load_data("/Users/julia.campos/Git Hub Projects/Python Projects/Python-Projects-/SpotifyDataAnalyzer_project/spotify-2023.csv")
print(df)
# ////////////

# step 2 

