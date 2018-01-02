# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:51:38 2017

@author: uq
"""
import argparse
import os
import hashlib

from util.message import Message_JP

def main(path):
    os.chdir(path + '/img')
    files = os.listdir()
    name_dic = {}
    # 画像ファイルの拡張子、MD5を収集する
    for file in files:
        name_org, ext = os.path.splitext(file)
        if ext != '.txt' and ext != '.db':
            md5 = ''
            with open(file, 'rb') as f:
                data = f.read()
                md5 = hashlib.md5(data).hexdigest()
                dic_img_info = {'ext': ext, 'md5': md5}
                name_dic[name_org] = dic_img_info
    # 収集した情報をもとにファイル名を修正していく
    for name_org in name_dic:
        if os.path.exists('{0}/{1}/{2}{3}'.format(
                path,
                'img',
                name_dic[name_org]['md5'],
                name_dic[name_org]['ext'])):
            print('{0}: {1}'.format(name_org, md5))
            continue
        os.rename(
            '{0}/{1}/{2}{3}'.format(
                path,
                'img',
                name_org,
                name_dic[name_org]['ext']),
            '{0}/{1}/{2}{3}'.format(
                path,
                'img',
                name_dic[name_org]['md5'],
                name_dic[name_org]['ext']))
        os.rename(
            '{0}/{1}/j_{2}{3}{4}'.format(
                path,
                'jumanpp',
                name_org,
                name_dic[name_org]['ext'],
                '.txt'),
            '{0}/{1}/j_{2}{3}{4}'.format(
                path,
                'jumanpp',
                name_dic[name_org]['md5'],
                name_dic[name_org]['ext'],
                '.txt'))
        os.rename('{0}/{1}/{2}{3}{4}'.format(
                path,
                'ocr',
                name_org,
                name_dic[name_org]['ext'],
                '.txt'),
            '{0}/{1}/{2}{3}{4}'.format(
                path,
                'ocr',
                name_dic[name_org]['md5'],
                name_dic[name_org]['ext'],
                '.txt'))
        
if __name__ == '__main__':
    msg_mn = Message_JP()
    parser = argparse.ArgumentParser()
    parser.add_argument('target_path', help=msg_mn.get('G_SELECT_DIR'))
    args = parser.parse_args()
    main(args.target_path)
