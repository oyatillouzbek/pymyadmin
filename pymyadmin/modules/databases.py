from pymyadmin.modules import BaseModule
from pymyadmin.modules import expose


class DatabaseModelView(BaseModule):
    """A view for the settings."""

    public = True
    endpoint = 'databases'
    verbose_name = 'Databases'

    @expose('/')
    def list(self):
        return self.render('databases/list.html')
