import os
import json
import torch
import torch.nn as nn

import matplotlib.pyplot as plt
import numpy as np
import cv2

def load_json(path):
    data = None
    with open(path, 'r') as f:
        data = json.load(f)
    return data

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def check_path(path):
    if not os.path.isfile(path):
        raise ValueError(f'File does not exist: {path}')
    
def convert_to_mask_path(image_path):
    #mask_path = image_path.replace('img', 'mask')
    mask_path = image_path.replace('/images/', '/images-mask/')
    if os.path.isfile(mask_path):
        return mask_path
    else:
        raise ValueError(f'Mask path not found. {mask_path}')
    

def load_model(model_path: str,
               model_class: nn.Module,
               device: torch.device, *args, **kwargs) -> nn.Module:
    """Loads a PyTorch model from a given path.

    Args:
        model_path: The path to the saved model file.
        model_class: The class of the model to load.
        device: The device to load the model onto.

    Returns:
        The loaded model.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    state_dict = torch.load(model_path, map_location=device)
    model = model_class(*args, **kwargs).to(device)
    if 'model_state_dict' in state_dict:
        model.load_state_dict(state_dict['model_state_dict'])
    else:
        model.load_state_dict(state_dict)
    return model


def combine_images(rgb_image_path, mask_image_path, output_path):
    # Read the RGB image using plt
    rgb_image = plt.imread(rgb_image_path)
    
    # Read the grayscale mask image using OpenCV
    mask_image = cv2.imread(mask_image_path, cv2.IMREAD_GRAYSCALE)

    if mask_image is None:
        raise FileNotFoundError(f"Mask image not found at {mask_image_path}")
    
    # Ensure the mask has the same width and height as the RGB image
    if rgb_image.shape[:2] != mask_image.shape[:2]:
        raise ValueError("The dimensions of the RGB image and the mask image do not match")
    
    # Expand the mask image to have a single channel
    mask_image = np.expand_dims(mask_image, axis=-1)
    
    # Concatenate the RGB image and the mask image along the channel dimension
    combined_image = np.concatenate((rgb_image, mask_image), axis=-1)
    
    # Save the combined image using plt
    plt.imsave(output_path, combined_image)
    
    return combined_image

def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)