import numpy as np
import tensorflow as tf
import keras_nlp
from flask import Flask, render_template, request

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


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('AverageReadTimeModel.html')


@app.route('/on_button_click', methods=['POST'])
def on_button_click():
    # Execute your python function here.
    link = request.form.get('link')
    print(f'Button clicked: {link}')
    return 'Button Click'
