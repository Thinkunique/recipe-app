    from django.test import TestCase

    from app.calc import add

    class CalcTests(TestCase):


        def test_add_two_numbers(self):
            """Test add two numbers"""

            self.assertEqual(add(1, 3), 4)
