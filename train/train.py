from dataset import read_data
import tensorflow as tf
import os
import pickle
# import numpy as np


batch, username_list = read_data('dataset')

with open('userinfo', 'wb') as f:
    pickle.dump(username_list, f)


N = batch[0]
feats = len(batch[0][0])
K = len(batch[1][0])

x = tf.placeholder(tf.float32, shape=[None, feats])
y = tf.placeholder(tf.float32, shape=[None, K])

W = tf.Variable(tf.zeros([feats, K]))
b = tf.Variable(tf.zeros([1, K]))

pred = tf.matmul(x, W) + b
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(pred, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=pred))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        train_step.run(feed_dict={x: batch[0], y: batch[1]})
    print(accuracy.eval(feed_dict={x: batch[0], y: batch[1]}))
    saver.save(sess, os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  'model', 'model.ckpt'))
