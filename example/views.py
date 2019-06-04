from pyweb.core.template import render_template


def get_home_page(request):
    print(request.path)
    print(request.method)
    print(request.cookie)
    return render_template('home.html')
