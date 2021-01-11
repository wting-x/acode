""" 数独是 9 横 9 竖共有 81 个格子，同时又分为 9 个九宫格。
    我们填写数独的顺序是将 9 个九宫格按照从左到右，从上到下
    的顺序排列，再将每个九宫格内部的空白格按照从左到右，从
    上到下的顺序排列，依次按照顺序填写空白格。"""

""" 解此种数独用达不到默认递归的深度
import sys  
sys.setrecursionlimit(100000) # 发现python默认的递归深度是很有限的
                              #（默认是1000），因此当递归深度超过999的
                              # 样子，就会引发这样的一个异常。
"""


def get_next(m:"数独矩阵", x:"空白格行数", y:"空白格列数"):
    """ 功能：获得下一个空白格在数独中的坐标。       
    """
    for next_y in range(y+1, 9):  # 下一个空白格和当前格在一行的情况
        if m[x][next_y] == 0:
            return x, next_y
    for next_x in range(x+1, 9):  # 下一个空白格和当前格不在一行的情况
        for next_y in range(0, 9):
            if m[next_x][next_y] == 0:
                return next_x, next_y
    return -1, -1               # 若不存在下一个空白格，则返回 -1，-1
        
def value(m:"数独矩阵", x:"空白格行数", y:"空白格列数"):
    """ 功能：返回符合"每个横排和竖列以及
              九宫格内无相同数字"这个条件的有效值。
    """ 
    i, j = x//3, y//3
    grid = [m[i*3+r][j*3+c] for r in range(3) for c in range(3)]
    v = set([x for x in range(1,10)]) - set(grid) - set(m[x]) - \
        set(list(zip(*m))[y])    
    return v

def start_pos(m:"数独矩阵"):
    """ 功能：返回第一个空白格的位置坐标"""
    for x in range(9):
        for y in range(9):
            if m[x][y] == 0:
                return x, y
    return -1, -1  # 若数独已完成，则返回 -1, -1

def try_sudoku(m:"数独矩阵", x:"空白格行数", y:"空白格列数"):
    """ 功能：试着填写数独 """    
    for v in value(m, x, y):
        if m[x][y] == 0:  # 判断是否为空格
            m[x][y] = v
            next_x, next_y = get_next(m, x, y)            
            if next_y == -1: # 如果无下一个空白格
                print(m)
                return True
            else:
                end = try_sudoku(m, next_x, next_y) # 递归
                if end:
                    return True
                m[x][y] = 0 # 在递归的过程中，如果数独没有解开，
                            # 则回溯到上一个空白格    

def sudoku(m):        
    x, y = start_pos(m)
    """ 解数独的一个结果
    try_sudoku(m, x, y)
    """
    # 解数独的所有结果
    for v in value(m, x, y):        
        m[x][y] = v
        next_x, next_y = get_next(m, x, y)
        try_sudoku(m, next_x, next_y)
             

                    
if __name__ == "__main__":
    m = [
        [7,0,0,1,0,0,0,8,3],
        [4,0,2,0,7,3,0,0,0],
        [0,0,0,4,5,0,0,2,7],
        [0,0,7,0,0,0,3,1,2],
        [0,4,3,8,0,0,0,0,0],
        [0,0,5,0,9,0,0,0,0],
        [0,2,1,0,8,0,0,0,0],
        [0,3,0,2,0,1,8,0,0],
        [0,0,0,0,0,0,2,6,1]
    ]

    sudoku(m)
    
"""
[
    [6, 9, 5, 1, 2, 3, 7, 4, 8], 
    [7, 4, 1, 8, 6, 9, 2, 5, 3], 
    [2, 3, 8, 4, 5, 7, 1, 6, 9], 
    [8, 1, 6, 7, 4, 5, 3, 9, 2], 
    [5, 2, 4, 3, 9, 8, 6, 7, 1], 
    [3, 7, 9, 6, 1, 2, 4, 8, 5], 
    [4, 8, 3, 9, 7, 1, 5, 2, 6], 
    [1, 6, 2, 5, 8, 4, 9, 3, 7], 
    [9, 5, 7, 2, 3, 6, 8, 1, 4]
]
"""