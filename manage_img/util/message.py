# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:33:48 2017

@author: uq
"""

import enum



class Message(object):
    def __init__(self):
        self.dic = NULL
    def get(self, key):
        return self.dic[key]

class Message_JP(Message):
    def __init__(self):
        self.dic = {
            'G_SELECT_DIR': '処理対象ディレクトリ',
            'W_DUPLICATE_IMG': '重複画像を検出'
            }
    

