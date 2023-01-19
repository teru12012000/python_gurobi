#FULLMENU!!!
import math
import gurobipy as gp
import time
model=gp.Model('FULLMENU')
n=13
#変数用意
x1=[]
x2=[]
x3=[]
x4=[]
D=[]
#変数のタイプをそれぞれ設定
for i in range(n):
 x1.append(model.addVar(vtype=gp.GRB.BINARY))
 x2.append(model.addVar(vtype=gp.GRB.BINARY))
 D.append(model.addVar(vtype=gp.GRB.INTEGER))
 x3.append(model.addVar(vtype=gp.GRB.BINARY))
 x4.append(model.addVar(vtype=gp.GRB.BINARY))
Z=model.addVar()
model.update()
#制約設定
fig=0
fit=0
for i in range(n):
  model.addConstr(x1[i]+x2[i]+x3[i]+x4[i]<=1)
  model.addConstr(D[i]<=12) 
  model.addConstr(D[i]>=8)
model.addConstr(x3[2]==1)
model.addConstr(x3[6]==1)
model.addConstr(x4[9]==1)
for i in range(n):
  fig*=math.exp(-1/15)
  fig+=2*(D[i]*(1.1*x1[i]+1.65*x2[i])+35*x3[i]+40*x4[i])
  fit*=math.exp(-1/45)
  fit+=(D[i]*(1.1*x1[i]+1.65*x2[i])+35*x3[i]+40*x4[i])
  if i==6 or i==8 or i==12:
    model.addConstr(fit-fig>=-100)    
model.addConstr(fit-fig>=-100)
model.setObjective(fit,gp.GRB.MAXIMIZE)
model.addConstr(gp.quicksum(x1[i] for i in range(n))+gp.quicksum(x2[i] for i in range(n))>=5)
model.addConstr(gp.quicksum(x1[i] for i in range(n))>=1)
model.addConstr(gp.quicksum(x3[i] for i in range(n))==2)
model.addConstr(gp.quicksum(x4[i] for i in range(n))==1)

#時間計測およびソルバー実行
start=time.perf_counter()  
model.optimize()
print(time.perf_counter()-start)

#結果出力
print(model.ObjVal)
fig=0
fit=0
for i in range(n):
  print(x1[i].X,x2[i].X,D[i].X,x3[i].X,x4[i].X)
  fig*=math.exp(-1/15)
  fig+=2*(D[i].X*(1.1*x1[i].X+1.65*x2[i].X)+35*x3[i].X+40*x4[i].X)
  fit*=math.exp(-1/45)
  fit+=(D[i].X*(1.1*x1[i].X+1.65*x2[i].X)+35*x3[i].X+36*x4[i].X)
print(fit-fig)
  
  

    


