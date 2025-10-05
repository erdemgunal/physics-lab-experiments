# EXPERIMENT 5: LIGHT THROUGH A PARALLEL SIDED BLOCK
# Data Analysis and Graph Generation

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def calculate_parallel_shift(L, theta1, theta2):
    """
    Calculate parallel shift: d = L * sin(theta1 - theta2) / cos(theta2)
    """
    theta1_rad = np.radians(theta1)
    theta2_rad = np.radians(theta2)
    return L * np.sin(theta1_rad - theta2_rad) / np.cos(theta2_rad)

def verify_snells_law(theta1, theta2, n_glass=1.5):
    """
    Verify Snell's law for glass block
    """
    return np.sin(np.radians(theta1)) / np.sin(np.radians(theta2))

def generate_shift_analysis():
    """
    Generate theoretical vs experimental shift graphs
    """
    pass

def error_analysis():
    """
    Calculate percentage errors in parallel shift
    """
    pass

if __name__ == "__main__":
    generate_shift_analysis()
    error_analysis()
