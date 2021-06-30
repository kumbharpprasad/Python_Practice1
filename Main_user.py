from user import User
from post import Post

# input to class & creat an object. Noramlly each class has seperate file and main_user is used to write an program to create object.

my_user1 = User("prasad@g.com", "Prasad", "DevOps Engineer", "psswd1")

# to print the output

my_user1.get_user_info()

# To change the job title parameter

my_user1.change_job_title("Disaster Recovery Architect\n")

#To post class example, Passing 2 attribute to creat an object

my_post = Post("Hello World", "Prasad Kumbhar")

my_post.get_post_info()
