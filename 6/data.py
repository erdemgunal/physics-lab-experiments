# EXPERIMENT 6: POLARIZATION
# Data Analysis and Graph Generation

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def malus_law(I0, theta):
    """
    Malus' law: I = I0 * cos²(theta)
    """
    return I0 * (np.cos(np.radians(theta)))**2

def analyze_polarization_data():
    """
    Analyze intensity changes with polarizer angle
    """
    pass

def generate_polarization_graphs():
    """
    Generate intensity vs angle graphs
    """
    pass

def verify_malus_law():
    """
    Verify Malus' law with experimental data
    """
    pass

if __name__ == "__main__":
    analyze_polarization_data()
    generate_polarization_graphs()
    verify_malus_law()
