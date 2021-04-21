from ..domain import WordChecker
import enchant

from flask import Blueprint, Response, request, jsonify

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/", methods=("GET",))
def english_words():
    if request.method == "GET":
        dictionary = enchant.Dict("en_US")
        checker = WordChecker(dictionary=dictionary, letters="cipth")
        english_words = checker.find_english_words()

        return jsonify(english_words)
