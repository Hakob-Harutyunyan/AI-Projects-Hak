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


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('AverageReadTimeModel.html')

@app.route('/trigger_python', methods=['POST'])
def trigger_python():
    link = request.form.get('link')
    print(f'{link} was clicked')
    # Here, call the python function you want to execute.
    your_python_function()
    return 'Function Triggered'

def your_python_function():
    print('Python Function Executed')
