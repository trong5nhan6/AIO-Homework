import torch
import torch.nn as nn

softmax_function = nn.Softmax()
data = torch.Tensor([1, 2, 3])
output = softmax_function(data)
print(output)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = max(x)
        return torch.exp(x-c) / sum(torch.exp(x-c))


my_softmax_stable = SoftmaxStable()
output = my_softmax_stable(data)
print(output)
