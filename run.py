from app import app, api
from app.users.apis import users_api
from app.properties.apis import properties_api

api.add_namespace(users_api, '{url_prefix}/users'.format(url_prefix=app.config['APP_URL_PREFIX']))
api.add_namespace(properties_api, '{url_prefix}/properties'.format(url_prefix=app.config['APP_URL_PREFIX']))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['APP_PORT'], debug=True)
