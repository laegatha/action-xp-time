import streamlit as st
import delta_days_calculator
import stats_days_plot

st.title("Time duration tool for action-based campaign")

st.write('What is the Minimum Detectable Effect I can expect after X days?')

# UI
daily_ss_per_group = st.sidebar.slider("Select the average daily number of users per group entering the experiment", 100, 20000)
baseline_conversion_rate = st.sidebar.slider("Select the Baseline Conversion Rate in %", 1, 100)
abs_or_rel = st.sidebar.selectbox("Select uplift type", ("absolute", "relative"))

# Fixed parameters
max_lim_days = 90
power = 0.8
confidence_level = 0.95

# Run
dd = delta_days_calculator.DeltaDays(daily_ss_per_group=daily_ss_per_group, 
                                    max_lim_days=max_lim_days,
                                    baseline_conversion_rate=baseline_conversion_rate,
                                    confidence_level=confidence_level,
                                    power=power)

l_days = list(range(1, max_lim_days + 1))
l_ss_per_group = dd.compute_cumulative_ss()
l_absolute_delta = dd.compute_absolute_delta(l_ss_per_group=l_ss_per_group)
l_relative_delta = dd.compute_relative_delta(l_absolute_delta=l_absolute_delta)

sdp = stats_days_plot.StatsDaysPlot()
sdp._plot_cumulative_mde(baseline_conversion_rate=baseline_conversion_rate,
                     l_days=l_days,
                     l_absolute_delta=l_absolute_delta,
                     l_relative_delta=l_relative_delta,
                     abs_or_rel=abs_or_rel)

st.image("mde_curve.png")



