from detoxify import Detoxify
from flask import Flask
import classyjson as cj

with open("config.json", "r") as config_file:
    CONFIG = cj.load(config_file)

detox_model = Detoxify("original")
app = Flask(__name__)


def float32_to_float_ify(d: dict) -> dict:
    return {k: float(v) for k, v in d.items()}


@app.route("/analyze/<string:text>")
def analyze(text: str):
    return {"toxicity": float32_to_float_ify(detox_model.predict(text))}


if __name__ == "__main__":
    app.run(host=CONFIG.host, port=CONFIG.port, debug=CONFIG.debug)
