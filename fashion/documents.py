from django_elasticsearch_dsl import DocType, Index
from fashion.models import Fashion

fashion = Index('fashion')

fashion.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@fashion.doc_type
class FashionDocument(DocType):
    class Meta:
        model = Fashion

        fields = [
            'image_id',
            'image_path',
            'embedding',
            'pub_date',
            'enable',
        ]
