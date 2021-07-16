import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

import torchtest as tt

inputs = Variable(torch.randn(20, 20))
targets = Variable(torch.randint(0, 2, (20, ))).long()
batch = [inputs, targets]
model = nn.Linear(20, 2)
device = "cuda" if torch.cuda.is_available() else "cpu"

# what are the variables?
print('Our list of parameters', [np[0] for np in model.named_parameters()])

# do they change after a training step?
# let's run a train step and see
tt.assert_vars_change(
    model=model,
    loss_fn=F.cross_entropy,
    optim=torch.optim.Adam(model.parameters()),
    batch=batch,
    device=device
)

# let's try to break this, so the test fails
params_to_train = [np[1] for np in model.named_parameters() if np[0] is not 'bias']

tt.assert_vars_change(
    model=model, 
    loss_fn=F.cross_entropy, 
    optim=torch.optim.Adam(params_to_train),
    batch=batch,
    device=device
)

# test to see if bias remains the same after training
tt.assert_vars_change(
    model=model,
    loss_fn=F.cross_entropy,
    optim=torch.optim.Adam(params_to_train),
    batch=batch,
    params=[('bias', model.bias)],
    device=device
)