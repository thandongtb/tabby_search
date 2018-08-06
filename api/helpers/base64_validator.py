import cv2

def valid(img):
    error = 0
    try:
        if img.shape[2] != 3:
            if img.shape[2] == 1:
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            elif img.shape[2] == 4:
                img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
            else:
                error = 1
    except:
        error = 1
    return img, error
