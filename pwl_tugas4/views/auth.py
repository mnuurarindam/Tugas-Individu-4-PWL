from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError
from pyramid.httpexceptions import HTTPFound

from .. import models

# login

@view_config(route_name='login', renderer='pwl_tugas4:templates/login.jinja2')
def login_view(request):
    return {}

# login with jwt
@view_config(route_name='login_jwt', request_method='POST', renderer='json')
def login_jwt(request):
    try:
        # get the request body
        body = request.POST
        # get the user
        user = request.dbsession.query(models.User).filter_by(username=body['username']).first()
        # check the password
        if user.password == body['password']:
            # generate the token
            token = request.create_jwt_token(user.id)
            # return the token
            # redirect to the home page
            url = request.route_url('home')
        else:
            return Response('Wrong password', content_type='text/plain', status=401)
    except SQLAlchemyError as e:
        print(e)
        return Response(db_err_msg, content_type='text/plain', status=500)
    
# logout
@view_config(route_name='logout')
def logout_view(request):
    request.session.invalidate()
    return Response('Logged out', content_type='text/plain', status=200)

# register
@view_config(route_name='register', renderer='../templates/register.jinja2')
def register_view(request):
    return {}

# register process
@view_config(route_name='register_process', request_method='POST', renderer='json')
def register_process(request):
    try:
        # get the request
        body = request.POST
        # create a new user
        user = models.User(
            name=body['name'],
            username=body['username'],
            password=body['password'],
            role="user"
        )
        # save the user
        request.dbsession.add(user)
        request.dbsession.flush()
        
        url = request.route_url('login')
        return HTTPFound(url)

    
    except SQLAlchemyError as e:
        print(e)
        return Response(db_err_msg, content_type='text/plain', status=500)
    
db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""