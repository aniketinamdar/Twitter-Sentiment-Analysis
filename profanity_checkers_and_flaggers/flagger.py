import pandas as pd
tweet = 'asshole is the cuntlicker motherfucker bender ' #replace with get tweet
flags  = []
bad_words_dict = pd.read_csv('profanity_en.csv')
for index, row in bad_words_dict.iterrows():
    if (tweet.find(row['text']) != -1):
        if type(row['category_1']) != float and row['category_1'] not in flags:
            flags.append(row['category_1'])
        if type(row['category_2']) != float and row['category_2'] not in flags:
            flags.append(row['category_2'])
        if type(row['category_3']) != float and row['category_3'] not in flags:
            flags.append(row['category_3'])
print(flags)

