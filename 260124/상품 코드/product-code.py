product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class sol:
    def __init__(self, product_name='codetree', product_code='50'):
        self.name = f"is {product_name}"
        self.code = f"product {product_code}"

a = sol()
print(a.code, a.name)
b = sol(product_name, product_code)
print(b.code, b.name)