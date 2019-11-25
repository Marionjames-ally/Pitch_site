from app import create_app,db
from app.models import User


# creating app instance
app = create_app('production')

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Comment = Comment,Category = Category,Subscribe = Subscribe)

