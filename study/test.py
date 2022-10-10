import gurobipy as gp

model=gp.Model("lo1")
x1=model.addVar(name="x1")
x2=model.addVar(name="x2")
x3=model.addVar(ub=30,name="x3")
model.update()

model.setObjective(15*x1+18*x2+30*x3,gp.GRB.MAXIMIZE)

C_1=model.addConstr(2*x1+x2+x3<=60)
C_2=model.addConstr(x1+2*x2+x3<=60)




model.optimize()
print(f'Opt. value={model.ObjVal}')
for v in model.getVars():
  print(v.VarName,v.X)
