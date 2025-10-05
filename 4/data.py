# EXPERIMENT 4: REFRACTION OF LIGHT
# Data Analysis and Graph Generation

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def snells_law(n1, theta1, n2, theta2):
    """
    Verify Snell's law: n1*sin(theta1) = n2*sin(theta2)
    """
    return n1 * np.sin(np.radians(theta1)) - n2 * np.sin(np.radians(theta2))

def calculate_refractive_index(theta_incident, theta_refracted, n_air=1.0):
    """
    Calculate refractive index of material
    """
    return n_air * np.sin(np.radians(theta_incident)) / np.sin(np.radians(theta_refracted))

def generate_angle_graphs():
    """
    Generate incident vs refracted angle graphs
    """
    pass

def generate_sin_graphs():
    """
    Generate sin(incident) vs sin(refracted) graphs
    """
    pass

def error_analysis():
    """
    Calculate refractive index errors and standard deviation
    """
    pass

if __name__ == "__main__":
    generate_angle_graphs()
    generate_sin_graphs()
    error_analysis()
