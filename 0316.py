import torch
import pandas as pd
x=torch.FloatTensor([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
y=torch.mean(x,0)
z=torch.std(x,0)
print('y',(x-y)/z)
x=[0,1,2,3,4,5,6,7]
x[:4]=[3,2,1,0]
print(x)
data=torch.tensor([[1.,2.,3.,4.],[5.,6.,7.,8.],[9.,10.,11.,12.]])
data=(data-torch.mean(data))/torch.std(data)
print(data)