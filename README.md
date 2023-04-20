# action-xp-time
> A self-service statistical tool for business  

<img src="https://media2.giphy.com/media/f3jZ8moRBbEvNJjOtu/giphy.gif?cid=ecf05e472zvedh6hp53wa0hqxaf46bnnljx3a8wot1viuor7&rid=giphy.gif&ct=g" align="right" width="280">

_**"How long should I run my A/B test?"**_ is asking a CRM Manager.  
I remember how many time this question was resulting in too much inefficient workload for both side. Getting the different specifications from the business to finally run the famous `power.prop.test` function on R to compute either the sample size or the uplift we can detect.

[action-xp-time](https://action-xp-time.streamlit.app/) is an A/B test time duration tool built with [Streamlit](https://streamlit.io/) and hosted on the Community Cloud. It computes the **Minimum Detectable Effect (MDE)** after X days for a given baseline conversion rate. The MDE is a calculation that estimates the smallest improvement that is statistically significant. It determines how "sensitive" an experiment is.

# How do I use this tool?

 Go to the sidebar on the left and follow the steps: 
* **Step 1:** fill in the **average daily number of users** entering your experiment (control & test).
* **Step 2:** fill in the **baseline conversion rate** you observed in the past for your specific audience.
* **Step 3:** select **"absolute"** if you want to observe the uplift in percentage points or **"relative"** for in percentage terms.  
  
An example with parameters selected by default:
* Step 1: **5000 users** per day are meeting the requirements of our experiment and can be targeted by our campaign.
* Step 2: We observed in the past for this segment of users that the **conversion rate is equal to 50%**.
* Step 3: We want to observe the difference between the test group conversion rate and the control group conversion rate in percentage points.   
We select **"absolute"**. _Which is better, absolute or relative change?_ [See here](#which-is-better-absolute-or-relative-change)  

# How do I read the results?

You end up with this graph bellow. _What do we see?_  
* **Every 5 days** the MDE value is displayed. In our example case, after 10 days we will be able to detect a significant uplift of 1.2pp.
* Below the graph they are 3 help sentences describing the MDE and the number of users in the experiment **after 7, 14 & 30 days**.

<img src="mde_curve.png" align="center" width="500">  
  
 * After <span style="color:blue">_7 days_</span>, the control and the test groups are populated by <span style="color:blue">_17500 users each_</span> and the MDE is equal to <span style="color:green">1.5pp (absolute) / 3.0% (relative).</span>
 * After <span style="color:blue">_14 days_</span>, the control and the test groups are populated by <span style="color:blue">_35000 users each_</span> and the MDE is equal to <span style="color:green">1.1pp (absolute) / 2.2% (relative).</span>
 * After <span style="color:blue">_30 days_</span>, the control and the test groups are populated by <span style="color:blue">_75000 users each_</span> and the MDE is equal to <span style="color:green">0.7pp (absolute) / 1.4% (relative).</span>

# How to deploy your webapp on Streamlit Community Cloud?

<img src="https://media3.giphy.com/media/3o8doT5DaMjfH3paHC/giphy.gif?cid=ecf05e47z4e0d2uzm9tlllh7kpj2euzgrdmm1w9ds8iwxs3g&rid=giphy.gif&ct=g">


# What are the Statistics behind?

# Which is better, absolute or relative change?


