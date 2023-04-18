import numpy as np
import matplotlib.pyplot as plt


class PlotMDE:
    def __init__(self, 
                l_days,
                l_absolute_effect_size,
                l_relative_effect_size,
                baseline_conversion_rate):
        self.l_days = l_days
        self.l_absolute_effect_size = l_absolute_effect_size
        self.l_relative_effect_size = l_relative_effect_size
        self.baseline_conversion_rate = baseline_conversion_rate

    def plot_cumulative_mde(self, abs_or_rel_effect='absolute'):
    
        if abs_or_rel_effect=='relative':
            l_effect_size = self.l_relative_effect_size
        else:
            l_effect_size = self.l_absolute_effect_size
            
        plt.plot(self.l_days, l_effect_size)
        plt.title(f'''What is the Minimum Detectable Effect I can expect after X days 
                    and a baseline conversion rate of {round(self.baseline_conversion_rate)}%?''')
        plt.xlabel("Days")
        if abs_or_rel_effect=='relative':
            plt.ylabel("Relative effect size")
        else:
            plt.ylabel("Absolute effect size")
            
        l_x_y = []
        for x, y in zip(self.l_days, l_effect_size):
            l_x_y.append((x, y))
        coordinates = [l_x_y[i] for i in np.arange(0, len(self.l_days), 10)]
        
        for couple in coordinates:
            label = str(round(couple[1] * 100, 1)) + '%'
            plt.annotate(label,
                        couple,
                        textcoords='offset points',
                        xytext=(0, 2),
                        ha='left')
        
        plt.savefig("mde_curve.png")
        