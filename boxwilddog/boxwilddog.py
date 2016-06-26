#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2016 ccdjh <ccdjh.marx@gmail.com>

import time
import json
import types 
import random
import re
import hashlib

import urllib2


class Model(object):
    def __init__(self,**arg): #callback:dict

        class_dict_more = self.__class__.__dict__.copy()

        arg_1 = arg.copy()

        for i in arg_1.keys():
            a = None if i in class_dict_more.keys() else arg_1.pop(i)

        for i in class_dict_more.items():
            a = None if type(i[1]) is types.ListType else class_dict_more.pop(i[0]) 

        for i in class_dict_more.items():
            if i[1][0] == "auth_property":
                class_dict_more[i[0]][2] = HelperHandler.helper_auth()
            if i[1][0] == "time_property":
                class_dict_more[i[0]][2] = HelperHandler.helper_time()

        self.massage = class_dict_more

        for i in class_dict_more.items():
            arg_1[i[0]] = arg[i[0]] if arg_1.has_key(i[0]) else i[1][2]
        self.value = arg_1



class StringProperty(object):
    def __new__(cls,**arg):
        string_property_arg = arg
        me = 'string_property'
        string_property_dict ={}
        default_io = string_property_arg.has_key('default')
        default  = string_property_arg['default'] if default_io else 'none'
        return [me,string_property_dict,default,{}]


class TimeProperty(object):
    def __new__(cls,**arg):
        time_property_arg = arg
        me = 'time_property'
        time_property_dict ={}
        default_io = time_property_arg.has_key('default')
        default  = time_property_arg['default'] if default_io else HelperHandler.helper_time()
        return [me,time_property_dict,default,{}]

class AuthProperty(object):
    def __new__(cls,**arg):
        auth_property_arg = arg
        me = 'auth_property'
        auth_property_dict ={}
        default_io = auth_property_arg.has_key('default')
        default  = auth_property_arg['default'] if default_io else HelperHandler.helper_auth()
        return [me,auth_property_dict,default,{}]



class HelperHandler():

    @classmethod
    def helper_auth(cls):
        t = str(int(time.time()))
        ex = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        e = "".join(random.sample(ex,10))
        x = "".join(random.sample(ex,10))
        return t + e + x

    @classmethod
    def helper_time(cls):
        return str(int(time.time()))

