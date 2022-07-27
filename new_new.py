import json
def train(as_of_date, countries, categories):
    args=locals()
    #args["as_of_date"] == "as_of_date_value"
    #args["countries"] == "countries_value"
    #args["categories"] == "categories_value"
    print(args)
    args = json.dumps(args)
    print(args)
 

if __name__ == "__main__":
    train("03/08/1999","Brazil","man")