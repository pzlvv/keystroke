from dataset import read_data
import tensorflow as tf
import os
import pickle
# import numpy as np

with open('userinfo', 'rb') as f:
    username_list = pickle.load(f)


# mnist = input_data.read_data_sets("MNIST_data", one_hot=True)
batch, _ = read_data('testset')

N = len(batch[0])

feats = len(batch[0][0])
# K = len(batch[1][0])
K = len(username_list)

x = tf.placeholder(tf.float32, shape=[None, feats])
y = tf.placeholder(tf.float32, shape=[None, K])

W = tf.Variable(tf.zeros([feats, K]))
b = tf.Variable(tf.zeros([1, K]))

pred = tf.matmul(x, W) + b
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(pred, 1))
prediction = tf.arg_max(pred, 1)
# correct_prediction = tf.equal(tf.argmax(y), tf.argmax(pred))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=pred))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

saver = tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess, os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'model', 'model.ckpt'))

    print(pred.eval(feed_dict={x: batch[0]}))
    result = prediction.eval(feed_dict={x: batch[0]})
    print(result)

for i in result:
    print(username_list[i])
