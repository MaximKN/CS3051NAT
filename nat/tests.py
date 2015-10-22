from django.test import TestCase
from nat.models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        a = Article()
        a.set_attributes("Test title", "Test description",
                         0, "Test link", 1)
        a.save()

    def test_article_attributes(self):
        a = Article.objects.get(title="Test title")
        self.assertEqual(a.title, "Test title")
        self.assertEqual(a.description, "Test description")
        self.assertEqual(a.source, 0)
        self.assertEqual(a.link, "Test link")

    def test_article_short_description(self):
        a = Article.objects.get(title="Test title")
        self.assertEqual(a.get_short_text(), "Test description")

