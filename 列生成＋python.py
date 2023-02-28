# -*- coding: cp936 -*-
import numpy as np
import random
from gurobipy import *

L = 120  # 最大长
M = 240  # 总数
demands = [10, 11, 11, 12, 12, 12, 10, 11, 12, 10]
lengths = [92, 59, 97, 32, 38, 55, 80, 75, 108, 57]
demands = np.array(demands)
lengths = np.array(lengths)
c = {}
x = {}
mol = Model("XP")
for i in range(M):
    c[i] = mol.addVar(obj=1, vtype=GRB.BINARY, name="c[%s]" % i)  # 添加决策变量
for i in range(10):
    for j in range(M):  # 添加变量
        x[j, i] = mol.addVar(lb=0, obj=0, vtype=GRB.INTEGER, name="c[%s][%s]" % (j, i))

for k in range(10):
    coef = [1 for j in range(M)]
    var = [x[j, k] for j in range(M)]
    mol.addConstr(LinExpr(coef, var), ">=", demands[k], name="demands")

for l in range(M):
    coef = [lengths[i] for i in range(10)]
    var = [x[l, i] for i in range(10)]
    mol.addConstr(LinExpr(coef, var), "<=", L * c[l], name="withlimit")

mol.optimize()

mol.printAttr('x')
obj = mol.getObjective()
print(obj)
for v in mol.getVars():
    print('%s %g' % (v.varName, v.x))
