# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
import os
SECRET_KEY = "(pA,=~[P\t C|uA)q\x0bZUQ3Q-e"

FB_APP_ID = 557755904711507

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
