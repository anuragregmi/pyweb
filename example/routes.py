from .views import get_home_page

routes = {
    "/": get_home_page,
    "/home/": lambda x: "Its Home",
    "/anurag/": lambda x: "Its Anurag"
}
