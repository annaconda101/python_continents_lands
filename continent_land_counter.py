from filmpond_exercise.filmpond_exercise import FilmpondChallenge

url = 'https://s3-ap-southeast-2.amazonaws.com/uat-filmpond-bucket/candidates/map.txt'
continents = []

fp = FilmpondChallenge()
fp.get_continents_from_url(url, continents)

print 'There are %s continents in this map.' %(len(continents))
for i,continent in enumerate(continents):
    print 'Continent %s has %s +.' %(i+1, len(continent))
