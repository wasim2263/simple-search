import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'simple_search.settings')

django.setup()

from django_seed import Seed

from developersearch.models import Developers, ProgrammingLanguages, Languages

seeder = Seed.seeder()
seeder.add_entity(Developers, 100)
seeder.execute()

developers = Developers.objects.all()
programming_languages = ProgrammingLanguages.objects.all()
languages = Languages.objects.all()
for dev in developers:
    for language in languages:
        if (language.id % 2 == 0 and dev.id % 2 == 0) or (language.id % 2 != 0 and dev.id % 2 != 0):
            continue
        dev.languages.add(language)
    for programming_language in programming_languages:
        if (programming_language.id % 2 == 0 and dev.id % 2 == 0) or (programming_language.id % 2 != 0 and dev.id % 2 != 0):
            continue
        dev.programming_languages.add(programming_language)
