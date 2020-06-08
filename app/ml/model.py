import pandas as pd
import numpy as np
import gzip
import struct
import torch 
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class CNN1(nn.Module):    
    def __init__(self):
        # 항상 torch.nn.Module을 상속받고 시작
        super(CNN1, self).__init__()

        eps_value = 1e-03
        # 간단하게 생각하면 03 <- 0 갯수임 
        # 1e-03 = 0.001
        # 1e+01 = 10
            
        conv1 = nn.Conv2d(1, 128, kernel_size = (4,21), stride = 1) # 6@24*24
        nn.init.xavier_normal_(conv1.weight)
        #xavier_normal_ 이게 균등분포
        conv1.bias.data.fill_(0)
            
        batch_conv1 = nn.BatchNorm2d(128, momentum = 0.99, eps = eps_value)
        pool1 = nn.MaxPool2d(kernel_size=(997,1)) # 6@12*a12
        
        self.CNN1_module = nn.Sequential(
            conv1,
            batch_conv1,
            nn.ReLU(),
            pool1
        )
            
        conv2 = nn.Conv2d(1, 128, kernel_size = (8,21), stride = 1) # 6@24*24
        nn.init.xavier_normal_(conv2.weight)
        conv2.bias.data.fill_(0)
            
        batch_conv2 = nn.BatchNorm2d(128, momentum = 0.99, eps = eps_value)
        pool2 = nn.MaxPool2d(kernel_size=(993,1)) # 6@12*a12
            
        self.CNN2_module = nn.Sequential(
            conv2,
            batch_conv2,
            nn.ReLU(),
            pool2
        )
            
        conv3 = nn.Conv2d(1, 128, kernel_size = (16,21), stride = 1) # 6@24*24
        nn.init.xavier_normal_(conv3.weight)
        conv3.bias.data.fill_(0)
            
        batch_conv3 = nn.BatchNorm2d(128, momentum = 0.99, eps = eps_value)
        pool3 = nn.MaxPool2d(kernel_size=(985,1)) # 6@12*a12
            
        self.CNN3_module = nn.Sequential(
            conv3,
            batch_conv3,
            nn.ReLU(),
            pool3
        )
            
        fc1 = nn.Linear(384, 512)
        batch_fc1 = nn.BatchNorm1d(512, momentum = 0.99, eps = eps_value)
        nn.init.xavier_normal_(fc1.weight)
        fc1.bias.data.fill_(0)
            
        fc2 = nn.Linear(512, 512)
        batch_fc2 = nn.BatchNorm1d(512, momentum = 0.99, eps = eps_value)
        nn.init.xavier_normal_(fc2.weight)
        fc2.bias.data.fill_(0)
            
        fc3 = nn.Linear(512, 2)
        nn.init.xavier_normal_(fc3.weight)
        fc3.bias.data.fill_(0)
            
        self.fc_module = nn.Sequential(
            fc1,
            batch_fc1,
            nn.ReLU(),
            fc2,
            batch_fc2,
            nn.ReLU(),
            fc3
        )
            
    def forward(self, x):
        out1 = self.CNN1_module(x) # @16*4*4
        out2 = self.CNN2_module(x) # @16*4*4
        out3 = self.CNN3_module(x) # @16*4*4
        # make linear
            
        out = torch.cat((out1, out2, out3), dim = 1)
        dim = 1
            
        for d in out.size()[1:]: #16, 4, 4
            dim = dim * d
        
        out = out.view(-1, dim)
        out = self.fc_module(out)
        return out
