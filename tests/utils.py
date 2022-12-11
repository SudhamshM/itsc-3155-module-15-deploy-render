from src.models import Movie, db

# function to refresh db after deleting
def refresh_db():
    Movie.query.delete()
    db.session.commit()