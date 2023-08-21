from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import Article
from django.urls import reverse
from rest_framework import status
from ..serializer import ArticleSerializer, UserSerializer

class ReadArticleTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testUser',password='testPassword1234')
        self.articles = [
            Article.objects.create(
                title= 'Test Articles', 
                text = 'testArticle text',
                owner = self.user,
            ),
            
            Article.objects.create(
                title= 'Test Articles 2', 
                text = 'testArticle text',
                owner = self.user,
            ),
            
            Article.objects.create(
                title= 'Test Articles 3', 
                text = 'testArticle text',
                owner = self.user,
            )
        ]        
        self.expected_data = ArticleSerializer(self.articles, many=True)
        self.url_list = reverse('articles')
        print(self.url_list)
        #self.url_retrive = reverse('articleDetail')
        


    # def test_list_articles(self):
    #     response = self.client.get(self.url_list)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     # self.assertEqual(response.data, self.expected_data.data)


class CreateArticleTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testUser1',password='1234')
        self.article = Article.objects.create(title='Hello World', text='Some test text',owner = self.user)
        self.data = {'title':'Hello World', 'text':'Some test text'}
        self.url = reverse('articles')
        self.client.force_authenticate(user=self.user)

    def test_create_article(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)