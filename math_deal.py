#!/usr/bin/python
# coding:utf-8

'''
Created on:
@author:
Email:
Version:
Description:
Help:
'''

import random


def generate_verification_code(len=6):

    code_list = []
    for i in range(10):
        code_list.append(str(i))
    for i in range(65, 91):
        code_list.append(chr(i))
    for i in range(97, 123):
        code_list.append(chr(i))
    myslice = random.sample(code_list, len)

    verification_code = ''.join(myslice)
    return verification_code


if __name__ == "__main__":

    # 把字符串变成了函数并且还为该函数提供了全局变量。
    namespace = {"name": "wupeiqi", "data": [18, 73, 84]}
    code = '''def hellocute():return  "name %s ,age %d" %(name,data[0],) '''
    func = compile(code, '<string>', "exec")
    exec func in namespace
    result = namespace['hellocute']()
    print result

    str = generate_verification_code(4)
    print "str = %s" % str



