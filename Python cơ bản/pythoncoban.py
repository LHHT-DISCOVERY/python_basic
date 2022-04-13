print("\n\n") 
print("\t\t\t----- CODE PYTHON BASIC -----\n\n")
# kieu so trong pythonn
print("----------------------------------------------------------------------------------------------------------------")
print("\tI. KIỂU SỐ TRONG PYTHON\t(line 5)\n")
a=4;b=9.6;c =0.12345678910111213141516
print(" a = ",a);print(" b = ",b);print(" c = ",c,)
# kieu dulieu

print("----------------------------------------------------------------------------------------------------------------")
print("\tII. DATATYPE TRONG PYTHON\t(line 11)\n")
print(" a = ",a);print(" c/a = ",c/a)
print(" b/a = ",b/a)
print(" kieu du lieu cua a : " ,type(a))
print(" kieu du lieu cua b : " ,type(b))
print(" kieu du lieu cua b/a : ", type(b/a))
print(" kieu du lieu cua c/a : " ,type(c/a)) 

print("----------------------------------------------------------------------------------------------------------------")
print("\tIII. LẤY SỐ NGUYÊN VÀ THẬP PHÂN TRONG PHÉP TÍNH TOÁN\t(line 20)\n")
from decimal import* #import thu vien
getcontext().prec = 22 #lay 30 chu so phan nguyen va phan thap phan  
print(" gia tri 10/3 la : " ,Decimal(10)/3,); 
print(type(Decimal(10)/3)) ;print("\n")
#tao phan so
print("----------------------------------------------------------------------------------------------------------------")
print("\tIV. PHÂN SỐ TRONG PYTHON\t(line 27)\n")
from fractions import* #import thu vien , luu y: import fractions , ham ghi Hoa
frac1=Fraction(9,6);
frac2=Fraction(3,6);
frac3=Fraction(2,6);
print(" frac1+frac2 = ",frac1+frac2)
print(" frac2+frac3 = ",frac2+frac3)
print(' frac3+frac2 = ',frac3+frac2)

#tao so phuc
print("----------------------------------------------------------------------------------------------------------------")
print("\tV. SỐ PHỨC TRONG PYTHON\t(line 38)\n")
d =  complex(2,3)
print(d);
print(d.real) ; print(d.imag) # lay phan thuc và phan ao
print("\n")
# cac phep toan tron python
print("----------------------------------------------------------------------------------------------------------------")
print("\tVI. CÁC PHÉP TOÁN TRONG PYTHON\t(line 45)\n")
print(b//a); # ket qua lay phan nguyen
print(b%a) # chia lay phan du
print(b**3) ;print("\n") ;# ham mu

#thu vien math
#import<tenthuvien>

# kieu du lieu chuoi
print("----------------------------------------------------------------------------------------------------------------")
print("\tVII. KIỂU DỮ LIỆU CHUỖI\t(line 55)\n")
ten = " Ly Huynh Huu Tri"
print(" ten la:", ten)
#chuoi nhieu dong
Ten = ''' Ly 
 Huynh
 Huu 
 Tri'''
print(Ten)

print("----------------------------------------------------------------------------------------------------------------")
print("\tVIII. ĐỊNH DẠNG % THAY THẾ CHUỖI\t(line 66)\n")
t = " Ly Huynh Huu %s %s " %(" Tri"," yeu Ngyen Thi My Lin"); # %s thay bang (Tri),(yeu Nguyen Thi My Lin)
print(t)
str = "%s %s"
kq = str %(" lY HUYNH HUU TRI"," LOVE NGUYEN THI MY LIN")
print(kq,"\n\n")
# ki hieu %s %r thay the vs moi doi tuong ca so, lan string 
print("----------------------------------------------------------------------------------------------------------------")
print("\tIX. ĐỊNG DẠNG % THAY THẾ\t(line 74)\n")
k = " %s" %("3")
print(k)
ki = " %s" %("tri")
print(ki)
kj = " %r" %("LIN")
print(kj)
# ki hieu %d thay the cho mot so
i = " %d" %(3)
print(i)
j = " %.3f"%(3.99999) # %.1 la lam tron den mot chu so 
print(j,"\n\n")
# dinh dang chuoi , "chuoi f" 
print("----------------------------------------------------------------------------------------------------------------")
print("\tX. CHUỖI f\t(line 88)\n")
k = " cod"
kw = f"{k}er_Tri Huu\n\n";
print(kw)
#vd chuoi f
print("----------------------------------------------------------------------------------------------------------------")
print("\tXI. ỨNG DỤNG CHUỖI f\t(line 94)\n")
name = " Huu Tri";
address = " Quang Nam"
phone = " 0333915138 "
hienthi = f" student : {name}\n Address : {address}\n Phone: {phone}\n\n"
print(hienthi)
print("----------------------------------------------------------------------------------------------------------------")
print("\tXII. FORMAT TRONG PYTHON\t(line 101)\n")
fr = " 1:{one} , 2:{two} , 3:{three}".format(one = "huu tri" , two = "my lin" , three=1)
print(fr)
frm = " 1: {} , 2: {} , 3: {}".format("one", 222 , "333")
print(frm)
frm1 = " 1: {0} , 2: {1} , 3: {2}".format("one", 222 , "333") # tính từ số 0
print(frm1)
frm2 = " 1: {2} , 2: {1} , 3: {0}".format("one", 222 , "333")
print(frm2)
print("\n\n")
print("----------------------------------------------------------------------------------------------------------------")
print("\tXIII. ỨNG DỤNG FORMAT TRONG PYTHON (căn lề,form)\t(line 112)\n") 
fra4 = "{:^50}".format(" LÝ HUỲNH HỮU TRÍ ") # CĂN LỀ GIỮA , cách 50
print(fra4)
fra5 = " Tri{:-^5}>Lin".format("Yeu") # tri--yeu-->Lin
print(fra5)
fra6 = "{:<0}".format(" LÝ HUỲNH HỮU TRÍ ") # CĂN LỀ TRÁI , cách 80
print(fra6)
fra7 = "{:>50}".format(" LÝ HUỲNH HỮU TRÍ ") # CĂN LỀ PHẢI , cách 80
print(fra7, "\n\n\n")
row_0 = "+{:-^75}+".format("BẢNG TEST FORMAT (line 121)")
row_1 = "+{:-<21}+{:-^31}+{:->21}+".format("","","")
row_2 = "|{:^5}|{:^15}| {:^30}| {:<20}|".format("STT","ID","Họ và Tên","Ngày/Tháng/năm Sinh")
row_3 = "|{:^5}|{:^15}| {:<30}| {:<20}|".format("0","106190087","Lý Huỳnh Hữu Trí","20/10/2001")
row_4 = "|{:^5}|{:^15}| {:<30}| {:<20}|".format("1","106190088","Nguyễn Thị Mỹ Linh","3/2/2001")
row_5 = "|{:^5}|{:^15}| {:<30}| {:<20}|".format("2","106190089","Hứa Việt Toàn","2/1/2001")
row_6 = "|{:^5}|{:^15}| {:<30}| {:<20}|".format("4","106190090","Tôn Thất Thanh Sang","9/3/2001")
row_7 = "|{:^5}|{:^15}| {:<30}| {:<20}|".format("5","106190091","Nguyễn Ngọc Hiếu","23/4/2001")
row_8 = "|{:^5}|{:^15}| {:<30}| {:<20}|".format("6","106190092","Trần Văn Thái","20/5/2001")
row_9 = "+{:-<21}+{:-^31}+{:->21}+".format("","","")
print(row_0);
print(row_1);
print(row_2);
print(row_3);
print(row_4);
print(row_5)
print(row_6);
print(row_7)
print(row_8);
print(row_9)
print("\n\n")
print("----------------------------------------------------------------------------------------------------------------")
print("\tXIV. PHƯƠNG THỨC CHUỖI TRONG PYTHON\t(line 143)\n") 
a="lý hUỳnh hữU Trí"
b=a.capitalize() #viet hoa chữa cái đầu tiên , còn lại viết thường
c=a.upper() # viết hoa toàn  bộ chuỗi
d=a.lower() # viet thường toàn bộ chuỗi
e=a.swapcase() # viết hoa thành viết thường , viết thường thành viết hoa
f=a.title()
'''g=a.center(width,[fillchar]) 
trả về 1 chuỗi đc căn giữa với chiều rộng width, kí tự [fillchar] là 1 chuỗi có độ dài là 1'''
g=a.center(30,"*") 
h=a.rjust(30,"*") # tương tự căn phải
m=a.ljust(30,"*") # căn trái
print(" chuoi ban dau a = " ,a), 
print(" viet hoa chu dau chuoi a :   " ,b)
print(" viet hoa toan bo chuoi a : ",c)
print(" viet thuong toan bo chuoi a : ",d)
print(" viet chu thuong thanh hoa chu hoa thanh thuong chuoi a : ",e)
print(" viet hoa chu cai dau tien trong chuoi a : ",f)
print(" căn giữa chuoi a , bằng dau '*' :  " , g)
print(" căn phai chuoi a , bằng dau '*' :  " , h)
print(" căn trai chuoi a , bằng dau '*' :  " , m)
print("\n")
print("--------------------CÁC PHƯƠNG THỨC SỬ LÝ CỦA CHUỖI--------------------(line 165) \n")

print(" 1. phương thức encode --- line 167 \n")
"""
hàm encode dùng để mã hóa hiển thị các ngôn ngữ 
"""
print(" chuoi ban dau a = " ,a), 
v = a.encode()
print(" sau khi ma hoa chuoi a : ",v); print("\n")

print(" 2. phương thức join --- line 175\n")
'''hàm có tác dụng cộng chuỗi '''
print(" chuoi ban dau a = " ,a), 
x = a.join([' đẹp trai ', ' 2 ' , ' yêu Mỹ Lin ', ' ']) #sd dấu cách <" "> để hiển thị đc a , mà ko muốn cộng thêm kì tự cuối cùng 
# cách hàm thực hiện : kí tự 1 + a + kí tự 2 + a + kí tự 3 + a + kí tự 4 ,..
# b1 : đẹp trai + lý hUỳnh hữU Trí (đẹp trai + a)
# b2 : đẹp trai + lý hUỳnh hữU Trí + 2 + lý hUỳnh hữU Trí (b1 + 2 + a) 
# kq : đẹp trai + lý hUỳnh hữU Trí + 2 + lý hUỳnh hữU Trí + yêu Mỹ Lin)(b2+yêu mỹ lin + ...{a + " kí tự thứ 4 -> + a + kí tự thứ 5,..."})
print(" sau khi su dung phuong thuc join : " , x), print("\n")

print(" 3. phương thức replace --- line 185 \n") # phương thức thay thế
"""
thay thế kí tự này bằng kí tự khác
x = a.replace('kí tự bị thay thế ',' kí tự đc thay thế' , count )" count là : 0 điền thì thay thế toàn bộ , count là : hoặc thay thế bao nhiêu lần kí tự
"""
print(" chuoi ban dau a = " ,a)
x1 = a.replace('í','é')
print(" chuoi sau khi thay the la : " , x1),print("\n")

print(" 4. phương thức strip --- line 194\n") # trả về chuỗi đã đc xóa phần đầu và phần cuối của (kí tự) đc truyền vào hàm strip 
print(" chuoi ban dau a = " ,a),
x2 = a.strip('í') # cắt chữ nào nằm ở hai đầu
# có thể cắt nhiều hơn nếu bạn muốn thực hiện truyền : <"abcd"> vào hàm strip ->cắt abcd ở 2 đầu chuỗi
print(" kq sau khi xoa ki tu <í> ở 2 đầu chuoi đc truyen vao hàm strip la : " ,x2)
print("\n")

print(" a. right strip --- line 201\n");print(" chuoi ban dau a = " ,a)
x3= a.rstrip('Trí') # cắt chữ 'Trí' nằm ngoài cùng ở bên phải
print(" kq sau khi xoa ki tu <Trí> đc truyen vao hàm strip la : " ,x3)
print("\n")

print(" b. left strip --- line 206\n");print(" chuoi ban dau a = " ,a)
x4 = a.lstrip('lý') # cắt chữ 'lý' nằm ở ngoài cùng bên trái
print(" kq sau khi xoa ki tu <lý> đc truyen vao hàm strip la : " ,x4)
print("\n")

print("----------CÁC PHƯƠNG THỨC TÁCH CHUỖI----------(line 211) \n")

print(" 1. phương thức split --- line 213 \n")
print(" chuoi ban dau a = " ,a)
# x5 = a.split("kí tự", count) với <"kí tự"> cần cắt và bỏ , count là : cắt bao nhiêu lần
x5 = a.split(" ") # <" ">cắt và bỏ khoảng trắng 
print(" kq sau khi su dung ham split() : " ,x5) # đc xem như left split()
print("\n")

print(" a. right split --- line 220\n");print(" chuoi ban dau a = " ,a)
x6 = a.rsplit(" ",2) # <" ">cắt và bỏ khoảng trắng từ bên phải qua 2 lần 
print(" kq sau khi su dung ham split() cat bo tu ben phai qua 2 lan : " ,x6)
print("\n")

print(" 2. phương thức partition --- line 225 \n")
print(" chuoi ban dau a = " ,a);
# x7 = a.partition('ki tu', so lan cat) # cắt lấy từng chuỗi
x7 = a.partition('hữU')
print(" kq sau khi dung partition la :" , x7) 
# tương tự right partition , 7 = a.rpartition('hữU')
print("\n")

print(" 3. phương thức count --- line 233 \n")
print(" chuoi ban dau a = " ,a); # đếm kí tự 
x8 = a.count('U') ;x88 = a.count('h')
print(" kq sau khi sd phuong thuc count : " , x8,x88)
print("\n")

print(" 4. phương thức tính số lần xuất hiện của kí tự --- line 239 \n")
print(" chuoi ban dau a = " ,a) # đếm kí tự
x9 = a.count('U' , 0 , 8) # tìm số chữ 'U' xuất hiện từ 0->8 
print(" kq sau khi sd phuong thuc tan xuat xuat hiên cua ki tu 'U' : " , x9)
print("\n")

print(" 5. phương thức startswith --- line 245 \n")
print(" chuoi ban dau a = " ,a) 
# x8 = a.startswith('ki tu' , khoang xuat hien )
x10 = a.startswith('h',3,8) #kiểm tra xem chuỗi có bắt đầu bằng kí tự ko , nếu đúng true , sai false
# kiểu tra xem từ 3->9 chữ bắt đầu có phải là "h" ko ?
print(" kq sau khi sd phuong thuc startswith kiemtra chuoi : " , x10)
print("\n")

#nếu ko tuyền vào khoảng cách tìm thì mặc định là đầu chuỗi nếu là startswith hoặc cuối chuỗi nếu là endswith
print(" 6. phương thức endswith --- line 254 \n")
print(" chuoi ban dau a = " ,a) 
# x11 = a.endswith('ki tu' , khoang xuat hien )
x11 = a.endswith('h',3,10) #kiểm tra xem chuỗi có kết thúc bằng kí tự ko , nếu đúng true , sai false
# kiểu tra xem từ 3->10 chữ kết thúc có phải là "h" ko ?
print(" kq sau khi sd phuong thuc endswith kiemtra chuoi : " , x11)
print("\n")

print(" 7. phương thức find (tìm kiếm) --- line 262 \n")
print(" chuoi ban dau a = " ,a) 
# x12 = a.find('ki tu')
x12 = a.find('h') # tìm vị trí đầu tiên chuỗi xuất hiện từ trái sang 
print(" kq sau khi sd phuong thuc find kiemtra chuoi : " , x12)
 # tương tự : từ phải sang x12 = a.rfind('ki tu')
print(" -tương tự cho index --- line 269 \n")
# tương tự index : x12 = a.index('ki tu') , nếu ko có sẽ báo lỗi

print(" 8. phương thức kiểm tra chữ thường(islower) --- line 271 \n")
print(" chuoi ban dau a = " ,a) 
x13 = a.islower(); # kiểm tra chuỗi có toàn chữ thường hay ko 
print(" kq sau khi kiemtra chuoi : ",x13)
print("\n")

print(" 9. phương thức kiểm tra chữ hoa (isupper) --- line 277 \n")
print(" chuoi ban dau a = " ,a) 
x14 = a.isupper(); # kiểm tra chuỗi có toàn chữ hoa hay ko 
print(" kq sau khi kiemtra chuoi : ",x14)
print("\n")

print(" 10. phương thức kiểm tra có phải kiểu số (isdigit) --- line 283 \n")
z="3d"
print(" chuoi ban dau z = " ,z) 
x15 = z.isdigit(); # kiểm tra chuỗi có là kiểu số hay ko 
print(" kq sau khi kiemtra chuoi : ",x15)
print("\n")
print(" -tương tự : phương thức chuỗi isspace() dùng để kiểm tra chuỗi có phải là toàn bộ đều là khoảng trắng hay ko ? ")

print("\n\n")
print("----------------------------------------------------------------------------------------------------------------")
print("\tXV. LIST TRONG PYTHON\t(line 293)\n") 
# giới hạn bằng cặp ngoặc vuông[]
# các phần tử của list cách nhau bởi dẩu ","
# list có khả năng chứa mọi giá trị đối tượng của python và gồm chính nó 
print(' KHÁI NIỆM LIST: \n') ;t =  ["tri",21]; # đây là một list t
print(" ",t)
# hoặc
tr = [["123",'456'],['789','ly Huynhhuu tri']] # a=[] list rỗng
print(" ",tr) ; print("\n")
# tạo lis phần tử từ 0 -> (n-1)
print( ' 1.tạo lis phần tử từ 0 -> (n-1)----line 303\n')
# tạo ra 1 list aa = (<bien cần tạo > for <bien cần tạo> in range(n : tạo ra bao nhiêu phần tử ))
aa = [i for i in range(30)] # tạo một list gán vào biến aa và in ra màn hình vs list đc tạo nằm trong từ 0 ->30
print(" ",aa) ;print("\n")
# tạo một công thức từ list
print(' 2.tạo một công thức từ list ---- line 308 \n')
ab = [ [n,n*1 , n*2] for n in range(1,4)]; # in ra 3 phần từ trong list ab từ 1 -> 4 , với công thức [n,n*1 , n*2]
print(" ",ab);print("\n")
# đưa ra danh sách từng kí tự trong chuỗi
print(" 3.đưa ra danh sách từng kí tự trong chuỗi ----line 312\n")
ac = list("lý huỳnh hữu trí");
print('',ac ,"  \n")
# list là 1 một tập hợp nhiều phần tử , nhưng data int ko phải tập hợp nhiều phần tử nên ko sd list(int) ;
# toán tử cộng
print(' 4.toán tử cộng trong list ----line 317\n');
aaa=[1,2,3]
aaa += ["lý huỳnh", 'hữu trí'];
print(" " ,aaa); print("\n")
# một chuỗi cộng vs list ko đc vd : a = "ly huynh" ; a += ["huu",'tri'] => ko chạy đc 
print(' 5.toán tử nhân trong list ----line 322\n');
#vd:
aab=[1,2,3]
aab*=2 # nhân lên 2 lần list aab
print(" ",aab); print("\n")
# ko thể nhân 2 list vs nhau , nghĩa là nhân với một số nào đó lên n lần , ps: chuỗi thì đc 
print(' 6.toán tử kiểm tra có nằm trong list hay ko (toán tử in trả về true nếu có , false nếu ko) ----line 328\n');
s = [1,2];
zx = 1 in s; # kiểm tra 1 có nằm trong list s ko 
zz = "tri" in s # # kiểm tra "tri" có nằm trong list s ko 
print(" " , zx, "\t ;" , zz) ; print("\n")
# 
print(' 7.lấy ra phần tử nằm trong list,Xắp Xếp , Đảo  ----line 334\n');
#vd:
tr1 = [123,456,[789,'ly Huynhhuu tri']] # lenght là 3 : 0,1,2,3 phần tử 
kq = tr1[1] # lấy ra phần tử index thứ 1 , đầu tiên là 0 và indexx bắt đầu tính từ 0
# lấy ra phần tử cuối lấy [-1]
print(" ",kq) ; print("\n")
print("  a.lấy ra phần tử trong list của list ---line 340 \n")
kq1 = tr1[2][1] # lấy ra phần tử thứ 1 trong lisw thứ 2 với  tr1 = [123,456,[789,'ly Huynhhuu tri']]
print(" ",kq1); print("\n")
print("  b.lấy ra 1 list phần tử trong list ,các thao tác vs list ---line 343 \n")
print("- list ban đầu : " , tr1)
kq2 = tr1[1:3] # lấy phần tử từ 1 đến 3 ; 3 là độ dài lấy ra của tr1
print(" " , kq2)
#vd lấy ra toàn bộ trong list:
kq3 = tr1[:3] # lấy ra toàn bộ trong list ; 3 là lenght list
print(" " , kq3)
#vd lấy ra toàn bộ rồi đảo trong list :
kq4 = tr1[::-1] # lấy ra toàn bộ rồi đảo trong list
print(" " , kq4)
#vd  lấy từ đầu đến phần tử thứ 2 trong list:
kq5= tr1[:2] # lấy từ đầu đến phần tử thứ 2 trong list ; nếu lấy từ n trở đi thực hiện [n:]
print(" " , kq5)
# vd đảo : 
kq40 = [2,3,4,5,6,7,8,9]
kq41 = kq40[::-1] # lấy ra toàn bộ rồi đảo trong list
print("- list ban đầu : " , kq40)
print("- list sau khi đảo : " , kq41)
print('\n')
print(' 8.thay đổi nội dung nằm trong list ----line 362\n');
# vd : tr2 = [123,456,[789,'ly Huynhhuu tri']]
tr2 = [123,456,[789,'ly Huynhhuu tri']]
print("- list ban đầu : " , tr2)
# HOẠT ĐỘNG : CHỈ VIỆC GỌI NÓ RA [đưa vào vị trí cần thay đổi nội dung] VÀ GÁN CHO GIÁ TRỊ MỚI LÀ OK .
#!lưu ý list đếm từ 0 , nên chú ý vị trí thay đổi
tr2[1] = "my lin"  # thay đổi vị trí 1 của tr2 là : 456 rồi gán bằng " my lin"
tr3 = tr2[1] # gán tr3 bằng tr2 tại ví trí 1 cần thay đổi
print("- list sau khi đổi nội dung 'tr2' : " , tr2) # gọi lại tr2 sau khi đổi để xem kq 
print('\n')
# lưu ý : vd:  zzz = [[index(0)],[index(1)],[index(2)],...[.index(n).],..n..] 
# nếu thay đổi nguyên list con cú pháp : zzz[indexx "vị trí cần thay thế"] = ' kí tự thay vào '
#thay đổi vị trí trong list con của list cú pháp:
# => zzz[muốn thay đổi list con thứ bao nhiêu tín từ 0][vị trí cần thay đổi trong list con đó tính từ 0] = ' kí tự thay vào '
print("----------------------------------------------------------------------------------------------------------------")
print("\tXVI. MA TRAN (LIST) TRONG PYTHON\t(line 377)\n")
#vd:
print(" KHÁI NIỆM : - matrix là một list nằm trong 1 list  \n")
matrix = [[1,2,3],[4,5,6],[7,8,9]];
print(' ',matrix[0])#truy xuất từng danh sách
print(' ',matrix[1])#truy xuất từng danh sách
print(' ',matrix[2])#truy xuất từng danh sách 
print("\n")
print(" - truy xuất vào danh sách matrix giống như truy xuất trong list , code truy xuất ở line --- 334 ")
print(' - lưu ý không được phép gán list này qua list kia, dẫn đến khi muốn thay đổi mỗi mảng này thì kéo theo mảng đầu thay đổi \n')
print('- muốn thay đổi mảng gán mảng ban đầu mà ko làm mảng ban đầu thay đổi thì \n')
print(' cách sử lý là : --- line 392')
#xử lý khi gán giá trị mà thay đổi 1 biến , biến còn lại ko thay đổi
b2 = matrix ;
b2[0] = 'TRÍ'
b1 = list(matrix)
b1[0] = 'TRÍ'
print(" mảng b sau khi gán từ matrix và thay đổi : " ,b2)
print(" mảng matrix ban đầu bị kéo thay đổi theo : " , matrix)
print(" mảng sau khi đc sử lí, mảng b1 thay đổi nhưng matrix vẫn ko thay đổi : " , b1 )
print(' - lưu ý khi copy 1 list của matrix \n')
# thay thế trong ma trận cx tương tự thay đổi trong list
print("\n")
print("-------------------CÁC PHƯƠNG THỨC SỬ LÝ CỦA LIST--------------------(line 400) \n")
print(" 1. phương thức count (đếm vị số lần lặp lại của phần tử trong list) ---401")
ace = [1,2,3,4,5]
print(" -list ban đầu : ",ace)
c =  ace.count(1)
print(" -đếm xem số 1 xuất hiện bao nhiêu lần : ",c), print("\n") , # nếu có in ra , còn ko có báo lỗi 
print(" 2. phương thức index (vị trí của phần tử nằm trong list) ---line 406")
c1 =  ace.index(1)
print(" -list ban đầu : ",ace)
print(" -đếm xem số 1 nằm ở vị trí của phần tử nằm trong list : ",c1), print("\n") 
# nếu ko có số tồn tại thì báo lỗi 
print(" 3. phương thức copy (copy phần tử nằm trong list) ---line 411")
c2 =  ace.copy()
# vd thay thế ace tại vị trí 0 bằng ''hữu trí'' để xem ace có bị thay đổi theo hay ko ?
c2[0] = 'hữu tri'
print(" -list ban đầu : ",ace)
print(" -thay mảng c2 bằng vị trí đầu tiên của ace bằng 'hữu trí': ",c2) 
print(" -test thử sau khi thay đổi c2 thì ace có thay đổi ko  : ",ace , "=> vẫn ko thay đổi"), print("\n") 
print(" 4. phương thức clear (xóa các phần tử trong list) ---line 418")
c3 =  ace.clear()
print(" -list ban đầu : ",ace)
print(" -xóa các phần tử trong list : ",c3), print("\n") 
print(""" vidu : tiền tèo bằng 1 list 50 , sau đó in ra = 50 , sau đó in ra tiền của gấu tèo và tiền tèo => bằng 50 ;
 + nếu tiền của gấu = rỗng thì in ra ? tại sao tiền của tèo là 50 mà gấu tèo bị mất ?  """)
tien_teo =[50];
print(" tien teo :",tien_teo)
tien_gauteo = tien_teo # gán tiền tèo bằng tiền gấu tèo
print(" tien cua gau teo :  ",tien_gauteo)

tien_gauteo.clear() ; # chỉ cần tien_gauteo bị clear thì cả 2 thèn đều bị xóa
print(" tien teo :",tien_teo)
print(" tien cua gau teo :  ",tien_gauteo) ; print('\n')

#
print(" 5. phương thức append ( nhét phần tử vào trong list) --- line 434")
ace1 = [1,2,3,4,5]
print(" list ban đầu:" , ace1)
ace1.append(10) # thêm 10 vào phần tử cuối mảng
ace2 = [1,2,3]
ace2.append([12,13,14]) # thêm list con [12,13,14] vào list cha và thêm vào cuối mảng
print(" list sau khi thêm phần tử (append):" , ace1 ,"\n list sau khi thêm list con  (append):" ,ace2 ) ; print("\n")

print(" 6. phương thức extend ( cũng là nhét phần tử nhưng mở rộng ra trong list) --- line 442") # nghĩa khi thêm vào ko tách list nhở mà là 1 list lớn hơn vs ban đầu
ace3 = [0,1,2,3]
print(" list ban đầu:" , ace3)
ace3.extend([12,13,14]) # thêm list con [12,13,14] vào list cha và thêm vào cuối mảng
print(" list sau khi thêm phần tử bổ sung (extend):" ,ace3 , "=> list đã đc thêm và mở rộng ")  ; print("\n")
# nếu đưa 1 list vào ko muốn dùn vòng lặp thì dùng extend để đưa vào

print(" 7. phương thức insert ( sửa phần tử x tại vị trí y trong list) --- line 449") # nghĩa khi thêm vào ko tách list nhỏ mà là 1 list lớn hơn vs ban đầu
ace4 = [0,1,2]
print(" list ban đầu:" , ace4)
ace4.insert(1,6) # thêm phần tử "6" , tại vị trí 1 , nếu lớn hơn lenght list thì mặc định truyền vào cuối như append
print(" list sau khi sửa phần tử 6 , tại vị trí 1 (insert):" ,ace4, "=> list đã đc thêm  ")  ; print("\n") 

print(" 8. phương thức pop (bỏ đi vị trí đó , trả về giá trị ở vị trí bị bỏ đi đó trong list) --- line 455") 
ace5 = [0,1,3]
print(" list ban đầu:" , ace5)
ace6 = ace5.pop(2) ; #ace5.pop(2) bỏ đi vị trí thứ 2 và xuất ra giá trị ở vị trí thứ 2
print(" list sau khi bỏ phần tử ở vị trí thứ 2 => " ,ace5 , "và xuất ra giá trị ở vị trí thứ 2 mà ta bỏ đi : " ,ace6)  ; print("\n")
# khi ko truyền vào trong <pop()> mặc đị bỏ đi vị trí cuối cùng và xuất ra giá trị ở vị trí cuối cùng

print(" 9. phương thức remove (bỏ đi giá trị của phần tử trong list) --- line 462")
ace7 = [0,1,3]
print(" list ban đầu:" , ace7)
ace7.remove(0) ; #ace7.remove(0) bỏ đi giá trị 0 trong list 
print(" list sau khi bỏ giá trị 0 trong list ban đầu => " ,ace7) 
# nếu 2 phần tử có giá trị giống nhau trong 1 list mà ta muốn xóa hết thì remove 2 lần  
# nếu ko có trong list thì chạy bị lỗi 
print("\n")

print(" 10. phương thức reverse (đảo các phần tử trong list) --- line 471")
ace8 = [0,1,3]
print(" list ban đầu:" , ace8)
ace8.reverse() ; #ace8.remove() đảo giá trị trong list
print(" list sau khi đảo giá trị  => " ,ace8)  
print("\n")

print(" 11. phương thức sort (xắp sếp các phần tử trong list) --- line 478")
ace9 = [0,1,3,9,4,2]
print(" list ban đầu:" , ace9)
ace9.sort() ; #ace9.sort(), tương đương với ace9.sort(reverse=False) 
#lưu ý xắp xếp các giá trị trong list cùng data type, mặc định ace9.sort() xắp xếp từ nhỏ đến lớn
print(" list sau khi xắp sếp các phần tử nhỏ đến lớn trong list  => " ,ace9)
ace10= [0,5,1,3,9,4,2];
print(" list ban đầu:" , ace10)
ace10.sort(reverse=True) ; #ace10.sort(reverse=True) xắp xếp các giá trị trong list từ lớn đến nhỏ
print(" list sau khi xắp sếp các phần tử lớn đến nhỏ trong list  => " ,ace10)  
print("\n")
print("----------------------------------------------------------------------------------------------------------------")
print("\tXVII. TUPLE TRONG PYTHON\t(line 490)\n")
# được giới hạn bởi cặp ngoặc ()
# các phần tử của tuple đc phân cách nhau bởi dấu phẩy
# tuple có khả năng chứa mọi giá trị 
# tốc độc truy xuất nhanh hơn list 
# dung lượng chiếm trong bộ nhớ nhỏ hơn list
# bảo vệ dữ liệu của bạn sẽ không bị thay đổi 
# có thể lạm dụng key của dictionary
#  tuple như chang list
print(" KHÁI NIỆM : \n")
# vd:
tup = (1,2,3,3,4,5,"ly huynh huu tri",("3,nguyen thị my lin"))
#  nêu truyền vào 1 phần tử như tup = (1) ; thì tup là kiểu dữ liệu int
print(" ",tup) ; print("\n")
print(" ------------DÙNG TUPLE TẠO MỘT DÃY SỐ CHIA HẾT CHO 2 : --- line 504 ------------")
tup1 = (i for i in range(10) if i % 2 ==0)
print(" ", tuple(tup1)) # cách in ra 

a12 = tuple("huu tri") ;
print(" ",a12)
print("\n")

print("------------------- CÁC TOÁN TỬ TRONG TUPLE --------------------(line 512) \n")

print(" 1. toán tử cộng trong tuple --- line 514")
tup3 = (1,5,8)
tup4 = tup3 + (2,4,6)
print( " ",tup4) ; print("\n")
print(" 2. toán tử nhân trong tuple (nhân 1 tuple vs một số)--- line 518")
tup5 = tup3 * 5 
print(" ", tup3); print("\n")
print(" 3. toán tử in trong tuple --- line 521")
print(" tup3 là : " , tup3)
tup6 = 2 in tup3 # kiểm tra 2 có trong tại trong tuple 3 hay ko ?  có thì trả về true , ko trả về false 
print(" kiểm tra số 2 có tồn  tại trng tuple 3 hay ko : ", tup6); print("\n")
print(" 4. truy xuất các phần tử trong tuple --- line 514")
tup3 = (1,5,8)
tup7 = tup3[2] # lấy giá trị trong tuple ở vị trí 2 , bắt đầu từ 0 -> n
print(" lấy giá trị tại vị trí 2 ở trong tuple 3 :  ", tup7) ; print("\n")
print(" 5. kiểm tra độ dài trong tuple --- line 529") 
tup3 = (1,5,8)
tup8 = len(tup3) # kiểm tra độ dài ở tuple 3
print(" kiểm tra độ dài ở trong tuple 3 :  ", tup8) ; print("\n")
print(" 6. đảo phần tử trong tuple --- line 533") 
tup3 = (1,5,8)
tup9 = tup3[::-1] # đảo phần tử 
print(" đảo phần tử ở trong tuple 3 :  ", tup9) ; print("\n")
print(" +++++ KHÔNG THỂ THÊM , THAY ĐỔI PHẦN TỬ, KÝ TỰ VÀO TUPLE NHƯ LIST +++++ \n")
print(" 7. ma trận trong tuple --- line 533") 
tup10 = ((1,5,4), (2,34,5),(23.435,343))
print(" ma trận ở trong tuple 10 :  ", tup10) ; print("\n")
print(" -in ra ma trận bằng cách gọi từng phần tử trong tuple 10 : ")
print(' ',tup10[0]) # in ra ma trận 
print(' ',tup10[1]) # in ra ma trận 
print(' ',tup10[2]) # in ra ma trận 
print("\n")

print("-------------------CÁC PHƯƠNG THỨC SỬ LÝ CỦA TUPLE--------------------(line 547) \n")
print(" 1. phương thức count (đếm số lần lặp lại của phần tử trong tuple) ---line 548")
tup11 = (1,2,3,4,5)
print(" -tuple ban đầu : ",tup11)
cc1 =  tup11.count(1)
print(" -đếm xem số 1 xuất hiện bao nhiêu lần : ",cc1), print("\n") , # nếu có in ra , còn ko có báo lỗi 
print(" 2. phương thức index ( lấy ra vị trí của phần tử nằm trong tuple) ---line 553")
c1c =  tup11.index(3)
print(" -list ban đầu : ",tup11)
print(" -đếm xem số 3 nằm ở vị trí của phần tử nằm trong tuple : ",'vị trí thứ : ',c1c) ; print("\n") 
# nếu ko có số tồn tại thì báo lỗi 
# trong khi list dùng append để thêm , còn tuple dùng toán tử += để thêm VD: t11 += (phần tử cần thêm vào)
print(" lưu ý !! : tuple ko cho phép sửa đổi nội dung như list , đọc comment line --- 491 \n")
print("----------------------------------------------------------------------------------------------------------------")
print("\tXVIII. HASHABLE VÀ UNHASHABLE (PHÂN BIỆT LIST VÀ TUPLE) TRONG PYTHON\t(line 561)\n")
print(" 1. hàm id --- line 562") 
a11 = id ("huu tri")
print(" hàm a11 = id ('huu tri') có địa chỉ tại a11 là :  ", a11)
b1 = id(a11)
print( """ a11 = id ("huu tri") ; b1 = id(a11) có địa chỉ tại b1 là : """, b1)
print(" hàm print(id(huutri)) có địa chỉ là : " , id ("huu tri") , "=> giống với địa chỉ ở a11 ")
print(" => địa chỉ thay đổi vs kiểu chuỗi , còn số nguyên thì ko đổi  ")
print("\n")
print(" 2. toán tử cộng --- line 570") 
n = 69 
print(""" n = 69 , print (n) => kq trả về mành hình là :  """ , n )
print(" lệnh print(n+1) kq trả về mành hình là : " , n+1 )
print(" lệnh print(n.__add___(1)) kq trả về mành hình là : " ,n.__add__(1)) ; print("\n")

print(" 3. toán tử trừ --- line 576") 
n = 69 
print(""" n = 69 , print (n) => kq trả về mành hình là :  """ , n )
print(" lệnh print(n-1) => kq trả về mành hình là : " , n-1 )
print(" lệnh print(n.__sub___(1)) => kq trả về mành hình là : " ,n.__sub__(1)) ; print("\n")

print(" 4. toán tử nhân --- line 582") 
n = 69 
print(""" n = 69 , print (n) => kq trả về mành hình là :  """ , n )
print(" lệnh print(n*3) => kq trả về mành hình là : " , n*3 )
print(" lệnh print(n.__mud___(1)) => kq trả về mành hình là : " ,n.__mul__(3)) ; print("\n")

print(" 5. toán tử đảo --- line 588") 
n = 69 
print(""" n = 69 , print (n) => kq trả về mành hình là :  """ , n )
print(" lệnh print(-n) kq trả về mành hình là : " , -n )
print(" lệnh print(n.__neg___(1)) kq trả về mành hình là : " ,n.__neg__()) ; print("\n")

print(" ! LƯU Ý GIỮA HASHABLE OBJECT VÀ UNHASHABLE OBJECT ----- LINE 594 \n")
# mỗi toán tử của mỗi đối tượng sẽ có 1 phương thức đi kèm 
# sự khác biệt giữa hash object và unhash object 
# vd: s1 = ["huutri"] ;  s1 = s1 + " coder" ; s1 += s1 + " coder" thì ko có khác biệt gì vs nhau 
# => đều thay đổi giá trị như nhau , nhưng mục đích hiển thị giống nhau giữa 2 toán tử 
# vd : s1 = [1,2] , s2 = [3,4] ; s1 = s1 + [0] ; s2 += [0] ; thì toán tử s2 += [0] ko thay đổi giá trị
# => khi với unhash object thì s2 nó ko thay đổi ,cũng  mục đích hiển thị giống nhau giữa 2 toán tử 
# unhash object là list chứa các phương thức như : add , sub ,mud ,... có thể thay đổi dữ liệu 
# và tuple và chuỗi là 1 hash object , hash object ko thể thay đổi dữ liệu , thay đổi bằng sd toán tử += ,... 
print("----------------------------------------------------------------------------------------------------------------")
print("\tXIX. KIỂU DỮU LIỆU SET TRONG PYTHON\t(line 604)\n")
# được giới hạn bằng dấu ngoặc nhọn {} ,tất cả những gì nằm trong phần tử của set
# các phần tử của set đc cách nhau bởi dấu phẩy 
# set không chứa nhiều hơn 1 phần tử trùng lặp 
# set chỉ chứa các hash table object nhưng nó ko phải là hash table object 
# vd : 
set_1 = {89, 34}
print(" giá trị của set_1 là :" , set_1)
print(" kiểu dữ liệu của set_1 là : " , type(set_1))
set_2 = {89," Huu Tri ",(33,54,34)};
print(" giá trị của set_2 là :" , set_2)
# không thể sử dụng set có chứa mảng vd : set = {"huutri", [45,54,45]} như vậy thì ko thả kiểu dữ liệu list(mảng) vào đc 
# không thể sử dụng set có kiểu tuple chứa mảng vd : set = {("huutri", [45,54,45])}
print("\n")# set ko chứa đc unhash table
print("------------------- CÁC TOÁN TỬ TRONG SET --------------------(line 618) \n")

print(" 1. toán tử IN trong SET --- line 620")
print(" kiểm tra xem 1 có nằm trong set {1,2,4} ko ?  " ,1 in {1,2,3}) 
print("\n")
print(" 2. toán tử trừ trong SET --- line 623")
# toán tử trừ : kq trả về là kq tồn tại trong set 1 mà ko tồn tại trong set 2
print(" toán tử trừ :kq trả về là kq tồn tại trong set 1 mà ko tồn tại trong set 2")#vd :
print(" kết quả khi trừ 2 set : {1,2,3} - {2,3} là : " , {1,2,3}-{2,3})
print("\n")
print(" 3. toán tử và trong SET --- line 628")
# toán tử và : kq trả về là kq vừa tồn tại trong set 1 mà vừa có trong set 2
print(" toán tử và : kq trả về là kq vừa tồn tại trong set 1 mà vừa có trong set 2")#vd :
print(" kết quả và của 2 set : {1,2,3} & {2,3} là : " , {1,2,3}&{2,3})
print("\n")
print(" 4. toán tử hoặc trong SET --- line 633")
# toán tử hoặc: kq trả về là lấy tất cả các phần tử ở trong 2 set
print(" toán tử hoặc: kq trả về là lấy tất cả các phần tử ở trong 2 set")#vd :
print(" kết quả hoặc của 2 set : {1,2,3} | {2,3} là : " , {1,2,3}|{2,3})
print("\n")
print(" 5. toán tử so trong SET --- line 638")
# toán tử so: kq trả về là lấy hết tất cả phần tử 2 bên và loại bỏ những thèn trùng nhau
print(" toán tử so: kq trả về là lấy hết tất cả phần tử 2 bên và loại bỏ những thèn trùng nhau")#vd :
print(" kết quả so của 2 set : {1,2,3}  {2,3} là : " , {1,2,3}^{2,3})
print("\n")
# set ko quan tâm đến vị trí phần tử nằm trong set nên ko đc hỗ trợ 
print("-------------------CÁC PHƯƠNG THỨC SỬ LÝ CỦA SET--------------------(line 644) \n")
print(" 1. phương thức clear ---645")
set_5 = {2,44,6}
print(" set ban đầu : " , set_5)
print(" clear set ban đầu : " ),set_5.clear() # clear set 5
print("\n")
print(" 2. phương thức pop ---650")
set_6 = {2,44,45,6}
print(" set ban đầu : " , set_6)
print(" pop set ban đầu : " ,set_6.pop()) # lấy ra vị trí ban đầu 
print("\n")
print(" 3. phương thức remove ---655")
set_7 = {4,6,44}
print(" set ban đầu : " , set_7)
print(" remove số 44 khỏi set ban đầu : " ),set_7.remove(44) # remove set 7
print(" ", set_7)
print("\n")
print(" 4. phương thức discard(như remove nhưng remove nếu ko có thì báo lỗi còn dis thì khum) ---661")
set_10 = {422,452,44,346}
print(" set ban đầu : " , set_10)
print(" discard số 44 khỏi set ban đầu : " ),set_10.discard(44) # discard set 10
print(" ", set_10)
print("\n")
# lưu ý nếu 2 phần tử giống nhau thì set chỉ hiển thị 1 phần tử , và set có thể hiển thị ko theo thú tự trong khi khai báo types set ban đầu
print(" 5. phương thức copy(copy set) ---668")
set_11 = {4242,4542,444,3446}
set_12 = set_11.copy()
print(" set ban đầu : " , set_11)
print(" tạo set 12 copy từ set ban đầu: " , set_12)
print("\n")
print(" 6. phương thức add(thêm phần tử vào set) ---674")
set_13 = {442,42,44,344}
set_13.add(123)
print(" set ban đầu : " , set_13)
print(" thêm phần tử 123 -> vào set ban đầu: " , set_13)
print("\n")
print(" LƯU Ý : set ko phải là 1 hash object vì :  ")
# nhắc lại : set ko phải là 1 hash object
# vì id nó ko thay đổi sau khi add thêm vào set nghĩa là thay đổi nội dung của set 
#vd
set_14 = {1,2,3,4}
print(" ", id(set_14))
set_14.add(5)
print(" ",id(set_14))
print("\n")
print("----------------------------------------------------------------------------------------------------------------")
print("\tXX. KIỂU DỮU LIỆU DICT TRONG PYTHON\t(line 690)\n")
# dict được giới hạn bằng cặp ngoặc nhọn 
#các phần tử ccash nhau bởi dấu phẩy 
# các phần tử là một key-value 
# các cặp key - value đc sd bằng dấu 2 chấm
# các key - value là mọt hash object
print(" -1. Cách khởi tạo DICT ---- line 696")
dic = {"name" :" hữu trí" , "age " : 21} 
# với key là name , value là " hữu trí " , .. tương tự vế sau
print(" ", dic)
print (" kiểu dữ liệu : " , type(dic))
dic1 = {}
print( ' khởi tạo DICT rỗng : ' , dic1 )
print (" kiểu dữ liệu : " , type(dic1)); print("\n")
print(" -2. Cách khởi tạo từ một mapping object ---- line 704") ; print("\n")
print(" -3. Cách khởi tạo bằng iterable ---- line 705")
# cú pháp : dict(interable)
iter_ = [ (" name " , "tri") , (" age" , 21)]
dic2 = dict(iter_)
print(" " , dic2)
print(" " , type(dic2))
print("\n")
print(" -4. Khởi tạo bằng keywword argument")
# vd:
name = "tri"
age = 21
dic3 = dict (name = "tri" , age = 21)
print(" ", dic3)
print(" " , type(dic3)) ;print(" \n")
print(" -5. Sử dụng phương thức Fromkeys ---- line 719")
iter_1= ("name" , "age") , # sẽ suất ra mành hình key = none
dic4 = dict.fromkeys(iter_1)
print(" ", dic4)
# truyền vào giá trị mặc định của nó 
print(" ----- Truyền vào giá trị mặc định \n")
dic5 = dict.fromkeys(iter_1 ,"tow")
print(" " , dic5)
print(" " , type(dic5))
print("\n")
print(" -6. Lấy value trong DICT bằng KEY ---- line 729")
iter_2 = ("lastname" , "age" , "year" )
dic6 = dict.fromkeys(iter_2 , "huutri")
print( " lấy giá trị của key 'year' từ : " , dic6 ) ;
print (" kq là : " ,dic6["lastname"])
dic7 = {"me" : "tôi" , "my" : " của tôi"}
print( " lấy giá trị của key 'my' từ : " , dic7 )
print(" kq là : " , dic7["my"])
# lưu ý nếu gọi key ko tồn tại thì sẽ báo lỗi
print("\n")
print(" -7. Thay đổi nội dung DIC trong python ---- line 739")
dic8 = {"me" : "tôi" , "my" : " của tôi"}
print( " thay đổi giá trị giá trị của key 'my' từ : " , dic8 )
# thay đổi từ MY = của tôi thành MY = của tay
dic8["my"] = "của tay"
print(" kq là : "  , dic8)
print(" kq từ 'my' : " , dic8["my"])
print("\n")
print(" -8. Thêm thủ công nội dung DIC trong python ---- line 747")
#vd
dic9 = {"coder" : "ly huynh " , "age" : 20}
print(" dic9 = " , dic9)
dic9["coder"] = dic9["coder"] + "huu tri"
dic9["age"] = dic9["age"] + 1 
# thêm một phần tử chưa hề có key trong dic
dic9["year"] = "2022"
print( " kq sau khi thêm thủ công trở thành dic9 mới hoàn chỉnh là : "  , dic9)
print(" \n")
print("-------------------CÁC PHƯƠNG THỨC SỬ LÝ CỦA DICT--------------------(line 756) \n")
print(" 1. phương thức copy ---- line 758")
dic10 = {"coder" : "ly huynh " , "age" : 20}
dic11 = dic10.copy() # địa chỉ dic11 khác với dic10
print(" dic 10 ban đầu là : " , dic10);
print(" dic 11 sau khi copy từ dic 10 là : " , dic11)
print(" \n")
print(" 2. phương thức clear ---- line 764")
dic12 = {"coder" : "ly huynh " , "age" : 20}
print(" dic12 ban đầu là :" , dic12)
dic12.clear()
print(" dic12 sau khi clear là : " ,dic12)
print("\n")
print(" 3. phương thức get (lấy value từ key)---- line 770")
dic13 = {"coder" : "ly huynh " , "age" : 20}
print(" dic 13 có giá trị là : " , dic13)
value = dic13.get("age")
# ngoài ra cú pháp còn đc sd đó là  value = dic13.get("age" , "giá  trị mặc định nếu ko có key trong dict")
print(" dic13 sau khi sử dụng phương thức get lấy value từ key coder là : " , value)
print(" kết quả của dic13 còn lại sau khi get là : " , dic13);print("\n")
print(" 4. phương thức items (trả về 2 giá trị là key và value )---- line 777")
dic14= {"coder" : "ly huynh " , "age" : 20}
print(" dic 14 có giá trị là : " , dic14)
value1 = dic14.items()
print(" dic14 sau khi sử dụng phương thức items là : " , value1)
print(" ** hoặc lấy ra từng key , value --- cú pháp line 784")
# hoặc cách khác để lấy ra từ phần tử như key hoặc value
# cú pháp : value1 = list(dic14.items()) ; print(value1[0]) -> kq là key1 và value 1 , [0][0] -> key1
print("\n")
print(" 5. phương thức keys (lấy danh sách những key có trong dic)---- line 786")
dic15 = {"coder" : "ly huynh " , "age" : 20}
print(" dic 15 có giá trị là : " , dic15)
key=dic15.keys()
print(" kết quả sau khi thực hiện phương thức keys là : " , key)
print("\n")
print(" 6. phương thức value (lấy danh sách những value có trong dic)---- line 792")
dic16 = {"coder" : "ly huynh " , "age" : 20}
print(" dic 16 có giá trị là : " , dic16)
value2=dic16.values()
print(" kết quả sau khi thực hiện phương thức value là : " , value2)
print("\n")
print(" 7. phương thức pop(giống như phương thức get ,pop có tác dụng lấy hoàn toàn ra khỏi dic)---- line 798")
dic17 = {"coder" : "ly huynh " , "age" : 20}
print(" dic 17 có giá trị là : " , dic17)
value3=dic17.pop("coder") # tương tự nếu ko có key nó sẽ lỗi , ta xử lý bằng cách tương tự như với cú pháp 774
print(" kết quả sau khi thực hiện phương thức pop là : " , value3)
print(" kết quả của dic17 còn lại sau khi pop là : " , dic17)
print("\n")
print(" 8. phương thức popitem (lấy giá trị là key và value có trong dic)---- line 805")
dic18= {"coder" : "ly huynh " , "age" : 20}
print(" dic 18 có giá trị là : " , dic18)
value4 = dic18.popitem()
print(" dic18 sau khi sử dụng phương thức popitem là : " , value4)
print("\n")
print(" 9. phương thức setdefault (lấy giá trị value từ key có trong dic ngoài ra còn nhiệm vụ line 812)---- line 811")
# ngoài ra nếu ko có key thì nó mặc định bổ sung key vào dic , hoặc có  thể dùng để bổ sung key và value vào dic
dic19= {"coder" : "ly huynh " , "age" : 20}
print(" dic 19 có giá trị là : " , dic19)
value5 = dic19.setdefault("coder")
print(" dic19 sau khi sử dụng phương thức setdefault là : " , value5)
print(" **dùng để bổ sung thêm key hoặc value vào dic  ")
value6 = dic19.setdefault("người yêu " , "Nguyễn Thị Mỹ Lin")
print(" value sau khi gọi bổ sung : " , value6)
print( " kq sau khi bổ sung thêm cho dic19 là : " , dic19)
print("\n")
print(" 10. phương thức update (update value hoặc up cả key mới,values mới)---- line 822")
dic20= {"coder" : "ly huynh " , "age" : 20}
print(" dic 20 có giá trị là : " , dic20)
value7 = dic20.update(coder = " hữu trí ")
print(" dic20 sau khi sử dụng phương thức update là : " , value7) # hiển thị none nghĩ là trùng key
print(" giá trị dic20 mới là : " , dic20)
print( " **sử dụng update để cập nhập bổ sung ket và value mới cho dic ")
value=dic20.update(love = " trí love Lin 29/10/2021 ") 
# dic 20 đã đổi ly huynh thanh huu tri r tiếp tục lấy dic 20 đó update thêm key và value mới
print(" kq sau khi update thêm cho dic20 : " , dic20)
print("\n")
