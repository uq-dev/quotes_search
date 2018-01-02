# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:51:38 2017

@author: uq
"""
import argparse
import os

from util.ocr import OcrGoogleVision
from util.message import Message_JP

def main(path):
    """Run a label request on a single image"""
    os.chdir(path)
    files = os.listdir()
    ocr_analizer = OcrGoogleVision()
    for file in files:
        f = open('{0}.txt'.format(file), 'w') # 書き込みモードで開く
        ocr_analizer.set_file(file)
        f.write(ocr_analizer.analysis()) 
        f.close() # ファイルを閉じる 
    return 0

if __name__ == '__main__':
    msg_mn = Message_JP()
    parser = argparse.ArgumentParser()
    parser.add_argument('target_path', help=msg_mn.get('G_SELECT_DIR'))
    args = parser.parse_args()
    result = main(args.target_path)

