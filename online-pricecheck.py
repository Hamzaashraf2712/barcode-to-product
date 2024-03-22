import requests
from bs4 import BeautifulSoup

def get_product_info(product_name):
    base_url = 'https://www.naheed.pk'
    search_url = f'https://www.naheed.pk/catalogsearch/result/?q={"+".join(product_name.split())}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('li', class_='item')

        results = []
        for product in products:
            # Extract product name
            product_title_elem = product.find('a', class_='product-item-link')
            if product_title_elem:
                product_title = product_title_elem['title']
            else:
                product_title = 'N/A'

            # Extract product price
            product_price_elem = product.find('span', class_='price')
            if product_price_elem:
                product_price = product_price_elem.text.strip()
            else:
                product_price = 'N/A'

            # Check if both product title and price are valid before appending
            if product_title != 'N/A' and product_price != 'N/A':
                results.append({
                    'product_title': product_title,
                    'price': product_price
                })

        return results
    else:
        return None

# Test the function
product_name = input("Enter the product name: ")
results = get_product_info(product_name)

if results:
    for result in results:
        print("Product Title:", result['product_title'])
        print("Price:", result['price'])
        print("------")
else:
    print("Failed to retrieve data.")
