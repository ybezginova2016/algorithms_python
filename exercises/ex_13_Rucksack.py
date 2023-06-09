"""
Задача 2: Рюкзак

Турист собирается в поход. Он сможет нести N кг вещей.
Но вещей, которые он запланировал уложить в рюкзак, оказалось
намного больше. Нужно определить, какие вещи от наиболее
тяжелых к самым легким поместятся в рюкзак.
"""

things = {'зажигалка': 20,
          'компас': 100,
          'фрукты': 500,
          'рубашка': 300,
          'термос': 1000,
          'аптечка': 200,
          'куртка': 600,
          'бинокль': 400,
          'удочка': 1200,
          'салфетки': 40,
          'бутерброды': 820,
          'палатка': 5500,
          'спальный мешок': 2250,
          'жвачка': 10}

weight = int(input('Please enter the weight: ')) * 1000

sorted_things = dict(sorted(things.items(), key=lambda x: -x[1]))

for k, w in sorted_things.items():
    if w <= weight:
        print(k, sep='\n')

        weight -= w
