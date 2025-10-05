import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Data
V = [0.1248, 0.0435] # m/s (velocity)
R_squared = [0.0552, 0.0225] # cm^2 (radius squared)

# Convert R_squared values to m^2
R_squared_m2 = [r/10000 for r in R_squared]  # cm^2 -> m^2

# Linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(R_squared_m2, V)

print(f"V vs r² Graph Analysis:")
print(f"Slope: {slope:.4f} m/s per m²")
print(f"Y-intercept: {intercept:.4f} m/s")
print(f"R² value: {r_value**2:.4f}")

# LaTeX compatible font settings - maximized for report visibility
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'serif'],  # Fallback fonts
    'text.usetex': False,  # Keep False for compatibility
    'font.size': 18,       # Much larger base font size
    'axes.labelsize': 22,  # Much larger axis labels
    'axes.titlesize': 24,  # Much larger title
    'xtick.labelsize': 18, # Much larger tick labels
    'ytick.labelsize': 18, # Much larger tick labels
    'legend.fontsize': 18, # Much larger legend
    'figure.titlesize': 24,
    'mathtext.fontset': 'stix'  # Better math font rendering
})

# Create graph with maximum visibility for reports
plt.figure(figsize=(14, 10))  # Even larger figure for maximum readability
plt.scatter(R_squared_m2, V, color='red', s=200, label='Experimental data', zorder=5, 
           edgecolors='black', linewidth=2)  # Larger data points

# Linear fit line
x_fit = np.linspace(min(R_squared_m2), max(R_squared_m2), 100)
y_fit = slope * x_fit + intercept
plt.plot(x_fit, y_fit, 'b-', label=f'Linear fit: V = {slope:.3f}r² + {intercept:.4f}', linewidth=4)

plt.xlabel(r'$r^2$ (m$^2$)', fontweight='bold')  # Bold axis labels
plt.ylabel(r'$V$ (m/s)', fontweight='bold')      # Bold axis labels
plt.title('Velocity vs Radius Squared', fontweight='bold', pad=25)  # Bold title with more padding
plt.grid(True, alpha=0.5, linestyle='--', linewidth=1.0)  # Even more visible grid
plt.legend(frameon=True, fancybox=True, shadow=True, loc='upper left', 
          framealpha=0.95, edgecolor='black', facecolor='white')  # Enhanced legend

# Add more space around the plot
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90)

# Make the graph more professional and LaTeX-compatible
plt.tight_layout()

# Save as PDF for LaTeX/Overleaf
plt.savefig('velocity_vs_radius_squared.pdf', 
            format='pdf', 
            dpi=300, 
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none')

# Save as high-quality PNG as alternative
plt.savefig('velocity_vs_radius_squared.png', 
            format='png', 
            dpi=300, 
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none')

plt.show()

print(f"\nGraph saved as:")
print(f"- velocity_vs_radius_squared.pdf (recommended for LaTeX)")
print(f"- velocity_vs_radius_squared.png (alternative format)")

# Parameters needed for viscosity calculation
print("\n" + "="*50)
print("VISCOSITY CALCULATION")
print("="*50)

# Formula: η = (2 * g * (ρ2 - ρ1)) / (9 * m)
# Where m = slope (obtained from the graph)

g = 9.81  # gravitational acceleration (m/s²)

# Actual density values used in experiment
rho_2 = 7800  # kg/m³ (steel sphere density)
rho_1 = 900   # kg/m³ (glycerin density)

# Viscosity calculation
eta_graph = (2 * g * (rho_2 - rho_1)) / (9 * slope)

print(f"Parameters used:")
print(f"g = {g} m/s²")
print(f"ρ₂ = {rho_2} kg/m³")
print(f"ρ₁ = {rho_1} kg/m³")
print(f"m (slope) = {slope:.4f} (m/s)/m²")
print(f"\nCalculated viscosity:")
print(f"η_graph = {eta_graph:.4f} Pa·s")
print(f"η_graph = {eta_graph*1000:.2f} mPa·s")

print("\n" + "="*50)
print("FORMULA EXPLANATION")
print("="*50)
print("η_graph = (2 * g * (ρ₂ - ρ₁)) / (9 * m)")
print("Where:")
print("- η_graph: Viscosity calculated from the graph")
print("- g: Gravitational acceleration")
print("- ρ₂: Density of the falling object")
print("- ρ₁: Density of the fluid")
print("- m: Slope of the V vs r² graph")