from flask import Flask, request, abort
from detoxify import Detoxify
import classyjson as cj
import functools

with open("config.json", "r") as config_file:
    CONFIG = cj.load(config_file)

detox_model = Detoxify("original-small")
app = Flask(__name__)


@functools.lru_cache(maxsize=CONFIG.max_cache_size)
def analyze_text(text: str):
    return {k: float(v) for k, v in detox_model.predict(text).items()}


@app.route("/analyze/<string:text>")
def analyze_endpoint(text: str):
    auth = request.headers.get("authorization")

    if auth != CONFIG.auth:
        abort(401)

    return analyze_text(text)


if __name__ == "__main__":
    app.run(host=CONFIG.host, port=CONFIG.port, debug=CONFIG.debug)
