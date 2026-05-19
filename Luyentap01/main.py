#bai 1 
so = 10
sothuc = 3.8
chu = "bài tập học phần: cơ sở lập trình"
print(so,'\n',sothuc,'\n',chu)
#bai 2 
PI=3.14
chuvi = round(2*PI*5, 6)
print("chu vi hình tròn với bán kính r = 5 là",chuvi,end="\n")
#bai 3
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
print(a+b)
print(a-b)
print(a*b)
print("phép chia a và b",a/b)
#bai4
def sum_two_numbers(a, b):
    return(a+b)
c=int(input("nhập vào số nguyên c: "))
d=int(input("nhập vào số nguyên d: "))
print("kết quả phép tính cộng 2 số c và d là: ",sum_two_numbers(c,d))
#bai5 
name = input("nhập vào tên của bạn: ")
age = int(input("nhập vào số tuổi của bạn: " ))
average_score = float(input("nhập vào điểm trung bình của bạn: "))
age_next_year = age + 1
doubled_score = average_score ** 2
print("tên của bạn là:", name)
print("số tuổi của bạn là ",age)
print("tuổi của bạn trong năm tới là ",age_next_year)
print("điểm trung bình của bạn là" ,average_score)
print("gấp đôi điểm trung bình của bạn là: ",doubled_score)
print("biến name là kiệu dữ liệu ",type(name))
print("biến age là kiệu dữ liệu ",type(age))
print("biến average_score là kiệu dữ liệu ",type(average_score))
print("biến doubled_score là kiệu dữ liệu ",type(doubled_score))
print("biến age_next_year là kiệu dữ liệu ",type(age_next_year))
