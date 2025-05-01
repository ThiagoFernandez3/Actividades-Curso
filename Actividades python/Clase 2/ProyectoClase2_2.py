#Le pido al usuario los dos datos, el monto y el porcentaje de propina.
monto_total=int(input("Cual es el monto total de la cuenta?: "))
propina=int(input("Que porcentaje de propina quiere dejar?: "))
#Realizo las operaciones y las guardo en variables.
propina_total=(monto_total*propina/100)
cuenta=(monto_total+propina_total)
#Imprimo el resultado.
print(f"Su propina es de: {propina_total}$.\nEl total de su cuenta es de: {cuenta}$")
