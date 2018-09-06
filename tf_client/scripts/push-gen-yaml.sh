 
IMAGENAME="laojun/test:develop01"
DOCKERSERVER="192.168.1.201:5000"

if $KD_TEST_IMAGENAME
then
IMAGENAME = $KD_TEST_IMAGENAME
fi

id=`docker images ${IMAGENAME} -q`
echo $id
docker tag $id ${DOCKERSERVER}/${IMAGENAME}
 
docker push ${DOCKERSERVER}/${IMAGENAME}
echo "镜像更新成功"

python ./scripts/k8s_tensorflow.py \
    --num_workers 2 \
    --num_parameter_servers 1 \
    --grpc_port 2222 \
    --request_load_balancer true \
    --docker_image ${DOCKERSERVER}/${IMAGENAME} \
    > ./tf-k8s-with-lb.yaml