from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError

from .. import models


@view_config(route_name='api_movie_list',request_method='GET', renderer='json')
def my_view(request):
    # get all movies
    movies = request.dbsession.query(models.Movie).all()
    # endpoint for the list of movies
    data = []

    for movie in movies:
        data.append({
            'id': movie.id,
            'title': movie.title,
            'genre': movie.genre,
            'synopsis': movie.synopsis
        })

    return data

@view_config(route_name='api_movie_create', request_method='POST', renderer='json')
def api_movie_create(request):
    try:
        # get the request body
        body = request.json_body
        # create a new movie
        movie = models.Movie(
            title=body['title'],
            genre=body['genre'],
            synopsis=body['synopsis']
        )
        # save the movie
        request.dbsession.add(movie)
        request.dbsession.flush()
        # return the movie
        return {
            'id': movie.id,
            'title': movie.title,
            'genre': movie.genre,
            'synopsis': movie.synopsis
        }
    except SQLAlchemyError as e:
        print(e)
        return Response(db_err_msg, content_type='text/plain', status=500)
    
@view_config(route_name='api_movie_view', request_method='GET', renderer='json')
def api_movie_view(request):
    try:
        # get the movie id from the url
        movie_id = int(request.matchdict['id'])
        # get the movie
        movie = request.dbsession.query(models.Movie).get(movie_id)
        # return the movie
        return {
            'id': movie.id,
            'title': movie.title,
            'genre': movie.genre,
            'synopsis': movie.synopsis
        }
    except SQLAlchemyError as e:
        print(e)
        return Response(db_err_msg, content_type='text/plain', status=500)
    
@view_config(route_name='api_movie_update', request_method='PUT', renderer='json')
def api_movie_update(request):
    try:
        # get the movie id from the url
        movie_id = int(request.matchdict['id'])
        # get the movie
        movie = request.dbsession.query(models.Movie).get(movie_id)
        # get the request body
        body = request.json_body
        # update the movie
        movie.title = body['title']
        movie.genre = body['genre']
        movie.synopsis = body['synopsis']
        # return the movie
        return {
            'id': movie.id,
            'title': movie.title,
            'genre': movie.genre,
            'synopsis': movie.synopsis
        }
    except SQLAlchemyError as e:
        print(e)
        return Response(db_err_msg, content_type='text/plain', status=500)
    
@view_config(route_name='api_movie_delete', request_method='DELETE', renderer='json')
def api_movie_delete(request):
    try:
        # get the movie id from the url
        movie_id = int(request.matchdict['id'])
        # get the movie
        movie = request.dbsession.query(models.Movie).get(movie_id)
        # delete the movie
        request.dbsession.delete(movie)
        # return the movie
        return {
            'id': movie.id,
            'title': movie.title,
            'genre': movie.genre,
            'synopsis': movie.synopsis
        }
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