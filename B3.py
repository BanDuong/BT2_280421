import  requests
import pandas

re = requests.get("https://0dc66ea82a44ae6a54bf85f44014b2fd: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@shop850lang.myshopify.com/admin/api/2021-04/customers.json")
k= dict(re.json())
df = pandas.DataFrame(k)
df.to_csv("customer_data.csv",index=False)
