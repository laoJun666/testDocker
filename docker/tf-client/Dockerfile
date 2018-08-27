#Version:0.0.1
FROM tensorflow/tensorflow
MAINTAINER laojun "xqccf@foxmail.com"

#安装 vim 
RUN apt-get update
RUN apt-get install -y vim
ADD MNIST_data /home/tf-client/MNIST_data
#ENTRYPOINT ["cd","/home/tf-client"]
WORKDIR /home/tf-client

