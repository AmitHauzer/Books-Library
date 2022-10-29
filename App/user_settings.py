from datetime import date
from flask import flash, render_template, request, redirect, Blueprint, g, url_for
from App.login import login_required



settings_bp = Blueprint('settings', __name__, url_prefix='/settings')