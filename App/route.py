from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template("index.html")


#Invalid URL
@routes.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
#Internal Server Error
@routes.errorhandler(500)
def page_error(e):
    return render_template("505.html"), 500