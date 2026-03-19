""""
Functions needed: 

# 1. get_country_data(country_name)
#    → fetches data from restcountries API
#    → returns dictionary with name, population, region, languages, currencies

# 2. display_country(data)
#    → prints country info in a readable format

# 3. get_stock_price(ticker)
#    → fetches stock price from Yahoo Finance API
#    → returns current price and company name

# 4. display_stock(data)
#    → prints stock info in a readable format

# 5. save_report(country_data, stock_data)
#    → saves everything to a .txt file with timestamp

# 6. main()
#    → menu to tie everything together

"""

import requests # API installed
import datetime  # python library 

# step 1

def get_country_data(country_name):
    response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")  # raw answer from the internet
    data = response.json()  # converts response into a Python dictionary
    return data

def display_country(data):
    country = data[0]  # get the first item from the list
    print(f"Flag: {country['flag']}")
    print(f"Name: {country['name']['common']}")
    print(f"Capital: {country['capital'][0]}")
    print(f"Region: {country['region']}")
    print(f"Population: {country['population']}")
    print(f"Language: {list(country['languages'].values())[0]}") # adjusts how it is displayed 
    print(f"Currency: {list(country['currencies'].values())[0]['name']}") # adjusts how it is displayed 


# step 3 

def get_stock_price(ticker):
    reponse2 = requests.get(f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey=7NUSEVY4MY3J2ZG0")
    stockdata = reponse2.json()
    return stockdata

def display_stock(data):
    print(f"Symbol: {data['Global Quote']['01. symbol']}")
    print(f"Price: {data['Global Quote']['05. price']}")
    print(f"Open: {data['Global Quote']['02. open']}")
    print(f"Change: {data['Global Quote']['09. change']} ({data['Global Quote']['10. change percent']})")
    print(f"Last updated: {data['Global Quote']['07. latest trading day']}")


# step 4

def save_report(country_data, stock_data):
    now = datetime.datetime.now()
    file = open("report.txt", "w")
    
    file.write(f"Report generated: {now}\n")
    file.write("====================\n")
    
    file.write("-> COUNTRY INFO\n")
    file.write(f"Name: {country_data[0]['name']['common']}\n")
    file.write(f"Capital: {country_data[0]['capital'][0]}\n")
    file.write(f"Population: {country_data[0]['population']}\n")
    file.write(f"Region: {country_data[0]['region']}\n")
    file.write("====================\n")
    
    file.write("-> STOCK INFO\n")
    file.write(f"Symbol: {stock_data['Global Quote']['01. symbol']}\n")
    file.write(f"Price: {stock_data['Global Quote']['05. price']}\n")
    file.write(f"Change: {stock_data['Global Quote']['09. change']}\n")
    file.write(f"Last updated: {stock_data['Global Quote']['07. latest trading day']}\n")
    file.write("====================\n")
    
    file.close()
    print("Report saved to report.txt! ✅")   


# step 5

def main():
    country_data = None
    stock_data = None

    while True:
        print("\n1. Search country")
        print("2. Search stock")
        print("3. Save report")
        print("4. Quit")

        choice = input("Pick an option: ").strip()

        if choice == '4':
            print("Goodbye!")
            break

        elif choice == '1':
            country_name = input("Enter country name: ")
            country_data = get_country_data(country_name)
            display_country(country_data)

        elif choice == '2':
            ticker = input("Enter stock ticker (e.g. AAPL): ")
            stock_data = get_stock_price(ticker)
            display_stock(stock_data)

        elif choice == '3':
            if country_data is None or stock_data is None:
                print("⚠️ Please search a country and a stock first")
            else:
                save_report(country_data, stock_data)

main()


