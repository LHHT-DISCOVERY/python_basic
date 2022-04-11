# r là mở để đọc
# r+ mở để đọc và ghi
# w mở để ghi . trước đó nó sẽ xóa hết nội dung của file hiện có 
# w+ tạo ra 1 file nếu file đó hiện chưa có
# -> nếu file không tồn tại ,sẽ tạo ra một file với file chúng ta truyền vào 
# a mở để ghi
# -> nếu file không tồn tại sẽ tạo một file với tên là tên file chúng ta truyền vào
# a+ mở để đọc và ghi . đưa con trỏ về cuối file
# -> nếu file ko tồn tại , sẽ tạo ra một file với tên là tên file chung ta truyền vào 
# print(" một số phương thức để lấy nội dung của file ")




# print(" **phương thức read --- 11")
# ob_ject = open("huutri.txt") ; # hữu trí . txt với tên file là huutri.txxt
# data = ob_ject.read() ,# read(<số kí tự bạn muốn đọc>) ;vd read(2) bạn muốn đcọ 2 kí tự
# ob_ject.close()# đóng file tránh gây lỗi file
# print(data) 
# # luu y: thực hiện đọc xong dùng hàm ob_ject.close() ; đóng file lại
# print("\n")



# print('** phương thức Readline --- line 18')
# # giống read nhưng read 1 dòng
# ob_ject1 = open("huutri.txt") 
# data1 = ob_ject1.readline() # lệnh đọc từng dòng hoặc dùng list hoặc tuple để đọc vd : data = list(ob_jext1)
# ob_ject1.close() # đóng file tránh gây lỗi
# print(data1)

print(" **phương thức write --- line 24")
ob_ject2 = open('huutri.txt', mode = "a+") # mở file dưới dạng mode : a+ mở để đọc và ghi 
for x in range(100):
    data2 = ob_ject2.write("\nly huynh huu tri ")
ob_ject2.close() # đóng file
print(data2)
ob_ject6 = open("huutri.txt") # mở file
data3 = ob_ject6.read() # xem lại file vừa ghi
ob_ject6.close() # đóng file
print(data3)


# print(" **phương thức seek  --- line 29")
# ob_ject3 = open("huutri.txt", mode = "r") ; # mở file dưới dạng mode : r
# data3 = ob_ject3.read() ,# read(<số kí tự bạn muốn đọc>) ;vd read(2) bạn muốn đcọ 2 kí tự
# ob_ject3.seek(0) # xóa nhung dùng lệnh read để xem lại đc 
# data4 = ob_ject3.read() ,# đọc lại file sau khi seek
# ob_ject3.close()# đóng file tránh gây lỗi file
# print(data3) 
# print(data4)