# 人像风格迁移
## 项目简介
## 导入库
+ python3.7 
+ torch 1.3.1 torchvision 0.4.2  （GPU版，1.0+pytorch即可）
+ tensorflow（任意版本，支持tensorboard即可）
+ matplotlib
+ pillow 6.0.0(需要降到7.0.0以下版本，否则torchvision会报错)
## 结构目录
+ Data
    + 数据集目录
+ Demo
    + 测试demo目录
+ Model
    + 模型存储目录
+ Util
    + 工具类
+ Train
    + 训练类
+ Service
    + 服务类（端到端的接口类）
## 资料链接
+ 数据集
    + 人像Matting抠图数据集
        + 1. matting_human_datasets(半身人像Matting 14g)
            + [github.com/aisegmentcn/matting_human_datasets](https://github.com/aisegmentcn/matting_human_datasets)
        + 2. pytorch-deep-image-matting(抠图照 19g)
            + [pythonawesome.com/pytorch-implementation-of-deep-image-matting](https://pythonawesome.com/pytorch-implementation-of-deep-image-matting/)
+ 项目地址
    + 抠图训练
        + 1. 基于pytorch   
            + [Shirhe-Lyh/deep_image_matting_pytorch](https://github.com/Shirhe-Lyh/deep_image_matting_pytorch)
            + [znxlwm/UGATIT-pytorch](https://github.com/znxlwm/UGATIT-pytorch)
        + 2. 基于tensorflow
            + [foamliu/Deep-Image-Matting](https://github.com/foamliu/Deep-Image-Matting)
         
            
+ 论文地址
