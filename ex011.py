larg = float(input('digite a largura da parede:'))
alt = float(input('digite a altura da parede:'))
área = larg * alt
print('sua parede tem a dimensão de {:.2f}x{:.2f} e sua área e de {:.2f}M².'.format(larg, alt, área,))
tinta = área / 2
print('para pintar essa parede,você vai precisar de {:.2f}l de tinta'.format(tinta,))
