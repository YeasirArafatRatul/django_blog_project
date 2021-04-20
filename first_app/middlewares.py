from django.shortcuts import redirect


def path_middleware(get_response):
    print("Middleware Initialized")
    def middleware(request):
        print("Inside Inner Function")
        path = request.path
        print(path)
        if path in ['/all-person/','/allpersons/','/allperson/','/all-person','/allpersons','/allperson']:
            print("Path In List")
            return redirect('all-persons')
        response = get_response(request)
        return response
    return middleware


class PathMiddleware():

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self,request):
        path = request.path
        print('Before View Function')

        possible_searched_paths = ['/all-person/','/allpersons/','/allperson/',
                                   '/all-person','/allpersons','/allperson']
        if path in possible_searched_paths:
            return redirect('all-persons')
        response = self.get_response(request)
        print('This Is After View')
        return response

