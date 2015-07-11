# http://charlesleifer.com/blog/structuring-flask-apps-a-how-to-for-those-coming-from-django/

from flask import Blueprint, get_template_attribute, session, request, redirect, url_for, Response, jsonify

from flask.ext.login import login_required, current_user

import json

from renbroc import app

import datetime

from models import *

api = Blueprint('api', __name__)


"""
Example API calls below
"""

@api.route('/get_groups')
@login_required
def get_groups():
    """
    Return groups assigned to logged in user
    """

    # FUTURE: Properly reutrn error, Mongo is giving it's own
    if current_user.groups:
        return Response(response=json.dumps([g.to_dict() for g in current_user.groups]), status=200, mimetype="application/json")
    else:
        return return_json_error('No groups assigned to', 500)


@api.route('/post_publish/<chart_id>', methods=['POST'])
@login_required
def post_publish(chart_id):
    """
    Publish the chart.

    :param chart_id: chart's unique identifier
    """

    chart = Chart.objects.get(id=chart_id)

    if not chart.can_user_access(current_user):
        return return_json_error('Access Denied', 500)

    if request.method == 'POST':

        request_json = request.get_json()

        print 'saving json:'
        #print request_json.get('s3')

        chart.publish(current_user, request_json.get('options_id'), request_json.get('data_id'), request_json.get('s3'))

    if chart.is_published:
        chart_embed_script = get_template_attribute('macros_chart.html', 'chart_embed_script')
        response = {
            'message': 'Successfully uploaded to S3',
            'published_obj': chart.published_obj.to_dict(),
            'url_2300': chart.get_image_2300_url(),
            'embed_code': chart_embed_script(chart),
        }
        return Response(response=json.dumps(response), status=200, mimetype="application/json")
    else:
        return return_json_error('Publish failed', 500)





def return_chart_json(chart):
    """
    Returns the JSON represenatation of a chart.

    :param chart: object representing a chart
    """
    return Response(response=chart.to_json_chartable(), status=200, mimetype="application/json")

def return_json_error(msg, status_code):
    """
    Return the given error through the API.

    :param msg: Message to return as JSON with key 'message'
    :param status_code: HTTP status code to return
    """
    return Response(response=json.dumps({'message': str(msg)}), status=status_code, mimetype="application/json")


