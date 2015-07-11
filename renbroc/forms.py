
# Use the Flask implementation of Form
# https://flask-wtf.readthedocs.org/en/latest/
from flask_wtf import Form

# http://wtforms.readthedocs.org/en/latest/forms.html
from wtforms import BooleanField, StringField, validators, DateTimeField, HiddenField
from wtforms import SelectField, SelectMultipleField, widgets

# http://wtforms.readthedocs.org/en/latest/specific_problems.html#specialty-field-tricks
class MultiCheckboxField(SelectMultipleField):
    """
    Used to show checkboxes instead of a dropdown.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

 
class SampleForm(Form):
    """
    Basic options when searching charts. 
    """
    search_text = StringField('Text')
    search_date_start  = DateTimeField('Start Date', [validators.optional()], format='%m/%d/%Y')
    search_date_end  = DateTimeField('End Date', [validators.optional()], format='%m/%d/%Y')
    search_group = StringField('Group')
    search_user = StringField('User')
    is_active = HiddenField(default='1') # By default only want to show active charts in basic search
    search_date_type = HiddenField(default='updated')
