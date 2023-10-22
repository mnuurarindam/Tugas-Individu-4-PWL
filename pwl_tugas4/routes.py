def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    # Add routes for the api movie resource
    config.add_route('api_movie_list', '/api/movies')
    config.add_route('api_movie_create', '/api/movies/create')
    config.add_route('api_movie_view', '/api/movies/{id:\d+}')
    config.add_route('api_movie_update', '/api/movies/{id:\d+}/update')
    config.add_route('api_movie_delete', '/api/movies/{id:\d+}/delete')

    # Add routes for the login
    config.add_route('login', '/')
    config.add_route('login_jwt', '/login')
    config.add_route('logout', '/logout')

    # Add routes for the register
    config.add_route('register', '/register')
    config.add_route('register_process', '/register/process')

    # Add routes for the home
    config.add_route('home', '/home')


    config.scan()

