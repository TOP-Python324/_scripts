class Acoustic:
    # поле (невызываемый атрибут) класса
    material: str = 'wood'
    
    # конструктор
    def __init__(self, main_diameter: float, channels: int = 2):
        # атрибуты экземпляра
        self.channels = channels
        self.diameter = main_diameter


sony_px100 = Acoustic(3.5)

# вызов объекта класса Acoustic() приводит к вызову метода __call__() метакласса type:
# def type.__call__(cls, *args, **kwargs):
#     instance = cls.__new__(*args, **kwargs)
#     cls.__init__(instance, *args, **kwargs)
#     return instance

# >>> sony_px100.__dict__
# {'channels': 2, 'diameter': 3.5}

hedd_type07 = Acoustic(7.0)

# >>> hedd_type07.__dict__
# {'channels': 2, 'diameter': 7.0}

sven_rx1000 = Acoustic(3.0, 6)

# >>> sven_rx1000.__dict__
# {'channels': 6, 'diameter': 3.0}


# >>> sony_px100.material
# 'wood'
# >>> hedd_type07.material
# 'wood'
# >>> sven_rx1000.material
# 'wood'

# >>> Acoustic.material = 'fiberboard'
# >>>
# >>> sony_px100.material
# 'fiberboard'
# >>> hedd_type07.material
# 'fiberboard'
# >>> sven_rx1000.material
# 'fiberboard'

# >>> hedd_type07.material = 'wood'
# >>> hedd_type07.__dict__
# {'channels': 2, 'diameter': 7.0, 'material': 'wood'}
# >>> hedd_type07.material
# 'wood'
