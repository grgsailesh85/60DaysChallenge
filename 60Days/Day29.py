from skimage.feature import local_binary_pattern
from skimage import io
import matplotlib.pyplot as plt

# Read image in grayscale
image = io.imread("image.jpg", as_gray=True)

# LBP parameters
radius = 1
n_points = 8 * radius

# Compute LBP
lbp = local_binary_pattern(image, n_points, radius, method="uniform")

plt.imshow(lbp, cmap="gray")
plt.title("Local Binary Pattern")
plt.axis("off")
plt.show()