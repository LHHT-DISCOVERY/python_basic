card_number = list(input("Please enter a card number: ").strip())

# Remove the last digit from the card number
check_digit = card_number.pop()

# Reverse the order of the remaining numbers
card_number.reverse()

processed_digits = []
for index, digit in enumerate(card_number):
	if index % 2 == 0:
		doubled_digit = int(digit) * 2

		# Subtract 9 from any results that are greater than 9		
		if doubled_digit > 9:
			doubled_digit = doubled_digit - 9

		processed_digits.append(doubled_digit)
	else:
		processed_digits.append(int(digit))

total = int(check_digit) + sum(processed_digits)

# Verify that the sum of the digits is divisible by 10
if total % 10 == 0:
	print("số tài khoản hợp lệ")
else:
	print("số tài khoản không hợp lệ !")

while(1):
    card = list(input(" Nhập vào số tài khoản cần kiểm tra : "))
    xoa = card.pop()
    card.reverse()
    check = []
    for inde , stk in enumerate(card):
        if inde %2 == 0 :
            nhan = int(stk) * 2
            if nhan > 9 :
                nhan = nhan - 9 
            check.append(nhan)
        else :
            check.append(int(stk))
    tong =int (xoa) + sum(check)
    if tong % 10 ==0:
        print(" số tài khoản hợp lệ")
        print(" vui lòng bấm số 1 để thoát , bấm số 2 để tiếp tục ")
        so = int(input("xin mời nhập sự lựa chọn : "))
        if so == 2 :
            print("bạn đã chọn tiếp tục kiểm tra số tài khoản khác ")
            
        elif so == 1:
                
            print("bạn đã chọn thoát chương trình ")
            break 
        else: 
            print (" WRRINGGGGGG !!!!!! CẢNH BÁO ĐANG TẤN CÔNG HỆ THỐNG ")
            break
    elif tong % 10 != 0 :
        print(" số tài khoản không hợp lệ , vui lòng bấm số 1 để thoát , bấm số 2 để tiếp tục ")
        so = int(input("xin mời nhập sự lựa chọn : "))
        if so == 2 :
            print("bạn đã chọn tiếp tục kiểm tra số tài khoản khác ")
        elif so == 1:
            
            print("bạn đã chọn thoát chương trình ")
            break
        else :
            print(" WRRINGGGGGG !!!!!! CẢNH BÁO ĐANG TẤN CÔNG HỆ THỐNG")
            break
        
        