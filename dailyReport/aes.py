import random
from itertools import repeat
from Crypto.Cipher import AES
import base64

def rds(num):
    keymap = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'
    result = ''
    for num in repeat(None, num):
        result += keymap[random.randint(0, 47)]
    return result

def pad(s):
    BLOCK_SIZE = 16
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

def encrypt(data,key,iv):
    key = key.encode('utf-8')
    iv = iv.encode('utf-8')
    mode = AES.MODE_CBC
    do = AES.new(key, mode, iv)
    result = do.encrypt(pad(data).encode('utf-8'))
    return base64.b64encode(result).decode('utf-8')

def aesEnc(pwd,key):
    return encrypt(rds(64)+pwd,key,rds(16))