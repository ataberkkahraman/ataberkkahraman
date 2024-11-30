# FitnessData-DSA210Project

## Project Overview

Over the next three months, I’ll be diving deep into how my daily habits impact my one-rep max Bench Press performance. By analyzing factors like caloric intake, protein, carbohydrates, creatine consumption, sleep (both duration and quality), and body weight, I aim to uncover which habits drive the best results. Using data visualization and statistical tools, I’ll explore patterns and test whether specific tweaks to my routine can lead to measurable improvements.

The plan is simple: track my daily routines, correlate them with my Bench Press performance, and test hypotheses about what really makes a difference. Ultimately, I want this project to provide actionable insights to optimize my training and nutrition strategies.

---

## Objectives

1. **Understand Performance Influencers**  
   Explore the relationship between caloric intake, protein, carbohydrates, creatine, sleep patterns, body weight, and Bench Press performance.

2. **Identify Key Factors**  
   Pinpoint which variables have the strongest impact and develop a targeted approach to maximize strength gains.

3. **Data-Driven Optimization**  
   Use insights from the analysis to fine-tune my daily habits and consistently improve performance.

4. **Apply Data Science Skills**  
   Bring the concepts I’ve learned in my DSA 210 course into real-world application, enhancing my understanding of data analysis and visualization.

---

## Motivation

This project combines two passions of mine: fitness and data science. Here’s why it matters:

- **Personal Growth**  
  Fitness is more than a hobby; it’s a lifestyle. Learning how my habits impact my physical performance will help me improve in and out of the gym.
  
- **Scientific Approach**  
  I want my progress to be driven by data, not guesswork. This project gives me the tools to analyze and refine my approach.
  
- **Practical Application**  
  It’s a chance to apply the theoretical knowledge I’ve gained in class to a meaningful, hands-on project.
  
- **Long-Term Impact**  
  The findings won’t just improve my Bench Press—they’ll help me become better at approaching fitness and other goals scientifically.

---

## Dataset

The dataset for this project consists of three months of daily records. Here’s what I’ll be tracking:

- **Date**: The specific day of the record  
- **Calories**: Total caloric intake (kcal)  
- **Protein**: Amount of protein consumed (grams)  
- **Carbohydrates**: Amount of carbohydrates consumed (grams)  
- **Creatine**: Amount of creatine consumed (grams)  
- **Sleep Duration**: Total sleep duration (hours)  
- **Sleep Quality**: Self-rated sleep quality (scale of 1–10)  
- **Body Weight**: My body weight recorded daily (kg)  
- **Bench Press (1RM)**: My one-rep max Bench Press performance (kg)  
- **Day Difficulty**: A self-assessed rating of how challenging the day was (scale of 1–10).  

I’ll log all of this daily in an Excel file, ensuring consistent and accurate data collection. Outliers caused by illness, injuries, or significant routine changes will be flagged for review.

---

## Tools and Technologies

I’ll rely on the following tools for data analysis and visualization:

- **Python**: For data cleaning and statistical analysis  
- **Pandas**: To manipulate and preprocess data  
- **Matplotlib and Seaborn**: For creating visualizations (scatter plots, heatmaps, time series)  
- **SciPy**: For hypothesis testing and regression analysis  

---

## Analysis Plan

1. **Data Collection**  
   - Import daily Excel records into a Pandas DataFrame and preprocess the data by handling missing values and standardizing units.  

2. **Visualization**  
   - Use scatter plots, heatmaps, and time series plots to explore relationships between variables.  
   - Examples include:  
     - Scatter plot of protein intake vs. Bench Press performance  
     - Heatmap showing correlations between all variables  
     - Time series plot comparing performance trends over three months  

3. **Hypothesis Testing**  
   - Test hypotheses like:  
     - **H₀**: Daily habits have no effect on Bench Press performance.  
     - **Hₐ**: One or more daily variables significantly impact Bench Press performance.  
   - Run regression analysis to identify the strongest predictors of progress.

4. **Trend Analysis**  
   - Investigate patterns in performance over time, identifying peaks or plateaus.  
   - Analyze how body weight fluctuations and day-to-day difficulty ratings correlate with performance trends.

---

## Example Analysis

To illustrate, I’ll create a scatter plot to visualize the relationship between protein intake and Bench Press performance. The x-axis will represent daily protein intake (grams), and the y-axis will show my Bench Press 1RM (kg). If there’s a clear upward trend, it might suggest a strong correlation between protein consumption and strength gains.

Another example involves comparing performance on high-difficulty days (e.g., Day Difficulty = 8–10) versus low-difficulty days (e.g., Day Difficulty = 1–3). This could reveal how mental and physical stress impacts strength.

Similarly, I’ll look at body weight trends over time to see if changes in weight correlate positively or negatively with Bench Press performance. For example, if a steady weight gain coincides with performance improvements, it might indicate that my caloric and macronutrient intake is supporting strength gains.

---

## Conclusion

By the end of this project, I hope to answer the following questions:

- Which lifestyle habits most influence my Bench Press performance?  
- Can small, data-driven tweaks to my routine lead to measurable improvements?  
- How does body weight fluctuation play a role in performance?  
- How can I apply these insights to other fitness goals?

This isn’t just about improving my Bench Press; it’s about leveraging data science to unlock better results in every aspect of life. Whether it’s fitness, productivity, or learning, understanding the numbers behind performance is key to success.

---

I’m excited to see what the data reveals—and to turn this project into a roadmap for smarter, more effective training!
