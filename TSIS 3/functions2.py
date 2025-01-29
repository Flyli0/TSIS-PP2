movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

'''''''''''''''Task 1'''''''''''''''
def good_score(movies,name):
    sus = False
    for i in movies:
        if i['imdb'] > 5.5 and i['name'] == name:
            sus = True
    print(sus)

good_score(movies,'We Two')

'''''''''''''''Task 2'''''''''''''''
def good_movies(movies):
    sub = []
    for i in movies:
        if i['imdb'] > 5.5:
            sub.append(i['name'])
    return sub

print(good_movies(movies))

'''''''''''''''Task 3'''''''''''''''
def category(movies,cat):
    films = []
    for i in movies:
        if i['category'] == cat:
            films.append(i['name'])
    return films

print(category(movies,'Romance'))

'''''''''''''''Task 4'''''''''''''''
def mean_imdb(movies):
    summ = 0
    for i in movies:
        summ += i['imdb']
    return summ/len(movies)

print(mean_imdb(movies))

'''''''''''''''Task 5'''''''''''''''
def cat_mean_imdb(movies,cat):
    summ = 0
    count = 0
    for i in movies:
        if i['category'] == cat:
            count += 1
            summ += i['imdb']
    return summ/count  

print(cat_mean_imdb(movies,'Drama'))