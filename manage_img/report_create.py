# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:51:38 2017

@author: uq
"""
import argparse
import os
import base64

class HtmlReport(object):
    def __init__(self, path):
        self.path = path
    def create(self):
        f = open(self.path + '/report.html', 'w')
        os.chdir(self.path + '/img')
        files = os.listdir()
        idx = 1
        f.write('<HTML><HEAD><link rel="stylesheet" href="report.css"></HEAD><BODY><TABLE border=1>\n') 
        for file in files:
            name, ext = os.path.splitext(file)
            content = '<TR><TD>{0}</TD><TD>{1}</TD><TD>{2}</TD><TD class="juman"><DIV>{3}</DIV></TD></TR>\n'.format(\
                               idx,\
                               self.get_img('{0}{1}'.format(name, ext), ext.replace('.', '')),\
                               self.get_ocr('{0}{1}.txt'.format(name, ext)),\
                               self.get_juman('j_{0}{1}.txt'.format(name, ext)))  
            f.write(content)
            idx += 1
        f.write('</TABLE></BODY></HTML>') 
        f.close
    def get_img(self, file, ext):
        os.chdir(self.path + '/img')
        f = open(file, 'rb')
        enc_img = str(base64.b64encode(f.read()))
        f.close
        # return '<img src="data:image/jpeg;base64,{1}\">'.format(ext, enc_img.replace('b\'', '', 1)[:-1])
        return '<img src="img/{0}">'.format(file)
    def get_ocr(self, file):
        os.chdir(self.path + '/ocr')
        result = ''
        f = open(file, 'r')
        line = f.readline()
        while line:
            result += '{0}<BR>'.format(line)
            line = f.readline()
        f.close
        return result
    def get_juman(self, file):
        os.chdir(self.path + '/jumanpp')
        result = ''
        f = open(file, 'r')
        line = f.readline()
        while line:
            if line != 'EOS\n':
                result += '{0}<BR>'.format(line.replace(' ','&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', 1).replace('@','&nbsp;&nbsp;', 1))
            line = f.readline()
        f.close
        return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('target_path', help='パスを指定する')
    args = parser.parse_args()
    report = HtmlReport(args.target_path)
    report.create()

