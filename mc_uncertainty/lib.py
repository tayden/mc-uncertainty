import numpy as np


def variance(data):
    """Data is expected to have shape (mc_samples, n, classes)."""
    return np.var(data, axis=0)


def entropy(data):
    """Data is expected to have shape (mc_samples, n, classes)."""
    return -np.sum(data * np.log(data + 1e-10), axis=-1)


def predicted_entropy(data):
    """Data is expected to have shape (mc_samples, n, classes)."""
    return np.mean(entropy(data), axis=0)


def mutual_information(data):
    """Data is expected to have shape (mc_samples, n, classes).""" 
    entropy_exp_p = entropy(np.mean(data, axis=0))
    exp_entropy = np.mean(entropy(data), axis=0)
    return entropy_exp_p - exp_entropy