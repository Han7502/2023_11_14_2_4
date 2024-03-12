import math
import pyinputplus as pyip

#1個參數,有傳出值
def circle_area(radius):
    area = radius ** 2 * math.pi #"拍"3.14在math常數中
    return area



radius = pyip.inputFloat("請輸入半徑:")
area = circle_area(radius)#呼叫function傳出area
print(f"半徑{radius},園面積是{area}")