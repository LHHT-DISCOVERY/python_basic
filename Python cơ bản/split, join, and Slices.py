Ten_friend = ["trí","toàn","sang"]
print(f'{", ".join(Ten_friend)}')
# xuat voi kkieu so 
numbers = [1,2,3,4,5]
number_1 = str(numbers) # giả sử 
string_number = []
for number in numbers:
    string_number.append(str(number))
print(",".join(string_number))
print(number_1) # sai
# => ko thể dùng hàm str để ép thành kiểu string
print("\n")
print(" Tách một chuỗi ")
user_number = input("nhập vào 5 con số cách nhau bởi dấu phẩy : ")
tach_chuoi = user_number.split(",") # nghĩa là cứ sau 1 dấu phẩy là split , tách ra làm chuỗi
print(tach_chuoi)
# chuyển thành tuple()
tach_chuoi_1 = tuple(user_number.split(",")) ; print(tach_chuoi_1)
# strip ()
numbe_user = input(" nhập vào 5 số cách nhau bởi dấu cách : ")
numbe_user = numbe_user.split(" ")
list_moi = []
for num in numbe_user:
    list_moi.append(num.strip())
print(list_moi)
print(tuple(list_moi))
print('\n')
# đối với cắt một chuỗi 
vd = "Python"
print(list(vd))
print(tuple(vd))    
# silcing
cut = vd[0:3] # cắt lấy từ 0 đến 3
print(cut)
cut_1 = vd[3:] # lấy kí tự từ 3 trở đi
print(cut_1)
#cut_1 = vd[:] sai chép toàn bộ mảng 
# HÀM LEN
vd_1 = [1,2,3,4,5]
vd1 = len(vd_1)
print("chiều dài của mảng là : " ,vd1)
print ("""
       ----- Bài Tập ------
       https://www.teclado.com/30-days-of-python/python-30-day-7-split-join
       """)
#  bài tập 1
nhap_ten = input("nhập tên người dùng : ").split()
give_name = nhap_ten[0]
print("họ là ; " ,give_name)
sun_name = nhap_ten[-1]
print("tên là : " ,sun_name)
# bài tập 2 
base_number = [1,2,3,4,5]
base_moi = []
for i in base_number:
    base_moi.append(str(i))
print("|".join(base_moi))
# bài tập 3 
quotes = [
 	"'What a waste my life would be without all the beautiful mistakes I've made.'",
 	"'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
 	"'The very essence of romance is uncertainty.'",
 	"'We are not here to do what has already been done.'"
 ]
print(quotes)
for qoute in quotes :
    print(qoute.strip("'")) # cắt đi dấu {'} để nối các chuỗi lại với nhau
    

# bài 4 
namee = input("nhập tên người dùng : ").strip() # cắt bỏ khoảng trắng đầu tiền và cuối cùng nếu có
print(len(namee))
print(len(namee.split()))
