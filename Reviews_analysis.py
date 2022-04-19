#pip install google_trans_new 
#pip install --upgrade pandas
#Imports
from email import header
from operator import index
from google_trans_new import google_translator        
#from google.colab import drive 
from deep_translator import GoogleTranslator
from textblob import TextBlob
import pandas as pd
import csv
import nltk
nltk.download('stopwords')
from nltk.tokenize import TweetTokenizer
nltk.download('punkt')
import numpy as np
import time
from time import sleep
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import MaxAbsScaler
#import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
#%matplotlib inline
#from wordcloud import WordCloud, STOPWORDS #to plot word cloud 


#Reading a file with the reviews translated
file_path ='C:/Users/paulo/Documents/projects/trip-ad-scrap/Output_scrap_reviews/Restaurants_Review_Coco_Bambu_rank8_EN.csv'
path_splited = file_path.split('/')
path_to_file_en ="C:/Users/paulo/Documents/projects/trip-ad-scrap/Output_scrap_reviews/Translated_Datasets/" + path_splited[-1]

df_reviews_en = pd.read_csv(path_to_file_en)

#df_reviews = pd.read_csv(path_to_file_en)

####################################################################################################################################



# Create a function to get the subjectivity
def getSubjectivity(text):
   frase = TextBlob(text)
   return frase.sentiment.subjectivity
 

# Create a function to get the polarity
def getPolarity(text):
   frase = TextBlob(text)
   return frase.sentiment.polarity

# Function to label the analysis 
def getAnalysis(score):
  if score < 0:
    return 'Negative'
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'

# Function to label the SCORE 
def getScore_analysis(score):
  if score < 30:
    return 'Negative'
  elif score == 30:
    return 'Neutral'
  else:
    return 'Positive'
# Create two new columns 'Subjectivity' & 'Polarity'


df_reviews_en['Subjectivity'] = df_reviews_en['REVIEW_en'].apply(getSubjectivity)
df_reviews_en['Polarity'] = df_reviews_en['REVIEW_en'].apply(getPolarity)
df_reviews_en['Analysis'] = df_reviews_en['Polarity'].apply(getAnalysis)


df_reviews_en['SCORE_Analysis'] = df_reviews_en['SCORE'].apply(getScore_analysis)

# Show the new dataframe with columns 'Subjectivity' & 'Polarity'
###print(df_reviews_en[df_reviews_en.Polarity == 0])


#Normalizing SCORE and POLARITY to match the same proportions
#df = df_reviews_en['SCORE']
#scaler = MaxAbsScaler()
#scaler.fit(df)
#scaled = scaler.transform(df)
#scaled_df = pd.DataFrame(scaled, columns=['SCORE'])

#print(scaled)
#df_reviews_en = df_reviews_en[df_reviews_en.Analysis != df_reviews_en.SCORE_Analysis] #PAY ATTENTIOOOOON

df = df_reviews_en.reset_index(drop=True)
print(df) 

#Definindo função para normalizar por min_max
def min_max_scaling(series):
    return (series - series.min()) / (series.max() - series.min())

#Definindo colunas para serem normalizadas
columns_to_scale = ('SCORE','Polarity')
for col in columns_to_scale:
    df[col] = min_max_scaling(df[col])
#Tratando normalização da Polarity. Arredondado para duas casas decimais
df['Polarity'] = df['Polarity'].fillna(0.5)
df['Polarity'] = round(df['Polarity'],2)
print(df)    
print(df['SCORE'].max())
#print(df['SCORE_N'].min())      
print(df['Polarity'].max())


powerbi_path ="C:/Users/paulo/Documents/trip-ad-scrap/Output_scrap_reviews/to_test_on_pbi/Coco_Bambu_rank8_DF_n1.csv"
csvFile = open(powerbi_path, 'a', encoding="utf-8")
df.to_csv(powerbi_path)


#csvFile = open(powerbi_path, 'a', encoding="utf-8")
#csvWriter = csv.writer(csvFile)
#csvWriter.writerows(df)



value1 = df['SCORE'] 
value2 = df['Polarity']
value3 = df['SCORE'] - df['Polarity']

#results1 = pd.DataFrame({'SCORE': value1, 'Polarity': value2, 'S/P':value3})
results1 = pd.DataFrame({'SCORE': value1, 'Polarity': value2})
results1.plot()
plt.legend(loc='lower right')
plt.xlabel("index")
plt.ylabel("test2")
plt.show()