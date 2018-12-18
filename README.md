# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK

## Requirements
- Python 3.6
- Django (1.10, 1.11, 2.0)
- Django REST Framework
- Django Rest Auth

## Installation
```
	pip install django
	pip install djangorestframework
	pip install django-rest-auth
	pip install django-allauth
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `products`, so we will use the following URLS - `/products/` and `/products/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`products` | GET | READ | Get all products
`products/:id` | GET | READ | Get a single product
`products`| POST | CREATE | Create a new product
`products/:id` | PUT | UPDATE | Update a product
`products/:id` | DELETE | DELETE | Delete a product

## Use
We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation). Httpie is a user friendly http client that's written in Python. Let's install that.

You can install httpie using pip:
```
pip install httpie
```

First, we have to start up Django's development server.
```
	python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
	http  http://127.0.0.1:8000/api/v1/products/3
```
we get:
```
 {  "detail":  "Authentication credentials were not provided."  }
```
Instead, if we try to access with credentials:
```
	http http://127.0.0.1:8000/api/v1/products/3 "Authorization: Token 7530ec9186a31a5b3dd8d03d84e34f80941391e3"
```
we get the product with id = 3
```
{  "name":  "MagoGel",  "description":  "Mago procudts",  "year":  2019,  "created_by":  "admin"  }
```

## Login and Tokens

To get a token first we have to login
```
	http http://127.0.0.1:8000/rest-auth/login/ username="admin" password="root1234"
```
after that, we get the token
```
{
    "key": "2d500db1e51153318e300860064e52c061e72016"
}
```
**ALL request must be authenticated with a valid token, otherwise they will be invalid**

We can create new users. (password1 and password2 must be equal)
```
http POST http://127.0.0.1:8000/rest-auth/registration/ username="USERNAME" password1="PASSWORD" password2="PASSWORD"
```
And we can logout, the token must be your actual token
```
http POST http://127.0.0.1:8000/rest-auth/logout/ "Authorization: Token <YOUR_TOKEN>" 
```

The API have some restrictions:
-   The products are always associated with a created_by (user who created it).
-   Only authenticated users may create and see products.
-   Only the created_by of a product may update or delete it.
-   Unauthenticated requests shouldn't have access.

### Commands
```
http http://127.0.0.1:8000/api/v1/products/ "Authorization: Token <YOUR_TOKEN>"
http GET http://127.0.0.1:8000/api/v1/products/3 "Authorization: Token <YOUR_TOKEN>"
http POST http://127.0.0.1:8000/api/v1/products/ "Authorization: Token <YOUR_TOKEN>" name="MagoGel" description="Mago Product" year=2018
http PUT http://127.0.0.1:8000/api/v1/products/3 "Authorization: Token <YOUR_TOKEN>" name="MagoGel" description="Mago Product" year=2018
http DELETE http://127.0.0.1:8000/api/v1/products/3 "Authorization: Token <YOUR_TOKEN>"
```
Finally, I provide a DB to make these tests.

