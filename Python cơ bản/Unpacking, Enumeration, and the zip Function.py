movies = [
	(
		"Eternal Sunshine of the Spotless Mind",
		"Michel Gondry",
		2004
	),
	(
		"Memento",
		"Christopher Nolan",
		2000
	),
	(
		"Requiem for a Dream",
		"Darren Aronofsky",
		2000
	)
]


counter = 1 
for name , author , year in movies:
    print(f"{counter}.{name} by {author} in {year}")
    counter+=1
    
    
# ENUMERATE
namee = ["sang" , "toàn" , "trí"]
for c , ten in enumerate(namee, start=1):
    print(f"{c}.{ten}")
for d, ( nam , tg , y) in enumerate(movies,start=1):
    print(f"{d}.{nam}({y}) by {tg}")
    
    
    
pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]
for ( pet , ow) in zip(pets ,pet_owners):
    print(f"{pet} by {ow}.....")
    
    
#pets_and_owners = zip(pet_owners, pets)
sd = list(zip(pet_owners, pets))
for cun , chu in sd:
    print(f"{cun} by {chu}..")
#sd  = zip(pets_and_owners)# lưu ý: nếu sử dụng lại sẽ trống rỗng
# cách sử lý:  sd = list(zip(pets_and_owners))
print(f" đây nè :{sd} ")    
    
movie_titles = [
	"Forrest Gump",
	"Howl's Moving Castle",
	"No Country for Old Men"
]

movie_directors = [
	"Robert Zemeckis",
	"Hayao Miyazaki",
	"Joel and Ethan Coen"
]

movies = zip(movie_titles, movie_directors)

for title, director in movies:
	print(f"{title} by {director}.")

movies_list = list(movies)

#print(f"There are {len(movies_list)} movies in the collection.")
print(f"đây nè: {movies_list}.")

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for dem ,(tgg , ns , ny) in enumerate(main_characters,start=1):
    print(f"{dem}. {tgg} is a {ny.lower()} voiced by {ns}")
    
    
# UNPACKING
student = ("John Smith", 11743, ("Computer Science", "Mathematics"))
name, id_number, (major, minor) = student
print(name)
print(id_number)

# caau 3

letters = ["a", "b", "c"]
numbers = [1, 2]
a = len(letters)
b = len(numbers)
print(f"len a : {a}")
print(f"len b : {b}")
print(list(zip(letters, numbers)))
# lưu ý sử dụng Zip chú ý len của 2 list nếu ko dẫn đến việc mất dữ liệu 