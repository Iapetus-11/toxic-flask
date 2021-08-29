from flask import Flask, request, abort
from detoxify import Detoxify
import classyjson as cj

with open("config.json", "r") as config_file:
    CONFIG = cj.load(config_file)

detox_model = Detoxify("original")
app = Flask(__name__)


@app.route("/analyze/<string:text>")
def analyze(text: str):
    auth = request.headers.get("authorization")

    if auth != CONFIG.auth:
        abort(401)

    return {k: float(v) for k, v in detox_model.predict(text).items()}


if __name__ == "__main__":
    app.run(host=CONFIG.host, port=CONFIG.port, debug=CONFIG.debug)
