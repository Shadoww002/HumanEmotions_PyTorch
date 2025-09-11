import torch.nn as nn
from torch.utils.data import models
model = models.resnet18(pretrained=True)

# Freeze early layers
for param in model.parameters():
    param.requires_grad = False

# Replace last layer
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 7)  # 7 emotion classes
