import cv2
import numpy as np


def read_image(image_path: str) -> np.ndarray:
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    return img


def extract_green(img: np.ndarray) -> np.ndarray:
    return img[:, :, 1]


def extract_red(img: np.ndarray) -> np.ndarray:
    return img[:, :, 2]


def extract_blue(img: np.ndarray) -> np.ndarray:
    return img[:, :, 0]


def swap_red_green_channel(img: np.ndarray) -> np.ndarray:
    out = img.copy()
    out[:, :, 1], out[:, :, 2] = img[:, :, 2], img[:, :, 1]
    return out


def embed_middle(image1: np.ndarray, image2: np.ndarray, embed_size: (int, int)) -> np.ndarray:
    img1 = image1.copy()
    img2 = image2.copy()
    center_y = img1.shape[0] // 2
    center_x = img1.shape[1] // 2

    x = embed_size[ 0] // 2
    y = embed_size[1] // 2
    img_slice = img1[center_y-x:center_y+y, center_x-x:center_x+y,:]

    center2_y = img2.shape[0] // 2
    center2_x = img2.shape[1] // 2

    img2[center2_y-x:center2_y+y, center2_x-x:center2_x+y,:] = img_slice

    return np.copy(img2)


def calc_stats(img: np.ndarray) -> np.ndarray:
    mean, std = cv2.meanStdDev(img)
    return np.array([float(mean[0][0]), float(std[0][0])], dtype=np.float64)


def shift_image(img: np.ndarray, shift_val: int) -> np.ndarray:
    height, width = img.shape #lol
    shift = int(shift_val)
    padded_img = cv2.copyMakeBorder(img, 0, 0, shift, 0, cv2.BORDER_CONSTANT, value=0)
    padded_img = padded_img[:, :width]
    return padded_img


def difference_image(img1: np.ndarray, img2: np.ndarray) -> np.ndarray:
    image1 = img1.copy()
    image2 = img2.copy()
    imgdiff = image1 - image2
    normimg = cv2.normalize(imgdiff, None, 0, 255, cv2.NORM_MINMAX)
    return normimg.astype(np.uint8)


def add_channel_noise(img: np.ndarray, channel: int, sigma: int) -> np.ndarray:
    out = img.astype(np.float32).copy()
    noise = np.random.randn(*out[:, :, channel].shape).astype(np.float32) * float(sigma)
    chan = out[:, :, channel] + noise
    chan = cv2.normalize(chan, None, 0, 255, cv2.NORM_MINMAX)
    out[:, :, channel] = chan
    return np.clip(out, 0, 255).astype(np.uint8)


def add_salt_pepper(img: np.ndarray) -> np.ndarray:
    out = img.copy()
    h, w = out.shape
    n = 5000
    n = min(n, h * w // 2)  # avoid duplicates dominating on tiny images
    ys = np.random.randint(0, h, n)
    xs = np.random.randint(0, w, n)
    out[ys, xs] = 0
    ys = np.random.randint(0, h, n)
    xs = np.random.randint(0, w, n)
    out[ys, xs] = 255
    return out


def blur_image(img: np.ndarray, ksize: int) -> np.ndarray:
    if ksize % 2 == 0 or ksize < 1:
        raise ValueError("ksize must be odd and >= 1")
    return cv2.medianBlur(img, ksize,0)
