#class Post : to post an update like in insta & facebook

class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author

    def new_post(self, new_message):
        self.message = new_message

    def get_post_info(self):
        print(f"New Post= {self.message}\nFrom Author= {self.author}")

