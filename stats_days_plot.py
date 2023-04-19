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
        
        plt.style.use('dark_background')
        plt.plot(l_days, l_delta, color='grey')
        plt.suptitle(f'Minimum Detectable Effect after X days', fontsize=14, color='#90EE90', fontweight='bold')
        plt.title(f'Baseline Conversion Rate: {round(baseline_conversion_rate)}%', fontsize=10, color='grey', style='italic', fontweight='bold')
        plt.xlabel("Days")
        if abs_or_rel=='relative':
            plt.ylabel("Relative Uplift")
        else:
            plt.ylabel("Absolute Uplift")
            
        l_x_y = []
        for x, y in zip(l_days, l_delta):
            l_x_y.append((x, y))
        coordinates = [l_x_y[i] for i in np.arange(0, len(l_days), 5)]
        
        # display values for every 5 days
        for couple in coordinates:
            label_mde = str(round(couple[1] * 100, 1)) + '%'
            plt.annotate(label_mde,
                        couple,
                        textcoords='offset points',
                        xytext=(0, 2),
                        ha='left',
                        color='#90EE90',
                        fontweight='bold')
        
        # hide y axis labels
        ax = plt.gca()
        ax.set_yticks([])
        # hide top and right spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        # color in grey the axis
        ax.xaxis.label.set_color('grey')
        ax.yaxis.label.set_color('grey')
        ax.tick_params(axis='x', colors='grey')
        ax.spines['bottom'].set_color('grey')
        ax.spines['left'].set_color('grey')
        
        plt.savefig("mde_curve.png")
        