import copy
import time
from PIL import Image
import base64
import io
# id = "4301,长沙市;4302,株洲市;4303,湘潭市;4304,衡阳市;4305,邵阳市;4306,岳阳市; 4307,常德市;4308,张家界市;4309,益阳市;4310,郴州市;4311,永州市;4312,怀化市;4313,娄底市; 4321,株洲市;4322,岳阳地区;4323,益阳市;4325,娄底市;4326,邵阳市;4327,衡阳市;\ 4328,郴州市;4329,永州市;4330,怀化市;"
# bb = id.replace('\\','')
# ss = copy.deepcopy(bb)
# aa = ss.replace(';',',')
# cc = aa.split(',')
# del cc[-1]
#
# num = []
# c_name = []
#
# for i in range(0,44):
#     if i == 0:
#         num.append(cc[i])
#     elif i%2 == 0:
#         num.append(cc[i])
#     else:
#         c_name.append(cc[i])
#
# print(cc)
# print((num))
# print((c_name))

#ss=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#获取本地时间

def image2byte(image):
    '''
    图片转byte
    image: 必须是PIL格式
    image_bytes: 二进制
    '''
    # 创建一个字节流管道
    img_bytes = io.BytesIO()
    # 将图片数据存入字节流管道， format可以按照具体文件的格式填写
    image.save(img_bytes, format="JPEG")
    # 从字节流管道中获取二进制
    image_bytes = img_bytes.getvalue()
    return image_bytes

def byte2image(byte_data):
    '''
    byte转为图片
    byte_data: 二进制
    '''
    image = Image.open(io.BytesIO(byte_data))
    return image

image_path = "static\img.png"
image = Image.open(image_path)
byte_data = image2byte(image)
image2 = byte2image(byte_data)
list=[image2]
list.append([1])
print(list)




