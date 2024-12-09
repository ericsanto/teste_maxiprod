from django.test import TestCase
from authentication.models import UserCustom


class UserCustomTestCase(TestCase):

    def setUp(self) -> None:
        self.user1 = UserCustom.objects.create(
                username='éric',
                date_of_birth='2002-04-12',
                email='eric@teste.com',
                password='kansaskaz2y5',
                )

    def test_user_can_be_created(self):
        self.assertEqual(self.user1.username, 'éric')
    

