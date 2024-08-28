'''
Williams Villalba
******************************************
Importando sys (sistema) que es un built-in
Importando  call de Call_pictures'''

import sys
from Processing import Game

# Funcion de test
def main(args=None):
  if args is None:
    args = sys.argv[1:]
  print('Verificación de botellas')
  # Instancia de la class Game
  app = Game()
  app.run()



'''Es un Idiom __Punto de ingreso'''
if __name__ == '__main__':
  sys.exit(main())


