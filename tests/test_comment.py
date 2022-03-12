import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Victor = User(first_name = "Victor",
                                last_name = "Kibocha",
                                username = "Rocker",
                                password = "0719890523",
                                email = "vicikibocha@gmail.com")
        self.new_post = Post(post_title = "Sample Title",
                            post_content = "The jig is up! Every time I meet new people I introduce myself as 'I sell dope'.",
                            user_id = self.user_Victor.id)
        self.new_comment = Comment(comment = "Nice job! Love it.",
                                    post_id = self.new_post.id,
                                    user_id = self.user_Victor.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Victor, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))