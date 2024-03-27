#!/usr/bin/env python3
from decimal import Decimal

#El precio de un TOKEN se calcula con El "MarketCap"  divido entre el "Total Supply"


def calcular_precio(market_cap, total_supply):
  precio = market_cap / total_supply
  return precio

if __name__ == "__main__":
  
  try:
    market_cap_str = input("[+]-Cual es el MarketCap del token: ")
    market_cap = Decimal(market_cap_str.replace(",", "")) 

  except Exception as e:
    print("[!]El Valor no es valido.")
    exit()

  try:
    total_supply_str = input("[+]-Cual es el total suply de la cripto/token: ")
    total_supply = Decimal(total_supply_str.replace(",", ""))
    
  except Exception as e:
    print("[!]El valor no es valido.")
    exit()

precio = calcular_precio(market_cap, total_supply)
print(f"El precio aproximado de la criptomoneda es de: {precio:.2f}$ (USD)")