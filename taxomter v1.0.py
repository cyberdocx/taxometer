
print('''
d888888b  .d8b.  db    db  .d88b.  .88b  d88. d88888b d888888b d88888b d8888b.   db    db  db     .d88b.  
`~~88~~' d8' `8b `8b  d8' .8P  Y8. 88'YbdP`88 88'     `~~88~~' 88'     88  `8D   88    88 o88    .8P  88. 
   88    88ooo88  `8bd8'  88    88 88  88  88 88ooooo    88    88ooooo 88oobY'   Y8    8P  88    88  d'88 
   88    88~~~88  .dPYb.  88    88 88  88  88 88~~~~~    88    88~~~~~ 88`8b     `8b  d8'  88    88 d' 88 
   88    88   88 .8P  Y8. `8b  d8' 88  88  88 88.        88    88.     88 `88.    `8bd8'   88 db `88  d8' 
   YP    YP   YP YP    YP  `Y88P'  YP  YP  YP Y88888P    YP    Y88888P 88   YD      YP     VP VP  `Y88P'  
              indian old tax regime calculator                                              by cyberdocx
''')

gross_income=int(input('Enter your gross income:'))
deductions=int(input('Enter deductions amount:'))
taxable_income=(gross_income-deductions)
print("taxable income:",taxable_income)

rebate=12500

if taxable_income in range(0,251000):
    tax=taxable_income-250000
    print("No tax",tax)
if taxable_income in range(250000,500001):
    tax=(taxable_income-250000)*0.05
    print("tax @ 5%: ",tax)
    if tax < rebate:
        print('No tax using rebate')
if taxable_income in range(500001,1000001):
    tax=(taxable_income-500000)*0.2 + 12500
    print("tax @ 20%:",tax)
if taxable_income > (1000000):
    tax=(taxable_income-1000000)*0.3+22500
    print("tax @ 30%:",tax)