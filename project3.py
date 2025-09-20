from PIL import Image
import numpy as np
import requests
from io import BytesIO

# Download the image from a URL
url = "https://i1.pickpik.com/photos/191/956/858/tiger-animals-cat-predator-preview.jpg"
response = requests.get(url)

# Open the image and convert to grayscale
img = Image.open(BytesIO(response.content)).convert("L")
imginarray = np.array(img)  # Convert image to numpy array

# Adjust brightness
darker = np.clip(imginarray - 50, 0, 255)  # Darker version
brighter = np.clip(imginarray + 50, 0, 255)  # Brighter version
print("brightness increased", brighter)
print("darkness increased", darker)

# Show original and brightness-adjusted images
Image.fromarray(brighter).show()
Image.fromarray(darker).show()
Image.fromarray(imginarray).show()

# Singular Value Decomposition (SVD) for image compression
U, S, T = np.linalg.svd(imginarray)
k = 50  # Number of singular values to keep
s_k = np.diag(S[0:k])  # Create diagonal matrix from top k singular values
compressed_img = U[:, 0:k] @ s_k @ T[0:k, :]  # Reconstruct compressed image

# Print shapes and types for verification
print(type(U), np.ndim(U))
print(type(S), np.ndim(S), S)
print(type(s_k))
print(type(T), np.ndim(T))
print(type(compressed_img))

# Show compressed image and original image
Image.fromarray(compressed_img).show()
Image.fromarray(imginarray).show()
