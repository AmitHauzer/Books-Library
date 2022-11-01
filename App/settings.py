from datetime import date
from flask import flash, render_template, request, redirect, Blueprint, g, session, url_for
from App.Data.data import change_user_pass, get_an_object_from_db_with_id
from App.login import admin_login_required, login_required
from werkzeug.security import check_password_hash



settings_bp = Blueprint('settings', __name__, url_prefix='/settings')

@settings_bp.route('/')
@login_required
def settings():
    user = get_an_object_from_db_with_id(table='Users', id_pk=session.get('user_id'))
    return render_template('settings/settings.html', user=user)






@settings_bp.route('/changepassword', methods=['GET','POST'])
@login_required
def change_pass():
    user = get_an_object_from_db_with_id(table='Users', id_pk=session.get('user_id'))
    error = {
            'current_pass': None,
            'new_pass': None,
        }
    
    if request.method == "POST":
        current_pass = request.form.get('current_pass')
        new_pass = request.form.get('new_pass')
        confirm_pass = request.form.get('confirm_pass')
        
        # debug
        if not check_password_hash(user['password'], current_pass):
            error['current_pass'] = 'The current password is incorrect.'
            return render_template('settings/change_pass_form.html', user=user, error=error)
        elif new_pass != confirm_pass:
            error['new_pass'] = 'The passwords are not the same.'
            return render_template('settings/change_pass_form.html', user=user, error=error)
        # try to change pass
        else:
            try:
                change_user_pass(password=new_pass, id_pk=user['id'])
                flash('The password has been changed.')
            except Exception as ex:
                print(ex)
                flash(f'{ex}', category="error")

    return render_template('settings/change_pass_form.html', user=user, error=error)






@settings_bp.route('/changepermissions', methods=['GET','POST'])
@login_required
@admin_login_required
def admin_change_permissions():

    # only admin can see this option.
    
    return 'permissions'