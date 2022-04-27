
# Fossil Fuel Project - Consumption/Production Report
Reported by: Craig Calzado  - 
Codeup - Innis Cohort - April 27, 2022

---
  
## Project Overview

---
 
#### 1. Goals:
- Identify any patterns in fossil fuel production and consuption in the United States.
- Determine the trend of the yearly consumption/production of fossil fuels.
- Perdict the Consumption/Production of Fossil Fuel for the next 6 years.

--- 
 
#### 2. Description:
Working as a independent data scientist, the Codeup Instructor has come to me and asked for insight in terms of the fossil fuel for the next six years. He is in need of a better understanding othe trends and the future of fossil fuels in the United States.

--- 
 
#### 3. Initial Questions:
- What is the trend of the consumption of fossil fuels monthly and yearly?
- What is the trend of the production of fossil fuels monthly and yearly?
- What does the next six years of consumption/production of fossil fuels look like?
---
  
#### 4. Defined Deliverables:
- README file - provides a better understanding of the project
- Workbooks - Draftings of explored areas and conclusions drawn for the original data
- wrangle.py - provides reproducible code to automate acquiring and preparing the data
- explore.py - provides code to explore the data
- models.py - provides code to build the model
- Final Report - provides final presentation-ready wrangle and findings 

---

#### 5. Data Dictionary:
The final DataFrame used to explore the data for this project contains the following variables (columns).  The variables, along with their data types, are defined below:
 
|  Variables             |    Definition                              |    DataType             |
| :--------------------:   | :----------------------------------------: | :--------------------: |
|date (index) | Date order was placed |  datetime64[ns] |
|total_fossil_fuels_production_monthly | Value of fossil fuel production | object |
|total_fossil_fuels_consumption_monthly | Value of fossil fuel consumption | datetime64[ns] |

---

## PROJECT PLAN - USING THE DATA SCIENCE PIPELINE:
The following outlines the process taken through the Data Science Pipeline to complete this project. 
 
Plan➜ Acquire ➜ Prepare ➜ Explore ➜ Evaluate ➜ Deliver
 
#### 1. PLAN
- [x] Define the project goal
- [x] Determine proper format for the audience
- [x] Asked questions that would lead to final goal
- [x] Define an MVP

 
#### 2. ACQUIRE
- [x] Create a function to pull appropriate information from the zillow database
- [x] Create and save a wrangle.py file in order to use the function to acquire
 
#### 3. PREPARE

- [x] Import functions from wrangle.py module
- [x] Drop duplicate columns that are deemed unneccessary
- [x] Assign order_date as datetime
- [x] Set index as order_date for time series analysis
- [x] Create any new columns that are considered usable for a deeper dive into the data
 
#### 4. EXPLORE
Using Jupyter Notebook:
- [x] Answer key questions about hypotheses and find the best customer segment in regards to
- [x] Run at least two statistical tests
- [x] Document findings
- [x] Create visualizations with the intent to discover variable relationships
- [x] Identify variables related to customer segments and _________
- [x] Identify any potential data integrity issues
- [x] Summarize conclusions, provide clear answers, and summarize takeaways
- [x] Explain plan of action as deduced from work to this point
 
#### 5. EVALUATE
- [x] Identify believed areas of growth 
- [x] Establish appropriate statistcial tests to reinforce findings
- [x] Interpret and document findings
 
#### 6. DELIVERY
- [x] Include an introduction of the project and goals
- [x] Provide an executive summary of findings, key takeaways, recommendations, and rationale
- [x] Create a walkthrough of the analysis 
- [x] Provide final takeaways, recommend a course of action, and next steps
- [x] Be prepared to answer questions following the presentation
- [x] Prepare final notebook in Jupyter Notebook
- [x] Create clear walk-though of the Data Science Pipeline using headings and dividers
- [x] Explicitly define questions asked during the initial analysis
- [x] Visualize relationships
- [x] Document takeaways

---
  
## Reproducibility:
### Steps to Reproduce:
1. Have your env file with proper credentials saved to the working directory
2. Ensure that a .gitignore is properly made in order to keep privileged information private
3. Clone repo from github to ensure availability of the acquire and prepare imports
4. Ensure pandas, numpy, matplotlib, scipy, sklearn, and seaborn are available
5. Follow steps outline in this README.md to run final_fossil_fuel_report.ipynb

---

## KEY TAKEAWAYS:

### Conclusion: 
Looking at a month to month cycle the production of fossil fuels has a steady trend unlike the consumption of fossil fuels. The consumption of fossil fuels on a month to month cycle is seasonality peaking consumption in the summer and winter months. If we look at the yearly trends, the production of fossil fuels is at an exponential increase while the consumption of fossil fuels on a yearly cycle is steadily trending down. I utilized 9 models to determine the best model for predicting the production and consumption of fossil fuels. The previous year model was the best for predicting the consumption of fossil fuels and the Holt 15/12 model was the best for predicting the production of fossil fuels. Both models were able to predict the production and consumption of fossil fuels with a rmse in the 300's nearly half the oppsoing.


#### The goals of this project were to:
- Identify any patterns in fossil fuel production and consuption in the United States.
- Determine the trend of the consumption of fossil fuels.
- Perdict the Consumption/Production of Fossil Fuel for the next 6 years.

#### Recommendation(s)/Observation(s):
 - As production of fossil fuels increase and the consumption of fossil fuels decrease, we may see a decline in the price of fossil fuels.
 - The consumption of fossil fuels on a monthly cycle is seasonality peaking consumption in the summer and winter months may be due to A/C and Heating.
 - Find alternative energy sources for the summer and winter months.
 - The production of fossil fuels will continue to increase through the years 2022-2028.
 - There is steady decline in the consumption of fossil fuels through the years 2022-2028.

#### Next Steps:
With more time, I would like to:

 - Look into other fuel types and compare the trends of fossil fuels.
 - Look into how to improve the impact of profit by individual products

---

 ## References:

If you have any questions, please contact me at: craig.a.calzado@gmail.com 

Subject line: "Fossil Fuel Project" (note: anything else will be ignored)






