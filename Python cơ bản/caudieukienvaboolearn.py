print(bool(0))              # False
print(bool(6))              # True

print(bool("Caterpillar"))  # True
print(bool(""))             # False

print(bool([]))             # False
print(bool([0, 1, 2, 3]))   # True

print(bool(True))           # True
print(bool(False)) 

print(5 < 10)     # True
print(5 > 10)     # False
print(10 > 10)    # False
print("A" < "a")  # True

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False

a = [1, 2, 3]
b = a

print(id(a))  # 139685763327296
print(id(b))  # 139685763327296

print(a == b)  # True
print(a is b)  # True
# Câu lệnh điều kiện 
a = 0 

while(1):
    a+=1
    age = int(input(" Nhập số  tuổi của bạn (nhập 5 lần sẽ thoát ) : "))
    if 0 < age < 18 :
        print ( " bạn còn trẻ trâu vãi =]]")
    elif age < 0 or age > 100 :
        print(" bạn nhập sai tuổi mình rồi ")
        print (" kết thúc chương trình ")
        break
    else:
        print(" bạn đã trưởng thành , kiếm ny đi nào ^^")
    if a == 5 :
        print(" Đã nhập 5 lần , kết thúc chương trình")
        break
print ("\n")
# 2) Cố gắng sử dụng toán tử hoặc chức năng để điều tra sự khác biệt giữa điều này:is và id
numbers = [1, 2, 3, 4]
new_numbers_1 = numbers + [5]
print(new_numbers_1)
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)
print(new_numbers_1 == numbers)
print(new_numbers_1 is numbers)
print (" False vì id numbers là : " , id(numbers) , "!= id new_numbers_1 là : " , id(new_numbers_1) , "\n Nên numbers ko thể là new_numbers_1")
# 3) Yêu cầu người dùng nhập một số. Cho người dùng biết con số đó là dương, âm hay không.
s = int(input("Nhập vào 1 số bất kì  : "))
if s < 0 :
    print ("là số âm ")
else :
    print ("là số dương ")
print( ''' Viết một chương trình để xác định xem một nhân viên có nợ bất kỳ giờ làm thêm giờ nào hay không.
      Bạn nên hỏi người dùng nhân viên đã làm việc bao nhiêu giờ trong tuần này, 
      cũng như mức lương theo giờ cho nhân viên này.
      Nếu nhân viên làm việc hơn 40 giờ, bạn nên in một tin nhắn nói rằng nhân viên phải trả 
      thêm một số tiền, cũng như số tiền đến hạn.
      Số tiền bổ sung còn nợ là 10% tiền lương theo giờ của nhân viên cho mỗi giờ làm việc 
      trong 40 giờ. Trên thực tế, người lao động được trả 110% 
      tiền lương theo giờ của họ cho bất kỳ giờ làm thêm nào.''')
name = input (" Nhập họ và tên cảu nhân viên : ").strip().title()
gio_lam = float(input( f" nhập số giờ làm trong tuần này của {name}: "))
muc_luong = float (input(f" nhập mức lương trong 1 giờ của {name} : ")) 
d = float (gio_lam*muc_luong) 
if gio_lam > 40 :
    print (f" số tiền phải trả thêm cho {name} là : " ,str ((gio_lam - 40 )*muc_luong) , "%")
elif gio_lam == 40:
    print (f" sô tiền phải trả cho {name} là : "  , str(d)  , "$")
else :
    print(" số tiền nhận được (đã trừ đi 10% do ko đủ 40h làm việc)  : " , str(d- d*0.1) , "$")