import numpy
import codecs
import cv2

plain_text = 'NguyenHoangLong-NguyenNgocAnhTuan-CuTanPhat'
file_path = '/home/long/crypto'
file_name = 'saoemlaitatmay.mp3'
raw_file = file_path + '/' + file_name
en_text = bytes(plain_text, 'utf-32')

f = open(raw_file, "rb")
data = f.read()
f.close()
print(len(data))
print(type(data))
print(len(en_text))
print(type(en_text))
step = int(len(data)/len(en_text))
print(step)
output = file_path + '/output123.mp3'
f = open(output, 'wb')
count = 0
temp = bytes()
#-----------
# for i in range (0, len(data)):
#     if i%step == 0:
#         f.write(data[i:step+i])
#         temp += data[i:step+i]
#         if i > 0:
#             f.write(bytes(en_text[count]))
#             count += 1

# print(len(temp))
# f.write(data[count*step: len(data)])
#-----------
f.write(data)
f.write(en_text)
f.close()
