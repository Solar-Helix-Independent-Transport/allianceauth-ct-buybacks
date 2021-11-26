from allianceauth.services.hooks import UrlHook, MenuItemHook
from allianceauth import hooks
from . import urls

@hooks.register('url_hook')
def register_url():
    return UrlHook(urls, 'ctbuybacks', r'^ctb/')


class BuyBacks(MenuItemHook):
    def __init__(self):
        MenuItemHook.__init__(self,
                              'Active Buybacks',
                              'fas fa-dollar-sign fa-fw',
                              'ctbuybacks:list',
                              navactive=['ctbuybacks:'])

    def render(self, request):
        if request.user.has_perm('ctbuybacks.basic_access'):
            return MenuItemHook.render(self, request)
        return ''


@hooks.register('menu_item_hook')
def register_menu():
    return BuyBacks()


"""
@hooks.register('discord_cogs_hook')
def register_cogs():
    return ["fatfilters.fatcog"]
"""