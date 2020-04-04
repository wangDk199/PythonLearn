"""
判断传入的文件名是否为图片类型文件
"""

def picture(file) :
    if file.endswith('pang') or file.endswith('jpg') or \
        file.endswith('webbp') or file.endswith('bmp') or file.endswith('jpeg'):
       print(this_file, '是图片文件')
    else:
        print(this_file, '不是图片文件')

this_file = input('请输入文件类型：')
picture(this_file)

"""
设定一个函数，产生指定长度的验证码，验证码有大小写字母和数字组成
"""
import random

def generate_code(code_len = 4):
    """
    生成指定长度验证码

    ：param code_len:验证码的长度（默认为4）

    ：return ：有大小写英文字母和数字组成的随机验证码

    """

    all_chars = '123456789abcdefghijkmlnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

code = generate_code(4)
print(code)
    