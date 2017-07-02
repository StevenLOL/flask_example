# -*- coding:utf-8 -*-
# @author:Eric Luo
# @file:ai1.py
# @time:2017/7/1 0001 17:47


class Responce:
    speak = ""
    show = ""
    eventid = ""
    var = []
    pass


class Property:
    name = ""
    ask = ""
    resultID = ""
    property = []
    param = []
    similarity = []
    synonym_part = []
    isDefault = False
    pass


class Param:
    name = ""
    nameEntity = ""
    length_max = 99
    length_min = 1
    type = ""
    value_default = ""
    pass


class ConversationManager():
    pass
