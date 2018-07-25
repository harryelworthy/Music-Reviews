# MusicReviews

The main file to check here is [reviews.ipynb](reviews.ipynb), a Jupyter notebook. This uses [pitchfork.sqlite](pitchfork.sqlite) and [needledrop.csv](needledrop.csv) as sources, cited in the notebook. 

[STATAreviews.do](STATAreviews.do) will do the same things but in Stata - it uses [premerged.csv](premerged.csv) as a source, taken from the above sources.

[scrape.py](scrape.py) is a draft of a web scraper to get Pitchfork's scores from their site. Right now it just gets url's to each review, another step could be added to visit those reviews and put scores/artists/albums etc. into a dataframe. Not used as too intensive a scrape and a premade data source was found.
