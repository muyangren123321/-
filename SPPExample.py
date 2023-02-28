from gurobipy import *
import pandas as pd
import numpy as np

Nodes = ['1', '2', '3', '4', '5', '6', '7']
Arcs = {('1', '2'): 15,
        ('1', '4'): 25,
        ('1', '3'): 45,
        ('2', '5'): 30,
        ('2', '4'): 2,
        ('4', '7'): 50,
        ('4', '3'): 2,
        ('3', '6'): 25,
        ('5', '7'): 2,
        ('6', '7'): 1
        }
model = Model('dual problem')
# 添加决策变量
X = {}
for key in Arcs.keys():
    index = 'x_' + key[0] + ',' + key[1]
    X[key] = model.addVar(vtype=GRB.BINARY, name=index)
# 添加目标函数
obj = LinExpr(0)
for key in Arcs.keys():
    obj.addTerm(Arcs[key], X[key])
    model.setObjective(obj, GRB.MINIMIZE)
# 约束条件1和2
lhs_1 = LinExpr(0)
lhs_2 = LinExpr(0)
for key in Arcs.keys():
    if key[0] == '1':
        lhs_1.addTerm(1, X[key])
    elif key[1] == '7':
        lhs_2.addTerm(1, X[key])
model.addConstrs(lhs_1 == 1, name='start flow')
model.addConstrs(lhs_2 == 1, name='end flow')
# 约束条件3
for node in Nodes:
    lhs = LinExpr(0)
    if node != 0 and node != 7:
        for key in Arcs.keys():
            if key[1] == node:
                lhs.addTerm(1, X[key])
            elif key[0] == node:
                lhs.addTerm(-1, X[key])
    model.addConstrs(lhs == 0, name='flow conservation')
# 求解构造模型
model.write('model.lp')
model.optimize()
# 打印最优解
for var in model.getVars():
    if var.x > 0:
        print(var.varName, '\t', var.x)
print('objective:', model.ObjVal)
