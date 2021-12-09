#Create a dictionary of your favorite music artist and KEYS have to be the genre

fav_artists = {
    'Soul': "Jacob Banks",
    'RnB': "Adele",
    "Rap": 'JayZ',
    "Pop": "Beyonce",
    "Classical": "Hans Zimmer"
}

#Print only the keys
for genre in fav_artists.keys():
    print (genre)
    
#Print all the items in the dict
for genre,artist in fav_artists.items():
    print(genre, artist)
    
#Create a function that prints out your favorite music artist and genre
def favorite_Artists():
    for genre,artist in fav_artists.items():
        print(artist,genre)
favorite_Artists()