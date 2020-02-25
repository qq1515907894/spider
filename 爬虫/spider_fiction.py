# coding=utf-8
import requests,sys     #调库操作
from bs4 import BeautifulSoup
class downloader(object):   #downloader类
    def __init__(self):     #__init__函数，可以理解为java方法
        self.server = 'http://www.pgyzw.com/html/61/61945/'
        self.target = 'http://www.pgyzw.com/html/61/61945/index.html'
        self.names = []     #存放章节名
        self.urls = []      #存放章节链接
        self.nums = 0       #章节数

    def get_download_url(self):
        req = requests.get(url=self.target)
        req.encoding='gbk'
        html = req.text
        bf = BeautifulSoup(html)
        table=bf.find_all('table', class_='acss')
        a_bf = BeautifulSoup(str(table[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[0:])      #从下标为0开始
        for each in a[0:]:
            self.names.append(each.string)  #章节名
            self.urls.append(self.server+each.get('href'))  #章节链接
#http://www.pgyzw.com/html/61/61945/ + 24421276.html = www.pgyzw.com/html/61/61945/24421276.html
    def get_contents(self,target):
        req = requests.get(url=target)
        req.encoding='gbk'
        html = req.text
        bf = BeautifulSoup(html)
        div = bf.find_all('div',id='content')
        texts = div[0].text.replace('','')
        return texts    #返回获取的内容
    def writer(self,name,path,text):    #写文件操作
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:  #以当前目录新建文本文档，编码格式为utf-8
            f.write(name+'\n')      #写章节名+换行
            f.writelines(text)      #写本章节内容
            f.write('\n\n')
if __name__ == '__main__':
    dl = downloader()   #调用downloader类
    dl.get_download_url()   #获取章节url
    print('《一念永恒》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '一念永恒.txt', dl.get_contents(dl.urls[i]))#写第i章节名加第i章的内容
        sys.stdout.write("  已下载:%.3f%%" % float(i / dl.nums) + '\r')
        sys.stdout.flush()  #刷新缓冲区
    print('《一念永恒》下载完成')