import numpy as np
import requests
import csv

url = 'https://td2020-static.s3.amazonaws.com/glove.6B.50d.txt'
r = requests.get(url)

open('glove.6B.50d.txt', 'wb').write(r.content)

from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file = 'glove.6B.50d.txt'
word2vec_output_file = 'glove.6B.50d.txt.word2vec'
glove2word2vec(glove_input_file, word2vec_output_file)

from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)

with open('walmartscrapes (1-25).csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} ------> {row[1]}')
            line_count += 1
    print(f'Processed {line_count} lines.')


doc1desc = "The proven classic. With a legacy over 50 years in the making, it's the most scientifically researched and game-tested way to replace electrolytes lost in sweat. Gatorade Thirst Quencher is specifically made to help keep you hydrated, which is why it's trusted by some of the world's best athletes. Don't count the days. Make the days count. Grab your home workout equipment then refuel and replenish during your at-home workout with the carbs and electrolytes from Gatorade Thirst Quencher. When you sweat, you lose more than water. Gatorade Thirst Quencher contains critical electrolytes to help replace what's lost in sweat. Top off your fuel stores with carbohydrate energy, your body's preferred source of fuel. Tested in the lab and used by the pros. Cool Blue flavor Includes (12) 12 oz bottles Gatorade bottles are recyclable"
doc2desc = "Each family'size box of Honey Nut Cheerios breakfast cereal has the irresistible taste of golden honey and natural almond flavor that your whole family will enjoy. Made with 100% whole grain oats, each serving of little O's contains .75 grams of soluble fiber, which may reduce the risk of heart disease when paired with a diet low in saturated fat and cholesterol. Pour a bowl of this gluten-free cereal for breakfast, or pack it in a to-go container for a fun kids' snack. Either way, the honey-sweet taste of Cheerios makes every bowl un-bee-lievably tasty. BREAKFAST CEREALS: Sweetened Whole Grain oat cereal with real honey and natural almond flavor, Good source of iron and calcium HEART HEALTHY: *Three grams of soluble fiber daily from Whole Grain oat foods, like Honey Nut Cheerios cereal, in a diet low in saturated fat and cholesterol, may reduce the risk of heart disease. Honey Nut Cheerios cereal provides .75 grams per serving WHOLE GRAIN: First ingredient is Whole Grain and contains 12 essential Vitamins an"
doc3desc = "Deluxe edition includes six bonus tracks. Two CD collection. This just in-the album you wait for every year! Find the encouragement you need to stand firm in your faith and shine God's light with this cutting-edge collection of 30 chart-topping hits. It's guaranteed to be on constant replay as you take every lyric to heart-and in years to come, it'll bring back all your favorite memories of 2018!.Various Artists - WOW Hits 2018 (Various Artists) - CD"

corpusNames = ["Gatorade", "Honey Nut Cheerios", "WOW Hits 2018 CD"]
corpusDesc = [doc1desc, doc2desc, doc3desc]
query = "sports drink"

def clean(doc):
    # remove stop words (the, a)
    # lematizing
    # stemming
    doc = ''.join([char if str.isalpha(char) else ' ' for char in doc.lower()]).split()
    return [word for word in doc if word in model.wv.vocab]

print(model.n_similarity(clean(query), clean(doc1desc)))
print(model.n_similarity(clean(query), clean(doc2desc)))
print(model.n_similarity(clean(query), clean(doc3desc)))

def search(query, corpus):
    sim = lambda doc1, doc2: model.n_similarity(clean(doc1), clean(doc2))
    return np.argmax([sim(query, doc) for doc in corpus])

#@title Walmart Search
query = "sports drink" #@param {type:"string"}
if query:
    idx = search(query, corpusDesc)
    print('Matched Product:', corpusNames[idx])
    match_doc = corpusDesc[idx]
    print('Similar Product:', corpusNames[search(match_doc, [doc2desc, doc3desc])])
