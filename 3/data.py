# EXPERIMENT 3: THIN EDGES LENS
# Data Analysis and Graph Generation

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def lens_formula(do, di):
    """
    Calculate focal length using lens formula: 1/f = 1/do + 1/di
    """
    return 1 / ((1/do) + (1/di))

def magnification(di, do):
    """
    Calculate magnification: m = di/do
    """
    return di / do

def generate_focal_length_graph():
    """
    Generate 1/do vs 1/di graph to find focal length
    """
    # Graph where slope and intercepts give focal length
    pass

def statistical_analysis():
    """
    Calculate average focal length and standard deviation
    """
    pass

def error_analysis():
    """
    Calculate relative errors and maximum absolute error
    """
    pass

if __name__ == "__main__":
    # Load experimental data
    generate_focal_length_graph()
    statistical_analysis()
    error_analysis()
