from flask import Flask, request, render_template, redirect, url_for,flash,get_flashed_messages
import os, datetime
from .config.variables import SECRET_KEY

def blog():
    blog = Flask(__name__)

    # CONFIG
    blog.config["SECRET_KEY"] = SECRET_KEY  # ENCRYPTION FOR OUR SESSIONS

    # BLUEPRINT
    from .views.admin_auth import admin
    blog.register_blueprint (admin, url_prefix="/owner")

    # ERROR ROUTES

    # 404 ERROR
    @blog.errorhandler(404)
    def error_404(error):
        print("404 ERROR:", str(error))
        return render_template("error-404.html")
    
    # 500 ERROR
    @blog.errorhandler(Exception)
    def error_500(error):
        print("500 ERROR:", str(error))
        return render_template("error-500.html")

    return blog