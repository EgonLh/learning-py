from collectionData import CollectData

question = "What is Your Major?";
data_collection = CollectData(question=question);

data_collection.show_question()

print("Enter q at anytime to quit.\n")
while True:
    response = input ("Major :");
    if response == 'q':
        break
    data_collection.store_response(response)
    
##Showing the result
print("\n Thanks for the participating")
data_collection.show_result();