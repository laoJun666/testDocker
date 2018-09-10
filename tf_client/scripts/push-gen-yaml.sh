 
IMAGENAME="laojun/test:develop01"
DOCKERSERVER="192.168.1.201:5000"

file_path='current_imageName.txt'

if [ ! -f $file_path ];then
echo "配置文件不存在"
echo "使用默认镜像名称 <$IMAGENAME>"
else
image_name=`cat $file_path`
IMAGENAME=$image_name
echo "使用 配置项 镜像名 <$IMAGENAME>"
fi


id=`docker images ${IMAGENAME} -q`
echo $id
docker tag $id ${DOCKERSERVER}/${IMAGENAME}

docker push ${DOCKERSERVER}/${IMAGENAME}
echo "镜像更新成功"

python ./scripts/k8s_tensorflow.py \
    --num_workers 6 \
    --num_parameter_servers  2\
    --grpc_port 2222 \
    --request_load_balancer true \
    --docker_image ${DOCKERSERVER}/${IMAGENAME} \
    > ./tf-k8s-with-lb.yaml