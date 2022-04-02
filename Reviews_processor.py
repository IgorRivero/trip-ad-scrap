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
file_path ='C:/Users/paulo/Documents/trip-ad-scrap/Output_scrap_reviews/Restaurants_Review_Coco_Bambu_Meireles_rank4.csv'
path_to_file_en ="C:/Users/paulo/Documents/trip-ad-scrap/Output_scrap_reviews/Translated_Datasets/Restaurants_Review_Coco_Bambu_Meireles_rank4.csv"
#path_to_file_en_full_df ="C:/Users/paulo/Documents/trip-ad-scrap/Output_scrap_reviews/Translated_Datasets/full_df/Restaurants_Review_Coco_Bambu_Iguatemi_rank1_EN.csv"


df_reviews = pd.read_csv(file_path, names=collumn_names, header=None)



#Translating Reviews to EN
#Defining function to translate PT to EN
def translate_(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text) 
    time.sleep(2)
    return translated

#Translating each review row
#Creating a new file to save the translated review collumn
# open the file to save the review
csvFile = open(path_to_file_en, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
header = ['DATE','SCORE','SUBJECT','REVIEW','REVIEW_en']
#first way to save the translated review
csvWriter.writerow(header)
for i in range(len(df_reviews)):
    df_reviews['REVIEW_en'] = df_reviews.iloc[[i]]['REVIEW'].apply(translate_)
    #df_reviews = df_reviews.append(['REVIEW_en'], ignore_index=True)
    print(f"Line {i} translated")

    csvWriter.writerow(df_reviews.iloc[i])
    #time.sleep(2)
    
    #print(df_reviews.iloc[[i]])

'''#second way to save the translated review
df_reviews['REVIEW_en'] = df_reviews['REVIEW'].apply(translate_)
df_reviews.to_csv(path_to_file_en_full_df, encoding='utf-8', index=False)
#df_reviews.to_csv('fileRestaurants_Review_Coco_Bambu_Iguatemi_rank1_EN.csv_name', sep='\t', encoding='utf-8')
print(df_reviews)'''
csvFile.close()

time.sleep(2)

df_reviews_en_re = pd.read_csv(path_to_file_en).head()
#df_reviews = pd.read_csv(path_to_file_en)
print(df_reviews_en_re)
#print(len(df_reviews))
#print(translate_('ola mundo'))