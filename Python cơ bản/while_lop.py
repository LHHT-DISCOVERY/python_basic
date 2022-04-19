nhap = int(input(" nhập giá trị lớn hơn 10 : "))
while nhap < 10 :
    print(" vui lòng nhập lại " )
    nhap = int(input(" nhập giá trị khác lớn hơn 10 : "))
print(" bạn đã nhập đc số lớn hơn 10 ")

while 1 :
    chon = input("vui lòng chọn a or b or c , nhập q để thoát chương trình : ")
    if chon == "a":
        print("bạn đã nhập vào chữ a ")
    elif chon == "b":
        print("bạn đã nhập vào chữ b")
    elif chon == "c" :
        print("bạn đã nhập vào chữ c")
    elif chon == "q":
        break
    else :
        print("bạn đã nhập tùm bậy ")
for i in range(10):
    if i % 2 == 0:
        continue # nếu đúng chia hết cho 2 thì quay lên lặp lại , r mới in ra i 
    print(i)

# chương trình kiểm tra xem có các số nguyên tố nào từ 2 đến n với n nhập từ bàn phím
# cách 1 :

snt = int(input("Nhập vào số nguyên tố : "))
for nt in range(2,snt):
    if snt % nt == 0 :
        print(f"{snt} ko phải là số nguyên tố ")
        break
else:
    print(f"{snt} là số nguyên tố ")
        
# cách 2 
songuyento = int(input("nhập vào số cần kiểm tra : "))
dem = 2 ;
while dem < songuyento :
    if songuyento % dem == 0 :
        print(f"{songuyento} ko là số nguyên tố ")
        break
    dem+= 1
else :
    print(f"{songuyento} là số nguyên tố ")
# in ra các số nguyên tố từ 1 đến n 
tang = []
lietke = int(input(" nhập vào số n "))
for i in range(2,lietke+1):
    for e in range(2,i) :
        if i % e == 0 :
            break
    else :
        tang.append(str(i))
print( "các số nguyên tố : "  , ",".join(tang))
sample_string = input(" nhập vào một chuỗi : ")
# ko in ra chữ o
mang_moi = []   
for kitu in sample_string:
    if kitu == "o":
        continue
    mang_moi.append(kitu)
print("".join(mang_moi))