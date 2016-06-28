#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2016 ccdjh <ccdjh.marx@gmail.com>
from __future__ import absolute_import, division, print_function, with_statement


import sys
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


class box_wilddog_helper(object):

    def __init__(self,uri,auth):
        self.URL =uri
        self.AUTH = auth

    def counter_value(self,name):
        uri ='''https://%s.wilddogio.com/counter/%s.json'''%(self.URL,name)
        auth = self.AUTH
        url = '%s?auth=%s'%(uri,auth)

        request = urllib2.Request(url)
        request.add_header('Content-Type', 'application/json')
        request.add_header('Accept', 'application/json')
        request.get_method = lambda: 'GET'
        response = urllib2.urlopen(request)
        counter_value = response.read()
        if counter_value == 'null':
            counter_value = '0'
        else:
            counter_value = json.loads(counter_value)
        return counter_value #unicode


    def counter_plus(self,name):
        counter = self.counter_value(name)
        counter = str(int(counter) + 1)

        uri ='''https://%s.wilddogio.com/counter.json'''%self.URL
        auth = self.AUTH
        url = '%s?auth=%s'%(uri,auth)
        data = '''{"%s":"%s"}'''%(name,counter)

        request = urllib2.Request(url, data=data)
        request.add_header('Content-Type', 'application/json')
        request.add_header('Accept', 'application/json')
        request.get_method = lambda: 'PATCH'
        response = urllib2.urlopen(request)
        counter_value = response.read()

        return counter

    def counter_minus(self,name):
        counter = self.counter_value(name)
        if counter == u'0':
            counter = str(int(counter))
        else:
            counter = str(int(counter) - 1)

            uri ='''https://%s.wilddogio.com/counter.json'''%self.URL
            auth = self.AUTH
            url = '%s?auth=%s'%(uri,auth)
            data = '''{"%s":"%s"}'''%(name,counter)

            request = urllib2.Request(url, data=data)
            request.add_header('Content-Type', 'application/json')
            request.add_header('Accept', 'application/json')
            request.get_method = lambda: 'PATCH'
            response = urllib2.urlopen(request)
            counter_value = response.read()

        return counter


    def datum_get(self,name):
        uri ='''https://%s.wilddogio.com/datum/%s.json'''%(self.URL,name)
        auth = self.AUTH
        url = '%s?auth=%s'%(uri,auth)

        request = urllib2.Request(url)
        request.add_header('Content-Type', 'application/json')
        request.add_header('Accept', 'application/json')
        request.get_method = lambda: 'GET'
        response = urllib2.urlopen(request)
        counter_value = response.read()
        if counter_value == 'null':
            counter_value = 'none'
        else:
            counter_value = json.loads(counter_value)
        return counter_value #unicode


    def datum_push(self,name,value):


        uri ='''https://%s.wilddogio.com/datum.json'''%self.URL
        auth = self.AUTH
        url = '%s?auth=%s'%(uri,auth)
        data = '''{"%s":"%s"}'''%(name,value)

        request = urllib2.Request(url, data=data)
        request.add_header('Content-Type', 'application/json')
        request.add_header('Accept', 'application/json')
        request.get_method = lambda: 'PATCH'
        response = urllib2.urlopen(request)
        counter_value = response.read()
        # print counter_value
        return value

    def expires_get(self,name):
        uri ='''https://%s.wilddogio.com/expires/%s.json'''%(self.URL,name)
        auth = self.AUTH
        url = '%s?auth=%s'%(uri,auth)

        # print(url)

        request = urllib2.Request(url)
        request.add_header('Content-Type', 'application/json')
        request.add_header('Accept', 'application/json')
        request.add_header('User-agent', 'Mozilla/5.0')
        request.get_method = lambda: 'GET'
        response = urllib2.urlopen(request)
        expires_value = response.read()
        if expires_value == 'null':
            expires_value = 'none'
            return 'none'

        else:
            expires_value = json.loads(expires_value)
            # print expires_value
            expires_in_1 = unicode(int(expires_value[1]) - int(time.time()))
            # print expires_in_1

            if int(expires_in_1) < 0 :
                expires_in_1 = 0

            return '''["%s","%s","%s"]'''%(name,expires_value[0],expires_in_1)


    def expires_push(self,name,value,expires_in):
        uri ='''https://%s.wilddogio.com/expires.json'''%self.URL
        auth = self.AUTH
        url = '%s?auth=%s'%(uri,auth)
        # print int(time.time())
        expires_in_1 = unicode(int(time.time()) + int(expires_in))
        # print expires_in_1
        data = '''{"%s":["%s","%s"]}'''%(name,value,expires_in_1)
        # print data

        request = urllib2.Request(url, data=data)
        request.add_header('Content-Type', 'application/json')
        request.add_header('Accept', 'application/json')
        request.get_method = lambda: 'PATCH'
        response = urllib2.urlopen(request)
        expires_value = response.read()
        # print counter_value
        return '''["%s","%s","%s"]'''%(name,value,expires_in)





#test 


class sy(Model):
    a_auth = AuthProperty()
    a_time = TimeProperty()

    a1 = StringProperty()
    a2 = StringProperty(default='my a2')


def main():
    u = sys.argv[1]
    a = sys.argv[2]

    s = sy()
    print(s.value)


    k = box_wilddog_helper(u,a)
    # c = k.counter_minus('box')
    # c = k.counter_plus('box')
    # c = k.counter_value('box')

    # c = k.datum_push('box','love qing')
    c = k.datum_get('box31')

    # c = k.expires_push('box2','love qing22','10')
    # c = k.expires_get('box31')
    print(c)






if __name__ == '__main__':
    main()