class CollectData():
    """Collect Data from the participants"""
    
    def __init__(self,question):
        """Store a questions and prepare to store responses"""
        self.question = question;
        self.responses = [];
    
    def show_question(self):
        "Show the question to collection data"
        print(self.question)
    
    def store_response(self,new_response):
        """Store Responses here"""
        self.responses.append(new_response);
        
    def show_result(self):
        """Show all the response that have been given"""
        print("Here is the stored data");
        for response in self.responses:
            print("> "+response)