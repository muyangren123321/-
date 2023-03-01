# 假设我们有一个背包问题，即给定一组物品，每个物品有一个重量和一个价值，我们要在背包的容量限制下，选择一些物品放入背包，使得总价值最大。
#
# 我们可以用以下的Python代码来实现这个问题：

# 导入gurobipy模块
import gurobipy as gp

# 创建一个Model对象
model = gp.Model("knapsack")

# 定义物品的数量、重量和价值
n = 5  # 物品的数量
w = [2, 3, 4, 5, 6]  # 物品的重量
v = [6, 7, 8, 9, 10]  # 物品的价值

# 定义背包的容量
c = 10  # 背包的容量

# 创建一个变量列表，表示每个物品是否被选中（0或1）
x = model.addVars(n, vtype=gp.GRB.BINARY, name="x")

# 设置目标函数为总价值的最大化
model.setObjective(gp.quicksum(x[i] * v[i] for i in range(n)), gp.GRB.MAXIMIZE)

# 添加约束条件为总重量不超过背包容量
model.addConstr(gp.quicksum(x[i] * w[i] for i in range(n)) <= c, name="weight")

# 求解模型
model.optimize()

# 打印最优解和最优值
print("Optimal solution:")

for i in range(n):
    if x[i].x > 0.5:
        print(f"Item {i}: weight {w[i]}, value {v[i]}")
print(f"Total weight: {model.objVal}")
print(f"Total value: {model.objVal}")
