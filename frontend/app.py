import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# --- Configuration (Updated from your notebook) ---
IMG_HEIGHT = 224
IMG_WIDTH = 224
CLASS_NAMES = [
    'Amphibia', 'Animalia', 'Arachnida', 'Aves', 'Fungi', 
    'Insecta', 'Mammalia', 'Mollusca', 'Plantae', 'Reptilia'
]
MODEL_PATH = 'frontend/models/best_model.h5'


# --- Model Loading ---
@st.cache_resource  # Caches the model so it doesn't re-load
def load_keras_model():
    """Loads and returns the trained Keras model."""
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        return model
    except Exception as e:
        st.error(f"Error loading model from {MODEL_PATH}. Did you place your .h5 file there?\nError: {e}")
        return None

model = load_keras_model()


# --- Image Preprocessing ---
def preprocess_image(image_data):
    """
    Takes an uploaded image, resizes it, normalizes it,
    and prepares it for the model.
    """
    # Open the image using PIL
    image = Image.open(image_data)
    
    # Resize the image to the model's expected input size (224x224)
    image = ImageOps.fit(image, (IMG_WIDTH, IMG_HEIGHT), Image.Resampling.LANCZOS)
    
    # Convert the image to a numpy array
    image_array = np.asarray(image)
    
    # Normalize the image (matches your notebook's Rescaling(1./255))
    normalized_image_array = image_array / 255.0
    
    # Expand the dimensions to create a "batch" of 1 image
    # Model expects shape (1, 224, 224, 3)
    data = np.expand_dims(normalized_image_array, axis=0)
    
    return data

# --- Streamlit App ---
st.title("🔬 COS30082 Image Classifier")
st.write("Upload an image to predict its biological class (Amphibia, Aves, Fungi, etc.)")
st.write("---")

# Image uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    
    st.write("") # Add a little space
    
    # Check if the model loaded successfully
    if model is not None:
        with st.spinner('Classifying...'):
            # 1. Preprocess the image
            processed_image = preprocess_image(uploaded_file)
            
            # 2. Make a prediction
            prediction = model.predict(processed_image)
            
            # 3. Get the most confident prediction
            predicted_index = np.argmax(prediction)
            
            # 4. Get the class name from your list
            predicted_class_name = CLASS_NAMES[predicted_index]
            
            # 5. Get the confidence score
            confidence_score = np.max(prediction) * 100
        
        # Display the result
        st.success(f"Prediction: **{predicted_class_name}**")
        st.write(f"Confidence: **{confidence_score:.2f}%**")
    else:
        st.error("Model is not loaded. Please check the `MODEL_PATH` and restart the app.")

else:
    st.info('Please upload an image file to get a prediction.')