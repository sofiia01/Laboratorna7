import requests

response = requests.get('https://api.chucknorris.io/jokes/categories')
categories = response.json()

print("List of categories: ")
for category in categories:
    print(category)
category = input("Enter a category: ")
url = 'https://api.chucknorris.io/jokes/random?category=' + category
response = requests.get(url)
joke = response.json()

print("Category: ", category)
print("Data: ", joke['created_at'])
print("Anecdote: ", joke['value'])