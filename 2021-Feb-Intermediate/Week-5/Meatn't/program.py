def make_stock_dict(stock_filename):
    # Take the name of a file containing key-value pairs of stocked products.
    # Return a dictionary containing stocked products as keys with a number as a value.
    with open(stock_filename, 'r') as f:
        text = f.read().split('\n')
    return_val = {}
    for index in range(len(text)):
        items = text[index].split(',')
        return_val[items[0]] = int(items[1])
    return return_val

def restock(stock_dict, product, num_items):
    # Takes a stock dictionary, a product name and the number of items to add.
    # Updates the stock dictionary and prints an alert.
    stock_dict[product] = stock_dict[product] + num_items
    print(f"We're running low on {product}! Restocking with {num_items} items.")
    return stock_dict

# Write the rest of your program here
def main():
    stock_dict = make_stock_dict('stock_start.txt')
    min_dict = make_stock_dict('stock_min.txt')
    sales_report = {}
    print("Welcome to MEATN'T! We meatn't so you can!")
    product = input("Product: ")
    while product:
        freq = int(input("Number sold: "))
        stock_dict[product] -= freq
        if stock_dict[product] < min_dict[product]:
            stock_dict = restock(stock_dict, product, min_dict[product]*2)
        if product not in sales_report:
            sales_report[product] = freq
        else:
            sales_report[product] += freq
        product = input("Product: ")
    
    print("Let's see how much we sold!")
    for item in sales_report.keys():
        print(f"{sales_report[item]} units of {item}")

if __name__ == "__main__":
    main()