from flask import Flask, render_template

import utils


data = r"data\candidates.json"
candidates = utils.load_candidates_from_json(data)


app = Flask(__name__)


@app.route("/")  # Представление главной страницы
def page_list():
    return render_template("list.html", all=candidates)


@app.route("/candidate/<int:x>")   # Представление страницы кандидата по id
def single_page(x):
    single_card = utils.get_candidate(candidates, x)
    return render_template("single.html", single=single_card)


@app.route("/search/<string:candidate_name>")  # Представление кандидата по имени
def candidate_skill(candidate_name):
    for_result = utils.get_candidates_by_name(candidates, candidate_name.lower())
    count_user = len(for_result)
    return render_template("search.html", coincidences=for_result, count=count_user)


@app.route("/skill/<skill_name>")  # Представление кандидатов по скиллу
def get_by_skill(skill_name):
    for_result = utils.get_candidates_by_skill(candidates, skill_name.lower())
    count_user = len(for_result)
    return render_template("skill.html", candidates=for_result, count=count_user, skill=skill_name)


app.run(host='127.0.0.1', port=5000)
