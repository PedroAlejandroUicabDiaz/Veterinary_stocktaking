#!/bin/bash
# Automatin migration and set of superuser

python manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('master', 'alekarhurjas@gmail.com', 'theoneaboveall')" | python manage.py shell