from pymyadmin.modules import BaseModule
from pymyadmin.modules import expose


class SettingsModule(BaseModule):
    """A view for the settings."""

    public = True
    endpoint = 'settings'
    verbose_name = 'Settings'

    @expose('/')
    def list(self):
        return self.render('settings/list.html')
