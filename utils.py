import os
import tensorflow as tf
import numpy as np
from PIL import Image
import streamlit as st

# Path to the FOLDER
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "eye_disease_fixed_model")

@st.cache_resource
def load_my_model():
    if not os.path.exists(MODEL_PATH):
        return f"Error: Model folder missing at {MODEL_PATH}"
    try:
        # Keras 3 way to load Legacy SavedModel folders
        # 'serving_default' is the standard endpoint for exported models
        model_layer = tf.keras.layers.TFSMLayer(MODEL_PATH, call_endpoint='serving_default')
        return model_layer
    except Exception as e:
        return f"Model Load Error: {str(e)}"

def predict(image):
    model = load_my_model()
    if isinstance(model, str): return model, 0.0
    
    try:
        # Preprocessing
        img = image.convert('RGB').resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0).astype(np.float32)
        
        # In TFSMLayer, the output is a dictionary
        prediction_dict = model(img_array)
        
        # Keras 3 usually returns a dict with a key like 'outputs' or 'output_0'
        # Hum saare keys check kar lete hain safety ke liye
        output_key = list(prediction_dict.keys())[0]
        prediction = prediction_dict[output_key].numpy()
        
        classes = ["Cataract", "Diabetic Retinopathy", "Glaucoma", "Normal"]
        
        class_index = np.argmax(prediction)
        confidence = float(np.max(prediction))
        
        return classes[class_index], confidence
    except Exception as e:
        return f"Prediction Error: {str(e)}", 0.0