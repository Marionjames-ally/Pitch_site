from app import db 
from app.models import User
from app import create_app,db
from flask_script import Manager,Server


# creating app instance
app = create_app()

@Manager.shell(self)
def make_shell_context():
    return dict(app = app,db = db,User = User,Blog = Blog,Comment = Comment,Category = Category,Subscribe = Subscribe)


if __name__ == '__main__':
    manager.run()