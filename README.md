# Website and management system for my team

## Description

This is a Django project which include two apps, a website and a team member management. 

- Example: [Demo1](http://skyrover.charlieli.cn/),[Demo2](http://skyrover.charlieli.cn/manage/login)


## Deployment

### Postgres

Here I use [PostgreSQL](http://www.postgresql.org/) as my database, you can choose to use sqlite3 and skip this step for your convenient.

- Install [PostgreSQL](http://www.postgresql.org/).
- PostgreSQL configuration

```bash
$ psql postgres
```

To Make sure your database could be visited remotely,edit the `postgresql.conf` and modify `\#listen_addresses = ‘localhost’` to `listen_addresses = ‘*’ ` to listen to anywhere, `\#password_encryption = on` to `password_encryption = on` to enable password authentication. Edit `pg_hba.conf`, add `host all all 0.0.0.0 0.0.0.0 md5` to the last line to allow your client visiting postgresql server.

Linux:

```bash
$ vi /etc/postgresqlpv/9.4/main/postgresql.conf
$ vi /etc/postgresql/9.4/main/pg_hba.conf
```

or Mac:

```bash
$ vi /usr/local/var/postgres/postgresql.conf
$ vi /usr/local/var/postgres/pg_hba.conf
```

Restart PostgreSQL server

Linux:

```bash
$ /etc/init.d/postgresql restart
```

or Mac:

```bash
$ pg_ctl restart -D /usr/local/var/postgres
```

Create your own database

```bash
$ psql postgres
$ postgres=# create user “charlie” with password ‘123456’ nocreatedb;
$ postgres=# create database “charlieDB” with owner=”charlie”;
$ \q
```

You can test your database by

```bash
psql charlieDB
```

- Install psycopg2 to enable the connection bwtween django and postgresql

Linux:

```bash
$ sudo apt-get install python-psycopg2
```

or Mac:

```bash
$ sudo pip install psycopg2
```

Test if it's installed properly.

```bash
    $ python
    >>> import psycopg2
    >>> psycopg2.apilevel
	’2.0′
```

### Set up

- Git clone

```bash
$ git clone git@github.com:CCharlieLi/StaffManagmentSystem.git
```

- Edit settings.py to meet your PostgreSQL configuration

```
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'charlieDB',        #YOUR DATABASE NAME
    'USER': 'charlie',          #YOUR DATABASE USERNAME
    'PASSWORD': '123456',       #YOUR DATABASE PASSWORDch
    'HOST': '',
    'PORT': '5432',
}
```

- Synchronize model and database

```bash
$ python manage.py makemigrations
$ python manage.py migrate  
```

If you see something like this, you are good to go.

```bash
$ python manage.py makemigrations
Migrations for 'userapp':
  0001_initial.py:
    - Create model Appuser
$ python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, contenttypes, userapp, auth, sessions
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying sessions.0001_initial... OK
  Applying userapp.0001_initial... OK
```

- Install [Django REST framework](http://www.django-rest-framework.org/)

Note that REST framework requires the following:

```
Python (2.6.5+, 2.7, 3.2, 3.3, 3.4)
Django (1.5.6+, 1.6.3+, 1.7+, 1.8)
```

The following packages are optional:

```
Markdown (2.1.0+) - Markdown support for the browsable API.
django-filter (0.9.2+) - Filtering support.
django-guardian (1.1.1+) - Object level permissions support.
```

Install Django REST framework with: 

```bash
$ pip install djangorestframework
$ pip install markdown       # Markdown support for the browsable API.
$ pip install django-filter  # Filtering support
```

or clone the project from github and copy `rest_framework` folder to your project dictionary.(recommended)

```bash
$ git clone git@github.com:tomchristie/django-rest-framework.git
```

Add `rest_framework` to your INSTALLED_APPS setting.

```
INSTALLED_APPS = (
    ...
    'rest_framework',
)
```

If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. Add the following to your root urls.py file.

```
urlpatterns = [
    ...
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```


- Run and try

```bash
$ python manage.py runserver

System check identified no issues (0 silenced).
August 28, 2015 - 12:37:18
Django version 1.9.dev20150827233257, using settings 'XXX.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```


## License

MIT

## Contact

CCharlieLi(ccharlieli@live.com)

