from dm_recommendation_engine import UserRecommendationGenerator

feature_matrix_a = [
    [0,0,1,0,1],
    [1,0,0,0,0],
    [1,1,0,1,0],
    [0,0,1,1,1]
]

feature_matrix_b = [
    [1,1,0,1,0,0],
    [0,0,1,0,1,1],
    [0,0,1,1,0,0],
    [1,0,1,1,1,1]
]
rating = [4,5,5,5]
r = UserRecommendationGenerator()
r.train(rating,feature_matrix_a,feature_matrix_b)

print("Result:", r.predict([1,1,1,1,1],[1,1,1,1,1,1]))