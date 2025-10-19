import matplotlib.pyplot as plt

m_Fe = 0.1579  # Mass of iron, kg
m_aqua = 0.4066  # Mass of water in calorimeter, kg
m_Cu = 0.1065  # Mass of internal container (copper) of calorimeter, kg
T_1 = 24.1  # Initial temperature of calorimeter, °C
T_2 = 27.2  # Final temperature of calorimeter + iron, °C
c_aqua = 4200  # Heat capacity of water, J/kg°C
c_Cu = 386  # Heat capacity of copper, J/kg°C
c_Fe_theoretical = 450  # Theoretical specific heat of iron, J/kg°C

# Calculate experimental specific heat of iron
if T_2 != T_1 and m_Fe != 0:
    c_Fe_experimental = ((m_aqua * c_aqua + m_Cu * c_Cu) * (T_2 - T_1)) / (m_Fe * (100 - T_2))
else:
    c_Fe_experimental = 0

# Data for chart
labels = ['Experimental', 'Theoretical']
values = [c_Fe_experimental, c_Fe_theoretical]

# Create bar chart
bars = plt.bar(labels, values, color=['#FF6B6B', '#4ECDC4'])

# # Set y-axis to a narrower range to highlight the difference
# plt.ylim(450, 475)

# Add horizontal grid lines to show y values clearly
plt.grid(True, axis='y', linestyle='-', alpha=0.3)

# Add value labels on top of bars
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
             f'{value:.1f}', ha='center', va='bottom', fontweight='bold')

# Add horizontal lines at the value heights for better comparison
for i, value in enumerate(values):
    plt.axhline(y=value, color=bars[i].get_facecolor(), 
                linestyle='--', alpha=0.7, linewidth=1)

plt.ylabel('Specific Heat (J/kg°C)')
plt.title('Comparison of Specific Heat of Iron')
plt.tight_layout()
plt.show()