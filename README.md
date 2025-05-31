# Introduction

Powerhouse is a cutting-edge B2C eCommerce platform dedicated to gym enthusiasts, athletes, and anyone passionate about fitness. Specializing in high-quality gymwear and top-tier fitness equipment, Powerhouse offers a seamless online shopping experience tailored to individuals who demand both performance and style. From breathable, functional activewear to heavy-duty home gym gear, every product is curated to support serious training and everyday workouts alike. With user-friendly navigation and fast delivery, Powerhouse is the go-to online destination for fitness lovers looking to gear up and level up—all in one powerful platform.
### Project Goals

# User Stories

## Database Schemas

### User model

- The user model is the default Django user model.

| key          | Field Type    | Validation                  |
| ------------ | ------------- | --------------------------- |
| id           | IntegerField  |                             |
| password     | CharField     | max_length=128              |
| last_login   | DateTimeField |                             |
| is_superuser | BooleanField  |                             |
| username     | CharField     | max_length=150, unique=True |
| first_name   | CharField     | max_length=150, blank=True  |
| last_name    | CharField     | max_length=150, blank=True  |
| email        | EmailField    | max_length=254, unique=True |
| is_staff     | BooleanField  |                             |
| is_active    | BooleanField  |                             |
| date_joined  | DateTimeField |                             |

### Product model

- The product model is used to store all the available products.

| key         | Field Type      | Validation                                        |
| ----------- | --------------- | ------------------------------------------------- |
| id          | BigIntegerField | primary_key=True                                  |
| name        | CharField       | max_length=200                                    |
| description | TextField       |                                                   |
| price       | IntegerField    |                                                   |
| category    | ForeignKey      | Category, on_delete=models.SET_NULL               |
| image       | CloudinaryField |                                                   |
| created_at  | DateTimeField   | auto_now_add=True                                 |
| updated_at  | DateTimeField   | auto_now=True                                     |

### Category model

- The category model is used to store categories of products.

| key        | Field Type      | Validation        |
| ---------- | --------------- | ----------------- |
| id         | BigIntegerField | primary_key=True  |
| name       | CharField       | max_length=200    |
| created_at | DateTimeField   | auto_now_add=True |
| updated_at | DateTimeField   | auto_now=True     |

### Cart Item model

- The Cart item model is used to store cart items.

| key        | Field Type      | Validation                        |
| ---------- | --------------- | -----------------                 |
| id         | BigIntegerField | primary_key=True                  |
| quantity   | IntegerField    |                                   |
| user       | ForeignKey      | User, on_delete=models.CASCADE    |
| product    | ForeignKey      | Product, on_delete=models.CASCADE |
| added_at   | DateTimeField   | auto_now_add=True                 |

### ContactFormResponse model

- The ContactFormResponse model stores all contact forms sent to support/developers from users.

| key         | Field Type      | Validation       |
| ----------- | --------------- | ---------------- |
| id          | BigIntegerField | primary_key=True |
| name        | CharField       | max_length=100   |
| email       | CharField       | max_length=100   |
| subject     | CharField       | max_length=100   |
| description | TextField       |                  |

### Order model

- The Order model stores all orders placed by users.

| key           | Field Type      | Validation                      |
| -----------   | --------------- | ----------------                |
| id            | BigIntegerField | primary_key=True                |
| total_price   | IntegerField    |                                 |
| user          | ForeignKey      | User, on_delete=models.CASCADE  |
| first_name    | CharField       | max_length=100                  |
| last_name     | CharField       | max_length=100                  |
| email         | CharField       | max_length=255                  |
| state         | CharField       | max_length=100                  |
| address       | CharField       | max_length=255                  |
| zip           | CharField       | max_length=20                   |
| country       | CharField       | max_length=100                  |
| payment_method| CharField       | max_length=20                   |
| created_at    | DateTimeField   | auto_now_add=True               |


### Order Item model

- The Order Item model stores all items/products of an Order.

| key               | Field Type      | Validation                        |
| ------------------| --------------- | --------------------------------  |
| id                | BigIntegerField | primary_key=True                  |
| quantity          | IntegerField    |                                   |
| price_at_purchase | IntegerField    |                                   |
| product           | ForeignKey      | Product, on_delete=models.CASCADE |
| order             | ForeignKey      | Order, on_delete=models.CASCADE   |


## Agile development

Link to my [GitHub Agile Project](https://github.com/users/raed-nimer/projects/3)

## Tools and technologies used

### Languages and Frameworks

This project was created using the following languages and frameworks:

- [Django](https://www.djangoproject.com/) as the Python web framework.
- [Python](https://www.python.org/) as the backend programming language.

### Django Packages
| Packages                                                                   | Description (copied from the web) |
| :------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Django](https://pypi.org/project/Django/)                                 | Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.|
| [Pillow](https://pypi.org/project/Pillow/)                                 | PIL is the Python Imaging Library.|
| [gunicorn](https://pypi.org/project/gunicorn/)                             | Gunicorn, 'Green Unicorn', is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, implemented, light on server resource usage, and fairly speedy. |
| [psycopg2](https://pypi.org/project/psycopg2/)                             | Psycopg is the most popular PostgreSQL database adapter for the Python programming language.|
| [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) | Django package that provides Cloudinary storage for both media and static files and management commands for removing unnecessary files.|
| [dj-database-url](https://pypi.org/project/dj-database-url/)               | Use Database URLs in your Django Application.|
| [cloudinary](https://pypi.org/project/cloudinary/)                         | The Cloudinary Python SDK allows you to quickly and easily integrate your application with Cloudinary. Effortlessly optimize, transform, upload, and manage your cloud's assets.|
| [urllib3](https://pypi.org/project/urllib3/) | HTTP library with thread-safe connection pooling, file post, and more. |  

### Other tools and programs

- [Visual Studio Code.](https://code.visualstudio.com/) Did all of my coding and synchronizing with GitHub on VS Code.
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for hosting repositories.
- [Heroku](https://www.heroku.com/) where the backend Django app is deployed.
- [Grammarly](https://www.grammarly.com/) was used to double-check spelling mistakes.
- [Lucid](https://lucid.co/) was used to create database ERD

# Testing

### PEP8 Code Institute Python Linter Validation

- All Python files were tested and passed through the [Code Institute PEP8](https://pep8ci.herokuapp.com/) linter validator.

#### Powerhouse app

| File        | Result                                                          |
| ----------- | --------------------------------------------------------------- |
| urls.py     | ![PEP8 Linter](staticfiles/python-linter.png)                   |
| settings.py | All clear, no errors found                                      |

#### accounts app

| File      | Result                     |
| --------- | -------------------------- |
| admin.py  | All clear, no errors found |
| apps.py   | All clear, no errors found |
| models.py | All clear, no errors found |
| tests.py  | All clear, no errors found |
| urls.py   | All clear, no errors found |
| views.py  | All clear, no errors found |

#### base app

| File      | Result                     |
| --------- | -------------------------- |
| admin.py  | All clear, no errors found |
| apps.py   | All clear, no errors found |
| models.py | All clear, no errors found |
| tests.py  | All clear, no errors found |
| urls.py   | All clear, no errors found |
| views.py  | All clear, no errors found |

#### cart app

| File      | Result                     |
| --------- | -------------------------- |
| admin.py  | All clear, no errors found |
| apps.py   | All clear, no errors found |
| models.py | All clear, no errors found |
| tests.py  | All clear, no errors found |
| urls.py   | All clear, no errors found |
| views.py  | All clear, no errors found |

#### orders app

| File      | Result                     |
| --------- | -------------------------- |
| admin.py  | All clear, no errors found |
| apps.py   | All clear, no errors found |
| models.py | All clear, no errors found |
| tests.py  | All clear, no errors found |
| urls.py   | All clear, no errors found |
| views.py  | All clear, no errors found |

#### product app

| File      | Result                     |
| --------- | -------------------------- |
| admin.py  | All clear, no errors found |
| apps.py   | All clear, no errors found |
| models.py | All clear, no errors found |
| tests.py  | All clear, no errors found |
| urls.py   | All clear, no errors found |
| views.py  | All clear, no errors found |


# Deployment

### Deploy with Heroku

1. Login to [Heroku](https://www.heroku.com/) if you already have an account or [sign up](https://signup.heroku.com/) if you don't.
2. Click on the "New" button on the top right of the home page and select "Create new App" from the drop-down menu.
3. In the "App name" field, enter the unique name of your app.
   - Heroku displays a green tick if your app name is available.
4. In the "Choose a region" field, choose either the United States or Europe based on your location.
5. Click the "Create app" button.
6. Next page, top centre of the screen, select the "Settings" tab.
7. In the "Config Vars" section, click on the "Reveal config Vars" button.
8. Add environment variables from the local env.py file to the "Config Vars" section:
   - SECRET_KEY - Django secret key.
   - DATABASE_USER - Database user.
   - DATABASE_HOST - Database host.
   - DATABASE_NAME - Database name.
   - DATABASE_PASS - Database password.
   - CLOUDINARY_URL - Cloudinary API URL
9. Copy and paste these variables into the KEY field and their values into the VALUE field.
10. Select the "Deploy" tab at the top of the screen.
11. In the "Deployment method" section, select "GitHub".
    1. In "Connect to GitHub," click on the "Search" button. Find the project repository in the list and click on the "Connect" button.
    2. Scroll to the bottom of that page. Click on the "Deploy Branch" button to deploy.
    3. You should also see an option to enable automatic deployment. If you enable this, every time you push to GitHub, Heroku will automatically deploy the app.
12. Once the build starts, you should be able to see the logs at the bottom of the page. After successfully finishing building the app, you should see the link to your app.
