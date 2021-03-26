import numpy
import codecs
import cv2

plain_text = 'NguyenHoangLong-NguyenNgocAnhTuan-CuTanPhat'
file_path = '/home/long/crypto'
file_name = 'saoemlaitatmay.mp3'
raw_file = file_path + '/' + file_name
binary_text = plain_text.encode('utf-32')
binary_string = ''.join(format(ord(i), '08b') for i in plain_text)
print(binary_string)
print(len(binary_string))
img = cv2.imread("/home/long/crypto/image.png")
print(img.shape)
f = open(raw_file, 'rb')
bin_data = f.read()
step_size = int(len(bin_data)/len(binary_text))
j = 0
res_bin = bytes()
temp = bin_data.split(maxsplit = len(binary_text))
for i in range (0, len(binary_text) ):
    res_bin += bytes(temp[i])

    if j < len(binary_text):
        res_bin += bytes(binary_text[j])
        j +=1

print(len(res_bin))
# for i in range (0, len(bin_data), step_size):
#     print(bytes(bin_data[i:step_size:1]))
#     print(("-----------"))
#     temp = bytes(bin_data[i:step_size-1:1])
#     print(temp)
#     print("@@@@@")
#     res_bin += temp
#     if i > 0:
#         res_bin += bytes(binary_text[j])
#         j += 1
    
# for i in range (0, len(bin_data)):
#     temp = bytes(bin_data[i])
#     res_bin += temp
#     if i > 0 and i % step == 0:
#         # res_bin += 'b'
#         temp2 = bytes(binary_text[j])
#         res_bin += temp2
#         j += 1
        # print(j)

f.close()
output = open(file_path + '/outpu2t.mp3', 'w')
# for line in range (0, len(binary_text)):
#     output.write(bytes(res_bin[line]))
output.write(str(res_bin))
output.close()
