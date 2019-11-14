class XyzFlowMiddleware(object):
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("This is Before View Execute")
        
        
        #before Sending the request to Views
        #this line everything will be run as pre-processing
        
        
        response = self.get_response(request)
        # it is Forwording request to next level
        # it will give a response


        print("This Code Will Execute After view Execute")

        #After Receving the response this Code Will Execute
        #this line everything will be run as post-processing
        return response