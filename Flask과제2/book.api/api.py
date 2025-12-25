from flask_smorest import Blueprint
from flask.views import MethodView
from schemas import BookSchema

blp = Blueprint(
    "books",          
    "books",          
    url_prefix="/books",   
    description="Operations on books"
)

books = []
next_id = 1  

@blp.route("/")
class BooksResource(MethodView):
    @blp.response(200, BookSchema(many=True))
    def get(self):
        return books

