from django.core.management.base import BaseCommand, CommandError
from fashion.models import Fashion
from fashion.embedding import Embedding
from django.db import transaction
from tqdm import tqdm
from tabby_search.settings import QUANTITATION_FACTOR

class Command(BaseCommand):
    help = 'Generate Embedding Command'

    def add_arguments(self, parser):
        parser.add_argument('data_path', nargs='+', type=str)

    @transaction.atomic
    def orm_bulk_create(self, step = 200, words = None, path = None, image_id = None):
        if not words and not path:
            return False
        if len(words) < step:
            step = len(words)
        instances = [
            Fashion(
                image_path=str(path[i]),
                embedding=str(words[i]),
                image_id=str(image_id[i])
            )
            for i in range(0, step)
        ]

        Fashion.objects.bulk_create(instances)

    def handle(self, *args, **options):
        try:
            data_path = options['data_path'][0]
            Q = QUANTITATION_FACTOR
            embedding = Embedding(data_path=data_path)
            step = 200
            embs = embedding.get_embs()
            path = embedding.get_paths()
            image_id = embedding.get_img_ids()
            self.stdout.write(self.style.SUCCESS('Loading word embedding...'))
            words = embedding.quantization_factor(embed=embs, Q=Q)
            self.stdout.write(self.style.SUCCESS('Add to database...'))
            for i in tqdm(range(0, len(embs), step)):
                if i + step < len(embs):
                    self.orm_bulk_create(step=step, path=path[i : i + step], words=words[i : i + step], image_id = image_id[i : i + step])
                else:
                    self.orm_bulk_create(step=step, path=path[i : len(embs)], words=words[i : len(embs)], image_id = image_id[i : len(embs)])
        except Fashion.DoesNotExist:
            raise CommandError('Database Error')

        self.stdout.write(self.style.SUCCESS('Successfully add embedding to database'))