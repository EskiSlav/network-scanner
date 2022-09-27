import os
from flask import Flask
import requests

app = Flask(__name__)

TOKEN = os.environ.get("API_TOKEN")
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

@app.route('/send_message/<int:user_tg_id>/<text>')
def send_message(user_tg_id, text):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, user_tg_id)
    print(url)
    return get_url(url)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8082)