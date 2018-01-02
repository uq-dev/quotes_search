# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:51:38 2017

@author: uq
"""
import argparse
import os
from util.message import Message_JP
import hashlib

def main(path):
    os.chdir(path)
    files = os.listdir()
    for file in files:
        name_org, ext = os.path.splitext(file)
        md5 = ''
        with open(file, "rb") as f:
            data = f.read()
            md5 = hashlib.md5(data).hexdigest()
        if os.path.exists('{0}/{1}{2}'.format(path,md5, ext)):
            print('{0}: {1}'.format(file, md5))
            continue
        os.rename('{0}/{1}'.format(path, file),
            '{0}/{1}{2}'.format(path, md5, ext))

if __name__ == '__main__':
    msg_mn = Message_JP()
    parser = argparse.ArgumentParser()
    parser.add_argument('target_path', help=msg_mn.get('G_SELECT_DIR'))
    args = parser.parse_args()
    main(args.target_path)
