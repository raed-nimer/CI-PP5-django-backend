# Introduction

Powerhouse is a cutting-edge B2C eCommerce platform dedicated to gym enthusiasts, athletes, and anyone passionate about fitness. Specializing in high-quality gymwear and top-tier fitness equipment, Powerhouse offers a seamless online shopping experience tailored to individuals who demand both performance and style. From breathable, functional activewear to heavy-duty home gym gear, every product is curated to support serious training and everyday workouts alike. With user-friendly navigation, and fast delivery, Powerhouse is the go-to online destination for fitness lovers looking to gear up and level up—all in one powerful platform.
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
