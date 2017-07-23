from pyramid.response import Response
from sqlalchemy.exc import DBAPIError
from pyramid.httpexceptions import HTTPForbidden
from ..models.mymodel import banlist

def check(request, remote_addr):

    try:
        query = request.dbsession.query(banlist) # Checks if the ip is in banlist
        records = query.filter(banlist.ip == remote_addr).all()

    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)

    if remote_addr in records:
        return(HTTPForbidden())

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
