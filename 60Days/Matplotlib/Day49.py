import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv("survey_results_public.csv")
ids = data["Responder_id"]
lang_response = data["LanguagesWorkedWith"]

language_counter = Counter()

for response in lang_response :
    language_counter.update(response.split(";"))
    
most_repeated = language_counter.most_common(10)

languages = []
popularity = []

for item in most_repeated :
    languages.append(item[0])
    popularity.append(item[1])
    
    
languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)    
plt.title("Top 10 Most Popular Languages")

plt.xlabel("No. Of People who use")

plt.tight_layout()

plt.show()