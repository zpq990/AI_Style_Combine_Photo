# deep_image_matting
+ ## 操作手册
  1. 环境说明
    + 工程的技术用的是pytorch
    + 需要导入的包:
        + python3.7 
        + torch 1.3.1 torchvision 0.4.2  （GPU版，1.0+pytorch即可）
        + tensorflow（任意版本，支持tensorboard即可）
        + pillow 6.0.0(pillow 6.0.0需要降到7.0.0以下版本，否则torchvision会报错)
  2. 操作顺序
    + 运行 data/retrieve.py 图片预处理的类
        + 超参设定:只需要设定好训练数据的地址(main方法中的root_dir)
            + ![avatar](1.png)
    + 运行 train.py 训练(300epoch,本机是1050的笔记本显卡,训练了24小时不到,速度还不错) 
        + 超参设定:所有的超参都是在这个对象中,需要导入包
        parser = argparse.ArgumentParser(description='Train deep image matting model.')
            + ![avatar](1.png)
    + 运行 predict.py 测试(预测): 
        预测暂时只能预测作者已有的test集,自己的图片无法测试,研究中 __(todo)__
  3. 其它补充
+ ## 类说明
  1.
  2.
  3.
+ ## 问题说明
    + 环境问题
        + pytorch的cuda版有很多安装问题,初期安装遇到有如下三个问题
            + cuda版本的 torch 和 torchvision 版本不兼容,原因:pytorch的torch,torchvision必须对应,否则版本不兼容.(百度查询直接在清华源下载)
            + numpy中的一个子类pillow和pytorch不兼容(pillow 6.0.0需要降到7.0.0以下版本，否则torchvision会报错),
            找到6.0.0这个版本最为稳妥(网上直接下载whel文件然后pip直接安装)
            + cuda版本显卡对应(cuda版本需要对应本地显卡的型号,还有设置好环境变量)
    + 运行问题
        + data/retrieve.py
            + 这个是预处理图片数据的类
        + train.py
+ ## 未解决问题
