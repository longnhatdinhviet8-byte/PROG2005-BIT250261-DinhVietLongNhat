#bài 1
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False;
a=int(input("nhập số: "))
print(is_even(a))
#bài 2
b=int(input("nhập số: "))
c=int(input("nhập số: "))
d=int(input("nhập số: "))
maxx= max(b,c,d)
print ("số lớn  nhất là : ", maxx)
#bài 3
def greet(name="Student"):
    print("Hello, " + name + "!")
greet("Alice")
greet()
#bài 4 
tuoi = int(input("nhập tuổi của bạn: "))
if (tuoi >= 1) and(tuoi <= 120):
    print("tuổi của bạn nằm trong khoảng từ 1 đến 120")
else:
    print("tuổi của bạn không năm trong khoẳng từ 1 đến 120") 
#bài 5
chuoi = input("nhập vào chuỗi kí tự : ")
dem=0
for i in chuoi: 
    if i == 'a':
        dem += 1
print("số lần xuất hiện của kí tư 'a' trong chuỗi là : ", dem)
# bài 6 
do_c=float(input("nhập vào độ c: "))
do_f=do_c * 9/5 + 32
print (f"dộ F tương ứng là : {do_f}")
# bài 7 
can = float (input("nhập vào cân năng cuat bạn (kg) : "))
chieu_cao = float(input("nhập vào chiều cao của bạn (m0): "))
bmi = round((can / pow(chieu_cao, 2)), 2)
print (f"chỉ số BMI của bạn là : {bmi}")
# bài 8
so1 =int (input("nhập số thứ nhất : "))
so2 = int (input("nhập số thứ hai : "))
if type(so1) == int and type(so2) == int :
    if so1 == 0 or so2 == 0:
        print ("không thể thực hiện phêp chia do có số 0")
    else:
        print ("thương của 2 số là : ", so1 / so2)
else:
    print("dữ liệu không hợp lệ")
# bài 9
import math
can=int(input("nhập vào 1 số: "))
if(can < 0):
    print("không thể thực hiện phép căn")
else:
    print("căn bậc 2 của số là : ", math.sqrt(can))
# bài 10 
so_hs= int(input("nhập vào số học sinh : "))
bangdiem = []
diem = 0
for i in range(so_hs):
    diem = list(map(int, input(f"nhập lần lượt điểm toán-lý-hóa của học sinh thứ {i+1}").split()))[:3]
    bangdiem. append(diem)
kt=int(input("nhập số học sinh cần kiểm tra"))
if kt <so_hs:
    print(f"điểm trung bình của bạn {kt} là : ",round((sum(bangdiem[kt-1])/3),2))
else:
    print("số học sinh không tồn tại")