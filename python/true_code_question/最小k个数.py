#@Time:2020/9/21 20:40
#@Author:liuAmon
#@e-mail:utopfish@163.com
#@File:最小k个数.py
__author__ = "liuAmon"
import numpy as np
x=[[1,2,3,4],[1,2,3,5],[2,3,4,5]]
y=[[3,4,5,6],[1,2,4,8],[3,3,3,3]]

corr = np.corrcoef(x, y)
print(corr)