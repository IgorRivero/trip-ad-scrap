#pip install google_trans_new 
#pip install --upgrade pandas
#Imports
from email import header
from google_trans_new import google_translator        
#from google.colab import drive 
from deep_translator import GoogleTranslator
from textblob import TextBlob
import pandas as pd
import csv
import nltk
#nltk.download('stopwords')
from nltk.tokenize import TweetTokenizer
#nltk.download('punkt')
import numpy as np
import time
from time import sleep
#import seaborn as sns
#import matplotlib.pyplot as plt
#%matplotlib inline
#from wordcloud import WordCloud, STOPWORDS #to plot word cloud


#READING FILES
collumn_names = ['DATE','SCORE','SUBJECT','REVIEW']
file_path ='C:/Users/paulo/Documents/trip-ad-scrap/Output_scrap_reviews/Restaurants_Review_Coco_Bambu_Iguatemi_rank1.csv'
path_splited = file_path.split('/')
path_to_file_en ="C:/Users/paulo/Documents/trip-ad-scrap/Output_scrap_reviews/Translated_Datasets/" + path_splited[-1]
path_to_file_en_full_df ="C:/Users/paulo/Documents/trip-ad-scrap/Output_scrap_reviews/Translated_Datasets/full_df/Restaurants_Review_Coco_Bambu_Iguatemi_rank1_EN.csv"


#df_reviews = pd.read_csv(path_to_file_en).head()
#path_to_file_en = 
print(path_splited[-1])
print(path_to_file_en)