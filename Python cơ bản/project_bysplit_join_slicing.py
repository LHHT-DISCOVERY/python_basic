movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
so_luong = int(input(" Nhập số lượng bộ phim muốn thêm vào : "))
for _ in range(so_luong):
    name = input(" Nhập vào tên của bộ phim : ")
    price = int(input(" Nhập vào ngân sách : "))
    movie = name,price
    new_movie = movies.append(movie)
print(movies)
total = 0 
count = 0 ;
for i in movies:
    total += i[1]
    count +=1
tb = total/count
print(f" Ngân sách trung bình các bộ phim là : {tb} $")
dem = 0 
for i in movies:
    if i[1] > tb :
        dem += 1
        print(f" Bộ phim : {i[0]} - cao hơn {i[1]-tb}$ so với mức trung bình ")
print(" =>  có" ,dem , " bộ phim cao hơn mức trung bình ") 
