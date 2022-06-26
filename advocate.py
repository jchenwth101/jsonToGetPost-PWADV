

import requests
import json

headers = {"token":"eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJqb2VsLmNoZW5vd2V0aCIsImlhdCI6MTY1NjExMjgzNiwiZXhwIjoxNjU2NjQ3OTk5fQ.MBl7kniRAx5Gtv0QzpUkBh8f89vveSJjZN0Dfxyk3uBpo1t8-Wv--GpNm2OEYjQX2WGAeaZjDpOgAj1bxNNnvd4-X0xXwuwqRcS3Bwvk2zpeIx30bSwaTVE-fUFb7UYScEBfiuhaoGHOex8M-MPEd7Htu9RQEg_BkMd4cEReV7wpl8k8ge79cAMw7f5AYzP7TrfPSVPQnyl3P8ouKhtlUWuE-rMkNZQfnStdCdLigmB_-HW71sDjDevjlSeusKwtOpZvQFOL_s8H8ZHcPIeziQF1QV24ZfBT_BHvjuJID8ubo0vC567mWwcKXX9Y0FApnAyIdAku5aoRJsJPiQx2yddHpzlLt69YAe-vAAeUFtc_Du71B_KKkDejkMMsG6qgHp4o8QFBcZEek8Zb7Qk0eLrsk2nm1ttDJAtE25MI0C8iZEmvQPYkerhIwAUeOyQUEKbdRfDE3cX4Ch-LHyKUdHOGJI0_2Sy318QSQh9OeR-N5DeVykjAK4VvLP4XRs0XbsfioJeed9R0uyIMpbXgq7kqV-_2FgnbhgRX8ObTQ65Ppz8xqhxd04tNdmV7agIUUZmzHHuMHmcGInrt2kQIPkIJO1I3Ww3AO_GzJ1oBAcRAfg5ElWMKQ3q-GwTxoCcrPRm-ozvfspdRkT02qAk-3H6H4FziLFOjjk_8XiXIdLY"}

r = requests.get('https://pa-kobayashi-test.herokuapp.com/getProblems', headers=headers)
# r.status_code
# data = r.json
# print(data)
print("original JSON data: ")
print("----------------------------------------------")
print(r.text)
print(r.url)
print("----------------------------------------------")
print()
print()
# r.text = data
# print(data)
# f = open('data.json',)

# # returns JSON object as 
# # a dictionary
# data = json.load(f)
# print(data)
   
# Iterating through the json
# list
# for i in data:
#     print(i)
   
# Closing file
# # f.close()
# python_obj = r.text
# print(python_obj)

results = []
results_json = {'solution': results}

json_obj = json.loads(r.text)['data']
for index, list_item in enumerate(json_obj):
    print(index, list_item)
    if list_item['operator'] == "+":
        result = list_item['operand1'] + list_item['operand2']
    if list_item['operator'] == "*":
        result = list_item['operand1'] * list_item['operand2']
    elif list_item['operator'] == "-":
        result = list_item['operand1'] - list_item['operand2']
    
    print(result)
    results.append(result)
    
    #if index == 10:
    #    break

url = 'https://pa-kobayashi-test.herokuapp.com/submitAnswers'
response = requests.post(url, headers=headers, json=results_json)
print(response.text)

# print(json_obj['data'][0:1])
# x = json_obj.values("operand1")
# print(x.value())


# for value in json_obj:
#     x="operand1"
#     y="operand2"
#     if "operator"=="-":
#         result = x - y
#     print(result)


# def findResult(json_obj):
#     for item in json_obj:
#         x="operand1"
#         y="operand2"
#         if "operator"=="-":
#             result = x - y
#             print(result)
#         elif "operator"=="+":
#             result = x + y
#             print(result)
#         elif "operator"=="*":
#             result = x * y
#             print(result)
#             return result
# print(findResult(json_obj))





# print("\nUnique Key in a JSON object:")


# for x in json_obj.items():
#     if operator == "*":
    
    
   

