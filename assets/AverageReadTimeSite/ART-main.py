import numpy as np
import tensorflow as tf
import keras_nlp

tokenizer = keras_nlp.models.BertTokenizer.from_preset(
    "bert_base_en_uncased",
)

model_path = "../../AverageReadTime Model"

model = tf.keras.models.load_model(model_path)

@tf.function
def eager_to_tensor_function(eager_tensor):
    return [eager_tensor]

def predict(text):
    return model.predict(eager_to_tensor_function(tokenizer(text)))\
    