from filmpond_exercise.filmpond_exercise import FilmpondChallenge

file_path = 'test/fixtures//map.txt'
continents = []

fp = FilmpondChallenge()
fp.get_continents_from_file_path(file_path, continents)

print 'There are %s continents in this map.' %(len(continents))
for i,continent in enumerate(continents):
    print 'Continent %s has %s +.' %(i+1, len(continent))
