import tensorflow as tf

RELU_SCALE = 1.43

def mlp(t_in, widths):
    weights = []
    #assert len(t_in.get_shape()) == 2
    prev_width = t_in.get_shape()[1]
    prev_layer = t_in
    for i_layer, width in enumerate(widths):
        v_w = tf.compat.v1.get_variable("w%d" % i_layer, shape=(prev_width, width),
                initializer=tf.keras.initializers.VarianceScaling(distribution="uniform"))
        v_b = tf.compat.v1.get_variable("b%d" % i_layer, shape=(width,),
                initializer=tf.constant_initializer(0.0))
        weights += [v_w, v_b]
        t_layer = tf.matmul(prev_layer, v_w) + v_b
        if i_layer < len(widths) - 1:
            t_layer = tf.nn.relu(t_layer)
            #t_layer = tf.nn.tanh(t_layer)
        prev_layer = t_layer
        prev_width = width
    return prev_layer, weights

def embed(t_in, n_embeddings, size, multi=False):
    if multi:
        varz = [tf.compat.v1.get_variable("embed%d" % i, shape=(n_embeddings, size),
                    initializer=tf.keras.initializers.VarianceScaling(distribution="uniform"))
                for i in range(t_in.get_shape()[1])]
    else:
        varz = [tf.compat.v1.get_variable("embed", shape=(n_embeddings, size),
                    initializer=tf.keras.initializers.VarianceScaling(distribution="uniform"))]
    embedded = tf.nn.embedding_lookup(varz, t_in)
    eshape = embedded.get_shape()
    if multi:
        embedded = tf.reshape(embedded, (-1, eshape[1].value * eshape[2].value))
    return embedded, varz

def fixed_embed(t_in, varz):
    embedded = tf.nn.embedding_lookup(varz, t_in)
    return embedded
