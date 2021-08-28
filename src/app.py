from detoxify import Detoxify
from flask import Flask
import classyjson as cj

with open("config.json", "r") as config_file:
    CONFIG = cj.load(config_file)

detox_model = Detoxify("original")
app = Flask(__name__)


@app.route("/analyze/<string:text>")
def analyze(text: str):
    return {"toxicity": detox_model.predict(text)}


if __name__ == "__main__":
    app.run(host=CONFIG.host, port=CONFIG.port, debug=CONFIG.debug)
