import bottle
import random

APP = bottle.default_app()

@APP.route('/')
def index():
  return '<p>Hello</p>'
  
@APP.route('/random')
def myrandom():
  try:
    return random.randint(0, 10)
  except e:
    return e.message

if __name__ == '__main__':
  bottle.run(application=APP)
