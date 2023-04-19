import numpy as np
from replica_powerproptest_r import Power


class DeltaDays:
    def __init__(self,
                 daily_ss_per_group,
                 max_lim_days,
                 baseline_conversion_rate,
                 confidence_level,
                 power):
        self.daily_ss_per_group = daily_ss_per_group
        self.max_lim_days = max_lim_days
        self.baseline_conversion_rate = baseline_conversion_rate * 0.01
        self.confidence_level = confidence_level
        self.power = power
        self.po = Power()

    def compute_cumulative_ss(self) -> list:
        return np.cumsum([self.daily_ss_per_group] * self.max_lim_days)

    def compute_absolute_delta(self, l_ss_per_group) -> list:
        return [self.po._compute_delta(p1=self.baseline_conversion_rate,
                                       n=ss,
                                       alpha=1-self.confidence_level,
                                       beta=1-self.power) for ss in l_ss_per_group]

    def compute_relative_delta(self, l_absolute_delta: list) -> list:
        return [x / self.baseline_conversion_rate for x in l_absolute_delta]
