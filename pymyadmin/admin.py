import os
import inspect

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

