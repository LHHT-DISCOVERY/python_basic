# kĩ thuật công chuỗi
hourly_wage = input("Please enter your hourly wage: ")
hours_worked = input("How many hours did you work this week? ")

print("Hourly wage:" + hourly_wage)
#print(hourly_wage)

print("Hours worked:" + hours_worked)
#print(hours_worked)
age = 20
print("Hours worked:" + str(age) )
# Kĩ thuật format
a = "{} Lý Huỳnh Hữu Trí có số tuổi là :  {}".format("họ và tên : ", 19)
print (a)
b = "{} Hữu Trí {} tuổi là một {} Engineer"
print(b.format("thần đồng", 21 , "AI"))
# Hoặc 
c = "{name} ước mơ trở thành {work} in Xingapo"
print(c.format(name = "Lý Huỳnh Hữu Trí", work = "kĩ sư AI "))
# Nội suy chuỗi với f-String
name = "Trí"
age = 18 
d = f"{name} là sinh viên ở {age * 12} tháng"
print(d)
# xử lí chuỗi cơ bản 
print ("heLLo woRld".lower())
print("helo woRld".upper())
print("helo woRld".capitalize())
print("helo woRld".title())
user_name = " ROLF SMITH  "
print( user_name.strip())  # "ROLF SMITH" xóa khoảng trắng 
print( user_name.title())  # "Rolf Smith"
print( user_name.strip().title()) # vừa k=xóa khoảng trắng vừa ghi hoa kí tự đầu tiên
# Bài tập vận dụng 
greeting = "Hello world "
print("{}!".format(greeting))
# hoặc 
print(f"{greeting} ! ")
ss = input ("what is your name : ").strip().title()
print (f" Hello , {ss} ! ")
title = "joker".upper()
dire = "Viet Nam"
release_year = 2022 
rr = f"{title} ( {release_year }) , director by {dire}"
print(rr)


print(""" 
      ------ PROJECT ĐẦU TIÊN -----
      """)
namee = input(" Nhập tên nhân viên : ").strip().title()
price = float(input (" nhập số tiền lương trên một giờ : "))
work = float(input(" nhập số giờ làm việc trên một tuần : "))
print(" Tên nhân viên là : " , namee )
print (f" Tổng thu nhập của {namee} trong một tuần " ,str ( work * price) , "$")