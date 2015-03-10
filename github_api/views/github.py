from functools import wraps
from flask import redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github

github_blueprint = make_github_blueprint(
    client_id="in_env_variable",
    client_secret="in_env_variable",
    scope="user:email,user:follow",
    redirect_to="myrepos.index")


def require_github_login(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        if github.authorized:
            print("IDIDIDDIDID")
            return view(*args, **kwargs)
        else:
            return redirect(url_for("github.login"))

    return decorated_view



