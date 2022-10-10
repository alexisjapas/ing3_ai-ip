def color_to_gray(image):
    return 0.299*image[:, :, 0] + 0.587*image[:, :, 1] + 0.114*image[:, :, 2]


def to_uint8(image):
    image = image.astype(np.double)
    image = (image - image.min()) / (image.max() - image.min()) * 2**8
    return image.astype(np.uint8)


def histogram(image):
    image = to_uint8(image)
    hist = np.zeros(2**8, 
