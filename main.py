import streamlit as st
import delta_days_calculator
import stats_days_plot

st.title("How Long Should I run my A/B Test?")
st.markdown('''Minimum detectable effect (MDE) is a calculation that estimates the smallest improvement 
            that is significant. It determines how "sensitive" an experiment is.''')
st.markdown('Common business _"Rule of Thumb"_: stop the experiment when _MDE = 1.5pp (absolute)_.')

# UI
st.sidebar.markdown("![Alt Text](https://media2.giphy.com/media/3owzW5c1tPq63MPmWk/giphy.gif?cid=ecf05e47fy9o4eytgxvhyea5wl7z3793403ij439nuk89hox&rid=giphy.gif&ct=g)")

st.sidebar.markdown('Step 1: Average Daily Number of Users')
daily_n = st.sidebar.number_input("What is the daily number of users coming into the experiment (control & test)?", 
                                  value=5000, min_value=100)
st.sidebar.markdown('Step 2: Baseline Conversion Rate')
baseline_conversion_rate = st.sidebar.number_input("What is the conversion rate of the control group?", 
                                             value=50, min_value=1, max_value=99)
st.sidebar.markdown('Step 3: Absolute vs. Relative')
abs_or_rel = st.sidebar.selectbox("Do you want to display the absolute or the relative uplift?", ("absolute", "relative"))
st.sidebar.markdown('"absolute" refers to the uplift in percentage points: $\ p2 - p1$')
st.sidebar.markdown('"relative" refers to the uplift in percentage terms: $\ (p2 - p1)/p1 * 100$')

st.sidebar.markdown('_Confidence level = 95%_')
st.sidebar.markdown('_Power of the test = 80%_')

# Fixed parameters
max_lim_days = 40
power = 0.8
confidence_level = 0.95

# Run
dd = delta_days_calculator.DeltaDays(daily_ss_per_group=daily_n / 2, 
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

st.markdown(f'''After :blue[_7 days_], the control and the test groups are populated by :blue[_{int(l_ss_per_group[6])} 
            users each_] and the MDE is equal to :green[{round(l_absolute_delta[6] * 100, 1)}pp (absolute) / 
            {round(l_relative_delta[6] * 100, 1)}% (relative).]''')

st.markdown(f'''After :blue[_14 days_], the control and the test groups are populated by :blue[_{int(l_ss_per_group[13])} 
            users each_] and the MDE is equal to :green[{round(l_absolute_delta[13] * 100, 1)}pp (absolute) / 
            {round(l_relative_delta[13] * 100, 1)}% (relative).]''')

st.markdown(f'''After :blue[_30 days_], the control and the test groups are populated by :blue[_{int(l_ss_per_group[29])} 
            users each_] and the MDE is equal to :green[{round(l_absolute_delta[29] * 100, 1)}pp (absolute) / 
            {round(l_relative_delta[29] * 100, 1)}% (relative).]''')



