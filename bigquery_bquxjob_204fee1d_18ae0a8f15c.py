# -*- coding: utf-8 -*-
"""BigQuery bquxjob_204fee1d_18ae0a8f15c

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/bigquery_job.ipynb
"""

# @title Setup
from google.colab import auth
from google.cloud import bigquery
from google.colab import data_table

project = 'lustrous-acumen-399315' # Project ID inserted based on the query results selected to explore
location = 'US' # Location inserted based on the query results selected to explore
client = bigquery.Client(project=project, location=location)
data_table.enable_dataframe_formatter()
auth.authenticate_user()

"""## Reference SQL syntax from the original job
Use the ```jobs.query```
[method](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query) to
return the SQL syntax from the job. This can be copied from the output cell
below to edit the query now or in the future. Alternatively, you can use
[this link](https://console.cloud.google.com/bigquery?j=lustrous-acumen-399315:US:bquxjob_204fee1d_18ae0a8f15c)
back to BigQuery to edit the query within the BigQuery user interface.
"""

# Running this code will display the query used to generate your previous job

job = client.get_job('bquxjob_204fee1d_18ae0a8f15c') # Job ID inserted based on the query results selected to explore
print(job.query)

"""# Result set loaded from BigQuery job as a DataFrame
Query results are referenced from the Job ID ran from BigQuery and the query
does not need to be re-run to explore results. The ```to_dataframe```
[method](https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.job.QueryJob.html#google.cloud.bigquery.job.QueryJob.to_dataframe)
downloads the results to a Pandas DataFrame by using the BigQuery Storage API.

To edit query syntax, you can do so from the BigQuery SQL editor or in the
```Optional:``` sections below.
"""

# Running this code will read results from your previous job

job = client.get_job('bquxjob_204fee1d_18ae0a8f15c') # Job ID inserted based on the query results selected to explore
results = job.to_dataframe()
results

"""## Show descriptive statistics using describe()
Use the ```pandas DataFrame.describe()```
[method](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
to generate descriptive statistics. Descriptive statistics include those that
summarize the central tendency, dispersion and shape of a dataset’s
distribution, excluding ```NaN``` values. You may also use other Python methods
to interact with your data.
"""

results.describe()

import pandas as pd
import matplotlib.pyplot as plt

# Sample data from the provided table
data = pd.DataFrame({
    'purchaser': [False] * 25,
    'user_count': [1371, 357, 6, 3, 238, 1084, 181, 11, 4, 53, 36, 274, 7, 19, 17, 21, 261, 898, 46, 45, 16, 18, 9, 25, 41],
    'geo_country': ['United States', 'United States', 'Argentina', 'Iceland', 'India', 'United States', 'Canada',
                    'United Arab Emirates', 'United Arab Emirates', 'Spain', 'Spain', 'India', 'Ireland', 'Ireland',
                    'Ireland', 'South Korea', 'United States', 'United States', 'France', 'France', 'France',
                    'France', 'Egypt', 'Japan', 'Japan'],
    'traffic_source': ['google', 'shop.googlemerchandisestore.com', '(direct)', '<Other>', '<Other>', '<Other>',
                       '<Other>', 'google', '(direct)', 'google', '(direct)', 'google', '(data deleted)', 'google',
                       '(direct)', '(direct)', '(data deleted)', '(direct)', '(direct)', '<Other>', '(data deleted)',
                       'shop.googlemerchandisestore.com', 'google', '<Other>', 'google']
})

# Grouping data by 'geo_country' and 'traffic_source' and summing up 'user_count'
grouped_data = data.groupby(['geo_country', 'traffic_source'])['user_count'].sum().reset_index()

# Sorting data by 'user_count' in descending order
grouped_data.sort_values(by='user_count', ascending=False, inplace=True)

# Plotting the data
plt.figure(figsize=(12, 6))
plt.barh(grouped_data['geo_country'] + ' (' + grouped_data['traffic_source'] + ')', grouped_data['user_count'], color='skyblue')
plt.xlabel('User Count')
plt.ylabel('Geo Country (Traffic Source)')
plt.title('User Count by Geo Country and Traffic Source')
plt.gca().invert_yaxis()  # Reverse the order to display the highest user count at the top
plt.tight_layout()

# Show the plot
plt.show()

# Interpretation of the graph
print("Interpretation of the User Count by Geo Country and Traffic Source:")
for idx, row in grouped_data.iterrows():
    print(f"Geo Country: {row['geo_country']}, Traffic Source: {row['traffic_source']}")
    print(f"User Count: {row['user_count']}")
    print("=" * 30)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = pd.DataFrame({
    'purchaser': [False, False, False, False, False, False, False, False, False, False,
                  False, False, False, False, False, False, False, False, False, False,
                  False, False, False, False, False],
    'user_count': [1371, 357, 6, 3, 238, 1084, 181, 11, 4, 53, 36, 274, 7, 19, 17, 21, 261, 898, 46, 45,
                   16, 18, 9, 25, 41],
    'geo_country': ['United States', 'United States', 'Argentina', 'Iceland', 'India', 'United States', 'Canada',
                    'United Arab Emirates', 'United Arab Emirates', 'Spain', 'Spain', 'India', 'Ireland', 'Ireland',
                    'Ireland', 'South Korea', 'United States', 'United States', 'France', 'France', 'France',
                    'France', 'Egypt', 'Japan', 'Japan'],
    'traffic_source': ['google', 'shop.googlemerchandisestore.com', '(direct)', '<Other>', '<Other>', '<Other>',
                       '<Other>', 'google', '(direct)', 'google', '(direct)', 'google', '(data deleted)', 'google',
                       '(direct)', '(direct)', '(data deleted)', '(direct)', '(direct)', '<Other>', '(data deleted)',
                       'shop.googlemerchandisestore.com', 'google', '<Other>', 'google']
})

# Create box plots for purchasers segmented by geo country
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, x='geo_country', y='user_count', hue='purchaser')
plt.xlabel('Geo Country')
plt.ylabel('User Count')
plt.title('Box Plot of User Count for Purchasers by Geo Country')
plt.xticks(rotation=90)
plt.tight_layout()

# Create box plots for purchasers segmented by traffic source
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, x='traffic_source', y='user_count', hue='purchaser')
plt.xlabel('Traffic Source')
plt.ylabel('User Count')
plt.title('Box Plot of User Count for Purchasers by Traffic Source')
plt.xticks(rotation=90)
plt.tight_layout()

# Filter data for non-purchasers
non_purchasers_data = data[data['purchaser'] == False]

# Create box plots for non-purchasers segmented by geo country
plt.figure(figsize=(12, 6))
sns.boxplot(data=non_purchasers_data, x='geo_country', y='user_count')
plt.xlabel('Geo Country')
plt.ylabel('User Count')
plt.title('Box Plot of User Count for Non-Purchasers by Geo Country')
plt.xticks(rotation=90)
plt.tight_layout()

# Create box plots for non-purchasers segmented by traffic source
plt.figure(figsize=(12, 6))
sns.boxplot(data=non_purchasers_data, x='traffic_source', y='user_count')
plt.xlabel('Traffic Source')
plt.ylabel('User Count')
plt.title('Box Plot of User Count for Non-Purchasers by Traffic Source')
plt.xticks(rotation=90)
plt.tight_layout()

# Show the plots
plt.show()