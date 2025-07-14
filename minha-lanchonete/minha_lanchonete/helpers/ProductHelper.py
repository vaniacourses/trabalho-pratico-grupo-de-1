

class ProductHelper:
    
    @classmethod
    def is_pizza(cls, product):
        if not product:
            return False
        try:
            product.pizza
            return True
        except:
            return False
        
    @classmethod
    def is_drink(cls, product):
        if not product:
            return False
        try:
            product.drink
            return True
        except:
            return False