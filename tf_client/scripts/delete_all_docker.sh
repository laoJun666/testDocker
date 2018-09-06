#!/bin/bash



delete_all_continar(){
    #删除所有docker容器
    echo "删除所有docker容器"
    docker rm `docker ps -a -q`
}

delete_all_none_images(){
    #删除所有 <none> 镜像
    echo "删除所有 <none> 镜像"
    docker rmi $(docker images | awk '/^<none>/ { print $3 }')
}


if [ "$1" == "-all" ];
then
    delete_all_continar
    delete_all_none_images
elif [ "$1" == "-images" ];
then
    delete_all_none_images
else
    delete_all_continar
fi
