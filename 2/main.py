import matplotlib.pyplot as plt
import os
import numpy as np
from scipy import stats

V = [0.1248, 0.0435] # m/s (velocity)
R_squared = [0.0552, 0.0225] # cm^2 (radius squared)

R_squared_m2 = [r/10000 for r in R_squared]  # cm^2 -> m^2

slope, intercept, r_value, p_value, std_err = stats.linregress(R_squared_m2, V)

print(f"V vs r² Graph Analysis:")
print(f"Slope: {slope:.4f} m/s per m²")
print(f"Y-intercept: {intercept:.4f} m/s")
print(f"R² value: {r_value**2:.4f}")

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'serif'],
    'text.usetex': False,       # mathtext ile LaTeX uyumu
    'font.size': 22,            # genel font, legend ve tick'ler için de baz alınabilir
    'axes.labelsize': 26,       # X ve Y label
    'axes.titlesize': 30,       # grafik başlığı
    'xtick.labelsize': 22,      # X tick
    'ytick.labelsize': 22,      # Y tick
    'legend.fontsize': 22,      # legend
    'figure.titlesize': 30,
    'mathtext.fontset': 'cm'    # LaTeX tarzı matematik fontu
})


plt.figure(figsize=(14, 10))
plt.scatter(R_squared_m2, V, color='red', s=200, label='Experimental data', zorder=5, 
           edgecolors='black', linewidth=2)  # Larger data points

x_fit = np.linspace(min(R_squared_m2), max(R_squared_m2), 100)
y_fit = slope * x_fit + intercept
plt.plot(x_fit, y_fit, 'b-', label=f'Linear fit: V = {slope:.3f}r² + {intercept:.4f}', linewidth=4)

plt.xlabel(r'$r^2$ (m$^2$)', fontweight='bold')
plt.ylabel(r'$V$ (m/s)', fontweight='bold')
plt.title('Velocity vs Radius Squared', fontweight='bold', pad=25)
plt.grid(True, alpha=0.5, linestyle='--', linewidth=1.0)
plt.legend(frameon=True, fancybox=True, shadow=True, loc='upper left', 
          framealpha=0.95, edgecolor='black', facecolor='white')

plt.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.90)

plt.tight_layout()

save_path = 'graphs'
os.makedirs(save_path, exist_ok=True)

plt.savefig(f'{save_path}/velocity_vs_radius_squared.pdf', 
            format='pdf', 
            dpi=300, 
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none')

plt.savefig(f'{save_path}/velocity_vs_radius_squared.png', 
            format='png', 
            dpi=300, 
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none')

plt.show()

print(f"\nGraph saved as:")
print(f"- velocity_vs_radius_squared.pdf (recommended for LaTeX)")
print(f"- velocity_vs_radius_squared.png (alternative format)")

print("\n" + "="*50)
print("VISCOSITY CALCULATION")
print("="*50)

g = 9.81

rho_2 = 7800
rho_1 = 900

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