import numpy as np
import pandas as pd
# importing some libraries for visulizations
import matplotlib.pyplot as plt
from itertools import cycle, islice
#import seaborn as sns
import matplotlib
import pandas as pd


# Importing the dataset
UnemploymentGenderAge = pd.read_csv('./DatasetsCsv/Labor_market_statistics_UnemploymentGenderAge.csv',encoding='latin-1')
UnemploymentGenderAge=UnemploymentGenderAge.set_index('Year')
UnemploymentGenderAge=UnemploymentGenderAge.rename(index=str, columns={"Juveniles under 20 years":"Juveniles_under_20_years",
                                                                                               "Younger people under 25 years":"Younger_people_under_25_years",
                                                                                               "55 years and over":"over_55",
                                                                                               "Long-term unemployed":"Long_term_unemployed",
                                                                                               "Severely disabled persons":"Severely_disabled_persons"})

by_age=pd.DataFrame({'Male': UnemploymentGenderAge.Male,
                     'Female':UnemploymentGenderAge.Female,}, index=UnemploymentGenderAge.index)  

ax=by_age.plot(x=None, y=None, kind='line', ax=None, subplots=False, sharex=None, sharey=False, 
               layout=None,use_index=True, grid=True, legend=True, style=None, 
                 yticks=None, xlim=None, ylim=None,colormap=None)
plt.title('Unemployment by gender'  )
plt.xlabel('Years')
plt.ylabel('Number of Unemplyed')


by_age=pd.DataFrame({'Male': UnemploymentGenderAge.Male,
                     'Female':UnemploymentGenderAge.Female,}, index=UnemploymentGenderAge.index)  

ax=by_age.plot(x=None, y=None, kind='line', ax=None, subplots=False, sharex=None, sharey=False, 
               layout=None,use_index=True, grid=True, legend=True, style=None, 
                 yticks=None, xlim=None, ylim=None,colormap=None)
plt.title('Unemployment by gender'  )
plt.xlabel('Years')
plt.ylabel('Number of Unemplyed')




