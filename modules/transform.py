"""Transform module
"""
 
import tensorflow as tf
import tensorflow_transform as tft
 
# Map features to their respective keys (all lowercase)
FEATURE_KEYS = {
    "Study_Hours_Per_Day": "study_hours",
    "Extracurricular_Hours_Per_Day": "extracurricular_hours",
    "Sleep_Hours_Per_Day": "sleep_hours",
    "Social_Hours_Per_Day": "social_hours",
    "Physical_Activity_Hours_Per_Day": "physical_activity_hours",
    "GPA": "gpa"
}
LABEL_KEY = "Stress_Level" 
 
def transformed_name(key):
    """Renaming transformed features"""
    return key + "_xf"
 
def preprocessing_fn(inputs):
    """
    Preprocess input features into transformed features
    
    Args:
        inputs: map from feature keys to raw features.
    
    Return:
        outputs: map from feature keys to transformed features.    
    """
    
    outputs = {}
    
    # Process features
    for original_key, new_key in FEATURE_KEYS.items():
        outputs[transformed_name(new_key)] = tft.scale_to_0_1(inputs[original_key])
    
    # Process label
    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)
    
    return outputs
