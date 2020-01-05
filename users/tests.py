from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):
    """Test user and superuser creation."""

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='TestNormal',
                                        email='normal@user.com',
                                        password='foo')
        self.assertEqual(user.username, 'TestNormal')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='', email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('TestSuper',
                                                   'super@user.com',
                                                   'foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='TestSuper', email='super@user.com',
                password='foo', is_superuser=False)


class SingUpViewTest(TestCase):
    pass
