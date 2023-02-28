# 定义变量
x_1 = model.addVar(vtype=GRB.BINARY)
x_2 = model.addVar(vtype=GRB.BINARY)
x_3 = model.addVar(vtype=GRB.BINARY)
y = model.addVar(vtype=GRB.BINARY)
# 定义为连续变量
# x_1=model.addVar(lb=-GRB.INFINITY,ub=GRB.INFINITY,vtype=GRB.CONTINOUS)
# x_2=model.addVar(lb=-GRB.INFINITY,ub=GRB.INFINITY,vtype=GRB.CONTINOUS)
# x_3=model.addVar(lb=-GRB.INFINITY,ub=GRB.INFINITY,vtype=GRB.CONTINOUS)
# y=model.addVar(lb=0,ub=GRB.INFINITY,vtype=GRB.CONTINOUS)
# y=and(x_1,x_2,x_3);y=or(x_1,x_2,x_3)
model.addGenConstrAnd(y, x_1, x_2, x_3, "andconstr")  # model.addGenConstrOr(y,x_1,x_2,x_3,"orconstr")
# 重载形式
model.addConstr(y == and_([x_1, x_2, x_3]), "andconstr")  # model.addConstr(y==or_([x_1,x_2,x_3]),"orconstr")
