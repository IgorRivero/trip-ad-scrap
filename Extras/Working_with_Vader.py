import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer



sent = SentimentIntensityAnalyzer()

powerbi_path ="C:/Users/paulo/Documents/trip-ad-scrap/Output_scrap_reviews/to_test_on_pbi/Coco_Bambu_rank8_DF_n1.csv"

df = pd.read_csv(powerbi_path)
polarity = [sent.polarity_scores(i)['compound'] for i in df['REVIEW_en']]
df['vader_score'] = polarity
print(df)


####################################FLAIR################



#Definindo função para normalizar por min_max
def min_max_scaling(series):
    return (series - series.min()) / (series.max() - series.min())

#Definindo colunas para serem normalizadas

df['vader_score'] = min_max_scaling(df['vader_score'])

#Tratando normalização da Polarity. Arredondado para duas casas decimais
df['vader_score'] = df['vader_score'].fillna(0.5)
df['vader_score'] = round(df['vader_score'],2)

print(df[['Polarity','vader_score']])    


#CALCULANDO A MEDIA PONDERADA
#Mp1 40/60
#Mp2 30/70
#Mp3 20/80
weight_Score = 0.4
weight_Comment = 0.6

df['Mp1'] = round(((df['SCORE']*weight_Score) + (df['Polarity']*weight_Comment))/(weight_Score + weight_Comment),2)

weight_Score = 0.3
weight_Comment = 0.7

df['Mp2'] = round(((df['SCORE']*weight_Score) + (df['Polarity']*weight_Comment))/(weight_Score + weight_Comment),2)

weight_Score = 0.2
weight_Comment = 0.8

df['Mp3'] = round(((df['SCORE']*weight_Score) + (df['Polarity']*weight_Comment))/(weight_Score + weight_Comment),2)




print(df.head())
powerbi_path2 ="C:/Users/paulo/Documents/trip-ad-scrap/Output_scrap_reviews/to_test_on_pbi/Coco_Bambu_rank8_DF.csv"
csvFile = open(powerbi_path2, 'a', encoding="utf-8")
df.to_csv(powerbi_path2)