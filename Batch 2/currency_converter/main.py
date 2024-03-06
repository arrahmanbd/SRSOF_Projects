def bdt_to_usd(amount):
    x = amount * 0.012
    print(f"{x} USD")

def bdt_to_gbp(amount):
    x = amount * 0.009
    print(f"{x} GBP")

def bdt_to_aed(amount):
    x = amount * 0.045
    print(f"{x} AED")

def bdt_to_eur(amount):
    x = amount * 0.011
    print(f"{x} EUR")

print("\n🪙🪙 Currency Converter 💰")
print('Press ❌ to exit')
print("-" * 20)
while True:
    option = input("Amount in Bangladeshi Taka (BDT): ")
    if option=='x' or option=='X':
        print("Thanks for using our programme 💰🤑")
        break
    else:
        amount_bdt =float(option)
        bdt_to_usd(amount_bdt)
        bdt_to_gbp(amount_bdt)
        bdt_to_aed(amount_bdt)
        bdt_to_eur(amount_bdt)
