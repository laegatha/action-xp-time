import numpy as np
import matplotlib.pyplot as plt


class StatsDaysPlot:
    def __init__(self):
        pass

    @staticmethod
    def _plot_cumulative_mde(baseline_conversion_rate: float,
                             l_days: list,
                             l_absolute_delta: list,
                             l_relative_delta: list,
                             abs_or_rel='absolute'):
    
        if abs_or_rel=='relative':
            l_delta = l_relative_delta
        else:
            l_delta = l_absolute_delta
            
        plt.plot(l_days, l_delta)
        plt.title(f'''What is the Minimum Detectable Effect I can expect after X days 
                    and a baseline conversion rate of {round(baseline_conversion_rate)}%?''')
        plt.xlabel("Days")
        if abs_or_rel=='relative':
            plt.ylabel("Relative Uplift")
        else:
            plt.ylabel("Absolute Uplift")
            
        l_x_y = []
        for x, y in zip(l_days, l_delta):
            l_x_y.append((x, y))
        coordinates = [l_x_y[i] for i in np.arange(0, len(l_days), 10)]
        
        for couple in coordinates:
            label = str(round(couple[1] * 100, 1)) + '%'
            plt.annotate(label,
                        couple,
                        textcoords='offset points',
                        xytext=(0, 2),
                        ha='left')
        
        plt.savefig("mde_curve.png")
        