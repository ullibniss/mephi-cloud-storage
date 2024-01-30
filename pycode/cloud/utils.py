from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Upload files", 'url_name': 'home'},
]

class DataMixin:
    paginate_by = 20

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        return context