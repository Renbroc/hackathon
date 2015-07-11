
# Change example to your application name
from renbroc import app

from .models import *

from flask.ext.admin import Admin, BaseView, expose

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from flask.ext.security import login_required, current_user, roles_required



renbroc_admin = Blueprint('renbroc_admin', __name__, url_prefix='/renbroc_admin')


# Add admin to running app
admin = Admin(app, name='Renbroc Admin')


class SecureModelView(ModelView):
    """
    Makes sure admin areas require logins from authorized users.
    """

    def is_admin(self):
        """
        Makes user is an administrator. 
        """
        # Temporarily comment out before the 'and' if you need to manually create the first admin
        return current_user.is_authenticated() and current_user.has_role('Admin')

    def _handle_view(self, name, **kwargs):
        if not self.is_admin():
            return redirect(url_for('index'))



class UserView(SecureModelView):
    """
    Extends SecureModelView for User mongo collection
    """
    can_delete = False
    column_default_sort = ('email', True)
    column_exclude_list = ('password', 'last_login_at', 'last_login_ip')
    form_excluded_columns = ('password')
    #column_sortable_list = ('email', 'first_name', 'last_name', 'current_login_at')
    column_filters = ('email', 'first_name', 'last_name', 'active')

    # Form columns order not working??!?
    form_columns = ('email', 'first_name', 'last_name', 'active', 'roles', 'default_group', 'groups', 'last_login_at', 
        'current_login_at', 'last_login_ip', 'current_login_ip', 'login_count')

    form_widget_args = {
        'email': {
            'readonly': True
        },
        'last_login_at': {
            'readonly': True
        }, 
        'current_login_at': {
            'readonly': True
        }, 
        'last_login_ip': {
            'readonly': True
        }, 
        'current_login_ip': {
            'readonly': True
        }, 
        'login_count': {
            'readonly': True
        }
    }






class ChartView(SecureModelView):
    """
    Extends SecureModelView for Chart mongo collection
    """
    can_delete = False

    column_exclude_list = ('comments')

    column_filters = ('is_active', 'created_at', 'updated_at')

    form_columns = ('author', 'collaborators', 'group', 'is_active', 'comments', 'tags', 'embed_version',
        'current_data', 'current_options', 'created_at', 'updated_at')

    """
    form_subdocuments = {
        'current_data': {
            'form_subdocuments': {
                'data': {}
            }
        }
    }
    """

    form_widget_args = {
        'current_data': {
            'readonly': True
        }, 
        'current_options': {
            'readonly': True
        }, 
        'author': {
            'readonly': True
        }, 
        'created_at': {
            'readonly': True
        }, 
        'updated_at': {
            'readonly': True
        }
    }





admin.add_view(ChartView(Chart, endpoint='admin/renbroc/example', category='Example'))
