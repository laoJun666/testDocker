#Version:0.0.2
FROM tensorflow/tensorflow
MAINTAINER laojun "xqccf@foxmail.com"

#安装 vim 
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y inetutils-ping
ADD mnistTest /home/tf-client/mnistTest
#ENTRYPOINT ["cd","/home/tf-client"]
WORKDIR /home/tf-client

