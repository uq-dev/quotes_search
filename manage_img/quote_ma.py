# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:51:38 2017

@author: uq
"""
import argparse
import os

from util.message import Message_JP

def main(path):
    os.chdir(path)
    files = os.listdir()
    for file in files:
        name_org, ext = os.path.splitext(file)
        if ext == '.txt':
            os.system('jumanpp < {0} > {1}'.format(file, 'j_' + name_org + ext))

if __name__ == '__main__':
    msg_mn = Message_JP()
    parser = argparse.ArgumentParser()
    parser.add_argument('target_path', help=msg_mn.get('G_SELECT_DIR'))
    args = parser.parse_args()
    main(args.target_path)
