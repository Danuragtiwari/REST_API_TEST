from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Invoice

class InvoiceAPITests(APITestCase):
    def setUp(self):
        self.invoice_data = {
            'date': '2023-12-18',
            'customer_name': 'Test Customer'
        }

    def test_create_invoice(self):
        url = reverse('invoice-list-create')
        response = self.client.post(url, self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)

    def test_retrieve_invoice(self):
        invoice = Invoice.objects.create(**self.invoice_data)
        url = reverse('invoice-detail', args=[invoice.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], self.invoice_data['customer_name'])

    def test_update_invoice(self):
        invoice = Invoice.objects.create(**self.invoice_data)
        updated_data = {
            'date': '2024-01-01',
            'customer_name': 'Updated Customer'
        }
        url = reverse('invoice-detail', args=[invoice.id])
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], updated_data['customer_name'])

    def test_delete_invoice(self):
        invoice = Invoice.objects.create(**self.invoice_data)
        url = reverse('invoice-detail', args=[invoice.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Invoice.objects.count(), 0)
