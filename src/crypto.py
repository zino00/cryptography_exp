def get_str_bits(s):
    list_b = []
    for c in s:
        list_b.append((ord(c) - ord('0')))
    return list_b


# 流密码
class RC4(object):
    def __init__(self, key=None):
        if not key:
            key = b'default_key'
        self.key = key.decode('utf-8')
        self._init_slist()

    # 初始化s列表 单下划线开头表示权限为protected
    def _init_slist(self):
        # 初始化s列表
        self.slist = [i for i in range(256)]
        # 初始化t列表
        length = len(self.key)
        t = [ord(self.key[i % length]) for i in range(256)]
        # 用t产生s的初始置换
        j = 0
        for i in range(256):
            j = (j + self.slist[i] + t[i]) % 256
            self.slist[i], self.slist[j] = self.slist[j], self.slist[i]
        # 加解密

    def do_crypt(self, ss):
        i = 0
        j = 0
        result = ''
        ss = ss.decode('utf-8')
        for s in ss:
            i = (i + 1) % 256
            j = (j + self.slist[j]) % 256
            self.slist[i], self.slist[j] = self.slist[j], self.slist[i]
            t = (self.slist[i] + self.slist[j]) % 256
            result += chr(ord(s) ^ self.slist[t])
            self.slist[i], self.slist[j] = self.slist[j], self.slist[i]
        return result.encode('utf-8')


class LFSR:
    def __init__(self, c=None, a=None, lenc=0):
        if a is None:
            a = []
        if c is None:
            c = []
        self.a = a
        self.c = c
        self.lenc = lenc
        lena = len(a)
        if lena < lenc:
            cnta = (lenc - lena) // lena + 1
            for i in range(cnta):
                self.a.extend(a)

    def LeftShift(self):
        lastb = 0
        lenc = self.lenc
        for i in range(lenc):
            lastb = lastb ^ (self.a[i] & self.c[i])
        b = self.a[1:]
        outp = self.a[0]
        b.append(outp)
        self.a = b
        return outp


class cypto_LFSR:
    def __init__(self, key, lfsr1 = None, lfsr2 = None):
        if lfsr1 is None:
            lfsr1 = [0, 1, 0, 1]
        if lfsr2 is None:
            lfsr2 = [0, 0, 1, 1]
        Keymap = get_str_bits(key)
        lenk = len(Keymap)
        self.lfsr1 = LFSR(Keymap, lfsr1, lenk)
        self.lfsr2 = LFSR(Keymap, lfsr2, lenk)
        self.Key = Keymap
        self.lc = 0

    def GetBit(self):
        ak = self.lfsr1.LeftShift()
        bk = self.lfsr2.LeftShift()
        ck = ak ^ ((ak ^ bk) & self.lc)  # JK触发器
        self.lc = ck
        return ck

    def do_crypt(self, LFSR_msg):
        text = []
        for i in LFSR_msg:
            j, cnt = i, 8
            tmp = []
            while cnt > 0:
                tmp.append(self.GetBit() ^ (j & 1))
                j = j >> 1
                cnt = cnt - 1
            res = 0
            for iti in range(7, -1, - 1):
                res = res << 1
                res = res + tmp[iti]
            text.append(res)
        return bytes(text)


# 仿射加密
def EX_GCD(a, b, arr):  # 扩展欧几里得
    if b == 0:
        arr[0] = 1
        arr[1] = 0
        return a
    g = EX_GCD(b, a % b, arr)
    t = arr[0]
    arr[0] = arr[1]
    arr[1] = t - int(a / b) * arr[1]
    return g


def inv(a, n):  # ax=1(mod n) 求a模n的乘法逆x
    arr = [0, 1, ]
    gcd = EX_GCD(a, n, arr)
    if gcd == 1:
        return (arr[0] % n + n) % n
    else:
        return -1


class Radiate:
    # 加密
    def encryption(self, plaintext, KeyConf):
        strr = ''
        KeyConf = KeyConf.decode('utf-8')
        plaintext = plaintext.decode('utf-8')
        a = int(KeyConf.split('\n')[0])
        b = int(KeyConf.split('\n')[1])
        for i in plaintext:
            temp = ord(i) - 97
            t = (temp * a + b) % 26
            te = chr(t + 97)
            strr += te
        return strr

    # 解密
    def decryption(self, ciphertext, KeyConf):
        strr = ''
        KeyConf = KeyConf.decode('utf-8')
        ciphertext = ciphertext.decode('utf-8')
        a = int(KeyConf.split('\n')[0])
        b = int(KeyConf.split('\n')[1])
        aa = inv(a, 26)
        for i in ciphertext:
            temp = ord(i) - 97
            t = ((temp - b + 26) % 26) * aa % 26
            te = chr(t + 97)
            strr += te
        return strr


# 分组加密
from Crypto.Cipher import AES
from Crypto.Cipher import DES


# 分组密码
class des_crypto:

    def __init__(self, Key, mode):
        self.key = Key
        self.mode = mode
        # self.mode = DES.MODE_CBC #改为可修改

    def encrypt(self, decryptText):
        if self.mode == DES.MODE_ECB:
            cipher1 = DES.new(self.key, self.mode)
        elif self.mode == DES.MODE_CTR:
            cipher1 = DES.new(self.key, self.mode, nonce= b'0000000')
        else:
            cipher1 = DES.new(self.key, self.mode, self.key)
        # 分组补全
        length = 8
        TextNum = len(decryptText)
        add = (length - (TextNum % length)) % length
        decryptText = decryptText + (b'\0' * add)
        encryptText = cipher1.encrypt(decryptText)
        return encryptText

    def decrypt(self, encryptText):
        if self.mode == DES.MODE_ECB:
            cipher2 = DES.new(self.key, self.mode)
        elif self.mode == DES.MODE_CTR:
            cipher2 = DES.new(self.key, self.mode, nonce=b'0000000')
        else:
            cipher2 = DES.new(self.key, self.mode, self.key)
        decryptText = cipher2.decrypt(encryptText)
        decryptText = decryptText.rstrip(b'\0')
        return decryptText


class aes_crypto:

    def __init__(self, Key, mode):
        self.key = Key
        self.mode = mode

    def encrypt(self, decryptText):
        iv = str(self.key)[:16].encode()
        if self.mode == AES.MODE_ECB:
            cipher1 = AES.new(self.key, self.mode)
        elif self.mode == AES.MODE_CTR:
            cipher1 = AES.new(self.key, self.mode, nonce=b'0000000')
        else:
            cipher1 = AES.new(self.key, self.mode, iv)
        # 分组补全
        length = 16
        TextNum = len(decryptText)
        add = (length - (TextNum % length)) % length
        decryptText = decryptText + (b'\0' * add)
        encryptText = cipher1.encrypt(decryptText)
        return encryptText

    def decrypt(self, encryptText):
        iv = str(self.key)[:16].encode()
        if self.mode == AES.MODE_ECB:
            cipher2 = AES.new(self.key, self.mode)
        elif self.mode == AES.MODE_CTR:
            cipher2 = AES.new(self.key, self.mode, nonce=b'0000000')
        else:
            cipher2 = AES.new(self.key, self.mode, iv)
        decryptText = cipher2.decrypt(encryptText)
        decryptText = decryptText.rstrip(b'\0')
        return decryptText


# RSA
def Ex_Euclid(a, b):
    if 0 == b:
        x = 1
        y = 0
        q = a
        return x, y, q
    xyq = Ex_Euclid(b, a % b)
    x = xyq[0]
    y = xyq[1]
    q = xyq[2]
    temp = x
    x = y
    y = temp - a // b * y
    return x, y, q


def ksm(a, b, n):
    res = 1
    t = a

    while (b):
        if b & 1:
            res = (res * t) % n
        t = (t * t) % n
        b >>= 1

    return res


def Get_Inverse(a, b):
    return Ex_Euclid(a, b)[0]


class RSA:
    def __init__(self):
        self.p = 587
        self.q = 113
        self.n = self.p * self.q
        self.e = 5
        self.d = (Get_Inverse(self.e, (self.p - 1) * (self.q - 1)) + (self.p - 1) * (self.q - 1)) % (
                (self.p - 1) * (self.q - 1))

    def encrypt(self, M):
        return ksm(M, self.e, self.n)

    def decrypt(self, C):
        return ksm(C, self.d, self.n)

    def Encrypt(self, plaintxt):
        s = plaintxt
        s1 = []
        for x in s:
            temp = int(format(ord(x), 'b'), 2)
            if temp >= 2 ** 8:
                s1.append(0)
                s1.append(int(temp / 256))
                s1.append(0)
                s1.append(temp % 256)
            else:
                s1.append(temp)
        if len(s1) % 2 == 1:
            s1.append(1)
        s2 = []
        i = 0
        while True:
            temp = s1[i] * (2 ** 8) + s1[i + 1]
            i = i + 2
            s2.append(self.encrypt(temp))
            if i >= len(s1):
                break
        return s2

    def Decrypt(self, cipher):
        s2 = cipher
        s3 = []
        i = 0
        while True:
            temp = self.decrypt(s2[i])
            i = i + 1
            s3.append(int(temp / 256))
            if temp % 256 != 1:
                s3.append(temp % 256)
            if i >= len(s2):
                break
        s4 = ''
        i = 0
        while True:
            if s3[i] == 0:
                temp = s3[i + 1] * 256 + s3[i + 3]
                s4 += chr(temp)
                i += 3
            else:
                s4 += chr(s3[i])
            i = i + 1
            if i >= len(s3):
                break
        return s4
