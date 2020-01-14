import torch as torch

# 测试torch_gpu是否可运行
print(torch.cuda.is_available())

# 查看torch版本
print(torch.__version__)

# 验证torchvision
import torchvision
print(torchvision.__version__)