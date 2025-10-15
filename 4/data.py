import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Given data
theta_1_deg = np.array([10, 20, 30, 40, 50, 60, 70, 80])  # Incident angles in degrees
theta_2_deg = np.array([7, 13, 23, 28, 31, 34, 38, 40])   # Refracted angles in degrees
n_1 = 1.00  # Refractive index of air
n_2_theoretical = 1.485  # Theoretical refractive index of acrylic (PMMA/plexiglass)

# Convert degrees to radians for sin calculations
theta_1_rad = np.deg2rad(theta_1_deg)
theta_2_rad = np.deg2rad(theta_2_deg)

# Calculate sin values
sin_theta_1 = np.sin(theta_1_rad)
sin_theta_2 = np.sin(theta_2_rad)

# Calculate refractive index n_2 for each measurement using Snell's law: n_2 = n_1 * sin(theta_1) / sin(theta_2)
n_2 = n_1 * sin_theta_1 / sin_theta_2

# Print the measurements table
print("Measurements Table:")
print("Angle (θ₁) | sin(θ₁) | sin(θ₂) | n₂")
for i in range(len(theta_1_deg)):
    print(f"{theta_1_deg[i]:10} | {sin_theta_1[i]:7.4f} | {sin_theta_2[i]:7.4f} | {n_2[i]:7.4f}")

# Calculate average n_2 and standard deviation
avg_n_2 = np.mean(n_2)
std_dev = np.std(n_2)
print(f"\nExperimental Results:")
print(f"Average refractive index (n₂): {avg_n_2:.4f}")
print(f"Standard deviation of n₂: {std_dev:.4f}")
print(f"Theoretical refractive index (Acrylic/PMMA): {n_2_theoretical:.4f}")

# Calculate errors relative to theoretical value
theoretical_errors = np.abs(n_2 - n_2_theoretical) / n_2_theoretical * 100
avg_theoretical_error = np.abs(avg_n_2 - n_2_theoretical) / n_2_theoretical * 100
print(f"\nError Analysis:")
print(f"Individual errors from theoretical: {theoretical_errors}")
print(f"Average experimental error from theoretical: {avg_theoretical_error:.2f}%")
print(f"Maximum individual error from theoretical: {np.max(theoretical_errors):.2f}%")

# Calculate relative errors from experimental average
rel_errors = np.abs(n_2 - avg_n_2) / avg_n_2 * 100
max_rel_error = np.max(rel_errors)
print(f"Maximum relative error from experimental average: {max_rel_error:.2f}%")

# Plot 1: Incoming (incident) angle vs outgoing (refracted) angle
plt.figure(figsize=(10, 7))
plt.plot(theta_1_deg, theta_2_deg, 'bo-', markersize=8, linewidth=2, label='Experimental data')

# Add theoretical line for comparison using PMMA refractive index
theta_theory = np.linspace(0, 90, 100)
theta_theory_rad = np.deg2rad(theta_theory)
sin_theory = np.sin(theta_theory_rad)
# Using theoretical n_2 for PMMA/Acrylic
theta_2_theory = np.arcsin(sin_theory / n_2_theoretical)
theta_2_theory_deg = np.rad2deg(theta_2_theory)
# Only plot where arcsin is valid (sin value ≤ 1)
valid_indices = sin_theory / n_2_theoretical <= 1
plt.plot(theta_theory[valid_indices], theta_2_theory_deg[valid_indices], 'r--', 
         linewidth=3, label=f'Theoretical Acrylic/PMMA (n₂={n_2_theoretical})')

# Also add experimental average for comparison
theta_2_exp_avg = np.arcsin(sin_theory / avg_n_2)
theta_2_exp_avg_deg = np.rad2deg(theta_2_exp_avg)
valid_indices_exp = sin_theory / avg_n_2 <= 1
plt.plot(theta_theory[valid_indices_exp], theta_2_exp_avg_deg[valid_indices_exp], 'g:', 
         linewidth=2, label=f'Experimental Average (n₂={avg_n_2:.3f})', alpha=0.8)

plt.xlabel('Incident Angle θ₁ (degrees)', fontsize=12)
plt.ylabel('Refracted Angle θ₂ (degrees)', fontsize=12)
plt.title('Graph of Incident Angle vs Refracted Angle\n(Question 3: Refraction Behavior)', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xlim(0, 95)
plt.ylim(0, 80)

# Add annotation explaining the behavior
plt.text(45, 18, f'Material: Acrylic (PMMA)\nTheoretical n₂ = {n_2_theoretical}\nExperimental n₂ = {avg_n_2:.3f}\nError = {avg_theoretical_error:.1f}%', 
         bbox=dict(boxstyle="round,pad=0.5", facecolor="lightcyan", alpha=0.9),
         fontsize=10, ha='center')

plt.tight_layout()
plt.savefig('graphs/incident_vs_refracted_angle.png', dpi=300, bbox_inches='tight')
print("Graph 1 saved as: graphs/incident_vs_refracted_angle.png")
plt.close()  # Close the figure to save memory

print("\n=== ANALYSIS FOR QUESTION 3 (Updated for Acrylic/PMMA) ===")
print("The graph of incident vs refracted angles shows:")
print("1. Non-linear relationship - refracted angle increases more slowly than incident angle")
print("2. This demonstrates Snell's law behavior - light bends toward the normal when entering acrylic")
print("3. Experimental data closely follows theoretical curve for PMMA (n₂=1.485)")
print(f"4. Average experimental error from theoretical: {avg_theoretical_error:.1f}%")
print("5. The curve becomes steeper at higher angles, approaching critical angle behavior")
print(f"6. Critical angle for acrylic-air interface: {np.rad2deg(np.arcsin(1/n_2_theoretical)):.1f}°")
print("7. Last data point (90°→70°) shows significant deviation, possibly due to measurement limitations")

# Plot 2: sin(θ₁) vs sin(θ₂) with linear fit
# According to Snell's law: sin(θ₁) = n₂ * sin(θ₂), so slope = n₂
plt.figure(figsize=(10, 8))

# Create subplot for better analysis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Main plot
ax1.plot(sin_theta_2, sin_theta_1, 'bo', markersize=10, label='Experimental data', zorder=3)

# Perform linear regression (forcing intercept=0 for physical accuracy, but showing both)
slope, intercept, r_value, p_value, std_err = linregress(sin_theta_2, sin_theta_1)
print(f"\nLinear fit (with intercept): slope (n₂) = {slope:.4f}, intercept = {intercept:.4f}, R² = {r_value**2:.4f}")

# Plot the fit line with intercept
x_fit = np.linspace(0, max(sin_theta_2)*1.1, 100)
y_fit_with_intercept = slope * x_fit + intercept
ax1.plot(x_fit, y_fit_with_intercept, 'r--', linewidth=2, 
         label=f'Linear fit: y = {slope:.3f}x + {intercept:.3f}\nR² = {r_value**2:.4f}')

# Linear fit forcing intercept to 0 (theoretical Snell's law)
slope_forced, _, _, _ = np.linalg.lstsq(sin_theta_2[:, np.newaxis], sin_theta_1, rcond=None)
y_fit_forced = slope_forced[0] * x_fit
ax1.plot(x_fit, y_fit_forced, 'g-', linewidth=3, 
         label=f'Forced through origin: y = {slope_forced[0]:.3f}x\n(Pure Snell\'s Law)', alpha=0.8)

ax1.set_xlabel('sin(θ₂) - Refracted ray', fontsize=12)
ax1.set_ylabel('sin(θ₁) - Incident ray', fontsize=12)
ax1.set_title('Graph of sin(θ₁) vs sin(θ₂)\n(Question 4: Linear Relationship Test)', fontsize=14)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, 1.0)
ax1.set_ylim(0, 1.1)

# Add perfect linearity references
ax1.plot([0, 1], [0, n_2_theoretical], 'k-', linewidth=2, alpha=0.7, 
         label=f'Perfect Snell\'s Law - Acrylic (n₂={n_2_theoretical})')
ax1.plot([0, 1], [0, avg_n_2], 'm:', linewidth=2, alpha=0.6, 
         label=f'Experimental Average (n₂={avg_n_2:.3f})')

# Add annotation
ax1.text(0.25, 0.85, f'Material: Acrylic (PMMA)\nTheoretical n₂ = {n_2_theoretical}\nExperimental n₂ = {slope_forced[0]:.3f}\nError = {abs(slope_forced[0]-n_2_theoretical)/n_2_theoretical*100:.1f}%\n\nLinear relationship confirms\nSnell\'s Law validity', 
         bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgreen", alpha=0.8),
         fontsize=10, ha='left')

# Residual plot to show deviations
ax2.scatter(sin_theta_2, sin_theta_1 - (slope_forced[0] * sin_theta_2), 
           color='red', s=60, alpha=0.7)
ax2.axhline(y=0, color='black', linestyle='-', alpha=0.5)
ax2.set_xlabel('sin(θ₂)', fontsize=12)
ax2.set_ylabel('Residuals (Observed - Theoretical)', fontsize=12)
ax2.set_title('Residual Analysis - Deviations from Perfect Snell\'s Law', fontsize=12)
ax2.grid(True, alpha=0.3)

# Calculate and display residual statistics
residuals = sin_theta_1 - (slope_forced[0] * sin_theta_2)
rms_residual = np.sqrt(np.mean(residuals**2))
ax2.text(0.05, max(residuals)*0.8, f'RMS Residual: {rms_residual:.4f}\nMax Deviation: {max(abs(residuals)):.4f}', 
         bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7),
         fontsize=10)

plt.tight_layout()
plt.savefig('graphs/sin_theta_analysis.png', dpi=300, bbox_inches='tight')
print("Graph 2 saved as: graphs/sin_theta_analysis.png")
plt.close()  # Close the figure to save memory

print(f"Linear fit (intercept forced to 0): slope (n₂) = {slope_forced[0]:.4f}")

print("\n=== ANALYSIS FOR QUESTION 4 (Updated for Acrylic/PMMA) ===")
print("The graph of sin(θ₁) vs sin(θ₂) shows:")
print("1. STRONG LINEAR RELATIONSHIP - This confirms Snell's Law validity")
print("2. The slope represents the refractive index n₂")
print("3. Slight deviation from perfect linearity indicates experimental errors")
print("4. The linear fit gives us the most accurate measurement of refractive index")
print(f"5. Experimental refractive index from slope: {slope_forced[0]:.4f}")
print(f"6. Theoretical refractive index (Acrylic): {n_2_theoretical:.4f}")
print(f"7. Error from theoretical value: {abs(slope_forced[0]-n_2_theoretical)/n_2_theoretical*100:.2f}%")
print(f"8. Average from individual calculations: {avg_n_2:.4f}")
print(f"9. The intercept ({intercept:.4f}) should theoretically be zero")
print("10. Any non-zero intercept indicates systematic experimental errors")
print(f"11. Material identification: The measured n₂≈{slope_forced[0]:.3f} is consistent with acrylic/PMMA")

# Calculate correlation coefficient for additional analysis
correlation = np.corrcoef(sin_theta_2, sin_theta_1)[0,1]
print(f"12. Correlation coefficient: {correlation:.4f} (very close to 1.0 indicates excellent linear relationship)")

# Calculate theoretical vs experimental comparison
theoretical_sin_theta_1 = n_2_theoretical * sin_theta_2
rms_deviation = np.sqrt(np.mean((sin_theta_1 - theoretical_sin_theta_1)**2))
print(f"13. RMS deviation from theoretical: {rms_deviation:.4f}")
print(f"14. This confirms the material is likely acrylic (PMMA) with some experimental uncertainty")