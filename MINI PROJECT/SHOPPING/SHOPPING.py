class shopping:
    def __init__(self):
        store_name='DINGA FOOD PRODUCTS'
        Wel_msg=f'Welcome to {store_name}'
        
        print('*'*94)
        print('*'*94)
        print (f'''
               
{Wel_msg:^94}
               
               ''')
        print('*'*94)
        print('*'*94)
    def services(self):
        print(f'''
              
| OFFERS [O] | PRODUCTS [P] |  WALLET [W]  |
              
              ''' )
        serv=input("Enter Service Code :")
        while(serv.upper()!='P'):
                serv=input("Enter Valid Service Code: ")
        obj.show_products()
    def orders():
         order={}
         print (f'''Enter Product code and quanity to add to cart | Exit [E]''')
         pro=input()
    def show_products(self):
        __products={
  "Organic Apples (per kg)": [150.59, "OAPP"],
  "Organic Bananas (per kg)": [82.18, "OBAN"],
  "Organic Strawberries (per kg)": [211.00, "OSTR"],
  "Organic Blueberries (per kg)": [217.60, "OBLU"],
  "Organic Avocados (per dozen)": [130.00, "OAVO"],
  "Organic Spinach (per dozen bunches)": [129.88, "OSPI"],
  "Organic Brinjal (per kg)": [60.88, "OBRI"],
  "Organic Carrots (per kg)": [42.74, "OCAR"],
  "Organic Potatoes (per kg)": [63.66, "OPOT"],
  "Organic Onions (per kg)": [112.93, "OONI"],
  "Organic Garlic (per kg)": [213.20, "OGAR"],
  "Organic Tomatoes (per kg)": [67.69, "OTOM"],
  "Organic Pepper (per kg)": [723.88, "OPEP"],
  "Organic Broccoli (per kg)": [86.59, "OBRO"],
  "Organic Cauliflower (per kg)": [147.88, "OCAU"],
  "Organic Whole Milk (per lit)": [101.85, "OMIL"],
  "Organic Free-Range Eggs (per dozen)": [75.49, "OEGG"],
  "Organic Unsalted Butter (per kg)": [214.30, "OBUT"],
  "Organic Cheddar Cheese (per kg)": [222.00, "OCHE"],
  "Organic Plain Yogurt (per kg)": [106.05, "OYOG"],
  "Organic Chicken Breast (per kg)": [219.82, "OCHI"],
  "Organic Grass-Fed Ground Beef (per kg)": [117.61, "OBEE"],
  "Organic Firm Tofu (per kg)": [117.52, "OTOF"],
  "Organic Black Beans (per kg)": [117.88, "OBEA"],
  "Organic Brown Rice (per kg)": [204.40, "ORIC"],
  "Organic Rolled Oats (per kg)": [206.83, "OOAT"],
  "Organic Extra Virgin Olive Oil (per lit)": [325.98, "OOIL"],
  "Organic Raw Honey (per kg)": [522.02, "OHON"],
  "Organic Peanut Butter (per kg)": [213.20, "OPEA"]
}
        print('-'*94)

        # padding and alignment
        
        print(f"|  {'PRODUCT NAME':<60} | {'PRODUCT CODE':^13} | {'PRICE':>10} | ")
        print('-'*94)
        for products, price in __products.items():
            print (f'''|  {products:<60} |  {price[1]:^13}| {price[0]:>10} | ''')
        print('-'*94)
obj=shopping()
obj.services()
obj.orders()
# serv=input("Enter service code: ")
# if serv.upper()== 'P':
#     obj.show_products()
# else:
#     serv=input("Enter a valid Service code: ")
# product_code=input("Enter product code: ")
# quantity=int(input("Enter quantity :"))
