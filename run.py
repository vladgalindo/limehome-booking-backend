from app import app, api, blueprint
from app.users.apis import users_api
from app.properties.apis import properties_api
from app.authentication.apis import authorization_api
from app.bookings.apis import booking_api

api.add_namespace(users_api, '{url_prefix}/users'.format(url_prefix=app.config['APP_URL_PREFIX']))
api.add_namespace(properties_api, '{url_prefix}/properties'.format(url_prefix=app.config['APP_URL_PREFIX']))
api.add_namespace(authorization_api, '{url_prefix}/auth'.format(url_prefix=app.config['APP_URL_PREFIX']))
api.add_namespace(booking_api, '{url_prefix}/booking'.format(url_prefix=app.config['APP_URL_PREFIX']))
app.register_blueprint(blueprint)

app.app_context().push()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['APP_PORT'], debug=True)
