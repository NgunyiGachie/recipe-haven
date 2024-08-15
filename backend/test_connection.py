import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres.lwfpwzgjbdlfctlgfunl",
        password="Nfee84AsEJMajB!",
        host="aws-0-eu-west-2.pooler.supabase.com",
        port="6543",
        database="postgres"
    )
    print("Connection successful")
except Exception as e:
    print(f"Error: {e}")

