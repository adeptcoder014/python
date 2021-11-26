import pandas

def f(x):
    covid_stats=pandas.read_csv("./static/Covid_Stats.csv")
    z=covid_stats[covid_stats["Deaths"]>=float(x)]
    return  z

def filtering_through_foods():
    '''
    Filters through the given  food type passed as string
    '''
    data=pandas.read_csv("./static/project_data.csv")
    # data=data[data["Good_Food"]==x]
    return(data)

filtered_row_data=filtering_through_foods()
file=filtered_row_data[filtered_row_data["Deaths"]<=.001]
file.to_csv('least_affected1.csv',index=False)
