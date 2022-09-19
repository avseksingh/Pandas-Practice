# import json
#
# # Opening JSON file
# with open('candidate_json_data.json') as json_file:
#     data = json.load(json_file)
#
#     # Print the type of data variable
#     print("Type:", type(data))
#
#     # Print the data of dictionary
#     print("\nPeople1:", data['people1'])
#     print("\nPeople2:", data['people2'])

# import json
# # json1_file = open('candidate_json_data.json')
# # json1_str = json1_file.read()
# # # json1_data = json.loads(json1_str)
#
# with open('F:\\Pandas-Practice\\ProjectDataExtractionandTextAnalysis\\candidate_json_data.json', 'r') as f:
#   data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
# print(data)
# person = open(candidate_json_data.json)
# person_dict = json.loads(person)

import json

# Opening JSON file
f = open('jsonfile.json')
print(json.loads(f))

# returns JSON object as
# a dictionary
# data = json.load(f)

# Iterating through the json
# list
# for i in data['emp_details']:
#     print(i)

# Closing file
f.close()