def calculate_vat(amount):
    """
    This function calcualtes the 20% VAT for a given price and adds to the original price.
    parameters: 
    Price (float): The original price before VAT.

    Returns: 
    float: the price including 20% VAT.
    """
    vat_rate=0.2 # VAT rate is 20% 
    total_including_vat=amount * (1+vat_rate) # Add 20% VAT to the original price
    return total_including_vat

output = calculate_vat(100.12)
print(output)