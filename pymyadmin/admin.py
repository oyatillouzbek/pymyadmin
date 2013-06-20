import os
import inspect
import json

from pymyadmin import modules
from flask.ext.admin import Admin


def load_views_from_module(module):

    views = dict()

    for member in inspect.getmembers(module):
        name, type_ = member
        if inspect.isclass(type_):
            class_ = type_
            if getattr(class_, 'public', None) is not True:
                continue
            views[name] = class_

    return views


def discover_modules_on(path):

    rootmod = 'pymyadmin.modules'
    findedmodules = dict()

    for fname in os.listdir(path):

        if not fname.endswith('.py'):
            continue
        name = fname.split('.py')[0]
        if name.startswith('__'):
            continue

        iname = '%s.%s' % (rootmod, name)
        findedmodules[name] = __import__(iname, fromlist=rootmod)

    return findedmodules


def make_view_instance(viewname, view, db=None):

    endpoint = view.endpoint
    category = view.category
    viewname = view.verbose_name

    viewinstance = view(name=viewname,
            category=category, endpoint=endpoint)

    return viewinstance


def setup_admin_for(app):

    modules_path = modules.__file__.rsplit(os.sep, 1)[0]
    findedmodules = discover_modules_on(modules_path)
    loadedviews = dict()

    admin = Admin(name='PyMyAdmin')

    for modname, module in findedmodules.iteritems():
        views = load_views_from_module(module)
        for viewname, view in views.iteritems():
            loadedviews[viewname] = view

    for viewname, view in loadedviews.iteritems():
        viewinstance = make_view_instance(viewname, view)
        admin.add_view(viewinstance)

    admin.init_app(app)


def get_or_create_database_config_for(username):
    #XXX Need to set path to file depending on OS...
    path_to = os.path.join('/home', username, '.config', '.pymyadmin')
    file_path = os.path.join(path_to, 'config.cfg')

    if os.path.isfile(file_path):
        file_opened = open(file_path, 'r')
        try:
            config = json.loads(file_opened.read())
        except ValueError:
            config = create_empty_database_config()
    else:
        try:
            file_opened = open(file_path, 'w')
        except IOError:
            os.makedirs(path_to)
            print 'created dirs'
            file_opened = open(file_path, 'w')
        config = create_empty_database_config()
        print 'created config'
        file_opened.write(config)
    
    file_opened.close()
    return config
    

def create_empty_database_config():
    #XXX Need to set basic settings here...
    empty_config = {}
    config = json.dumps(empty_config, indent=4, separators=(',', ': '))
    return config






