import streamlit as st
import effect_size
import plot_mde

st.title("Time duration tool for action-based campaign")

st.write('What is the Minimum Detectable Effect I can expect after X days?')

# UI
daily_ss_per_group = st.sidebar.slider("Select the average daily number of users per group entering the experiment", 100, 20000)
baseline_conversion_rate = st.sidebar.slider("Select the Baseline Conversion Rate in %", 1, 100)
st.sidebar.write('Effect size = Uplift divided by the standard deviation')
abs_or_rel_effect = st.sidebar.selectbox("Select effect size type", ("absolute", "relative"))

# Fixed parameters
max_lim_days = 90
power = 0.8
confidence_level = 0.95

# Run
es = effect_size.EffectSize(daily_ss_per_group=daily_ss_per_group, 
                            baseline_conversion_rate=baseline_conversion_rate,
                            max_lim_days=max_lim_days,
                            power=power,
                            confidence_level=confidence_level)

l_days = list(range(1, max_lim_days + 1))
l_ss_per_group = es.compute_cumulative_ss()
l_absolute_effect_size = es.compute_absolute_effect_size(l_ss_per_group=l_ss_per_group)
l_relative_effect_size = es.compute_relative_effect_size(l_absolute_effect_size=l_absolute_effect_size)

plot = plot_mde.PlotMDE(l_days=l_days,
                        l_absolute_effect_size=l_absolute_effect_size,
                        l_relative_effect_size=l_relative_effect_size,
                        baseline_conversion_rate=es.baseline_conversion_rate)

plot.plot_cumulative_mde(abs_or_rel_effect=abs_or_rel_effect)
st.image("mde_curve.png")



