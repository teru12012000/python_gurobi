#距離も変数化
import math
import gurobipy as gp
model=gp.Model('jog_or_pacerun')
n=10

x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
A7=list(range(11))
for i in range(n):
 x1.append(model.addVar(vtype="B"))
 x2.append(model.addVar(vtype="B"))
 x3.append(model.addVar())
 x4.append(model.addVar(vtype="B"))
 x5.append(model.addVar(vtype="B"))
Z=model.addVar()
model.update()


fig=0
fit=0
for i in range(n):
  model.addConstr(x1[i]+x2[i]+x4[i]+x5[i]<=1)
  model.addConstr(x3[i]<=20)
  model.addConstr(x3[i]>=6)
  
for i in range((n//2)+1):
  fig*=math.exp(-1/15)
  fig+=(x3[i]*(1.1*x1[i]+1.25*x2[i])+35*x4[i]+40*x5[i])
  fit*=math.exp(-1/45)
  fit+=(x3[i]*(1.1*x1[i]+1.25*x2[i])+35*x4[i]+40*x5[i])
  model.addConstr(fit-2*fig>=(-1*(i+1)*20))
for i in range((n//2)+1,n):
  fig*=math.exp(-1/15)
  fig+=(x3[i]*(1.1*x1[i]+1.25*x2[i])+35*x4[i]+40*x5[i])
  fit*=math.exp(-1/45)
  fit+=(x3[i]*(1.1*x1[i]+1.25*x2[i])+35*x4[i]+40*x5[i])
  model.addConstr(fit-2*fig>=(-1*(i+1)*10))
model.addConstr(gp.quicksum(x1[i] for i in range(n))+gp.quicksum(x2[i] for i in range(n))>=5)
model.addConstr(gp.quicksum(x4[i] for i in range(n))+gp.quicksum(x5[i] for i in range(n))>=1)  
model.setObjective(gp.quicksum((x3[i-1]*(1.1*x1[i-1]+1.25*x2[i-1])+35*x4[i-1]+40*x5[i-1])*math.exp(-(n-i)/45) for i in range(1,n+1)),gp.GRB.MAXIMIZE)
model.optimize()
print(model.ObjVal)
fig=0
fit=0
for i in range(n):
  print(x1[i].X,x2[i].X,x3[i].X,x4[i].X,x5[i].X)
  fig*=math.exp(-1/15)
  fig+=(x3[i].X*(1.1*x1[i].X+1.25*x2[i].X)+35*x4[i].X+40*x5[i].X)
  fit*=math.exp(-1/45)
  fit+=(x3[i].X*(1.1*x1[i].X+1.25*x2[i].X)+35*x4[i].X+40*x5[i].X)
print(fit-2*fig)
print(fig)
  
  

    


