import  requests
import pandas

re = requests.get("https://0dc66ea82a44ae6a54bf85f44014b2fd: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@shop850lang.myshopify.com/admin/api/2021-04/customers.json")
k= re.json()
df = pandas.DataFrame()
for customer in k['customers']:
    del customer['addresses']
    tmp = pandas.json_normalize(customer)
    df= df.append(tmp)
df = pandas.DataFrame(dict(df))
df.to_csv('customers_infor.csv',index=False)




