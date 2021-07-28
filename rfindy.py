s = 'lunes, martes, viernes'
print(s.rfind(','))
s = s[:s.rfind(',')] + ' y' + s[s.rfind(',')+1:]
print(s)
