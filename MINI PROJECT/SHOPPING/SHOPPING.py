class shopping:
    def __init__(self):
        store_name='DINGA FOOD PRODUCTS'
        for i in range(40):
            print('*', end=' ')
        print()
        for i in range(40):
            print('*', end=' ')
        print (f''' 
            


                        Welcome to {store_name}
            
            
            
            ''')
        for i in range(40):
            print('*', end=' ')
        print()
        for i in range(40):
            print('*', end=' ')
        print()
    def show_products(self):
        __products={
            "Organic Apples (per kg)": 150.59,
            "Organic Bananas (per kg)": 82.18,
            "Organic Strawberries (per kg)": 211.00,
            "Organic Blueberries (per kg)": 217.60,
            "Organic Avocados (per dozen)": 130.00,
            "Organic Spinach (per dozen bunches)": 129.88,
            "Organic Brinjal (per kg)": 60.88,
            "Organic Carrots (per kg)": 42.74,
            "Organic Potatoes (per kg)": 63.66,
            "Organic Onions (per kg)": 112.93,
            "Organic Garlic (per kg)": 213.20,
            "Organic Tomatoes (per kg)": 67.69,
            "Organic Pepper (per kg)": 723.88,
            "Organic Broccoli (per kg)": 86.59,
            "Organic Cauliflower (per kg)": 147.88,
            "Organic Whole Milk (per lit)": 101.85,
            "Organic Free-Range Eggs (per dozen)": 75.49,
            "Organic Unsalted Butter (per kg)": 214.30,
            "Organic Cheddar Cheese (per kg)": 222.00,
            "Organic Plain Yogurt (per kg)": 106.05,
            "Organic Chicken Breast (per kg)": 219.82,
            "Organic Grass-Fed Ground Beef (per kg)": 117.61,
            "Organic Firm Tofu (per kg)": 117.52,
            "Organic Black Beans (per kg)": 117.88,
            "Organic Brown Rice (per kg)": 204.40,
            "Organic Rolled Oats (per kg)": 206.83,
            "Organic Extra Virgin Olive Oil (per lit)": 325.98,
            "Organic Raw Honey (per kg)": 522.02,
            "Organic Peanut Butter (per kg)": 213.20
            }
        print('-'*80)

        # padding and alignment
        
        print(f"{'PRODUCT NAME':<60} | {'PRICE':>10}")
        print('-'*80)
        for products, price in __products.items():
            print (f'''{products:<60} | {price:>10}''')
obj=shopping()
obj.show_products()