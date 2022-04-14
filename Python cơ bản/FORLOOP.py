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
movie = movies[0];
print("\n")
print(f"tên phim 1 : {movie[0]} , sx năm : {movie[2]} ,by {movie[1]}")
print("\n")
movie_1 = movies[1]
print(f"tên phim 2 : {movie_1[0]} , sx năm : {movie_1[2]} ,by {movie_1[1]}")
movie_2 = movies[2]
print("\n")
print (f"tên phim 3 : movie_2[0], sx năm : {movie_2[2]} ,by {movie_2[1]}")
# hoặc
print("\n")
print (f"tên phim : {movies[0][0]} , sx {movies [0][2]} , movies[0][1]")
print (f"tên phim : {movies[1][0]} , sx {movies [1][2]} , movies[1][1]")
print (f"tên phim : {movies[2][0]} , sx {movies [2][2]} , movies[2][1]")
print("\n")
 # Vòng lặp for
for movi in movies :
    print(f" tên bộ phim :{movi [0]} \n author : {movi [1]} \n by {movi[2]} \n")
print("----- kết thúc vòng lặp For ------\n")

# hoặc
for film in movies:
	print(f"{film[0]} ({film[2]}), by {film[1]}")
print("kết thúc")
# hàm lặp gián đoạn 
for n in movies :
    if n[0] == "Memento":
        print(" Memento có trong các tập phim ")
        break


a= range(0,10,2)
print(list(a ))
print(tuple(a))
for number in range (10):
    print("hello")
print("\n")
print("""
      ---- BÀI TẬP ----
      """)
      
#1) Dưới đây chúng tôi đã cung cấp một danh sách các tuples, 
#trong đó mỗi tuple chứa chi tiết về một nhân viên của một cửa hàng:
# tên của họ, số giờ làm việc tuần trước, và tỷ lệ giờ của họ
#. In số tiền mỗi nhân viên sẽ được trả vào cuối tuần ở định dạng đẹp, có thể đọc được.
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
for nv in employees:
    print(f" Tên nhân viên : {nv[0]} \n số giờ làm việc : {nv[1]} \n lương : {nv[2] * nv[1]} \n ")
    
total = 0 ;
count = 0
for nv in employees:
    total += nv[2]
    count += 1
tbc = total / count 
for nv in employees:
    if nv[2] > tbc:
        print(f" {nv[0]} là nhân viên có số lương trung bình cộng cao nhất")



# Câu 3 : 
while(1):
    b = int(input ("nhập vào số nguyên dương : "))
    if b < 0 : 
        print ("xin mời nhập lại ")
    else :
        for c in range(1 ,b+1):
            print(c, end = " ")
        break
# Câu 4 :
sum =  0
while(1):
    n = int(input ("nhập vào số nguyên dương n : "))
    if n < 0 : 
        print ("xin mời nhập lại ")
    else :
        for e in range(0 , n+1):
            sum += e
        print (sum)
        break
# Câu 5 :
ten_nguoi =input("nhập họ và tên của bạn : ")
print(f"tên bạn vừa nhập là : {ten_nguoi.upper()}")

# câu 6 :
import re
s_tring = input (" nhập vào chuỗi : ")
kq= re.sub(r'\D' ,'',s_tring)
print(f" kết quả sau khi tách là : {kq} ")



