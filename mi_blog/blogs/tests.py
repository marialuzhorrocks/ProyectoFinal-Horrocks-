from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, Client
from blogs.models import Blog

class BlogModelTest(TestCase):
    def setUp(self):
        self.client = Client()  # Inicializar el cliente de prueba
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.blog = Blog.objects.create(
            titulo='Test Blog',
            subtitulo='Test Subtitulo',
            cuerpo='This is a test body of the blog.',
            autor=self.user,
        )

    def test_blog_creation(self):
        self.assertEqual(self.blog.titulo, 'Test Blog')
        self.assertEqual(self.blog.subtitulo, 'Test Subtitulo')
        self.assertEqual(self.blog.cuerpo, 'This is a test body of the blog.')
        self.assertEqual(self.blog.autor, self.user)
        self.assertIsNotNone(self.blog.fecha)  # Verificar que la fecha no sea None

    def test_blog_list_view(self):
        response = self.client.get(reverse('pages'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Blog')

    def test_blog_detail_view(self):
        response = self.client.get(reverse('page_detail', args=[self.blog.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Blog')
