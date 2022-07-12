from .models import Tag, Manufacturer, Product

MANUFACTURERS = (
    'Microlife', 'Beurer', 'Bausch & Lomb', 'Doctor Klaus', 'Samsung', 'Trek', 'Specialized', 'Xiaomi'
)

TAGS = (
    {'name': 'sports', 'quantity': 2, 'discount': 10},
    {'name': 'health', 'quantity': 5, 'discount': 20},
    {'name': 'electronics', 'quantity': 4, 'discount': 30}
)

PRODUCTS = (
    {
        'name': 'Mi Smart Band 6',
        'description': 'фитнес-браслет, поддержка Android/iOS, экран AMOLED 1.56" (152x486, сенсорный),'
                       'шагомер, пульсометр, время работы: 2 недели, корпус: пластик, браслет: силикон',
        'amount': 200,
        'price': 129.50,
        'manufacturer': Manufacturer.objects.get(name='Xiaomi')
    },
    {
        'name': 'Galaxy Fit2',
        'description': 'фитнес-браслет, поддержка Android/iOS, экран AMOLED 1.1" (126x294, сенсорный),'
                       'шагомер, пульсометр, время работы: 3 недели, корпус: пластик, браслет: силикон',
        'amount': 26,
        'price': 200,
        'manufacturer': Manufacturer.objects.get(name='Samsung')
    },
    {
        'name': 'Rockhopper Expert 29 M 2021',
        'description': '29", рама M, горный, трэйл, алюминий, вилка амортизационная с ходом 100 мм (алюминий),'
                       'трансмиссия 12 скор. (1х12), переключатели: задний Sram SX Eagle,'
                       'тормоз дисковый гидравлический',
        'amount': 5,
        'price': 3729,
        'manufacturer': Manufacturer.objects.get(name='Specialized')
    },
    {
        'name': 'FX 1 M 2021',
        'description': '28", рама M, городской, алюминий, вилка жесткая (сталь Hi-ten), трансмиссия 21 скор. (3х7),'
                       'переключатели: задний Shimano Altus/передний Shimano Tourney,'
                       'тормоз ободной механический, вес 12.57 кг',
        'amount': 8,
        'price': 1489,
        'manufacturer': Manufacturer.objects.get(name='Trek')
    },
    {
        'name': 'Galaxy S21 5G 8GB/256GB',
        'description': 'Android, экран 6.2" AMOLED (1080x2400), Exynos 2100, ОЗУ 8 ГБ, флэш-память 256 ГБ,'
                       'камера 64 Мп, аккумулятор 4000 мАч, 2 SIM',
        'amount': 21,
        'price': 3207.44,
        'manufacturer': Manufacturer.objects.get(name='Samsung')
    },
    {
        'name': 'Relins',
        'description': 'Раствор для линз, 360 мл.',
        'amount': 48,
        'price': 22.70,
        'manufacturer': Manufacturer.objects.get(name='Doctor Klaus')
    },
    {
        'name': 'ReNu MultiPlus 360',
        'description': 'Раствор для линз, 360 мл, контейнер в комплекте',
        'amount': 48,
        'price': 26.85,
        'manufacturer': Manufacturer.objects.get(name='Bausch & Lomb')
    },
    {
        'name': 'NC 200',
        'description': 'инфракрасный термометр, лобный/бесконтактный способ измерения,'
                       'результат: 3 секунды, память: с указанием времени/30 измерений',
        'amount': 96,
        'price': 240.15,
        'manufacturer': Manufacturer.objects.get(name='Microlife')
    },
    {
        'name': 'BY11',
        'description': 'электронный термометр, подмышечный/оральный/ректальный способ измерения,'
                       'результат: 10 секунд, память: 1 измерение, с гибким наконечником, водонепроницаемый',
        'amount': 149,
        'price': 24.57,
        'manufacturer': Manufacturer.objects.get(name='Beurer')
    },
)


def add_manufacturers():
    for manufacturer in MANUFACTURERS:
        Manufacturer.objects.create(name=manufacturer)
    print('Manufacturers added')


def add_tags():
    for tag in TAGS:
        Tag.objects.create(**tag)
    print('Tags added')


def add_products():
    for product in PRODUCTS:
        Product.objects.create(**product)
    print('Products added!')
