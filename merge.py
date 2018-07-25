import sqlite3, datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import linregress
from scipy.stats import ttest_rel

pd.set_option('precision', 2)
np.set_printoptions(precision=2)

con = sqlite3.connect('database.sqlite')

pitchfork = pd.read_sql('SELECT reviewid, title, score, best_new_music FROM reviews', con)
artist = pd.read_sql('SELECT * FROM artists', con)
years = pd.read_sql('SELECT * FROM years', con)
genres = pd.read_sql('SELECT * FROM genres', con)
con.close()

# combine into score-artist mapping
pppreviews = pd.merge(pitchfork, years, on = 'reviewid')
ppreviews = pd.merge(pppreviews, artist, on = 'reviewid')
previews = pd.merge(ppreviews, genres, on = 'reviewid')
# remove various artists
previews = previews[previews.artist != 'various artists']

# remove multi-year reviews [re-releases]
year_counts = years.groupby('reviewid').count().reset_index()
keepers = year_counts.loc[year_counts.year == 1, 'reviewid']
previews = previews.loc[previews.reviewid.isin(keepers)]

previews = previews.drop(columns = 'reviewid')
previews = previews.rename(index=str, columns={"score": "pitchfork", "best_new_music":"bnm"})

#print previews.shape

fantano = pd.read_csv('needledrop.csv')
fantano.artist = fantano.artist.str.lower()
fantano.title = fantano.title.str.lower()
reviews = pd.merge(previews, fantano, on = ['artist' , 'title'], how='outer', indicator=True)
reviews.fantano = pd.to_numeric(reviews.fantano, errors='coerce')
reviews = reviews[np.isnan(reviews.fantano) != True]

#print reviews.shape
#print list(reviews)
#print reviews.query('_merge == "both"')

reviews.to_csv('reviews.csv')