from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

model_path = '/content/model.h5'  # Replace with the path to your trained model
img_path = '/content/Y7.jpg'  # Replace with the path to your new image

# Load the trained model
model = load_model(model_path)

# Preprocess the new image
img = image.load_img(img_path, target_size=(150, 150))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0

# Make predictions
prediction = model.predict(img_array)
if prediction[0] < 0.5:
    print("The image does not contain a brain tumor.")
else:
    print("The image contains a brain tumor.")
