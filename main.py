import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

parameters = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=URL, headers=parameters)
data = response.text

soup = BeautifulSoup(data, "lxml")

a = soup.find(name="span", class_="a-price-whole").getText()
b = soup.find(name="span", class_="a-price-fraction").getText()
final_price = a + b
print(final_price)

title = soup.find(name="span", id="productTitle").getText().strip()
print(title)

# EMAIL USING SMTP
if float(final_price) < 100:
    my_email = "pythonusecode@gmail.com"
    password = "ohtuqsysukwikisz"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="harshitabaid15@gmail.com",
                            msg=f"Subject:{title}\n\n{final_price}\n{URL}".encode('ascii', 'ignore').decode('ascii'))
