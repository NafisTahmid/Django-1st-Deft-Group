from django.test import TestCase

# Create your tests here.
def Home(request):
    template_name = 'home.html'
    return render(request, template_name)
