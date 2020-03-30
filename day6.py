from termcolor import *


"""
打印杨辉三角
"""
def main() :
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()
if __name__ == '__main__':
    main()

# """
# 在屏幕上显示跑马灯文字
# """
# import os
# import time

# def main():
#     content = '人生短暂，有价值的人生才有意义。'
#     color = ['red', 'green', 'yellow', 'grey', 'blue', 'cyan']
#     i = 0
#     while True :
#         os.system('cls')
#         index = i % len(color) 
#         print(colored(content, color[index]))
#         time.sleep(0.2)
#         content = content[1:] + content[0]
#         i = i + 1

# if __name__ == '__main__':
#     main()