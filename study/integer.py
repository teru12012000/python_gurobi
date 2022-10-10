import gurobipy as gp
model=gp.Model("puzzle")
x=model.addVar(vtype="I")
y=model.addVar(vtype="I")
z=model.addVar(vtype="I")
model.update()

c1=model.addConstr(x+y+z==32)
c2=model.addConstr(2*x+4*y+8*z==80)

model.setObjective(y+z,gp.GRB.MINIMIZE)
model.optimize()

print(f'Opt. Val={model.ObjVal}')
print(f"(x,y,z)={x.X,y.X,z.X}")
