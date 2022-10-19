#距離も変数化
import math
import gurobipy as gp
model=gp.Model('jog_or_off')
n=10

x1=[]
x2=[]
x3=[]


for i in range(n):
 x1.append(model.addVar(vtype="B"))
 x2.append(model.addVar(vtype="B"))
 x3.append(model.addVar())
model.update()
model.setObjective(gp.quicksum((1.1*x1[i-1]*x3[i-1]+1.65*x2[i-1]*x3[i-1])*math.exp(-(n-i)/45)for i in range(1,n+1)),gp.GRB.MAXIMIZE)
model.addConstr(x1[0]+x2[0]<=1)
fig=0
for i in range(n):
  
  fig*=math.exp(-1/15)
  fig+=(1.1*x1[i]*x3[i]+1.65*x2[i]*x3[i])
  model.addConstr(fig<=90)
  model.addConstr(x1[i]+x2[i]<=1)
  model.addConstr(x3[i]<=20)
  model.addConstr(x3[i]>=6)
model.optimize()
print(model.ObjVal)
fig=0
for i in range(n):
  print(x1[i].X,x2[i].X,x3[i].X)
  fig*=math.exp(-1/15)
  fig+=(1.1*x1[i].X*x3[i].X+1.65*x2[i].X*x3[i].X)
print(fig)
print(model.ObjVal-fig*2)
  
  

    


