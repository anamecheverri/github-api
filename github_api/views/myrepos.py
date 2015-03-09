from flask import Blueprint, render_template, redirect, url_for, flash

from .api_login import require_github_login, github


myrepos = Blueprint("myrepos", __name__)


@myrepos.route("/", defaults={"page": 1})
@myrepos.route("/page/<int:page>")
def index(page):
    resp = github.get("/user/repos?page={}".format(page))

    #paginator = Paginator(resp, page)

    return render_template("index.html",
                           #paginator=paginator,
                           repos=resp.data)


