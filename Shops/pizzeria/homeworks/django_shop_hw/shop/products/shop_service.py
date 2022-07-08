from .models import Tag, Manufacturer, Product


class ProductsService:
    _products_filters = {
        'price_lte': lambda product, value: product.filter(price__lte=float(value)),
        'price_gte': lambda product, value: product.filter(price__gte=float(value)),
        'price_lt': lambda product, value: product.filter(price__lt=float(value)),
        'price_gt': lambda product, value: product.filter(price__gt=float(value)),
        'tags': lambda product, value: product.filter(tags__name=value)
    }

    def add_product(self, **kwargs):
        tags = kwargs.pop('tags')
        new_product = Product.objects.create(**kwargs)
        new_product.tags.set(tags)
        new_product.save()

    def get_product_by_uuid(self, product_uuid: str) -> Product:
        return Product.objects.select_related('manufacturer').prefetch_related('tags').get(uuid=product_uuid)

    def filter_products(self, url_query_params: dict) -> 'QuerySet':
        query_params = self._format_query_params(url_query_params)
        products = Product.objects.all()
        for arg, values in query_params.items():
            for value in values:
                query_filter = self._products_filters.get(arg, None)
                if query_filter:
                    products = query_filter(products, value)
        return products

    def _format_query_params(self, url_query_params: dict) -> dict:
        return {key: value.replace(' ', '').strip().split(",") for key, value in url_query_params.items()}
