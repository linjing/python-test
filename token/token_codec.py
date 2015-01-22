#!/usr/bin/python2.6

import time
from Crypto.Cipher import AES
import random
import hashlib
import base64

def debug(s):
    import sys
    print >> sys.stderr, s

def xor_str (fix, input, length):
    output = ''
    for i in range (length):
        output += chr (ord(fix[i]) ^ ord(input[i]))
    return output

class token_codec:
    # as I know, md5 digest length is 16.
    align_to = 16
    md5_len = 16
    master_key = 'abcdefghijklmnopqrstuvwxyz'
    source = master_key[:align_to]
    def __init__ (self, timeout = 1800):
        self.timeout = timeout

    def encode (self, token):
        now = int (time.time ())
        expire_time = now + self.timeout
        info = token + "," + str (expire_time)

        return self.encode_impl (info)
    
    def decode (self, info):
        try:
            tmp = self.deconde_impl (info)
            tmp_list = tmp.split (',')
            cnt = len (tmp_list)
            if cnt < 2:
                raise Exception ("bad format")
            expire_time = tmp_list[cnt-1]
            token = tmp[:-1-len(expire_time)]
            if int(tmp_list[cnt-1]) < time.time ():
                raise Exception ("token expired")
        except Exception, msg:
            raise Exception ('decode token failed: %s' % msg)

        return token


    def encode_impl (self, info):
        key = ''
        for i in range (self.align_to):
            key += random.choice (self.master_key)

        xor_key = xor_str (self.source, key, self.align_to)

        encryptor = AES.new(key, AES.MODE_CBC, key)
        if len (info) % self.align_to != 0:
            info += ','* (self.align_to - len (info) % self.align_to)
        ciphertext = encryptor.encrypt (info)

        m = hashlib.md5 ()
        m.update (info)

        token = xor_key + ciphertext + m.digest ()
        enc_tk = base64.standard_b64encode (token)

        return enc_tk

    def deconde_impl (self, info):
        token = base64.standard_b64decode (info)
        if len (token) < self.align_to * 2 + self.md5_len:
            raise Exception ("bad format: too short")

        xor_key = token[0:self.align_to]
        ciphertext = token[self.align_to:(len(token) - self.md5_len)]
        md5_str = token[(len(token) - self.md5_len):len(token)]

        key = xor_str (self.source, xor_key, self.align_to)

        decryptor = AES.new(key, AES.MODE_CBC, key)
        plain = decryptor.decrypt (ciphertext)

        m = hashlib.md5 ()
        m.update (plain)
        if m.digest () != md5_str:
            raise Exception ("bad digest")

        return plain.rstrip (',')

if __name__ == '__main__':
    t = token_codec ()
    tk = t.encode ('I am Lin Jing, I come from ZJ')
    print tk
    print t.decode (tk)
    
