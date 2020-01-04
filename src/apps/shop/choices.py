class OrderCartStatusChoices:
    """ Choices status cart """
    NEW = 'NEW'
    AWAITING = 'AWAITING'
    CREATING = 'CREATING'
    SHIPPING = 'SHIPPING'
    COMPLETED = 'COMPLETED'

    CHOICES = (
        (NEW, 'новый'),
        (AWAITING, 'ожидает оплаты'),
        (CREATING, 'изготовление'),
        (SHIPPING, 'доставка'),
        (COMPLETED, 'завершен'),
    )
