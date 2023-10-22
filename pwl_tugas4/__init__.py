from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.include('.models')
        config.set_authorization_policy(ACLAuthorizationPolicy())
        config.include('pyramid_jwt')
        config.set_jwt_authentication_policy('secret')
        config.scan()
    return config.make_wsgi_app()
