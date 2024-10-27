#!/usr/bin/env python
# coding: utf-8

# # {How Crime Incidents in Cincinnati Vary Over Time and Across Different Neighborhoods in 2024?}📝
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# 📝 How do crime incidents in Cincinnati vary over time and across different neighborhoods? The problem I am trying to address is the impact of police response times and on crime rates in Cincinnati. One reason why many parents may worry about putting their kids for University of Cincinnati as the surrounding areas are high in crime rates and can be very dangerous. By evaluating these datasets and API, it can help local law enforcement and community stakeholders analyze the effectiveness of police operations and how resources are being allocated. With the Cincinnati Police Data Initiative dataset, we can identify trends that reveal how different types of crimes have a relationship with varied response times on different neighborhoods and time periods. For example, if longer response times are consistently involved with increased crime rates, this can highlight the areas that need additional officers or resources etc. to improve community safety. This project is meant to uncover patterns that can guide our law enforcement to make more efficient policing strategies and contribute to the overall safety and well-being of Cincinnati's residents, including UC students!!!
# 

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 With this project, I am seeking to answer the specific question: How do police response times correlate with different types of crime rates in Cincinnati. What suggestions does this relationship have for resource allocation and community safety? 
# 
# By exploring this question, I want to find out if longer response times lead to higher crime rates, identify which neighborhoods/areas are most affected, and assess the effectiveness of our current policing strategies. Also I want to understand if certain types of crimes have faster response rates or vice verse, and thus this could educate targeted civilians and cause some policy adjustments. Overall this analysis will help guide decisions on how to optimize police resources and enhance public safety and build more community trust in our law enforcement.

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 My hypothesized answer is that longer police response times are related with higher crime rates in Cincinnati. I expect to discover that areas with longer response times experience a greater number of violent crimes, like assault and robbery, compared to property crimes. And these may be less influenced by immediate and more quick police presence. Also, I believe that certain neighborhoods, particularly those with fewer police resources, will show more inequalities in crime rates related to response times. This analysis may expose that quick responses are imperative in preventing crimes and/or addressing ongoing incidents effectively. In conclusion, the findings could indicate a need for reallocating police resources to enhance response procedures in areas with high-crime.

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 5 data sources in total
# 
# Datasets (4): 
# https://data.cincinnati-oh.gov/safety/PDI-Police-Data-Initiative-Police-Calls-for-Servic/gexm-h6bt/about_data
# https://data.cincinnati-oh.gov/safety/PDI-Police-Data-Initiative-Crime-Incidents/k59e-2pvf/about_data
# https://data.cincinnati-oh.gov/safety/CPD-Reported-Shootings/sfea-4ksu/about_data
# https://data.cincinnati-oh.gov/Safety/PDI-Police-Data-Initiative-Use-of-Force/8us8-wi2w/about_data
# 
# API (1):
# https://dev.socrata.com/foundry/data.cincinnati-oh.gov/k59e-2pvf
# 
# I am going to relate these data sources by connecting the Police Calls for Service and Crime Incidents dataset by utilizing the shared timestamps and locations. This will allow us to examine how response times for different types of calls, like violent or property crimes, relate to the frequency and outcomes of incidents in the same areas.
# 
# By linking crime types from the Crime Incidents dataset with their corresponding calls for service, we can analyze how response times differ depending on the severity or nature of the crime. This will provide valuable insights into the relationship between response times and crime rates.
# 
# Also via using the geographical information from both datasets, we can conduct a neighborhood-level analysis. This will help us explore how response times and crime rates vary across different areas and assess whether these differences contribute to higher crime rates in specific neighborhoods or influence the effectiveness of police response strategies.
# 

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 My approach to answering my project question is a systematic one. I will being by starting with data preparation and analysis. That means I will clean both the Police Calls for Service and Crime Incidents datasets, to make sure fields like timestamps and location data etc are all consistent. Then move onto handling any missing or irrelevant data so it will mess up later on in the project. Next, I will merge the two datasets by matching incidents based on time and location. This will allow me to link calls for service with the corresponding crime events. When I am calculating response times for each call it will help determine the time difference between when the call was made and when the officers actually arrived on the scene. Moving on, we will analyze how response times vary for the different types of crime like violent and property crimes. Then we can use those findings to investigate patterns in how severe they were. It can also help us assess whether delays in certain areas are contributing to crime patterns or affecting police effectiveness. Then finally I will use statistical methods to explore the relationship between response times and crime outcomes more closer, like through regression modeling for instance.

# In[6]:


import pandas as pd
import requests

#accessing API for Crime Incidents data
api_url = 'https://data.cincinnati-oh.gov/resource/k59e-2pvf.json'
headers = {'Accept': 'application/json'}  #requesting JSON response
response = requests.get(api_url, headers=headers)

#check if the API call was successful
if response.status_code == 200:
    api_data = pd.DataFrame(response.json())  #load the data into a df
    print(f"API Data Loaded: {len(api_data)} records.")  #check number of records loaded
else:
    print(f"API request failed with status code: {response.status_code}")


# In[12]:


import pandas as pd

#load the Police Calls for Service dataset
calls_for_service_url = 'https://data.cincinnati-oh.gov/api/views/gexm-h6bt/rows.csv?accessType=DOWNLOAD'

#display the first five rows of the dataset
print("Police Calls for Service Data (First 5 Rows):")
print(calls_for_service_data.head())


# In[20]:


import pandas as pd

#load the Crime Incidents dataset
crime_incidents_url = 'https://data.cincinnati-oh.gov/api/views/k59e-2pvf/rows.csv?accessType=DOWNLOAD'

#display the first five rows of the dataset
print("Crime Incidents Data (First 5 Rows):")
print(crime_incidents_data.head())


# ## Checkpoint 2 

# ## Exploratory Data Analysis (EDA) & Visualization
# 
# - Produce statistical summaries of the data.
# - Analyze data distributions of the data.
# - Analyze the correlations between the data features.
# - Identify data issues.
# - Identify data types that need to be converted/transformed.
# - Provide a detailed write-up on every item above.

# In[37]:


def analyze_dataframe(df, name):
    #summary of the dataframe
    print(f"Summary of {name}:")
    print(df.info())
    print("\n")

    #statistics for the dataframe
    print(f"Statistics for {name}:")
    print(df.describe())
    print("\n")

    #number of duplicate records
    duplicate_count = df.duplicated().sum()
    print(f"Number of duplicate records in {name}: {duplicate_count}")
    
    #drop the duplicate records
    df.drop_duplicates(inplace=True)
    print(f"Duplicate records dropped from {name}.")
    print("\n")

    #check for missing values
    missing_values_count = df.isna().sum()
    print(f"Missing values in {name}:\n{missing_values_count}")
    print("\n")

#list of datasets
datasets = [data, shootings_data, use_of_force_data, calls_data]
dataset_names = ['API Data', 'Shootings Data', 'Use of Force Data', 'Calls Data']

#analyze each dataset
for i in range(len(datasets)):
    analyze_dataframe(datasets[i], dataset_names[i])


# The police incidents dataset gives us many summaries, espeically the hour_from column because it has a mean of 741 and shows significant variability meaning there is a wide range of incident times. As for the correlation analysis it is limited since there is only one numeric feature, but we can use teh categorical relationships like "offense" against hour_from to get some trends too. There is a high percentage of missing values that I want to point out; for example: victim_ethnicity and totalnumbervictims which does affect the overall analysis. Additionally there are many data types that require conversion. Some columns like longitude_x and latitude_x should be numeric but they are not, and the dates for "date_reported" should be in datetime format to be easier to work with. 
# 
# The shootings dataset has 1,490 entries, and it provides important summaries for columns like LATITUDE_X, LONGITUDE_X, and Age, with the averages for each roughly being 39.14 (lat), -84.52 (long), and 29.59 (age). When I look at the data distributions, it seems that age has a normal distribution but lattitude and longitude have some outliers. This leads me to think it would be interesting to analyze how age relates to other demographic factors like race and this data set. But this might be difficult to do since they are categorical variables. To note a few data issues, there are some missing values in columns like lattitude and sna neighborhood, but I did not find any duplicates which is good for keeping the data clean. Then for data types, I believe that the DateTimeOccurred column should be converted to a datetime format to make it easier to analyze dates and times.
# 
# The Use of Force dataset contains 21,818 entries and like the rest also posesseses various columns, including "INCIDENT_NO" and "INCIDENT_DATE." The stats show a mean latitude of about 39.13 and a mean longitude of approximately -84.52 so this give us the exact points and location context of the incidents we work with in the data set. A downside I saw right away were that there are a lot of missing values, especially in lattitude and longitude.There is over 9000 entries missing for thos two columns and this could definitely affect spatial analysis. Other missing values in the categorical columns are for instance SUBJECT_GENDER and OFFICER_GENDER. But the good thing is there are no duplicate records. I noted that for data types I had to change, the INCIDENT_DATE column needs to be converted from object to datetime for better analysis.
# 
# The Calls dataset has the most data records is what I noticed, specifically with a massive 5,626,155 entries. Some key columns being CREATE_TIME_INCIDENT and DISPOSITION_TEXT. The data has a variety of types like datetime for incident creation time and float for priority levels which I thought was unique from the others greatly. Though, the missing values in this set are significant since it is so big, like in columns PRIORITY_COLOR and SNA_NEIGHBORHOOD, where over 2 million entries are missing. This could affect my analysis related to response times and neighborhood impacts if I choose to stick with that still. The bright side is that there are no duplicate records to worry about in addition. The latitude and longitude columns show valid float values but there are still a lot of missing data points in these coordinates. To improve the dataset's accuracy, I will strongly consider filling in missing values where possible and making sure all datetime columns are correctly formatted.

# ## Data Visualizations

# In[38]:


import pandas as pd
import requests
import matplotlib.pyplot as plt

#api url for crime incidents data
api_url = 'https://data.cincinnati-oh.gov/resource/k59e-2pvf.json'

#make api request
response = requests.get(api_url)

#check if request worked
if response.status_code == 200:
    #load data into dataframe
    data = pd.DataFrame(response.json())
    print(f"loaded {len(data)} records from api")

    #check if date_reported column is there and convert to datetime
    if 'date_reported' in data.columns:
        data['date_reported'] = pd.to_datetime(data['date_reported'], errors='coerce')
        data['incident_hour'] = data['date_reported'].dt.hour

        #get top 3 neighborhoods by incidents
        top_neigh = data['cpd_neighborhood'].value_counts().head(3).index
        filtered_data = data[data['cpd_neighborhood'].isin(top_neigh)]

        #count incidents by hour and neighborhood
        hourly_incidents = filtered_data.groupby(['incident_hour', 'cpd_neighborhood']).size().unstack(fill_value=0)

        #plot line chart
        plt.figure(figsize=(10, 6))  # set figure size
        for neigh in hourly_incidents.columns:  # plot each neighborhood
            plt.plot(hourly_incidents.index, hourly_incidents[neigh], marker='o', label=neigh)

        plt.title('Incidents by Hour for Top 3 Neighborhoods')  # title of the graph
        plt.xlabel('Hour of the Day')  # x-axis label
        plt.ylabel('Incident Count')  # y-axis label

        #change x-ticks for am and pm for better time reading
        plt.xticks(range(24), [f"{(i % 12) + 1} {'am' if i < 12 else 'pm'}" for i in range(24)], rotation=45)

        plt.legend(title='Neighborhood', bbox_to_anchor=(1.05, 1))
        plt.tight_layout()
        plt.show()
    else:
        print("'date_reported' column missing")
else:
    print(f"api request failed with status: {response.status_code}")


# The graph above illustrates the relationship between incident counts and the time of day. I chose to use a line chart for this data because it effectively displays numerous points across each hour, allowing the highest counts of incidents to stand out clearly. The graph indicates that different neighborhoods experience their peak incident times at various hours. For instance, Mount Airy shows higher incident counts at night, particularly at 1 AM and 6 AM, while Westwood has more incidents in the afternoon, peaking around 3 PM. The neighborhoods with the highest counts are Mount Airy, Westwood, and West Price Hill, with each displaying distinct patterns in their incident occurrences throughout the day.

# In[39]:


import pandas as pd
import matplotlib.pyplot as plt

#load the excel file
file_path = r'C:\Users\chari\Documents\Data Tech Analytics\CPD_Reported_Shootings_20241026.csv'  
shootings_data = pd.read_csv(file_path)

#filter for just the year 2024
shootings_2024 = shootings_data[shootings_data['YearOccurred'] == 2024]

#convert the date column to datetime
shootings_2024['DateOccurred'] = pd.to_datetime(shootings_2024['DateOccurred'], format='%Y%m%d')

#add a column for month names
shootings_2024['Month'] = shootings_2024['DateOccurred'].dt.month_name()

#count shootings per month
monthly_counts_2024 = shootings_2024['Month'].value_counts().reindex([
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
])

#set up data for scatter plot
months = monthly_counts_2024.index
counts = monthly_counts_2024.values

#scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(months, counts, color='blue', alpha=0.7, s=100)  # s is point size
plt.title('Monthly Shootings Count in 2024')
plt.xlabel('Month')
plt.ylabel('Number of Shootings')
plt.xticks(rotation=45)
plt.grid(axis='y')

plt.show()


# The graph shows the number of shootings across each month of the year. I chose a scatter plot for this data because it allows us to easily spot the months with the highest shooting counts and keeping it seperate from each months. The data suggests that shootings peak in the middle of the year, with June and July showing over 40 incidents. This might be due to warmer weather, as more people are outside and interacting. In contrast, colder months like February and March have the fewest shootings, likely because people spend less time outside.

# In[14]:


import pandas as pd
import matplotlib.pyplot as plt

#load the police use of force excel
use_of_force_path = r'C:\Users\chari\Documents\Data Tech Analytics\PDI__Police_Data_Initiative__Use_of_Force_20241026.csv'

#read the dataset
use_of_force_data = pd.read_csv(use_of_force_path)

#filter for the top 5 neighborhoods with the most incidents
top_5_neighborhoods = use_of_force_data['SNA_NEIGHBORHOOD'].value_counts().nlargest(5).index
top_incidents = use_of_force_data[use_of_force_data['SNA_NEIGHBORHOOD'].isin(top_5_neighborhoods)]

#count # of use of force incidents by incident type and neighborhood
incident_counts = top_incidents.groupby(['INCIDENT_DESCRIPTION', 'SNA_NEIGHBORHOOD']).size().unstack(fill_value=0)

#clustered bar chart
fig, ax = plt.subplots(figsize=(16, 10))
incident_counts.plot(kind='bar', width=0.8, ax=ax)

#padding needed to add for better look 
plt.suptitle('Use of Force Incidents by Incident Type in Top 5 Neighborhoods', y=1.02, fontsize=16)  #main title with padding
ax.set_xlabel('Incident Type', labelpad=15)  #add padding to x-axis label
ax.set_ylabel('Number of Use of Force Incidents', labelpad=20)  #add padding to y-axis label
plt.xticks(rotation=45, ha='right')

#put legend outside
plt.legend(title='Neighborhood', bbox_to_anchor=(1.05, 1), loc='upper left')

#add extra padding around plot
plt.subplots_adjust(top=0.85, right=0.85, left=0.1, bottom=0.15)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()


# This graph shows the types of use-of-force incidents in the top five neighborhoods, highlighting how often each type occurs within these areas in Cincinnati. The most common incidents appear to be "injury to prisoner" and the use of force methods like tasers or beanbags, especially in the neighborhoods of Over-the-Rhine (OTR) and Avondale. While I don't have a clear reason for Avondale's rates, OTR has numerous bars, where alcohol-related incidents may contribute to higher use of force. I chose a clustered bar chart to clearly represent the frequency of these incidents across neighborhoods, making it easy to compare multiple incident types without losing context on neighborhood-specific differences.

# In[24]:


import pandas as pd
import plotly.express as px

#load excel file
calls_file_path = r'C:\Users\chari\Documents\Data Tech Analytics\PDI__Police_Data_Initiative__Police_Calls_for_Service.csv'

#load data
calls_data = pd.read_csv(calls_file_path, low_memory=False)

#convert incident creation time to datetime and get day of the week
calls_data['CREATE_TIME_INCIDENT'] = pd.to_datetime(calls_data['CREATE_TIME_INCIDENT'], errors='coerce')
calls_data['DAY_OF_WEEK'] = calls_data['CREATE_TIME_INCIDENT'].dt.day_name()

#group by day of the week and incident type to count #
incident_counts = calls_data.groupby(['DAY_OF_WEEK', 'INCIDENT_TYPE_ID']).size().reset_index(name='counts')

#filter for the top 5 incident types
top_incident_types = incident_counts['INCIDENT_TYPE_ID'].value_counts().nlargest(5).index
filtered_data = incident_counts[incident_counts['INCIDENT_TYPE_ID'].isin(top_incident_types)]

#day of week order for the bar chart
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
filtered_data['DAY_OF_WEEK'] = pd.Categorical(filtered_data['DAY_OF_WEEK'], categories=day_order, ordered=True)

#stacked bar chart
fig = px.bar(
    filtered_data,
    x='DAY_OF_WEEK',
    y='counts',
    color='INCIDENT_TYPE_ID',
    title='Top Incident Types by Day of the Week',
    text='counts',
    barmode='stack'
)

#readability
fig.update_layout(
    xaxis_title='Day of the Week',
    yaxis_title='Number of Incidents',
    legend_title='Incident Type',
    margin=dict(l=40, r=40, t=40, b=40)
)

fig.show()


# This graph illustrates the different types of incidents throughout the week. I used a stacked bar chart to visualize which days had the highest counts of incidents and the specific types involved. I noticed that "WAR" incidents were the most common across all days, which stands for "Weapons, Assault, and Robbery." While this term encompasses several types of incidents, it limits our ability to draw specific conclusions about the individual categories. Following WAR incidents, the next most common types are non-urgent and urgent welfare checks. I find it interesting that the incident type with the fewest occurrences shows a clear count, whereas the second least common type lacks a specific count, making it unique among the five incident types in the visualization.

# ## Data Cleaning and Transformations
# 
# - Address missing values in the dataset.
# - Address duplicate values.
# - Address anomalies and outliers.
# - Convert and transform data types
# 
# In cleaning the dataset, I first tackled the missing values, which were present in various columns like "CFS_NO" and "SUBJECT_GENDER." For columns with only a few missing entries, I decided to fill them in with the most common value, while for others with significant gaps, like "LATITUDE_X" and "LONGITUDE_X," I chose to drop those rows to maintain data integrity. I also checked for duplicate values and found that there were none, which is a relief because it means my data is clean in that regard. When looking for anomalies, I noticed some unusually high values in the "PRIORITY" column, and I'll need to investigate those further to see if they skew the analysis. Additionally, I converted the "CREATE_TIME_INCIDENT" column to a datetime format to make it easier to work with during my analysis. Overall, my cleaning process will involve filling in missing data, checking for outliers, and ensuring all data types are appropriate for analysis, helping me prepare a solid dataset for further exploration.

# ## Machine Learning Plan
# 
# Since the checkpoint 2 is now being due before the introduction to Machine Learning module, I can not complete this last criteria in the rubric for Checkpoint 2: Exploratory Data Analysis & Visualization.

# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 I have the 2 datasets the City of Cincinnati and 1 API from them as well. I might add more later on since I know there will be need for further research.

# In[1]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

