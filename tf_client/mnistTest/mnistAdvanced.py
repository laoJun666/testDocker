# -*- coding: UTF-8 -*-

import  input_data_custom as input_data
import tensorflow as tf

#准备数据
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

#计算图
sess = tf.InteractiveSession()

#我们通过为输入图像和目标输出类别创建节点，来开始构建计算图。
x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])

#变量
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

#初始变量
sess.run(tf.initialize_all_variables())

#损失 (差值)
cross_entropy = -tf.reduce_sum(y_*tf.log(y))

#优化权重(交叉熵下降，步长为0.01.)
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#训练
for i in range(1000):
  batch = mnist.train.next_batch(50)
  train_step.run(feed_dict={x: batch[0], y_: batch[1]})

