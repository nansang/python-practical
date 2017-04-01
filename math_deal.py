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

    str = generate_verification_code(4)
    print "str = %s" % str