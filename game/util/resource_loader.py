import toml

def resource(file_dir = ''):
    toml_data = toml.load(file_dir)
    def new_cls(Cls):
        def callable(key = ''):
            c = Cls()
            toml_game_dict = toml_data[key]
            obj = {**toml_game_dict, **c.__dict__, 'key': key}
            c.__dict__.update(obj)
            return c
        return callable
    return new_cls
