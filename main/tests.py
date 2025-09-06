from django.test import TestCase, Client
from .models import Product

class ProductTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            name="Nike Mercurial",
            price=2500000,
            description="Sepatu bola terbaru",
            category="cleat",
            is_featured=True,
            views=10
        )
        self.assertEqual(product.name, "Nike Mercurial")
        self.assertEqual(product.price, 2500000)
        self.assertEqual(product.category, "cleat")
        self.assertTrue(product.is_featured)
        self.assertEqual(product.views, 10)

    def test_default_values(self):
        product = Product.objects.create(
            name="Adidas Predator",
            price=2000000,
            description="Sepatu bola klasik"
        )
        self.assertEqual(product.category, "jersey")
        self.assertEqual(product.views, 0)
        self.assertFalse(product.is_featured)

    def test_increment_views(self):
        product = Product.objects.create(
            name="Puma Future",
            price=1800000,
            description="Sepatu bola ringan"
        )
        initial_views = product.views
        product.increment_views()
        self.assertEqual(product.views, initial_views + 1)

    def test_is_popular_threshold(self):
        product_20 = Product.objects.create(
            name="Umbro Speciali",
            price=1500000,
            description="Sepatu bola klasik",
            views=20
        )
        self.assertFalse(product_20.is_popular)

        product_21 = Product.objects.create(
            name="Mizuno Morelia",
            price=2200000,
            description="Sepatu bola Jepang",
            views=21
        )
        self.assertTrue(product_21.is_popular)


class MainPageTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_nonexistent_page(self):
        response = Client().get("/burhan_fc_rules/")
        self.assertEqual(response.status_code, 404)
