from pyramid.response import Response
from sqlalchemy.exc import DBAPIError
from pyramid.httpexceptions import HTTPForbidden
from ..models.mymodel import banlist

def check(request, remote_addr):

    try:
        query = request.dbsession.query(banlist) # Checks if the ip is in banlist
        records = query.filter(banlist.ip == remote_addr).all()
        print('hi')
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)

    if remote_addr in records:
        return(HTTPForbidden())
