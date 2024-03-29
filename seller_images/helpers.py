import numpy as np
import base64
import sys
import cv2

def base64_encode_image(a):
    # base64 encode the input NumPy array
    return base64.b64encode(a).decode("utf-8")


def base64_decode_image(a, dtype, shape):
    # if this is Python 3, we need the extra step of encoding the
    # serialized NumPy string as a byte object
    if sys.version_info.major == 3:
        a = bytes(a, encoding="utf-8")

    # convert the string to a NumPy array using the supplied data
    # type and target shape
    a = np.frombuffer(base64.decodestring(a), dtype=dtype)
    a = a.reshape(shape)

    # return the decoded image
    return a

def base64_to_image(base64_string):
    try:
        imgdata = base64.b64decode(base64_string)
        image = np.asarray(bytearray(imgdata), dtype="uint8")
        image = cv2.imdecode(image,cv2.COLOR_BGR2RGB)
        return image
    except:
        return np.array([])