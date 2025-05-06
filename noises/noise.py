import numpy as np


def white_noise(size, ampl, **kwargs) -> np.ndarray:

    return np.random.uniform(-ampl, ampl, size)

def gaussian_noise(size, ampl, **kwargs) -> np.ndarray:

    return np.random.normal(0.0,ampl,size)