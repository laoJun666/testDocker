#!/bin/bash

DOCKERFILE="./Dockerfile"
IMAGENAME="laojun/test:develop03"
export KD_TEST_IMAGENAME=IMAGENAME

count=`'docker images ${IMAGENAME}'`

echo count
if [  count  !=  0  ];
then
echo "镜像<$IMAGENAME> 已存在，开始清理。。。"
echo "删除所有容器。。。"
sh delete_all_docker.sh
echo "删除目标镜像"
docker rmi `docker images ${IMAGENAME} -q`


fi


docker build --file=${DOCKERFILE} -t=${IMAGENAME} .

# docker run  ${IMAGENAME} ["--cluster_spec=worker|tf-worker0:2222,ps|tf-ps0:2222;tf-ps1:2222", "--job_name=worker", "--task_id=0"]

# docker run  ${IMAGENAME} --job_name=231

docker run  -it  ${IMAGENAME} --cluster_spec="worker|tf-worker0:2222,ps|tf-ps0:2222;tf-ps1:2222" \
              				  --job_name=ps\
               				  --task_id=1
