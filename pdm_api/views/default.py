from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPForbidden
from pyramid import request
from sqlalchemy.exc import DBAPIError
from ..models.mymodel import MyModel, request_log, access_log, banlist
from .check_banlist import check
from .add_request import add
import datetime


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    try:
        query = request.dbsession.query(MyModel)
        one = query.filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'pdm_api'}

@view_config(route_name='slack', renderer='../templates/slack.jinja2')
def api(request):
    if request.method == 'GET':
        return(HTTPForbidden())

    required_pkeys = [
        'token',
        'team_id',
        'team_domain',
        'service_id',
        'channel_id',
        'cannel_name',
        'user_id',
        'user_name',
        'text'
    ]
    remote_addr = str(request.remote_addr)
    check(request, remote_addr)

    header_values = {}

    for record  in request.POST.items():
        header_values[str(record[0])] = str(record[1])

    add(request, remote_addr, str(header_values))

    return(header_values)


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_pdm_api_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
