import urllib.request
import requests         
# import ctypes
import re
import time
import os

def save_img(img_url,dirname):
    #保存图片到磁盘文件夹dirname
    try:
        if not os.path.exists(dirname):
            print ('文件夹',dirname,'不存在，重新建立')
            #os.mkdir(dirname)
            os.makedirs(dirname)
        #获得图片文件名，包括后缀
        regex = re.compile('\?[^&]*')
        timestr = time.strftime('%Y%m%d',time.localtime(time.time()))
        basename = str(regex.search(img_url).group()).replace("?id=", "_")
        basename=timestr+basename
        # basename = os.path.basename(img_url)
        #拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        if(os.path.exists(filepath)):
            print("文件已经存在")
            return
        # print(filepath)
        #下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url,filepath)
    except IOError as e:
        print ('文件操作失败',e)
    except Exception as e:
        print ('错误 ：',e)
    print("Save", filepath, "successfully!")

    return filepath

# 请求网页，跳转到最终 img 地址
def get_img_url(raw_img_url = "https://area.sinaapp.com/bingImg/"):
    r = requests.get(raw_img_url)       
    img_url = r.url # 得到图片文件的网址
    # print('img_url:', img_url)
    return img_url

# 设置图片绝对路径 filepath 所指向的图片为壁纸
def set_img_as_wallpaper(filepath):
    pass
    # ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)

if __name__ == "__main__":
    dirname = os.environ['HOME'] + "/Pictures/bingImg"       # 图片要被保存在的位置
    img_url = get_img_url()
    filepath = save_img(img_url, dirname)   # 图片文件的的路径
    # set_img_as_wallpaper(filepath)
