import math
import gurobipy as gp
model=gp.Model('jog_or_off')
n=6

x1=[]
x2=[]

for i in range(n):
 x1.append(model.addVar(vtype="B"))
 x2.append(model.addVar(vtype="B"))
model.update()

model.setObjective(258*math.exp(-(n)/45)+gp.quicksum((13.2*x1[i-1]+19.8*x2[i-1])*math.exp(-(n-i)/45)for i in range(1,n+1)),gp.GRB.MAXIMIZE)
fig=187.5
fig_list=[]
fit=258
fit_list=[]
model.addConstr(x1[0]+x2[0]<=1)

for i in range(n):
  fig*=math.exp(-1/15)
  fig+=(13.2*x1[i]+19.8*x2[i])
  model.addConstr(fig<=200)
  model.addConstr(x1[i]+x2[i]<=1)
model.optimize()
print(model.ObjVal)
fig=187.5
for i in range(n):
  print(x1[i].X,x2[i].X)
  fig*=math.exp(-1/15)
  fig+=(13.2*x1[i].X+19.8*x2[i].X)
print(fig)
print(model.ObjVal-2*fig)
  

    


