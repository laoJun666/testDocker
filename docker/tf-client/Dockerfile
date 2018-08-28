#Version:0.0.2
FROM laojun/tf-client:develop
MAINTAINER laojun "xqccf@foxmail.com"

#安装 vim 
RUN apt-get update
RUN apt-get install -y vim
ADD mnistTest /home/tf-client/mnistTest
#ENTRYPOINT ["cd","/home/tf-client"]
WORKDIR /home/tf-client

