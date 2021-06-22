# VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO
cid = str(input("Em que cidade você nasceu? ")).strip()

print("Tem Santo no nome? ", cid[:5].upper() == 'SANTO')
print("Tem Santa no nome? ", cid[:5].upper() == 'SANTA')
print("Tem São no nome? ", cid[:3].upper() == 'SÃO')
