print("Classificação de consumo de água")

tipo_imovel = input("Digite o tipo do imóvel: (comercial, casa, apartamento)")
consumo_agua = float(input("Digite o consumo de água em m³: "))

if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada - Consulte o plano corporativo.")

elif tipo_imovel == "apartamento" and consumo_agua < 10:
    print("Consumo econômico - Excelente controle de água! ")
elif tipo_imovel == "apartamento" or (tipo_imovel == "casa" and consumo_agua <= 25):
    print("Consumo moderado - Dentro do padrão residencial. ")
else:
    print("Consumo excessivo - Adote medidas de economia e verifique vazamentos.")