from flask import Blueprint, render_template, redirect, url_for, flash

from .github import require_github_login, github


myrepos = Blueprint("myrepos", __name__)


@myrepos.route("/", defaults={"page": 1})
@myrepos.route("/page/<int:page>")
#@require_github_login
def index(page):

    resp = github.get("/user/repos?page={}".format(page))

    return render_template("index.html",
                           repos=resp.json())




