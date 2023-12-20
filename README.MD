
# Invoice Management API

This Django Rest Framework application provides endpoints to manage invoices and their associated details.

## Installation

1. Clone the repository:

   <pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"></svg></button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">git clone https://github.com/your_username/invoice-management-api.git
   cd invoice-management-api
   </code></div></div></pre>
2. Create a virtual environment and activate it:

   <pre><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python -m venv venv
   # For Windows: venv\Scripts\activate
   # For Unix or MacOS: source venv/bin/activate
   </code></div></div></pre>
3. Install the dependencies:

   <pre><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">pip install -r requirements.txt
   </code></div></div></pre>
4. Run database migrations:

   <pre><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python manage.py migrate
   </code></div></div></pre>
5. Run the development server:

   <pre><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python manage.py runserver
   </code></div></div></pre>

## API Endpoints

### Invoices

#### List/Create Invoices

* **URL:** `/invoices/`
* **HTTP Methods:** GET, POST
* **Description:** Endpoint to list all invoices or create a new invoice.
* **Payload Example (POST):**

<pre><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-json">{
      "date": "2023-12-18",
      "customer_name": "Test Customer",
      "details": [
          {
              "description": "Test Description",
              "quantity": 5,
              "unit_price": 10,
              "price": 50
          }
          // Add more details if needed
      ]
  }
  </code></div></div></pre>

#### Retrieve/Update/Delete Invoice

* **URL:** `/invoices/<int:pk>/`
* **HTTP Methods:** GET, PUT, DELETE
* **Description:** Endpoint to retrieve, update, or delete a specific invoice.

### Tests

The project includes comprehensive tests to ensure the functionality of the API endpoints. To run tests:

<pre><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python manage.py test your_app_name
</code></div></div></pre>

## Implementation Details

### Models

The application consists of two Django models:

* `Invoice`: Fields include Date and Customer Name.
* `InvoiceDetail`: Fields include Invoice (ForeignKey), Description, Quantity, Unit Price, and Price.

### Serializers

Serializer classes are defined to transform model instances into JSON representations and vice versa.

* `InvoiceSerializer`: Handles serialization and deserialization of Invoice objects.
* `InvoiceDetailSerializer`: Handles serialization and deserialization of InvoiceDetail objects.

### Views

Views are implemented using Django Rest Framework's generic views:

* `InvoiceListCreateView`: Handles listing and creation of Invoice instances.
* `InvoiceDetailView`: Handles retrieval, update, and deletion of specific Invoice instances.

### URLs

URL patterns are defined to map views to specific endpoints:

* `/invoices/`: Maps to `InvoiceListCreateView` for listing and creation of invoices.
* `/invoices/<int:pk>/`: Maps to `InvoiceDetailView` for retrieval, update, and deletion of specific invoices.
