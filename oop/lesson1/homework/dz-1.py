'''
Домашка
1. Создать классы Oxygen, Chlorine, Iron. (Один на выбор)
2. В качестве свойств описать температуру замерзания, плавления,
испарения
3. Написать метод agg_state(self, t), который принимает температуру в градусах цельсия и возвращает строчное представление текущего агрегатного состояния."
4. Добавить параметр шкалы измерения (цельсий, фаренгейт, кельвин).
5. Создать родительский класс Element, в котором будут содержаться
все методы.
6. Добавить метод для конвертации из одной шкалы в другую.
'''

class Element(object):

    # Setting base class variables on initialization
    def __init__(self, name, melt_temp, gaseous_temp, current_scale):
        self.name = name
        self.melt_temp = melt_temp
        self.gaseous_temp = gaseous_temp
        # making sure the scale value is correct
        if current_scale not in list(self.SCALES.keys()):
            raise ValueError(f'Scale argument is wrong, use one of these: {list(self.SCALES.keys())}')
        else:
            self.current_scale = current_scale

    # Immutable temperature scales
    SCALES = {
        'celsius': {
            'full_name': 'celsius scale',
            'short_name': 'celsius'
        },
        'fahrenheit': {
            'full_name': 'Fahrenheit scale',
            'short_name': 'fahrenheit'
        },
        'kelvin': {
            'full_name': 'Kelvin scale',
            'short_name': 'kelvin'
        }
    }

    # Immutable element states
    STATES = {
        'liquid': 'Liquid state',
        'gaseous': 'Gaseous state',
        'solid': 'Solid state'
    }

    def agg_state(self, t):
        if t < self.melt_temp:
            return f'{self.name}. Temp is {t} - {self.STATES["solid"]}'
        elif self.melt_temp < t < self.gaseous_temp:
            return f'{self.name}. Temp is {t} - {self.STATES["liquid"]}'
        else:
            return f'{self.name}. Temp is {t} - {self.STATES["gaseous"]}'

    # Any to any converter. Based on the current_scale. Dict is returned
    def convert(self, t):
        celsius = self.SCALES['celsius']['short_name']
        fahrenheit = self.SCALES['fahrenheit']['short_name']
        kelvin = self.SCALES['kelvin']['short_name']
        scale = self.current_scale

        return {
            celsius: round((t if scale == celsius else(t - 273.15 if scale == kelvin else ((t - 32) * 5 / 9 if scale == fahrenheit else ('Error. Wrong input')))), 2),
            fahrenheit: round((t if scale == fahrenheit else ((t - 273.15) * 5 / 9 + 32 if scale == kelvin else (t * 9 / 5 + 32 if scale == celsius else 'Error. Wrong input'))), 2),
            kelvin: round((t if scale == kelvin else (t + 273.15 if scale == celsius else ((t - 32) * 5 / 9 + 273.15 if scale == fahrenheit else 'Error. Wrong input'))), 2)
        }


# Creating Iron class instance with valid data
iron = Element('Iron', 1538, 2862, 'celsius')

# Checking the value state in different temperatures:
# Solid
print(iron.agg_state(22))
# Liquid
print(iron.agg_state(1540))
# Gaseous
print(iron.agg_state(3000))

# Converting temperature
print(iron.convert(45))
