from django.shortcuts import render, get_object_or_404
from .models import Article
from .serializer import ArticleSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from .utilities import UserPagination
from rest_framework import filters

# Create your views here.


################################################################
## widok funkcyjny
# @api_view(['GET', 'POST'])
# def list_create_articles(request, format=None):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         # return JsonResponse({'articles':serializer.data})
#         return Response(serializer.data)
#     else:
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #Paginacja w widoku funkcyjnym
# @api_view(['GET', 'POST'])
# def list_create_articles(request, format=None):
#     if request.method == 'GET':
#         pagination_class = UserPagination()
#         articles = Article.objects.all()
#         pages = pagination_class.paginate_queryset(queryset=articles, 
#                                                         request=request)
#         serializer = ArticleSerializer(pages, many=True)
#         return pagination_class.get_paginated_response(serializer.data)
#     else:
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, articleID, format=None):
#     article = get_object_or_404(Article, id=articleID)
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

################################################################
# # widok klasowy
# class ListCreateArticle(APIView):

#     def get(self, request, format=None):
#         article = Article.objects.all()
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Dodanie paginacji do widoku klasowego
# class ListCreateArticle(APIView):
#     pagitation_class = UserPagination()

#     def get(self, request, format=None):
#         articles = Article.objects.all()
#         pages = self.pagitation_class.paginate_queryset(queryset=articles, 
#                                                         request=request)
#         serializer = ArticleSerializer(pages, many=True)
#         return self.pagitation_class.get_paginated_response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class DetailDeleteArticle(APIView):    

#     def get(self, request, articleID, format=None):
#         article = get_object_or_404(Article, id=articleID)
#         serializer = ArticleSerializer(instance=article)
#         return Response(serializer.data)

#     def put(self, request, articleID, format=None):
#         article = get_object_or_404(Article, id=articleID)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, articleID):
#         article = get_object_or_404(Article, id=articleID)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


################################################################
# widoki mixinowe MIXINSViews

# class ListCreateArticle(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class DetailDeleteArticle(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Article.objects.all()    #pula obiektów, które dajmy do przetwarzania w danej klasie 
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


################################################################
# widoki generyczne

class ListCreateArticle(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['-date']
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class DetailDeleteArticle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()  # pula obiektów, które dajmy do przetwarzania w danej klasie
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    
    def get_permissions(self):
        #permission_classes = [permissions.IsAdminUser()] if self.request.method == 'GET' else [permissions.AllowAny()]
        #return [permission() for permission in ([permissions.IsAdminUser()] if self.request.method == 'GET' else [permissions.AllowAny()] ) ]
        return [permissions.IsAdminUser() if self.request.method == 'GET' else permissions.AllowAny()]

# @api_view(['GET'])
# def reverse_points(request):
#     endpoints = [reverse('articles'), reverse('users'), reverse('get_token')]
#     return Response(endpoints)

class APIRoot(APIView):
    def get(self, request, format=None):
        links = {
            'articles':reverse ('articles', request=request),
            'users':reverse ('users', request=request),
            'get_token':reverse ('get_token', request=request)

        }
        return Response(links)