from pwl_tugas4 import models
# hide warnings summary
import warnings
warnings.filterwarnings("ignore")

def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404


def test_api_movie_create(testapp, dbsession):
    # create a movie
    res = testapp.post_json('/api/movies/create', {
        'title': 'The Matrix',
        'genre': 'Sci-Fi',
        'synopsis': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.'
    }, status=200)

    assert res.json['title'] == 'The Matrix'
    assert res.json['genre'] == 'Sci-Fi'
    assert res.json['synopsis'] == 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.'

def test_api_movie_read(testapp, dbsession):
    # get the movie by id   
    res = testapp.get('/api/movies', status=200)

    assert res.status_code == 200



