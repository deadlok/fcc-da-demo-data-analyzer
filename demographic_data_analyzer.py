import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    #print(df.columns)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    s1 = pd.Series(1, index=df.loc[:,'race'])
    race_count = s1.groupby(level=0).count()
    
    # What is the average age of men?
    df_male = df[df.loc[:,'sex']=='Male']
    average_age_men = round(df_male.loc[:,'age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    df_bachelors = df[df.loc[:,'education']=='Bachelors']
    bachelors_cnt = df_bachelors.shape[0]
    total_cnt = df.shape[0]
    percentage_bachelors = round(bachelors_cnt / total_cnt * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    df_higher = df[df.loc[:,'education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    df_lower = df[~df.loc[:,'education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education = round(df_higher.shape[0] / df.shape[0] *100, 1)
    lower_education = round(df_lower.shape[0] / df.shape[0] *100, 1)

    # percentage with salary >50K
    #print(df_higher.drop_duplicates('salary'))
    df_higher_rich = df_higher[df_higher.loc[:,'salary'] == '>50K']
    df_lower_rich = df_lower[df_lower.loc[:,'salary'] == '>50K' ]
    higher_education_rich = round(df_higher_rich.shape[0] / df_higher.shape[0] *100, 1)
    lower_education_rich = round(df_lower_rich.shape[0] / df_lower.shape[0] *100, 1)

    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.loc[:,'hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_min_hours = df.loc[ df.loc[:,'hours-per-week'] == min_work_hours ]
    num_min_hours = df_min_hours.shape[0]

    df_high_salary_min_hours = df_min_hours[df_min_hours.loc[:,'salary'] == '>50K']
    num_high_salary_min_hours = df_high_salary_min_hours.shape[0]

    rich_percentage = round(num_high_salary_min_hours/num_min_hours*100, 1)

    # What country has the highest percentage of people that earn >50K?
    df_rich = df[df.loc[:,'salary']=='>50K']
    s_country = pd.Series(1,index=df.loc[:,'native-country']).groupby(level=0).count()
    s_country_rich = pd.Series(1,index=df_rich.loc[:,'native-country']).groupby(level=0).count()
    s_rich_percentage = round(s_country_rich / s_country * 100, 1)
    #print(s_rich_percentage)

    highest_earning_country = s_rich_percentage.idxmax()
    highest_earning_country_percentage = s_rich_percentage.max()

    # Identify the most popular occupation for those who earn >50K in India.
    df_rich_india = df[ (df.loc[:,'salary']=='>50K') & (df.loc[:,'native-country']=='India')]
    s_rich_occupation = pd.Series(1,index=df_rich_india.loc[:,'occupation']).groupby(level=0).count()
 
    top_IN_occupation = s_rich_occupation.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
