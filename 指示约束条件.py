#y=1-->x_1+x_2+x_3=1
model.addGenConstrIndicator(
    y,#binvar:0-1指示变量对象
    True,#binval：0-1指示变量取值TRUEorFALSE
    x_1+x_2+x_3=1,#lhs(float,Var,LinExpr,or TemConstr)与0-1指示变量相关的线性约束的左端项表达式
    GRB.EQUAL,#sense(char)：线性约束的符号
    1.0,#rhs(float)线性约束的右端项
    #name(string,optional),约束的名称
)