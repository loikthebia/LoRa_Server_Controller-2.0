#!/bin/python2.7
# coding=utf-8

import json


class Config():

	def __init__(self):
		try:
            with open('config.json', 'r') as f:
                self.config_data = json.load(f)
        except FileNotFoundError:
            print("File was not found")
            return False
        else:
            return True


    def get_post_url(self):
        return self.config_data['post_url']

    def get_get_url(self):
        return self.config_data['get_url']

    def get_aws_credentials(self):
        return self.config_data['awsCredentials']

    def get_mysql_credentials(self):
        return self.config_data['mysql_credentials']
