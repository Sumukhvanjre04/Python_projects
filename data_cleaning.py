import json

def load_data(filename):
    with open(filename,"r") as f:
        data=json.load(f)
    return data

data=load_data(r"D:\Prime AIML\Data pre processing\data_store.json")
print("The uncleaned data:")
for user in data:
       print(json.dumps(user, indent=4))


#clean and structure the data
def clean_data(data):
    text_to_num={"one":1,"two":2,"three":3,"four":4,"five":5}
    cleaned_data=[]
    unique_users=set()
    for user in data:
        raw_rating=str(user["rating"]).strip().lower()
        if raw_rating in text_to_num:
            raw_rating=text_to_num[raw_rating]
        user["rating"]=raw_rating
        
        if "age" not in user:
            user["age"]=None
      
        if user["name"].strip() in unique_users:
            continue
        unique_users.add(user["name"])
        cleaned_data.append(user)
       
    return cleaned_data

new_data=clean_data(data)
print("________________________________________________________________________________________")
print("The cleaned data:")
for data in new_data:
    print(json.dumps(data,indent=4))

#getting meaningful insights from data
print("________________________________________________________________________________________")
print("We are getting meaningful insights from the cleaned data.")
def insight_data(new_data):
    rating_data=[]
    poor_rating=[]
    for data in new_data:
        rating_data.append(float(data["rating"]))
    #print(rating_data)
    avg_rating=(sum(rating_data))/len(rating_data)
    print(f"\n1.The average rating is {avg_rating}")
    
    for rating in rating_data:
        if rating<3:
            poor_rating.append(float(rating))
    percent=(len(poor_rating)/len(rating_data))*100     
    print(f"2.The percentage of users rated below 3 is {percent}%") 
  
insight_data(new_data)


#building the recommendation feature
print("_________________________________________________________________________________________")
print("Now, we are building the recommendation features")
print("\nIf the user rating >= 4, we recommend the Samsung brand otherwise we recommend Apple brand\n")
def get_recommendations(new_data):
    recommendations=[]
    for user in new_data:
        curr_recomm={}
        curr_recomm["name"]=user["name"]
        if float(user["rating"])>=4:
            curr_recomm["brand"]="Samsung"
        else:
            curr_recomm["brand"]="Apple"
        recommendations.append(curr_recomm)
    return recommendations

rec=get_recommendations(new_data)
for user in rec:
    print(user)
