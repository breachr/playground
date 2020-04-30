import flask
import flask_praetorian
import flask_cors

from app import db
from app import app

guard = flask_praetorian.Praetorian()
cors = flask_cors.CORS()

# A generic ProtectedUser model that might be used by an app powered by flask-praetorian
class ProtectedUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    roles = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True, server_default='true')

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        return self.is_active


app.config['SECRET_KEY'] = 'top secret'
app.config['JWT_ACCESS_LIFESPAN'] = {'hours': 24}
app.config['JWT_REFRESH_LIFESPAN'] = {'days': 30}
# Initialize the flask-praetorian instance for the app
guard.init_app(app, ProtectedUser)
# Initializes CORS so that the api_tool can talk to the example app
cors.init_app(app)

# Add users for the example
# with app.app_context():
#     # db.create_all()
#     db.session.add(ProtectedUser(
#         username='TheDude',
#         password=guard.hash_password('abides'),
#     ))
#     db.session.add(ProtectedUser(
#         username='Walter',
#         password=guard.hash_password('calmerthanyouare'),
#         roles='admin'
#     ))
#     db.session.add(ProtectedUser(
#         username='Donnie',
#         password=guard.hash_password('iamthewalrus'),
#         roles='operator'
#     ))
#     db.session.add(ProtectedUser(
#         username='Maude',
#         password=guard.hash_password('andthorough'),
#         roles='operator,admin'
#     ))
#     db.session.commit()


# Set up some routes for the example

@app.route('/login', methods=['POST'])
def login():
    """
    Logs a user in by parsing a POST request containing user credentials and
    issuing a JWT token.
    .. example::
       $ curl http://localhost:5000/login -X POST \
         -d '{"username":"Walter","password":"calmerthanyouare"}'
    """
    req = flask.request.get_json(force=True)
    username = req.get('username', None)
    password = req.get('password', None)
    user = guard.authenticate(username, password)
    ret = {'access_token': guard.encode_jwt_token(user)}
    return (flask.jsonify(ret), 200)


@app.route('/protected')
@flask_praetorian.auth_required
def protected():
    """
    A protected endpoint. The auth_required decorator will require a header
    containing a valid JWT
    .. example::
       $ curl http://localhost:5000/protected -X GET \
         -H "Authorization: Bearer <your_token>"
    """
    return flask.jsonify(message='protected endpoint (allowed user {})'.format(
        flask_praetorian.current_user().username,
    ))


@app.route('/protected_admin_required')
@flask_praetorian.roles_required('admin')
def protected_admin_required():
    """
    A protected endpoint that requires a role. The roles_required decorator
    will require that the supplied JWT includes the required roles
    .. example::
       $ curl http://localhost:5000/protected_admin_required -X GET \
          -H "Authorization: Bearer <your_token>"
    """
    return flask.jsonify(
        message='protected_admin_required endpoint (allowed user {})'.format(
            flask_praetorian.current_user().username,
        )
    )


@app.route('/protected_operator_accepted')
@flask_praetorian.roles_accepted('operator', 'admin')
def protected_operator_accepted():
    """
    A protected endpoint that accepts any of the listed roles. The
    roles_accepted decorator will require that the supplied JWT includes at
    least one of the accepted roles
    .. example::
       $ curl http://localhost/protected_operator_accepted -X GET \
         -H "Authorization: Bearer <your_token>"
    """
    return flask.jsonify(
        message='protected_operator_accepted endpoint (allowed usr {})'.format(
            flask_praetorian.current_user().username,
        )
    )
