class_sp = ('Real Madrid',
            'Girona',
            'Atl. Madrid',
            'Barcelona',
            'Ath. Bilbao',
            'Real Sociedad',
            'Betis',
            'Getafe',
            'Valencia',
            'Las Palmas',
            'Rayo Vallecano',
            'Osasuna',
            'Villarreal',
            'Mallorca',
            'Alaves',
            'Sevilla',
            'Celta Vigo',
            'Cadiz',
            'Granada',
            'Almeria')
ordem_alf_class_sp = sorted(class_sp)


def imp_box():
    print('*' * 20)


imp_box()
print(class_sp[0:4])
imp_box()
print(class_sp[-5:])
imp_box()
print(ordem_alf_class_sp)
imp_box()
print(class_sp.index('Las Palmas')+1)

