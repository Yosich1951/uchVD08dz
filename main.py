from flask import Flask, render_template, request
import requests

#импортируем объект класса Flask
app = Flask(__name__)

# цитата
def get_quota():
    url = "https://api.quotable.io/random"
    # для получения результата нам понадобится модуль requests
    response = requests.get(url)
    # прописываем формат возврата результата
    # получить список со статьями.
    return response.json()

@app.route('/')
def home():
    quote = get_quota()
    return render_template('index.html', content=quote['content'])

if __name__ == '__main__':
   app.run(debug=True)
