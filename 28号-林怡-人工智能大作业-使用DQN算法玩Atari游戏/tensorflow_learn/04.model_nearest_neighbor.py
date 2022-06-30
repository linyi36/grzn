'''
A nearest neighbor learning algorithm example using TensorFlow library.
This example is using the MNIST database of handwritten digits
(http://yann.lecun.com/exdb/mnist/)
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
这里获取mnist数据集,然后采用L1距离的kNN算法进行分类
'''

from __future__ import print_function

import numpy as np
import tensorflow as tf

# Import MNIST data
from tensorflow_learn import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# In this example, we limit mnist data
Xtr, Ytr = mnist.train.next_batch(5000)  # 5000 for training (nn candidates) #训练5000张
Xte, Yte = mnist.test.next_batch(20)  # 200 for testing #测试200张

# tf Graph Input
xtr = tf.placeholder("float", [None, 784]) # 起形参的作用
xte = tf.placeholder("float", [784]) # 起形参的作用

# Nearest Neighbor calculation using L1 Distance(沿直角轴测得的距离,又叫"曼哈顿距离"或者"城市街道距离")
# [关于Lm Distance的解释](https://xlinux.nist.gov/dads/HTML/lmdistance.html)
# Calculate L1 Distance
# [关于tf.reduce_sum的用法](https://blog.csdn.net/u012193416/article/details/83349138?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)
# [reduction_indices的意义:控制压缩方向](https://blog.csdn.net/qq_33096883/article/details/77479766)
distance = tf.reduce_sum(tf.abs(tf.add(xtr, tf.negative(xte))), reduction_indices=1)  # |xtr-xte|
# Prediction: Get min distance index (Nearest neighbor)
# [kNN](https://baike.baidu.com/item/%E9%82%BB%E8%BF%91%E7%AE%97%E6%B3%95/1151153?fromtitle=Knn&fromid=3479559)
pred = tf.arg_min(distance, 0) # arg_min???字面上讲是返回最小值的坐标,没懂!

accuracy = 0.

# Initializing the variables
init = tf.initialize_all_variables()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)  # 运行并传递初始化参数

    # loop over test data
    for i in range(len(Xte)): #遍历测试数据
        # Get nearest neighbor
        nn_index = sess.run(pred, feed_dict={xtr: Xtr, xte: Xte[i, :]}) # [feed_dict的作用是替换图中某个tensor的值](https://blog.csdn.net/qq_36666115/article/details/80017305)
        # Get nearest neighbor class label and compare it to its true label
        print("Test", i, "Prediction:", np.argmax(Ytr[nn_index]), \
              "True Class:", np.argmax(Yte[i]))
        # Calculate accuracy
        if np.argmax(Ytr[nn_index]) == np.argmax(Yte[i]): # 测算正常
            accuracy += 1. / len(Xte) # 精度就加1/200
    print("Done!")
    print("Accuracy:", accuracy)
