#Version:0.0.1
FROM tensorflow/tensorflow
#FROM tensorflow/tf_grpc_server

MAINTAINER laojun "xqccf@foxmail.com"

#工作文件夹
ENV KD_WORKSPACE /home/tf_client
#python 包 搜索路径
ENV PYTHONPATH "$PYTHONPATH:/home"
#引导文件
ENV KD_LAUNCH_FILE launched.py
#启动文件
ENV KD_TARGET_FILE mnistTest/mnist_replica.py

#安装 vim 
#RUN apt-get update
#RUN apt-get install -y vim
#RUN apt-get install -y inetutils-ping
#复制项目文件夹
ADD . $KD_WORKSPACE/.
#复制引导脚本
ADD $KD_LAUNCH_FILE /var/.
#设置工作路径
WORKDIR $KD_WORKSPACE
#启动引导文件，注意这里不能使用环境变量，暂不支持
ENTRYPOINT ["/var/launched.py"]
