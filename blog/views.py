

# # Create your views here.
# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from .models import BlogPost, Comment, Category, Tag
# from .serializers import BlogPostSerializer, CommentSerializer, CategorySerializer, TagSerializer

# class BlogPostListView(generics.ListAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
#     permission_classes = []


# class BlogPostListCreateView(generics.ListCreateAPIView):
#     serializer_class = BlogPostSerializer
#     permission_classes = []

#     def get_queryset(self):
#         user = self.request.user
#         return BlogPost.objects.filter(author=user).order_by('-created_at')

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

# class BlogPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
#     permission_classes = []

# class CommentListView(generics.ListAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = []

# class CommentListCreateView(generics.ListCreateAPIView):
#     serializer_class = CommentSerializer
#     permission_classes = []

#     def get_queryset(self):
#         user = self.request.user
#         return Comment.objects.filter(author=user)

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

# class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = []

# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = []    

# class CategoryListCreateView(generics.ListCreateAPIView):
#     serializer_class = CategorySerializer
#     permission_classes = []

#     def get_queryset(self):
#         user = self.request.user
#         return Category.objects.filter(author=user)

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

# class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = []

# class TagListView(generics.ListAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     permission_classes = []    

# class TagListCreateView(generics.ListCreateAPIView):
#     serializer_class = TagSerializer
#     permission_classes = []

#     def get_queryset(self):
#         user = self.request.user
#         return Tag.objects.filter(author=user)

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

# class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     permission_classes = []


from rest_framework import generics
from .models import BlogPost, Comment, Category, Tag
from .serializers import BlogPostSerializer, CommentSerializer, CategorySerializer, TagSerializer

# BlogPost Views
class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = []

class BlogPostListCreateView(generics.ListCreateAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = []

    def get_queryset(self):
        return BlogPost.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        # Save without using author_name
        serializer.save()

class BlogPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = []

    

# Comment Views
class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = []

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        # Save without using author_name
        serializer.save()

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []

# Category Views
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = []

    def get_queryset(self):
        return Category.objects.all()

    def perform_create(self, serializer):
        # Save without using author_name
        serializer.save()

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

# Tag Views
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = []

class TagListCreateView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    permission_classes = []

    def get_queryset(self):
        return Tag.objects.all()

    def perform_create(self, serializer):
        # Save without using author_name
        serializer.save()

class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = []
