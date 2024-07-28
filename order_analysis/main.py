import pandas as pd

def read_data(file_path):
    return pd.read_csv(file_path)

def compute_total_revenue_by_month(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    revenue_by_month = df.groupby('month')['product_price'].sum().to_dict()
    return revenue_by_month

def compute_total_revenue_by_product(df):
    df['total_price'] = df['product_price'] * df['quantity']
    revenue_by_product = df.groupby('product_name')['total_price'].sum().to_dict()
    return revenue_by_product

def compute_total_revenue_by_customer(df):
    df['total_price'] = df['product_price'] * df['quantity']
    revenue_by_customer = df.groupby('customer_id')['total_price'].sum().to_dict()
    return revenue_by_customer

def get_top_10_customers(revenue_by_customer):
    sorted_customers = sorted(revenue_by_customer.items(), key=lambda item: item[1], reverse=True)
    top_10_customers = sorted_customers[:10]
    return top_10_customers

def main():
    file_path = 'orders.csv'
    df = read_data(file_path)

    revenue_by_month = compute_total_revenue_by_month(df)
    print("Total Revenue by Month:")
    print(revenue_by_month)

    revenue_by_product = compute_total_revenue_by_product(df)
    print("\nTotal Revenue by Product:")
    print(revenue_by_product)

    revenue_by_customer = compute_total_revenue_by_customer(df)
    print("\nTotal Revenue by Customer:")
    print(revenue_by_customer)

    top_10_customers = get_top_10_customers(revenue_by_customer)
    print("\nTop 10 Customers by Revenue:")
    print(top_10_customers)

if __name__ == "__main__":
    main()
