# -*- coding:utf-8 -*-
import chardet

class test(object):
    def __init__(self,name):
        print("郝垠鹏's name is ", name)

t = test('hao')
print('郝'.encode('UTF-8'))
print(chardet.detect('郝'.encode('UTF-8')))



