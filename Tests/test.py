from movie_recomendation_engine import ContentBasedRecommendationEngine

import pandas as pd

data = pd.read_csv("movie_data.csv")

rn = ContentBasedRecommendationEngine()

rn.train(data)

print(len(rn._r))
print(len(rn._r[0]))

print(rn.predict(552,10))
