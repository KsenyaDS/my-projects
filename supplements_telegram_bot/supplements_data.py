danger_levels = {
  'none': 'none',
  'zero': 'zero',
  'very_low': 'very_low',
  'low': 'low',
  'medium': 'medium',
  'high': 'high',
  'very_high': 'very_high',
}

danger_levels_names = {
  danger_levels['none']: 'неизвестная опасность',
  danger_levels['zero']: 'нулевая опасность',
  danger_levels['very_low']: 'очень низкая опасность',
  danger_levels['low']: 'низкая опасность',
  danger_levels['medium']: 'средняя опасность',
  danger_levels['high']: 'высокая опасность',
  danger_levels['very_high']: 'очень высокая опасность',
}

danger_levels_order = [
  danger_levels['none'],
  danger_levels['very_high'],
  danger_levels['high'],
  danger_levels['medium'],
  danger_levels['low'],
  danger_levels['very_low'],
  danger_levels['zero']
]

danger_levels_info = {
  danger_levels['none']: (f'<b>⚪ Неизвестно. Добавка не изучена</b>'),
  danger_levels['zero']: f'<b>🟢  Разрешено. Нет опасности</b>',
  danger_levels['very_low']: f'<b>🟢 Разрешено. Очень низкая опасность</b>',
  danger_levels['low']: f'<b>🟢  Разрешено. Низкая опасность</b>',
  danger_levels['medium']: f'<b>🟡 Не рекомендуется. Средняя опасность</b>',
  danger_levels['high']: f'<b>🔴 Запрещено. Высокая опасность</b>',
  danger_levels['very_high']: f'<b>🔴 Запрещено. Очень высокая опасность</b>',
}



supplements_info = [
  {
    'code': '100',
    'variants': [],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '100i',
    'variants': ['100(i)','куркумин','куркум','curcumin'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '100ii',
    'variants': ['100(ii)','turmeric','турмерик'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '101',
    'variants': ['b2', 'витамин в2', 'рибофлавин'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '102',
    'variants': ['тартразин'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '103',
    'variants': ['алканин', 'алканет','алкана'],
    'danger_level': danger_levels['high']
  },
  {
    'code': '104',
    'variants': ['хинолиновый желтый', 'желтый хинолиновый', 'хинолин желтый', 'желтый хинолин' 'quinoline yellow'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '105',
    'variants': ['желтый прочный ab'],
    'danger_level': danger_levels['high']
  },
  {
    'code': '106',
    'variants': ['e106', 'рибофлавин-5"-фосфат натрия','рибофлавин-5′-фосфат натриевая соль'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '107',
    'variants': ['жёлтый 2g'],
    'danger_level': danger_levels['high']
  },
  {
    'code': '110',
    'variants': ['солнечный закат'],
    'danger_level': danger_levels['high']
  },
  {
    'code': '1100',
    'variants': ['амилаза'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '1103',
    'variants': ['инвертаза'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '1104',
    'variants': ['липаза'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '1105',
    'variants': ['афилакт','лизоцим'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '111',
    'variants': ['оранжевый ggn','альфа-нафтол оранжевый'],
    'danger_level': danger_levels['very_high']
  },
  {
    'code': '120',
    'variants': ['кармин', 'carmine', 'carmin', 'карминовая кислота', 'кислота красная карминовая'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '1200',
    'variants': ['polydextrose','полидекстроз'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '1201',
    'variants': ['polyvinylpyrrolidone','поливинилпирролидон'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '1203',
    'variants': ['polyvinyl alcohol','поливиниловый спирт'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '1204',
    'variants': ['pullulan','пуллулан'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '122',
    'variants': ['кармуазин', 'азорубин', 'красный р', 'кармазин', 'червоний p', 'азарубин'],
    'danger_level': danger_levels['high']
  },
  {
    'code': '123',
    'variants': ['амарант'],
    'danger_level': danger_levels['very_high']
  },
  {
    'code': '124',
    'variants': ['понсо 4r','червоний e 124', 'понсо'],
    'danger_level': danger_levels['high']
  },
  {
    'code': '126',
    'variants': ['пунцовый 6r','понсо 6r'],
    'danger_level': danger_levels['very_high']
  },
  {
    'code': '128',
    'variants': ['red 2g', 'красный 2g'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '129',
    'variants': ['красный очаровательный ас'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '131',
    'variants': ['синий патентованный v'],
    'danger_level': danger_levels['high']
  },
  {
    'code': '132',
    'variants': ['индиго', 'индигокармин'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '133',
    'variants': ['бриллиантовый синий', 'бриллиантовый голубой fcf', 'синий блестящий fcf'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '134',
    'variants': ['spirulina extract','экстракт спирулины'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '140',
    'variants': ['хлорофилин', 'chlorophillin', 'хлорофиллин', 'хлорофилл'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '1400',
    'variants': ['декстрин'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '141',
    'variants': ['медные комплексы хлорофиллов и хлорофиллинов', 'хлорофилла медные комплексы','медные комплексы хлорофиллов'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '142',
    'variants': ['зеленый s'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '143',
    'variants': ['fast green fcf', 'зеленый прочный fcf', 'fast green', 'прочный зеленый', 'зеленый стойкий'],
    'danger_level': danger_levels['very_high']
  },
  {
    'code': '1452',
    'variants': ['starch aluminium octenyl succinate','крахмала и алюминиевой соли октенилянтарной кислоты эфир'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '150',
    'variants': ['сахарный колер', 'карамель жидкая', 'краситель натуральный карамельный', 'краситель пищевой натуральный «карамель»', 'краситель «карамель»', 'натуральный краситель карамельный', 'краситель карамель', 'карамельный краситель', 'caramel coloring agent', 'colouring natural caramel', 'caramel colour', 'краситель натуральный кола-карамель','кола карамель', 'краситель пищевой натуральный (карамель)', 'карамель', 'колер карамельный'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '1503',
    'variants': ['castor oil','касторовое масло'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '1505',
    'variants': ['triethyl citrate','триэтилцитрат'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '150a',
    'variants': ['сахарный колер i простой', 'сахарный колер (е150а)','сахарный колер простой','сахарный колер i'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '150b',
    'variants': ['сахарный колер (е150b)','сахарный колер ii'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '150c',
    'variants': ['карамельный колер', 'карамельний колер e-150c','сахарный колер iii','сахарный колер (е150c)'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '150d',
    'variants': ['сахарный колер iv', 'краситель натуральный «карамельный»', 'натуральный коричневый', 'сахарный колер e150d', 'краситель карамель e150d', 'сахарный колор iv', 'coloring agent caramel', 'colours caramel'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '1510',
    'variants': ['этиловый спирт', 'этанол', 'спирт этиловый'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '1517',
    'variants': ['glyceryl diacetate', 'diacetin','диацетин', 'глицерилдиацетат'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '1518',
    'variants': ['триацетин','триацетат глицерина','триацетоксипропан'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '1519',
    'variants': ['benzyl alcohol','бензиловый спирт'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '152',
    'variants': ['carbon black', 'hydrocarbon','уголь'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '1520',
    'variants': ['пропиленгликоль', 'пропилен-гликоль', 'propylene glycol'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '1521',
    'variants': ['polyethylene glycol','полиэтиленгликоль'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '153',
    'variants': ['е153', 'уголь древесный','уголь растительный'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '155',
    'variants': ['шоколадный коричневый ht', 'brown ht','коричневый ht'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '160',
    'variants': ['каротиноиды'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '160a',
    'variants': ['провитамин а', 'бета-каротин', 'экстракт натуральных каротинов', 'бета-каротин синтетический', 'beta-carotin', 'beta-carotine', 'beta-caroten', 'в-каротин', 'b-каротин', 'в-каротин'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '160b',
    'variants': ['е160b', 'аннато', 'анато', 'annato', 'анатто'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '160c',
    'variants': ['экстракт паприки', 'масло смолы паприки', 'паприка', 'капсантин', 'капсантен','paprika'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '160d',
    'variants': ['ликопен','ликопин'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '160e',
    'variants': ['е160е', 'апокаротенал', 'каротиновый альдегид','апокаротиновый альдегид'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '160f',
    'variants': ['пищевой оранжевый 7'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '161b',
    'variants': ['лютеин'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '162',
    'variants': ['красный бетанин', 'красный свекольный','свекольный бетанин'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '163',
    'variants': ['антоциан'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '164',
    'variants': ['шафран'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '170',
    'variants': ['карбонат кальция','карбонаты кальция'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '171',
    'variants': ['титана диоксид', 'белый пигмент', 'диоксид титана', 'titanium dioxide'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '172',
    'variants': ['оксид железа', 'оксиды железа'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '173',
    'variants': ['алюминий'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '174',
    'variants': ['серебро'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '175',
    'variants': ['золото'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '181',
    'variants': ['танин'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '200',
    'variants': ['сорбиновая кислота', 'sorbic acid'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '202',
    'variants': ['калия сорбат', 'сорбат калия', 'potassium sorbate'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '209',
    'variants': ['heptyl p-hydroxybenzoate','пара-оксибензойной кислоты гептиловый эфир'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '210',
    'variants': ['бензойная кислота'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '211',
    'variants': ['натрия бензоат','sodium benzoate'],
    'danger_level': danger_levels['high']
  },
  {
    'code': '213',
    'variants': ['calcium benzoate','бензоат кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '214',
    'variants': ['ethylparaben', 'ethyl para-hydroxybenzoate','пара-оксибензойной кислоты этиловый эфир'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '215',
    'variants': ['sodium ethyl para-hydroxybenzoate','пара-оксибензойной кислоты этилового эфира натриевая соль'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '216',
    'variants': ['пара-оксибензойной кислоты пропиловый эфир'],
    'danger_level': danger_levels['high']
  },
  {
    'code': '217',
    'variants': ['пара-оксибензойной кислоты пропиловый эфир натриевая соль'],
    'danger_level': danger_levels['high']
  },
  {
    'code': '218',
    'variants': ['пара-оксибензойной кислоты метиловый эфир'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '219',
    'variants': ['sodium methyl para-hydroxybenzoate','пара-оксибензойной кислоты метилового эфира натриевая соль'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '220',
    'variants': ['диоксид серы', 'so2', 'оксид серы', 'двуокись серы'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '222',
    'variants': [],
    'danger_level': danger_levels['high']
  },
  {
    'code': '223',
    'variants': ['пиросульфит натрия','sodium pyrosulphite', 'sodium metabisulfite', 'sodium pyrosulphate', 'натрия метабисульфит', 'метабисульфит натрия'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '224',
    'variants': ['калия метабисульфит','пиросульфит калия'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '225',
    'variants': ['сульфит калия'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '226',
    'variants': ['сульфит кальция'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '227',
    'variants': ['гидросульфит кальция'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '230',
    'variants': ['дифенил'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '231',
    'variants': ['орто-фенилфенол'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '232',
    'variants': ['орто-фенилфенола натриевая соль'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '234',
    'variants': ['вализин', 'низин'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '235',
    'variants': ['пималак','пимарицин', 'натамицин'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '236',
    'variants': ['муравьиная кислота'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '237',
    'variants': ['sodium formate','формиат натрия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '238',
    'variants': ['calcium formate','формиат кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '239',
    'variants': ['уротропин','гексаметилентетрамин'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '241',
    'variants': ['gum guaicum','гваяковая камедь'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '242',
    'variants': ['dimethyl dicarbonate','диметилдикарбона','велькорин'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '249',
    'variants': ['potassium nitrite','нитрит калия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '250',
    'variants': ['нитрит натрия'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '251',
    'variants': ['нитрат натрия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '252',
    'variants': ['калий азотнокислый', 'нитрат калия'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '260',
    'variants': ['уксус спиртовой пищевой', 'кислота уксусная', 'уксус пищевой', 'кислота уксусная пищевая', 'уксус столовый', 'раствор уксусной кислоты', 'уксус натуральный'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '261',
    'variants': ['potassium acetate','ацетаты калия', 'ацетат калия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '262',
    'variants': ['ацетаты натрия', 'ацетат натрия','диацетат натрия'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '263',
    'variants': ['calcium acetate','ацетат кальция','ацетаты кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '264',
    'variants': ['ammonium acetate','ацетат аммония','ацетаты аммония'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '270',
    'variants': ['молочная кислота', 'lactic acid'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '280',
    'variants': ['пропионовая кислота'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '290',
    'variants': ['диоксид углерода','двуокись углерода','co2'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '296',
    'variants': ['яблочная кислота'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '297',
    'variants': ['фумаровая кислота'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '300',
    'variants': ['витамин с', 'аскорбиновая кислота', 'ascorbic acid', 'vitamin c'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '301',
    'variants': ['натрия аскорбат'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '302',
    'variants': ['calcium ascorbate','аскорбат кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '303',
    'variants': ['potassium ascorbate','аскорбат калия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '305',
    'variants': ['ascorbyl stearate','аскорбилстеарат'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '307',
    'variants': ['токоферол','витамин е'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '311',
    'variants': ['octyl gallate','октилгаллат'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '312',
    'variants': ['dodecyl gallate','додецилгаллат'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '314',
    'variants': ['guaiac resin','гваяковая смола'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '315',
    'variants': ['isoascorbic acid', 'erythorbic acid','изоаскорбиновая','эриторбовая'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '316',
    'variants': ['изо-аскорбинат натрия', 'изо-аскорбат натрия','изоаскорбат натрия'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '317',
    'variants': ['erythorbin acid','изоаскорбат калия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '318',
    'variants': ['sodium erythorbin','изоаскорбат кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '319',
    'variants': ['tertiary butylhydroquinone','трет-бутилгидрохинон', 'трет бутилгидрохинон'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '320',
    'variants': ['бутилгидроксианизол', 'бутил гидроксианизол'],
    'danger_level': danger_levels['high']
  },
  {
    'code': '321',
    'variants': ['бутилгидрокситолуол'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '322',
    'variants': ['концентрат фосфатидный','phosphatidic concentrate', 'phosphatide concentrate'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '322i',
    'variants': ['lecithin', 'соевый лецитин', 'лецитин', 'soya lecithin', 'lecithin', 'soya licithin', 'soybean lecithin'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '323',
    'variants': ['anoxomer','аноксомер'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '325',
    'variants': ['лактат натрия'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '326',
    'variants': ['potassium lactate','лактат калия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '327',
    'variants': ['лактат кальция', 'calcium lactate'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '328',
    'variants': ['ammonium lactate','лактат аммония'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '329',
    'variants': ['magnesium lactate','лактат магния'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '330',
    'variants': ['лимонная кислота', 'citric acid'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '331',
    'variants': ['цитрат натрия', 'цитраты натрия','лимоннокислый натрий', 'натрий лимонно-кислый', 'sodium citrate'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '331i',
    'variants': ['цитрат натрия 1-замещенный'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '331ii',
    'variants': ['цитрат натрия 2-замещенный'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '331iii',
    'variants': ['цитрат натрия 3-замещенный'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '333',
    'variants': ['цитрат кальция', 'calcium citrate'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '334',
    'variants': ['кислота винная'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '335',
    'variants': ['sodium tartrates','тартраты натрия','тартрат натрия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '336',
    'variants': ['тартрат калия','тартраты калия'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '337',
    'variants': ['potassium sodium tartrate','тартрат калия-натрия', 'тартраты калия-натрия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '338',
    'variants': ['фосфорная кислота', 'ортофосфорная кислота', 'орто-фосфорная кислота'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '339',
    'variants': ['фосфат натрия', 'монофосфат натрия','фосфаты натрия'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '340',
    'variants': ['фосфат калия', 'фосфаты калия'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '340ii',
    'variants': ['dipotassium orthophosphate', '340(ii)','орто-фосфат калия 2-замещенный'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '341',
    'variants': ['фосфат кальция','фосфаты кальция'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '341iii',
    'variants': ['341(iii)', 'tricalcium orthophosphate','орто-фосфат кальция 3-замещенный'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '342',
    'variants': ['ammonium phosphates','фосфаты аммония','фосфат аммония'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '343',
    'variants': ['magnesium phosphates','фосфаты магния','фосфат магния'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '350',
    'variants': ['sodium malate', 'sodium hydrogen malate', 'sodium malates', 'натрий яблочнокислый','малаты натрия', 'малат натрия'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '351',
    'variants': ['potassium malates','малаты калия','малат калия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '352',
    'variants': ['calcium malates','малаты кальция','малат кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '354',
    'variants': ['calcium tartrate','тартрат кальция','тартраты кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '355',
    'variants': ['adipic acid'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '356',
    'variants': ['sodium adipates','адипиновая кислота'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '357',
    'variants': ['potassium adipates','адипаты калия','адипат калия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '359',
    'variants': ['ammonium adipates','адипаты аммония','адипат аммония'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '363',
    'variants': ['кислота янтарная'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '365',
    'variants': ['sodium fumarates','фумараты натрия','фумарат натрия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '375',
    'variants': ['ниацин','никотиновая кислота'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '380',
    'variants': ['ammonium citrates','цитраты аммония','цитрат аммония'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '384',
    'variants': ['isopropyl citrate','изопропилцитратная смесь'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '385',
    'variants': ['эдта', 'этилендиаминтетраацетат кальция-натрия'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '386',
    'variants': ['disodium ethylenediamine- tetra-acetate','этилендиаминтетраацетат динатрий'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '387',
    'variants': ['oxystearin','оксистеарин'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '392',
    'variants': ['extracts of rosemary','экстракты розмарина','экстракт розмарина'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '400',
    'variants': ['alginic acid','альгиновая кислота'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '401',
    'variants': ['натриевый альгинат','sodium alginate', 'альгинат натрия'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '402',
    'variants': ['potassium alginate','альгинат калия','альгинаты калия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '403',
    'variants': ['ammonium alginate','альгинат аммония','альгинаты аммония'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '404',
    'variants': ['calcium alginate', 'альгинат кальция','альгинаты кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '406',
    'variants': ['агар агар', 'agar'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '407',
    'variants': ['каррагенан', 'карраген','каррагинан','карагинан', 'карагенан'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '409',
    'variants': ['arabinogalactan','арабиногалактан'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '410',
    'variants': ['камедь рожкового дерева'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '412',
    'variants': ['гуаровая камедь', 'камедь гуара', 'гуаран'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '414',
    'variants': ['гуммиарабик', 'камедь акации', 'fibregum b'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '415',
    'variants': ['камедь ксантана', 'ксантановая камедь', 'ксантанова камедь', 'ксантановая смола', 'ксантанова смола'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '416',
    'variants': ['karaya gum','карайи камедь'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '417',
    'variants': ['тары камедь','камедь тари'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '418',
    'variants': ['gellan gum','геллановая камедь'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '420',
    'variants': ['сорбитол', 'сорбит', 'sorbitol'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '421',
    'variants': ['манит', 'маннит'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '422',
    'variants': ['глицерин', 'глицерол', 'glycerine', 'glycerin', 'агент глицериновый'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '425',
    'variants': ['konjac', 'konjac flour','конжак', 'конжаковая мука'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '426',
    'variants': ['soybean hemicellulose','гемицеллюлоза сои'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '427',
    'variants': ['cassia gum','камедь кассии'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '430',
    'variants': ['polyoxyethylene (8) stearate','полиоксиэтилен (8) стеарат'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '431',
    'variants': ['polyoxyethylene (40) stearate','полиоксиэтилен (40) стеарат'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '432',
    'variants': ['polyoxyethylene (20) sorbitan monolaurate','полиоксиэтилен (20) сорбитан монолаурат', 'твин 20'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '433',
    'variants': ['полисорбат 80', 'полисорбат', 'полиоксиэтиленсорбитан моноолеат','полиоксиэтилен (20) сорбитан моноолеат','твин 80'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '434',
    'variants': ['polyoxyethylene (20) sorbitan monopalmitate','полиоксиэтилен (20) сорбитан монопальмитат','твин 40'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '436',
    'variants': ['polyoxyethylene (20) sorbitan tristearate','полиоксиэтилен (20) сорбитан три-стеарат'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '440',
    'variants': ['пектин', 'pectine', 'pectin'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '445',
    'variants': ['глицериновые эфиры древесной смолы', 'глицериновый эфир древесной смолы','эфиры глицерина и смоляных кислот','эфир глицерина и смоляных кислот'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '450',
    'variants': ['е450', 'пирофосфат натрия', 'disodium diphosphate', 'пирофосфаты'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '450i',
    'variants': ['450(i)', 'пирофосфат динатрия', 'disodium diphosphate','дигидропирофосфат натрия', 'sodium acid pyrophosphate'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '450ii',
    'variants': ['450(ii)', 'пирофосфат тринатрия','trisodium diphosphate', 'моногидропирофосфат натрия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '450iii',
    'variants': ['450(iii)', 'tetrasodium diphosphate', 'пирофосфат тетранатрия','пирофосфат натрия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '450iv',
    'variants': ['450(iv)', 'пирофосфат дикалия', 'dipotassium diphosphate','дигидропирофосфат калия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '450ix',
    'variants': ['450(ix)', 'dimagnesium diphosphate', 'дигидрофосфат магния'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '450v',
    'variants': ['450(v)', 'пирофосфат тетракалия', 'tetrapotassium diphosphate','пирофосфат калия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '450vi',
    'variants': ['пирофосфат дикальция', 'пирофосфат кальция', '450(vi)', 'dicalcium diphosphate'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '450vii',
    'variants': ['450(vii)', 'дигидропирофосфат кальция', 'calcium dihydrogen diphosphate'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '450viii',
    'variants': ['450(viii)', 'dimagnesium diphosphate','пирофосфат димагния'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '451',
    'variants': ['е451', 'триполифосфат', 'трифосфат'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '452',
    'variants': ['полифосфаты'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '459',
    'variants': ['бета-циклодекстрин'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '460',
    'variants': ['cellulose','целлюлоза'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '461',
    'variants': ['methyl cellulose','метилцеллюлоза'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '463',
    'variants': ['hydroxypropyl cellulose','гидроксипропилцеллюлоза'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '464',
    'variants': ['hydroxypropyl methyl cellulose','гидроксипропилметилцеллюлоза'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '465',
    'variants': ['methyl ethyl cellulose','метилэтилцеллюлоза'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '466',
    'variants': ['карбоксиметилцеллюлозы натриевая соль', 'карбоксиметилцеллюлоза', 'карбоксиметилцеллюлоза натриевая соль', 'карбоксил метилюллоза', 'карбоксиметилцелюлоза','карбоксил метилюлоза', 'кмц'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '467',
    'variants': ['ethyl hydroxyethyl cellulose','этилгидроксиэтилцеллюлоза'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '468',
    'variants': ['crosslinked sodium carboxymethyl cellulose', 'croscarmellose','кросскарамеллоза','карбоксиметилцеллюлоза натриевая соль кроссвязанная'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '469',
    'variants': ['казеинат натрия', 'камедь целлюлозы ферментативно гидролизованная', 'казеинат','карбоксиметилцеллюлоза ферментативно гидролизованная'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '470iii',
    'variants': ['магниевые соли жирных кислот', 'magnesium stearate', 'e470b'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '471',
    'variants': ['моно- и диглицериды жирных кислот', 'глицерин моностеарат', 'mono- and diglycerides of fatty acids', 'моно и диглицериды', 'моно и диглицериды жирных кислот'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '472',
    'variants': ['е 472','эфиры и глицериды кислот'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '472a',
    'variants': ['acetic and fatty acid esters of glycerol','глицерина и уксусной и жирных кислот эфиры'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '472d',
    'variants': ['tartaric acid esters of mono- and diglycerides of fatty acids','моно- и диглицериды жирных кислот и винной кислоты эфиры','моно и диглицериды жирных кислот и винной кислоты эфиры'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '472e',
    'variants': ['е472е', 'datem', 'эфиры глицерина', 'диацетилвинной и жирных кислот','глицерина и диацетилвинной и жирных кислот эфиры'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '472f',
    'variants': ['mixed tartaric', 'acetic and fatty acid esters of glycerol','глицерина и винной, уксусной и жирных кислот смешанные эфиры'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '472g',
    'variants': ['succinylated monoglycerides','моноглицеридов и янтарной кислоты эфиры'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '476',
    'variants': ['полиглицерин', 'эфиры полиглицерина взаимоэтерифицированных рициноловых кислот', 'pgpr', 'эфиры полиглицерина взаимоэтерифицированных рациноловых кислот'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '480',
    'variants': ['dioctyl sodium sulphosuccinate', 'диоктилсульфосукцинат натрия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '483',
    'variants': ['stearyl tartrate','стеарилтартрат'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '484',
    'variants': ['stearyl citrate','стеарилцитрат'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '500',
    'variants': ['бикарбонат натрия', 'натрий двууглекислый', 'сода пищевая','гидрокарбонат натрия', 'карбонаты натрия', 'sodium bicarbonate', 'baking soda', 'сода питьевая', 'sodium hydrogen carbonate', 'карбонат натрия','карбонаты натрия'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '503',
    'variants': ['карбонат аммония', 'соли углеаммонийные', 'соль углеаммонийная', 'гидрокарбонат аммония', 'ammonium carbonate', 'ammonium hydrogen carbonate', 'углеаммонийная соль', 'аммония гидрокарбонат','карбонат аммония'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '504',
    'variants': ['карбонат магния','карбонаты магния'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '507',
    'variants': ['соляная кислота'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '508',
    'variants': ['хлорид калия'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '509',
    'variants': ['кальций хлористый', 'хлорид кальция'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '510',
    'variants': ['хлорид аммония'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '511',
    'variants': ['хлорид магния'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '514',
    'variants': ['сульфат натрия'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '515',
    'variants': ['сульфат калия'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '516',
    'variants': ['сульфат кальция'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '517',
    'variants': ['ammonium sulphate', 'сульфаты аммония', 'сульфат аммония'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '518',
    'variants': ['magnesium sulphate','сульфаты магния','сульфат магния'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '519',
    'variants': ['сульфат меди (ii)','сульфат меди'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '520',
    'variants': ['aluminium sulphate', 'сульфат алюминия','сульфаты алюминия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '521',
    'variants': ['aluminium sodium sulphate','сульфат алюминия-натрия','квасцы алюмонатриевые'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '523',
    'variants': ['aluminium ammonium sulphate','сульфат алюминия-аммония', 'квасцы алюмоаммиачные'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '524',
    'variants': ['гидроксид натрия'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '525',
    'variants': ['гидроксид калия'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '526',
    'variants': ['гидроксид кальция'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '529',
    'variants': ['calcium oxide','оксид кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '530',
    'variants': ['оксид магния'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '536',
    'variants': ['ферроцианид калия', 'гексацианоферрат калия', 'желтая кровяная соль', 'железистосинеродистый калий'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '538',
    'variants': ['calcium ferrocyanide','ферроцианид кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '539',
    'variants': ['тиосульфат натрия'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '542',
    'variants': ['bone phosphate', 'essentiale calcium phosphate', 'tribasic','фосфат костный','фосфат кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '551',
    'variants': ['диоксид кремния','двуоксид кремния'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '552',
    'variants': ['calcium silicate','силикат кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '553',
    'variants': ['magnesium silicates','силикаты магния','силикат магния'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '554',
    'variants': ['sodium aluminosilicate','алюмосиликат натрия','алюмосиликаты натрия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '555',
    'variants': ['алюмосиликат калия','алюмосиликаты калия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '556',
    'variants': ['calcium aluminium silicate','алюмосиликат кальция','алюмосиликаты кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '558',
    'variants': ['бентонит'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '559',
    'variants': ['алюмосиликаты','алюмосиликат'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '570',
    'variants': ['жирные кислоты'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '574',
    'variants': ['gluconic acid (d-)','глюконовая кислота'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '575',
    'variants': ['глюконо-дельта-лактон', 'глюконодельталактон','гдл'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '576',
    'variants': ['sodium gluconate','глюконат натрия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '577',
    'variants': ['potassium gluconate','глюконат калия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '578',
    'variants': ['calcium gluconate','глюконат кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '579',
    'variants': ['железистый глюконат', 'глюконат железа', 'ferrous gluconate'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '580',
    'variants': ['magnesium gluconate','глюконат магния'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '585',
    'variants': ['лактат железа'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '620',
    'variants': ['glutamic acid', 'l(+)-','глутаминовая кислота'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '621',
    'variants': ['глутамат натрия', 'глютамат натрия'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '622',
    'variants': ['monopotassium glutamate','глутамат калия 1-замещенный'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '623',
    'variants': ['calcium glutamate','глутамат кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '624',
    'variants': ['monoammonium glutamate','глутамат аммония 1-замещенный'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '625',
    'variants': ['magnesium glutamate','глутамат магния'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '626',
    'variants': ['гуаниловая кислота'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '627',
    'variants': ['гуанилат натрия','двунатриевый гуанилат'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '628',
    'variants': ['dipotassium guanylate','гуанилат калия 2-замещенный'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '629',
    'variants': ['calcium guanylate','гуанилат кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '630',
    'variants': ['inosinic acid','инозиновая кислота'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '631',
    'variants': ['инозинат натрия','инозинаты натрия'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '632',
    'variants': ['potassium inosinate','инозинат калия','инозинаты калия'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '633',
    'variants': ['calcium inosinate','инозинат кальция','инозинаты кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '635',
    'variants': ['5-рибонуклеотид натрия', 'натрий 5рибонуклеотид', 'натрий 5 рибонуклеотид', '5-рибонуклеотиды натрия','рибонуклеотиды натрия 2-замещенные'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '636',
    'variants': ['мальтол'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '637',
    'variants': ['этилмальтол'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '650',
    'variants': ['zinc acetate','ацетат цинка'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '900',
    'variants': ['polydimethylsiloxane','полидиметилсилоксан'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '901',
    'variants': ['beeswax white and yellow','воск пчелиный, белый и желтый'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '902',
    'variants': ['candelilla wax','воск свечной'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '903',
    'variants': ['воск карнаубский'],
    'danger_level': danger_levels['zero']
  },
  {
    'code': '904',
    'variants': ['шеллак'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '905c',
    'variants': ['petroleum wax', 'microcrystalline wax', 'paraffin wax','парафин','микрокристаллический воск'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '905d',
    'variants': ['mineral oil (high viscosity)','минеральное масло высокой вязкости',],
    'danger_level': danger_levels['none']
  },
  {
    'code': '905e',
    'variants': ['mineral oil (medium and low viscosity class i)','минеральное масло средней и низкой вязкости','минеральное масло класс i'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '907',
    'variants': ['hydrogenated poly-1-decene','поли-1-децен гидрогенизированный'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '908',
    'variants': ['воск рисовых отрубей'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '912',
    'variants': ['montanic acid esters', 'montan acid esters','монтановой (октакозановой) кислоты эфиры','монтановой кислоты эфиры','октакозановой кислоты эфиры'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '913',
    'variants': ['ланолин'],
    'danger_level': danger_levels['very_low']
  },
  {
    'code': '914',
    'variants': ['oxidized polyethylene wax', 'oxidized polyethylene','полиэтиленовый воск окисленный'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '920',
    'variants': ['cysteine', 'l-', 'and its hydrochlorides - sodium and potassium salts','цистеин, l- и его гидрохлориды - натриевая и калиевая соли','цистеин','натриевая и калиевая соли','гидрохлориды'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '927b',
    'variants': ['carbamide (urea)','карбамид','мочевина'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '928',
    'variants': ['benzoyl peroxide','перекись бензоила'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '930',
    'variants': ['calcium peroxide','перекись кальция'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '938',
    'variants': ['argon','аргон'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '939',
    'variants': ['gellium','гелий'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '941',
    'variants': ['nitrogen','азот'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '942',
    'variants': ['nitrous oxide', 'n2o','закись азота'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '943a',
    'variants': ['butane','бутан'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '943b',
    'variants': ['isobutane','изобутан'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '944',
    'variants': ['propane','пропан'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '948',
    'variants': ['oxygen','кислород'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '949',
    'variants': ['hydrogen','водород'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '950',
    'variants': ['ацесульфам калия', 'ацесульфам-к', 'ацесульфам к', 'ацесульфам k'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '951',
    'variants': ['аспартам'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '952',
    'variants': ['цикламат натрия', 'цикламовая кислота', 'cyclamic acid and na', 'ca salts' ],
    'danger_level': danger_levels['high']
  },
  {
    'code': '953',
    'variants': ['изомальт'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '954',
    'variants': ['сахарин', 'сахаринат натрия'],
    'danger_level': danger_levels['medium']
  },
  {
    'code': '955',
    'variants': ['сукралоза','трихлоргалактосахароза'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '957',
    'variants': ['thaumatin','тауматин'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '959',
    'variants': ['neohesperidine dihydrochalcone','неогесперидин дигидрохалкон'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '960',
    'variants': ['steviol glycosides', 'стевиол','стевиолгликозид','стевиозид','стевиазид'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '961',
    'variants': ['neotame','неотам'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '962',
    'variants': ['aspartame-acesulfame salt','аспартам-ацесульфама соль'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '965',
    'variants': ['мальтит', 'мальтитол', 'мальтитный сироп'],
    'danger_level': danger_levels['low']
  },
  {
    'code': '966',
    'variants': ['lactitol','лактит'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '968',
    'variants': ['erythritol','эритрит'],
    'danger_level': danger_levels['none']
  },
  {
    'code': '999',
    'variants': ['экстракт квиллайи','квиллай'],
    'danger_level': danger_levels['low']
  },

]
