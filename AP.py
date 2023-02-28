import random

import numpy as np
from gurobipy import *

# 生成匹配的价值矩阵
employee_num = job_num = 5
cost_matrix = np.zeros((employee_num, job_num))
for i in range(employee_num):
    for j in range(job_num):
        random.seed(i * employee_num + j)
        cost_matrix[i][j] = round(10 * random.random() + 5, 0)
# 构建模型对象
model = Model('Assignment_Problem')

# 循环引入决策变量
x = [[[] for i in range(employee_num)] for j in range(job_num)]
for i in range(employee_num):
    for j in range(job_num):
        x[i][j] = model.addVar(lb=0,ub=1,vtype=GRB.CONTINUOUS,name="x_"+str(i)+"_"+str(j))
# 目标函数
obj = LinExpr(0)
for i in range(employee_num):
    for j in range(job_num):
        obj.addTerms(cost_matrix[i][j], x[i][j])

model.setObjective(obj, GRB.MINIMIZE)

# 约束条件1
for j in range(employee_num):
    expr = LinExpr(0)
    for i in range(job_num):
        expr.addTerms(1, x[i][j])
    model.addConstr(expr == 1, name="D_" + str(j))

# 约束条件2
for i in range(employee_num):
    expr = LinExpr(0)
    for j in range(job_num):
        expr.addTerms(1, x[i][j])
    model.addConstr(expr == 1, name="R_" + str(i))

# 求解构造模型

model.write('model.lp')
model.optimize()

# 打印最优解

for var in model.getVars():
    if var.x > 0:
        print(var.varName, '\t', var.x)
print('objective:', model.ObjVal)
