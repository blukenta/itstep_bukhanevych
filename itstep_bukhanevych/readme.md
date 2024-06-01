# To-Do List
## Project Description
This project is a management of user's to do tasks on a website. 

All created tasks are displayed on the landing page, and the task creation button is also activated. The navbar sections and the task filter button are created for a cosmetic appearance. When successfully creating a new task, the user must enter the title of the task and the date of its completion. Including, after entering the data, you must pass the reCAPTCHA check, otherwise the task will not be created. After creating a task, it will be displayed in the general list of tasks with the following information: title, due date, completion status.

## DDoS Attack Protection


This project has two types of protection:
1. __Google reCAPTCHA__
2. __Rate limit__

The first method prevents the robot from creating any tasks. If, when creating a new task, you do not go through the official reCAPTCHA from Google, then the task will not be created. 

The second method prevents the same user from visiting the site multiple times. If a user exceeds the limit for entering the site within a short period of time, his access to the site will be terminated.

## Project Toolkit

| Backend  | Frontend | Additional |
| :-------------: |:-------------:|:-------------:|
| Python       | HTML            | icons        |
| Django       | CSS             |extensions    |
|              | JavaScript      |recaptcha     |
|              |                 |ratelimit     |
  

## Pre-Work Setup

1. Switch to the general project folder in terminal:
```
cd itstep_bukhanevych
```
2. Install all backend required dependencies:
```
pip install django
pip install django_icons
pip install django_extensions
pip install django_recaptcha
pip install django_ratelimit
```
3. Update dependency inclusion:
```
py manage.py makemigrations
py manage.py migrate
```
4. Change captcha keys in file `settings.py`:
```
RECAPTCHA_PUBLIC_KEY = 'your public key'
RECAPTCHA_PRIVATE_KEY = 'your private key'
```
> _Offical Google reCAPTCHA keys you can obtain [here](https://www.google.com/recaptcha)._

5. Start the server:
```
py manage.py runserver
```

## Website Frontend

![To-Do List](https://cdn.discordapp.com/attachments/910148729460359220/1246549310942740640/image.png?ex=665ccb03&is=665b7983&hm=bce2aa7b3babef988d6aed4cbe27b3b4e94cde3638bbf56d2897f5c30d01f312& "To-Do List")