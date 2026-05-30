#bài 1
nguyen= 999
thuc = 3.999
chuoi = "đạt GPA cao muôn cơ sở lập trình"
#địnhh dạng khi in ra 
print(f"giá trị của biến nguyen là: {nguyen}")
print(f"giá trị của biến thuc là: {thuc}")
print(f"giá trị của biến chuoi là: {chuoi}")
#bài 2
ten = input("nhập vào tên của bạn: ")
print(f"tên của bạn là: {ten}")
#bài 3
tuoi = int(input("nhập tuổi của bạn: "))
if (tuoi >= 1) and(tuoi <= 100):
    print("tuổi của bạn nằm trong khoảng từ 1 đến 100")
else:
    print("tuổi của bạn không nằm trong khoẳng từ 1 đến 100")
# bài 4
PI=3.14
chuvi = round(2*PI*5, 6)
print("chu vi hình tròn với bán kính r = 5 là",chuvi,end="\n")
# bài 5 
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
print(a+b)
print(a-b)
print(a*b)
print("phép chia a và b",a/b)
# bài 6
#C1
N = int(input("nhập vào số : "))
if N <= 1:
    print("số không hợp lệ ")
elif N == 2:
    print("Monday")
elif N == 3:
    print("Tuesday")
elif N == 4:
    print("Wednesday")
elif N == 5:
    print("Thursday")
elif N == 6:
    print("Friday")
elif N == 7:
    print("Saturday")
elif N == 8:
    print("Sunday")
else:
    print("số không hợp lệ")
# bài 7: Nhập vào số nguyên N (1-12). In ra tháng trong năm bằng tiếng Anh
N = int(input("nhập vào các tháng trong năm: "))
a =["January (Tháng Một)","February (Tháng Hai)","March","April","May ","June","July","August","September","October","November","December"]
print(a[N-1])
# bài 8
import sys
nam =int(input("nhập vào năm của bạn: "))
thang = int(input("nhập vào tháng của bạn: "))
if(thang >= 1 and thang <= 12):
    if(nam % 400 == 0 and thang == 2):
        print("29")
        sys.exit()
    if(nam % 400 != 0 and thang == 2):
        print("28")
        sys.exit()
    if((thang % 2 != 0 and thang <= 7 ) or (thang % 2 == 0 and thang >= 7)):
        print("31")
        sys.exit()
    else:
        print("30")
        sys.exit()