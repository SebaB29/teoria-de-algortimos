\* Maximizacion_Beneficios_Publicidad *\
Maximize
Beneficio_Total: 50000 Oferta_('A',_'1') + 100000 Oferta_('B',_'1')
 + 120000 Oferta_('B',_'2') + 100000 Oferta_('C',_'1')
 + 80000 Oferta_('D',_'1') + 5000 Oferta_('E',_'1') + 40000 Oferta_('F',_'1')
 + 90000 Oferta_('G',_'1') + 30000 Oferta_('H',_'1') + 70000 Oferta_('I',_'1')
Subject To
_C1: Oferta_('B',_'1') + Oferta_('B',_'2') <= 1
_C2: Oferta_('A',_'1') + Oferta_('D',_'1') <= 1
_C3: 30 Oferta_('A',_'1') + 80 Oferta_('B',_'1') + 120 Oferta_('B',_'2')
 + 75 Oferta_('C',_'1') + 50 Oferta_('D',_'1') + 2 Oferta_('E',_'1')
 + 20 Oferta_('F',_'1') + 100 Oferta_('G',_'1') + 15 Oferta_('H',_'1')
 + 40 Oferta_('I',_'1') <= 200
Binaries
Oferta_('A',_'1')
Oferta_('B',_'1')
Oferta_('B',_'2')
Oferta_('C',_'1')
Oferta_('D',_'1')
Oferta_('E',_'1')
Oferta_('F',_'1')
Oferta_('G',_'1')
Oferta_('H',_'1')
Oferta_('I',_'1')
End
