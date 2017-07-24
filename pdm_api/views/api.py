from pyramid.view import view_config
from pyramid.httpexceptions import HTTPForbidden
from pyramid import request
from sqlalchemy.exc import DBAPIError
from ..models.mymodel import MyModel, request_log, access_log, banlist
from .api_scripts import check_banlist, add_request
from .api_scripts.analyze import analyze
from ..settings import get_settings
import datetime

@view_config(route_name='slack', renderer='../templates/slack.jinja2')
def api(request):
    if request.method == 'GET':
        return(HTTPForbidden())

    required_keys = [
        'token',
        'team_id',
        'team_domain',
        'service_id',
        'channel_id',
        'cannel_name',
        'user_id',
        'user_name',
        'text',
        'timestamp'
    ]

    remote_addr = str(request.remote_addr)
    check_banlist.check(request, remote_addr)

    for record in required_keys:
        if record not in request.params:
            return(HTTPForbidden())

    header_values = {}

    for record  in request.POST.items():
        header_values[str(record[0])] = str(record[1])

    add_request.add(request, remote_addr, str(header_values))

    result = analyze().complete(str(header_values['text']))

    if result == True:
        pass #TODO: 100% Translated


    return(header_values)
