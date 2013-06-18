from flask.ext.admin import expose
from flask.ext.admin import BaseView


class BaseModule(BaseView):
    """All pymyadmin modules should extends this class."""

    # Boolean that specifies if the module is available or not.
    public = None

    # The module is from the given category. For example, modules with
    # the same category, all appears in the same menu, as sub-menu items,
    # in the admin.
    category = None

    # Specify the URL to access the module.
    endpoint = None

    # The string used in the admin menu to identify the module.
    verbose_name = None


__all__ = ['BaseModule', 'expose']
