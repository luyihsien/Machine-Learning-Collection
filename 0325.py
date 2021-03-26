#test loss
import torch,numpy as np
import torch.nn as nn#import torch.nn
def invert_list_to_tensor(list):
    return torch.tensor(list,dtype=float)

wx,label=invert_list_to_tensor([[1,1,1]]),invert_list_to_tensor([[0,0,0]])
criterion=nn.MSELoss(reduction='mean')
print(criterion(wx,label))
# w=nn.Linear(3,1)
# print(w(torch.randn(2,3)).squeeze(1))
a=np.array([[1,1,1,1],[2,2,2,2]])
b=a[:,-1]
print(b)
#np like pd and torch
# print(b)