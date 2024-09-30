from django.test import TestCase
from django.contrib.auth.models import User


class SampleTestCase(TestCase):

    def test_sample(self):
        User.objects.first()
        self.assertTrue(True)
        print("I ran")
