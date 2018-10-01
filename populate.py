import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'simple_search.settings')

django.setup()

from django_seed import Seed

seeder = Seed.seeder()

from developersearch.models import Developers, ProgrammingLanguages, Languages

seeder.add_entity(Developers, 100)
seeder.execute()
developers = Developers.objects.all()
programmin_languages = ProgrammingLanguages.objects.all()
languages = Languages.objects.all()

for dev in developers:
    for programmin_language in programmin_languages:
        if (programmin_language.id % 2 == 0 and dev.id % 2 == 0) or (
                programmin_language.id % 2 != 0 and dev.id % 2 != 0):
            continue
        programmin_language.developers.add(dev)
    for language in languages:
        if (language.id % 2 == 0 and dev.id % 2 == 0) or (
                language.id % 2 != 0 and dev.id % 2 != 0):
            continue
        language.developers.add(dev)
