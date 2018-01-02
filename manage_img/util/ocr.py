# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:33:48 2017

@author: yuku
"""
import base64
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

class Ocr(object):
    def __init__(self):
        self.file = ''
    def set_file(self, file):
        self.file = file

class OcrGoogleVision(Ocr):
    def analysis(self):
        credentials = GoogleCredentials.get_application_default()
        service = discovery.build('vision', 'v1', credentials=credentials)
        with open(self.file, 'rb') as image:
            image_content = base64.b64encode(image.read())
            service_request = service.images().annotate(body={
                'requests': [{
                    'image': {
                        'content': image_content.decode('UTF-8')
                    },
                    'features': [{
                        'type': 'TEXT_DETECTION',
                        'maxResults': 1
                    }]
                }]
            })
            response = service_request.execute()
            text = ''
            if 'textAnnotations' in response['responses'][0]:
                text = response['responses'][0]['textAnnotations'][0]['description']
            return text
