print 'Welcome to Pypet!'

cat = {
  'name': 'Crookshanks',
  'age': 5,
  'weight': 9.5,
  'hungry': True,
  'photo': '(=^o.o^=)__',
}

mouse = {
  'name': 'Scabbers',
  'age': 3,
  'weight': 1.5,
  'hungry': False,
  'photo': '<:3 )~~~~',
}
pets = [cat, mouse]

def feed(pet):
  if pet['hungry'] == True:
    pet['hungry'] = False
    pet['weight'] = pet['weight'] + 1
    print 'omnomnom!'
  else:
    print 'The Pypet is not hungry!'

for pet in pets:
  print '-----------------------------'
  print 'Hello ' + pet['name'] + '!'
  print pet['photo']
  print 'Weight: ' + str(pet['weight'])
  feed(pet)
  print 'Weight: ' + str(pet['weight'])
  print '-----------------------------'

print cat
feed(cat)
print cat
feed(cat)

print 'Hello '+ cat ['name']
print ['photo']
