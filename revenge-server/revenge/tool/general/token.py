# coding=utf-8

import time
import hashlib
import os
import base64

class Token:
    def __init__(self):
        pass

    def __generate_md5_token(self, string):
        timestamp = int(time.time())  #获取13位的UNIX时间戳
        md5_string = string + str(timestamp)
        token = hashlib.md5(md5_string.encode('utf-8')).hexdigest()

        return token

    def generate_md5_token_from_string(self, source):
        return self.__generate_md5_token(source)

    def generate_md5_token_from_file(self, file_name, block_size=64*1024):
        file_hash = hashlib.md5()
        with open(file_name, "r+b") as f:
            for block in iter(lambda: f.read(block_size), ""):
                file_hash.update(block)
        token = file_hash.hexdigest()

        return token

    def generate_sha1_token_from_file(self, file_name, block_size=64*1024):
        file_hash = hashlib.sha1()
        with open(file_name, "r+b") as f:
            for block in iter(lambda: f.read(block_size), ""):
                file_hash.update(block)
        token = base64.b64encode(file_hash.digest())

        return token

    def get_md5_token_name(self, file_name):
        file_base, file_ext = os.path.splitext(file_name)
        token = self.__generate_md5_token(file_base + file_ext)
        token_name = token + file_ext

        return token_name