medida = float(input('Digite a medida em Mts: '))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000
print('A medida de {}m corresponde a: '.format(medida))
print(km, 'km')
print(hm, 'hm')
print(dam, 'dam')
print(dm, 'dm')
print(cm, 'cm')
print(mm, 'mm')
