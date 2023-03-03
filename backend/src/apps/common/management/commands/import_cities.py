import yaml
from django.core.management.base import BaseCommand, CommandError

from ...models import City


class Command(BaseCommand):
    help = "Import cities from a yaml file"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_NOT_MODIFIED(
                "Import cities... wait...",
            )
        )
        City.objects.all().delete()
        try:
            with open(
                "src/apps/common/fixtures/cities.yaml",
                "r",
            ) as yaml_file:
                data = yaml.safe_load(yaml_file)
                i = 0
                for item in data:
                    City.objects.create(name=item["name_uz"], region_id=item["region_id"])
                    i += 1
        except FileNotFoundError as e:
            raise CommandError("File cities yaml doesn't exists") from e

        self.stdout.write(self.style.SUCCESS(f"{str(i)} cities successfully imported"))
