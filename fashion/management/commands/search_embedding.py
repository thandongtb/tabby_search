from django.core.management.base import BaseCommand
from fashion.models import Fashion
from watson import search as watson

class Command(BaseCommand):
    help = 'Seach Embedding'

    def add_arguments(self, parser):
        parser.add_argument('embedding', nargs='+', type=str)

    def handle(self, *args, **options):
        search_results = watson.filter(Fashion, "Your search text")
        for result in search_results:
            print(result.path, result.image_path)
        self.stdout.write(self.style.SUCCESS('Search embedding successful'))