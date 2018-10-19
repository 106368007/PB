# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 18:30:19 2018

@author: chinja
"""

import tensorflow as tf

# 宣告常數
A = tf.constant(10, dtype=tf.int64)

with tf.Session() as sess:
    print( A ) 
    # Tensor("Const_42:0", shape=(), dtype=int64)
    
    print( sess.run(A) ) 
    # 10

    # 使用 sess.run() 才能取得 A 的值