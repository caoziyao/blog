# coding: utf-8

import hashlib

def hexdigest(pwd):

    salt = 'abcdefght'

    def hashhex(ascii_str):
        m = hashlib.sha1()
        m.update(ascii_str.encode('ascii'))
        r = m.hexdigest()
        return r

    r = hashhex(pwd)
    r = hashhex(r + salt)
    return r

def main():
    print(hexdigest('1221'))

if __name__ == '__main__':
    main()