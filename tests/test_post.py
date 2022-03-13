import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Vyonna = User(first_name = "Vyonna",
                                last_name = "Njenga",
                                username = "Vee",
                                password = "0719890523",
                                email = "njengavyonna@gmail.com")
        self.new_post = Post(post_title = "Sample Title",
                            post_content = "Every time I meet new people I introduce myself as 'I sell dope'.",
                            user_id = self.user_Vyonna.id)
        self.new_comment = Comment(comment = "Nice job! Love it.",
                                    post_id = self.new_post.id,
                                    user_id = self.user_Vyonna.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Vyonna, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))