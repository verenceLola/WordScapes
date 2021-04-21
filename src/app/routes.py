from ..domain import WordChecker
import enchant
from collections import defaultdict
from flask import Blueprint, Response, request, jsonify

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/", methods=("POST",))
def english_words():
    if request.method == "POST":
        json_data = defaultdict(lambda: None)
        json_data.update(request.get_json())

        letters = json_data["letters"]
        min_word_length = json_data["min_word_length"]
        max_word_length = json_data["max_word_length"]

        dictionary = enchant.Dict("en_US")

        if not letters:
            return jsonify({"error": "missing letters data"}), 400

        checker = WordChecker(
            dictionary=dictionary,
            letters=letters,
            min_word_length=min_word_length,
            max_word_length=max_word_length,
        )
        english_words = checker.find_words()

        return jsonify(english_words)
