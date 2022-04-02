df = df_reviews_en
print(df) 
#def absolute_maximum_scale(series):
#    return series / series.abs().max()
'''columns_to_scale = 'SCORE'
for col in columns_to_scale:
    df[col] = absolute_maximum_scale(df[col])
    print(col)'''
#df['SCORE_N'] = absolute_maximum_scale(df['SCORE'])

def min_max_scaling(series):
    return (series - series.min()) / (series.max() - series.min())

columns_to_scale = ('SCORE','Polarity')
for col in columns_to_scale:
    df[col] = min_max_scaling(df[col])