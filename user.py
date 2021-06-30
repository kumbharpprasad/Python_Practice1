#Class user - Blue print of user attribute.

# object constructor function for class. #Self is for current class & all 4 values (email, name, password, job_title)
# must be provided to create an object
#for class, first letter must in capital (stad. practice)

class User:
    def __init__(self, email, name, job_title, password):
        self.email = email             #self.<emai> is attribute (variable) of class User
        self.name = name
        self.job_title = job_title
        self.password = password

    #To change the job title & password for user object. #self is access the attribute of user class in below functions.

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.job_title = new_job_title
        print(f"Title has been changed to {self.job_title}")

    #To display the user information - just to show that object has created.
    #self.<name> to access the attribute in User class.

    def get_user_info(self):
        print(f"The user {self.name} with job title {self.job_title} has been added to system. You may contact him on {self.email}. Thank you")



