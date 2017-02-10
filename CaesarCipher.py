# -*- coding: utf-8 -*-
"""

"""

Insertion_Sort_instruction = """
    We start with the first element in the array. One element by itself is already sorted. Then we consider the next
element in the array. If it is smaller than the first, we swap them. Next we consider the third element in the array.
We swap it leftward until it is in its proper order with the first two elements. We then consider the fourth element,
and swap it leftward until it is in the proper order with the first three. We continue in this manner with the fifth
element, the sixth, and so on, until the whole array is sorted.
"""

def insertion_sort(s):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(s)):
        cur = s[k]                          # 建立游标
        j = k                               # 拿到当前游标值
        while j > 0 and s[j-1] > cur:       # 当前一位值大于游标的值
            s[j] = s[j-1]                   # 交换位置
            j -= 1                          # 游标向前移
        s[j] = cur                          # 获取游标值



Insertion_Sort_summary = """
    The nested loops of insertion-sort lead to an O(n**2) running time in the worst case. The most work is done if the
array is initially in reverse order. On the other hand, if the initial array is nearly sorted or perfectly sorted,
insertion-sort runs in O(n) time because there are few or no iterations of the inner loop.
"""

#####################################

class CaesarCipher:
    """
    Class for doing encryption and decryption using a Caesar cipher.
    类似上面的插入排序，规则为自定,用ord()和chr()判断取得字母的排序
    """

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        print('init')
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            print(encoder)
            decoder[k] = chr((k - shift) % 26 + ord('A'))
            print(decoder)
        self.forward = ''.join(encoder)
        print('forward  is', self.forward)
        self.backward = ''.join(decoder)
        print('backward is', self.backward)

    def encrypt(self, message):
        """Return string representing encripted message."""
        return self._transform(message, self.forward)           # 传入消息和加密表forward

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self._transform(secret, self.backward)           # 传入密文和解密表forward

    def _transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)                                    # 将original的每个字母与code比较，调换成对应字母
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


#####################################

if __name__ == '__main__':
    print('{0:-<10} {1} {2:->10}'.format('\n-', 'Insertion_Sort', '-'))
    s = ['5', '4', '1', '6', '9']
    insertion_sort(s)
    print("insertion_sort's result is ", s)

    print('{0:-<10} {1} {2:->10}'.format('\n-', 'CaesarCipher', '-'))
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE S."
    print("message is ", message)
    coded = cipher.encrypt(message)
    print('after encrypt\nSecret:  ', coded)
    answer = cipher.decrypt(coded)
    print('after decrypt\nMessage: ', answer)
