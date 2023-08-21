from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testUser', password='testPassword1234')
        self.article = Article.objects.create(
            title= 'Test Article', 
            text = 'testArticle text',
            owner = self.user
            )
    # def test_article_title(self):
    #     article = Article.objects.get(id=self.article.id)
    #     self.assertEqual(article.title, 'Test Article')

    # def test_article_text(self):
    #     article = Article.objects.get(id=self.article.id)
    #     self.assertEqual(article.text, 'testArticle text')
    

    