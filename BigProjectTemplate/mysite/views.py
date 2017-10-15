from django.http import JsonResponse

from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy


# Homepage version (my version 도 참조 바람)
class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context


class TemplateFileNameMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_fn'] = self.template_name
        return context


#--- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'


#--- User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


# redirect according to username after login
class MyLoginView(LoginView):
    def get_success_url(self):
        # NOK. if self.request.user.username == 'shkim':
        if self.request.method == 'POST':
            if self.request.POST['username'] == 'shkim':
                # return '/blog/'
                return '/'
        else:
            super().get_success_url()
