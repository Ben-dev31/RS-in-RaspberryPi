import numpy as np


def rubber_zener_filter(x:np.ndarray, thr:float) -> np.ndarray:
    """
        x : data to filter
        thr : threshold value
    """
    y = np.zeros_like(x)
    y[x > thr] = x[x > thr] - thr    # cas ou le signal x > a
    y[x < -thr] = x[x < -thr] + thr  # cas ou le signal x < a
    return y

def diode_filter(x:np.ndarray, thr:float) -> np.ndarray:
    """
        x : data to filter
        thr : threshold value
    """
    return np.where(x < thr, 0, x - thr)