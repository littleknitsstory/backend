Quick start
-----------

1. Add "lks" to your INSTALLED_APPS setting like this::

        INSTALLED_APPS = [
            'lks'
        ]

2. Include the lks API in your project api/urls.py like this::

        path('lks/', include('lks.api.v1')),

3. Run ``python manage.py migrate`` to create the lks models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a lks (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/lks/ to participate in the api.