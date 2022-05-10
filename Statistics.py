import pandas as pd


powerbi_path ="C:/Users/paulo/Documents/trip-ad-scrap/Output_scrap_reviews/to_test_on_pbi/Coco_Bambu_rank8_DF.csv"
df = pd.read_csv(powerbi_path)
df['Words_count'] = df['SUBJECT'].str.count(' ') + 1

print(df['Words_count'].sum())
