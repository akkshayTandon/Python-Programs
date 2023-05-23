import cv2

# Configurable Parameters
source = "cepheus-verse-logo.jpg"        # source of the image to be resized
destination = "resized.png"   # name and destination of new resized image
scale_percent = 50 # percent by which image is resized

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# Resize according to scale_percent
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)
new_size = (new_width, new_height)

output = cv2.resize(src, new_size)

cv2.imwrite(destination, output)
cv2.waitKey(0)