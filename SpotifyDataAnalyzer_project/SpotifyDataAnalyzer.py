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
import os  # Python library that lets your code interact with your computer's file system
os.chdir("/Users/julia.campos/Git Hub Projects/Python Projects/Python-Projects-/SpotifyDataAnalyzer_project") # "cd" into a folder — same as terminal's cd command


# step 1

def load_data(filename):
    df = pd.read_csv(filename, encoding='latin-1')
    df['streams'] = pd.to_numeric(df['streams'], errors='coerce') # if a value can't be converted to a number, just make it blank
    return df

# ////// testing ///////
#df = load_data("/Users/julia.campos/Git Hub Projects/Python Projects/Python-Projects-/SpotifyDataAnalyzer_project/spotify-2023.csv")
#print(df)
# ////////////

# step 2 

def top_songs(df, n=10):
    # sort the dataframe by streams from highest to lowest
    # .head(n) gets the first n rows (top 10 by default)
    return df.sort_values('streams', ascending=False).head(n) # ascending=False means biggest number first

# ////// testing ///////
#df = load_data("spotify-2023.csv")
#print(top_songs(df))
# ////////////

# step 3

def top_artists(df, n=10):
    return df.groupby('artist(s)_name')['track_name'].count().sort_values(ascending=False).head(n) # groups all rows by artist and counts their songs 

# step 4 - graphing 

def plot_top_songs(df):
    # get the top 10 songs using our top_songs function
    top = top_songs(df)

    # set the size of the graph 
    plt.figure(figsize=(12, 6))

    # create a HORIZONTAL bar chart (song names on y axis, streams on x axis)
    plt.barh(top['track_name'], top['streams'])

    # add title and axis labels
    plt.title("Top 10 Most Streamed Songs on Spotify")
    plt.xlabel("Streams")
    plt.ylabel("Song")

    # format stream numbers with commas 
    # lambda x, _ means "for each number x on the axis, format it with commas"
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1_000_000_000:.1f}B')) # shows 3.7B instead of 3,700,000,000

    # makes everything fit nicely inside the window
    plt.tight_layout()

    # display the graph
    plt.show()

df = load_data("spotify-2023.csv")
plot_top_songs(df)

# step 5 - graphing 

def plot_top_artists(df):
    top2 = top_artists(df)

    plt.figure(figsize=(12, 6))

    plt.barh(top2.index, top2.values, color = 'green') 
# top2 is a series (not a DataFrame) so we use .index for artist names
# and .values for song counts (no column names needed)

    plt.title("Top 10 Most Streamed Artists on Spotify")
    plt.xlabel("Artist count")
    plt.ylabel("Artists")

    plt.tight_layout()

    plt.show()

df = load_data("spotify-2023.csv")
plot_top_artists(df)



   