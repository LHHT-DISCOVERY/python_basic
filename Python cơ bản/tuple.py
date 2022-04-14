movies = [
    ("The Room", "Tommy Wiseau", "2003", "$6,000,000")
]

title = input("Title: ")
director = input("Director: ")
year = input("Year of release: ")
budget = input("Budget: ")
print (movies)
new_movie = title, director, year, budget
print(f" {new_movie[0]} ,{new_movie[1]}, ({new_movie[2]})")
# thêm phần tử vào tuple
movies.append(new_movie)
print(movies[0])
print(movies[1])
print (movies)
del movies[1]
print(" Đã delete movies[1] còn lại  :" ,movies)
# ngoài del ra còn có các phương thức khác để sử lý như
# movies.pop(0)
# movies.remove(movies[0])