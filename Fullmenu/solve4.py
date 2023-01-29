# FULLMENU!!!
import math
import gurobipy as gp
import time
model = gp.Model('FULLMENU')
n = 13

x1 = []
x2 = []
x3 = []
x4 = []
x7 = []
A7 = list(range(11))
for i in range(n):
    x1.append(model.addVar(vtype=gp.GRB.BINARY))
    x2.append(model.addVar(vtype=gp.GRB.BINARY))
    x3.append(model.addVar(vtype=gp.GRB.INTEGER))
    x4.append(model.addVar(vtype=gp.GRB.BINARY))
    x7.append(model.addVar(vtype=gp.GRB.BINARY))
Z = model.addVar()
model.update()

fig = 0
fit = 0
for i in range(n):
    model.addConstr(x1[i]+x2[i]+x4[i]+x7[i] <= 1)
    model.addConstr(x3[i] <= 12)
    model.addConstr(x3[i] >= 8)
model.addConstr(x4[2] == 1)
model.addConstr(x4[6] == 1)
model.addConstr(x7[9] == 1)
for i in range(n):
    fig *= math.exp(-1/15)
    fig += 2*(x3[i]*(1.1*x1[i]+1.65*x2[i])+35*x4[i]+36*x7[i])
    fit *= math.exp(-1/45)
    fit += (x3[i]*(1.1*x1[i]+1.65*x2[i])+35*x4[i]+36*x7[i])
    if i == 6 or i == 8 or i == 12:
        model.addConstr(fit-fig >= -100)
model.addConstr(fit-fig >= -100)
model.setObjective(fit, gp.GRB.MAXIMIZE)


model.addConstr(gp.quicksum(x1[i] for i in range(
    n))+gp.quicksum(x2[i] for i in range(n)) >= 5)
model.addConstr(gp.quicksum(x1[i] for i in range(n)) >= 1)
model.addConstr(gp.quicksum(x4[i] for i in range(n)) == 2)
model.addConstr(gp.quicksum(x7[i] for i in range(n)) == 1)
start = time.perf_counter()
model.optimize()
print(time.perf_counter()-start)
print(model.ObjVal)
fig = 0
fit = 0
for i in range(n):
    print(x1[i].X, x2[i].X, x3[i].X, x4[i].X, x7[i].X)
    fig *= math.exp(-1/15)
    fig += 2*(x3[i].X*(1.1*x1[i].X+1.65*x2[i].X)+35*x4[i].X+36*x7[i].X)
    fit *= math.exp(-1/45)
    fit += (x3[i].X*(1.1*x1[i].X+1.65*x2[i].X)+35*x4[i].X+36*x7[i].X)
print(fit-fig)
