simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
simpsons.sort() # sắp sếp dánh sách theo thứ tự bảng chữ cái
print(simpsons)
student = {"Name  " : "Lý Huỳnh Hữu Trí" , "Lớp" : [19]}
print(student["Lớp"])
student_1 = (
	"John Smith",
	[88, 76, 92, 85, 69]
)
student_1[1].append(92)
print(student_1)
student = {"Name  " : "Lý Huỳnh Hữu Trí" , "Lớp" : [19]}    
print(student.get('khóa'),[])

# CÁC CÁCH THÊM VÀO DICTIONARIES
student = {"Name  " : "Lý Huỳnh Hữu Trí" , "Lớp" : [19]}
student["age"] = 21
print(student)
student["Lớp"].append(21) # thêm số 21 và lớp tron dict
print(student)
student["Lớp"] = 20 # sửa lại : Lớp
print(student)
del student["Lớp"] # xóa đi Lớp 
print(student)
print("\n")
# update cho dictionaries
movie = {
	"title": "Avengers: Endgame",
	"directors": ["Anthony Russo", "Joe Russo"],
	"year": 2019
}

meta_info = {
	"runtime": 181,
	"budget": "$356 million",
	"earnings": "$2.798 billion",
	"producer": "Kevin Feige"
}
meta_info.update(movie)
print(meta_info)
print('\n')
# hoặc chúng ta update trực tiếp
movie = {
	"title": "Avengers: Endgame",
	"directors": ["Anthony Russo", "Joe Russo"],
	"year": 2019
}

movie.update({
	"runtime": 181,
	"budget": "$356 million",
	"earnings": "$2.798 billion",
	"producer": "Kevin Feige"
})
print(movie)
print("\n")
movie = {
	"title": "Avengers: Endgame",
	"directors": ["Anthony Russo", "Joe Russo"],
	"year": 2019
}
#   LẶP LẠI MỘT DICT
for Attribu in movie :
    print(Attribu) # in ra attrib 
print("\n")
for key in movie:
    print(movie[key]) # in ra các key sau dấu ":"
print("\n")
for value in movie.values():
    print(value) # in ra các từ khóa có trong một dictionaries
print("\n")
# in tất cả trong dict
for ke in movie:
    print(f"{ke} : {movie[ke]}")
print("\n")
# cách 2
for ki , valu in movie.items():
    print(f"{ki} : {valu}")
print("\n")
# BÀI TẬP
nhom_nhac = {
 	"title" : "The Dark Side of the Moon",
 	"artirt" : "Pink Floyd",
 	"year" : 1973,
 	"track" : (
 		"Speak to Me",
 		"Breathe",
 		"On the Run",
 		"Time",
 		"The Great Gig in the Sky",
 		"Money",
 		"Us and Them",
 		"Any Colour You Like",
 		"Brain Damage",
 		"Eclipse"
 	)
 }
for o , value in nhom_nhac.items():
    print(f"{o} : {value}") # in ra các từ khóa và giá trị bên cạnh
print("\n")
# xóa năm phát hành 
del nhom_nhac["year"]
del nhom_nhac["track"]
nhom_nhac["ngày phát hành "] = " 1 tháng 3 năm 1973"
print(nhom_nhac)
print("\n")
# cập nhật cho nhom_nhac
bai_hat = {
    "tên bài hát " :(
        "lạc trôi",
        "em của ngày hôm qua",
        "chúc vợ ngủ ngon")
    }
nhom_nhac.update(bai_hat)
for iu , value in nhom_nhac.items():
    print(f"{iu} : {value}")
print("\n")
print( nhom_nhac.get("ngày phát hành " , "không tồn tại")) # get(từ khóa cần kiếm , kết quả nếu ko có từ khóa cần kiếm)
# muốn tra 1 key trong 1 dict thì dùng get
#hoặc có thể dùng cách dưới :
print(nhom_nhac["ngày phát hành "])