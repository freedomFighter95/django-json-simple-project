from django.test import TestCase
from receipts.models import Receipt
from decimal import Decimal


# Create your tests here.

class ReceiptTest(TestCase):
    fixtures = ["receipts.json",]
    def test_receipt(self):
        receipt = Receipt.objects.get(id=4)
        total = receipt.total()
        print(total)

        expected = Decimal(60.00)
        self.assertEqual(expected, total)
