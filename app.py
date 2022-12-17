from utils import *

from flask import Flask, render_template

data = load_candidates_from_json()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("list.html", items=data)


@app.route('/candidate/<int:x>')
def get_candidate(x):
    candidate = get_candidate_by_id(x, data)
    return render_template("single.html", candidate=candidate)


@app.route('/search/<candidate_name>')
def search(candidate_name):
    candidates = get_candidates_by_name(candidate_name, data)
    candidates_count = len(candidates)
    return render_template("search.html", candidates_count=candidates_count,
                           candidates=candidates)


@app.route('/skill/<skill_name>')
def get_skill(skill_name):
    candidates = get_candidate_by_skill(skill_name, data)
    candidates_count = len(candidates)
    return render_template("skill.html", count=candidates_count,
                           candidates=candidates, skill=skill_name)


if __name__ == '__main__':
    app.run(debug=True)
