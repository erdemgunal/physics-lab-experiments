# EXPERIMENT 2: VISCOSITY COEFFICIENT OF GLYCERIN
# Data Analysis and Graph Generation

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Physical constants
rho_steel = 7850  # kg/m³ - density of steel ball
rho_glycerin = 1260  # kg/m³ - density of glycerin
g = 9.81  # m/s² - gravitational acceleration

def calculate_terminal_velocity(distance, time):
    """
    Calculate terminal velocity from distance and time
    """
    return distance / time

def calculate_viscosity_coefficient(radius, velocity):
    """
    Calculate viscosity coefficient using Stokes' law
    η = (2gr²(ρ_ball - ρ_fluid)) / (9v)
    """
    return (2 * g * radius**2 * (rho_steel - rho_glycerin)) / (9 * velocity)

def generate_velocity_vs_radius_graph():
    """
    Generate velocity vs radius² graph as mentioned in the existing files
    """
    # This will create the velocity_vs_radius_squared.png graph
    pass

def stokes_law_analysis():
    """
    Analyze data according to Stokes' law
    """
    pass

def error_analysis():
    """
    Calculate percentage errors and standard deviations
    """
    pass

if __name__ == "__main__":
    # Load experimental data
    # Generate graphs including velocity_vs_radius_squared.png
    generate_velocity_vs_radius_graph()
    stokes_law_analysis()
    error_analysis()
