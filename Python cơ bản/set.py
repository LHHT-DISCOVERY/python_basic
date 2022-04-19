vegetables = {"carrot", "lettuce", "broccoli", "onion", "carrot"}
vegetables.add("potato") # thêm vào 1 mục
print(vegetables)
vegetables.update(["khoai tây", "salach"]) # thêm vào nhiều mục
print(vegetables)
# Xóa 1 mục trong set
vegetables.remove("onion")
print(vegetables)
# hoặc 
vegetables.pop()
print(vegetables)
# Set operations
letters = {"a", "b", "c"}
numbers = {1, 2, 3}
letters.update(numbers)
print(letters)
# hoặc union
letters_and_numbers = letters.union(numbers)
print(letters_and_numbers)
chiahetcho2 = {2,4,6,8,10,12,14,16,18}
chiahetcho3 = {3,6,9,12,15,18}
c2_3 = chiahetcho2.intersection(chiahetcho3)
# =============================================================================
# nghĩa là liệt kê các số vừa có trong 2 vừa có trong 3 thì là số chia hết cho 2 and 3
# tóm lại intersection là liệt kê ra các phần từ giống nhau trong 2 cái set và ưu tiên set có len lớn hơn trước
# =============================================================================
print(c2_3)
# liệt kê các phần từ có trong 2 ko có trong 3
k2_3 = chiahetcho2.difference(chiahetcho3)
print(k2_3) # tương tự với kiểu string nó cx phân biệt được 

bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077",'Doom Eternal'}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}
print(bundle_1.difference(bundle_2)) # có trong 1 ko có trong 2 
print(bundle_2.difference(bundle_1)) # có trong 2 ko có trong 1
print(bundle_1.symmetric_difference(bundle_2)) # có trong 1 ko có trong 2 và ngược lại
# =============================================================================
# kiểm tra xem có nằm trong set ko 
# =============================================================================
# vd
munber = {1,2,3,4,5,56,66}
print(4 in munber) # kiểm tra xem 4 có nằm trong munber ko 
ten = {"sang" , "toàn" , "trí"}
print ("hiếu" in ten) # kiểm tra xem "hiếu có nằm trong ten ko ?
# hoặc kiểm tra trực tiếp
print("t" in "trí")
print(4 in {1,2,3})
print("\n")
# =============================================================================
# Hoặc
# =============================================================================
student = {
	"name": "Eric Cartman",
	"age": 10,
	"school": "South Park Elementary"
}
# kiểm tra xem có key nào trong student hay ko ??
print("age" in student)
# kiểm tra xem có value nào nằm trong student hay là không ?
print("uth Park Elementary" in student.values())
# =============================================================================
# BÀI TẬP và các cách tạo ra set 
# =============================================================================
tao_1 = set()
tao_1.update([2,3,46,54])
print(tao_1)
# cách 1 :  tạo 1 set 
tao_2 = set(range(1,6)) # in từ 1 đến 5 
print(tao_2)
# cách 2 : tạo 1 set
tao_3 = set()
for i in range(1,6):

    tao_3.add(i)
print( "tao_3 đây nè : " , tao_3)\
# cách 3 tạo 1 set :
tao_4 = set()
tao_4.add(1)
tao_4.add(2) ;tao_4.add(3);tao_4.add(4);tao_4.add(5)
print(tao_4)
print("hợp : " , tao_1.union(tao_3))
print("giao : " , tao_1.intersection(tao_3))
print("bất đối xứng  : " ,tao_1.symmetric_difference(tao_3))
# =============================================================================
# symmetric_difference nghĩa là in ra các phần tử có trong tao 1 và ko có trong to3 và ngược lại co tao3 ko cso tao 1
# =============================================================================
# bài tập kiểm tra phạm vi nhập của người dùng 
day_so = range(1,11)
n = int(input(" nhập n (phạm vi từ 1 - 10): "))
if n in day_so :
    print(" bạn đã nhập trong phạm vi cho phép ")
else :
    if n < day_so[0] :
        print(" bạn đã nhập quá nhỏ và ngoài phạm vi cho phép ")
    else : 
        print(" bạn đã nhập quá lớn so với phạm vi cho phép")