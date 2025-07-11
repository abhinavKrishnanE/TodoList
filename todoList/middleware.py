import time

class DelayMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.path.startswith('/todolist/tasklist/'):
            time.sleep(3)
        return self.get_response(request)
