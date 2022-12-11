from flask.testing import FlaskClient
from src.models import db, Movie
from tests.utils import refresh_db

def test_get_all_movies(test_app: FlaskClient):
    # start by refreshing db, adding dark knight movie with 5 rating
    refresh_db()
    test_movie = Movie(title = 'The Dark Knight', director='Christopher Nolan', rating=5)
    db.session.add(test_movie)
    db.session.commit()

    result = test_app.get('/movies')
    page_data: str = result.data.decode()


    assert result.status_code == 200
    assert f'<td><a href="/movies/{test_movie.movie_id}">The Dark Knight</a></td>' in page_data
    assert '<td>Christopher Nolan</td>' in page_data
    assert '<td>5</td>' in page_data

def test_get_all_movies_empty(test_app: FlaskClient):
    # start by refreshing db, and visiting empty movies page
    refresh_db()
    result = test_app.get('/movies')
    page_data: str = result.data.decode()
    # make sure pages loads successfully and table not in page html
    assert result.status_code == 200
    assert '<td>' not in page_data