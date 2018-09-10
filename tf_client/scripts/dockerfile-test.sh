#!/bin/bash

DOCKERFILE="./Dockerfile"
IMAGENAME="laojun/test:develop06"
config_file_path='current_imageName.txt'
current_path=`dirname $0`
#



check(){
count=`docker images ${IMAGENAME} -q`

if [  $count ];
then
echo "镜像<$IMAGENAME> 已存在，ID：$count 开始清理。。。"
echo "删除所有容器。。。"
sh $current_path/delete_all_docker.sh
echo "删除目标镜像"
docker rmi `docker images ${IMAGENAME} -q`

fi
}


build(){
echo '开始构建镜像'

docker build --file=${DOCKERFILE} -t=${IMAGENAME} .

echo '构建镜像 完成！'
echo $IMAGENAME > $config_file_path
echo "镜像名： $IMAGENAME 已输出到： $config_file_path"
}



testRunImage(){

echo "开始运行 镜像 <$IMAGENAME>"

docker run  ${IMAGENAME} ["--cluster_spec=worker|tf-worker0:2222,ps|tf-ps0:2222;tf-ps1:2222", "--job_name=worker", "--task_id=0"]

# docker run  ${IMAGENAME} --job_name=231

# docker run  -it  ${IMAGENAME} --cluster_spec="worker|tf-worker0:2222,ps|tf-ps0:2222;tf-ps1:2222" \
#               				  --job_name=ps\
#                				  --task_id=0
}




check
build

if [ "$1" = '-t' ];then
testRunImage
elif [ "$1" = '-p' ];then
sh $current_path/push-gen-yaml.sh
fi