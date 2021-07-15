import smtplib
import requests
from bs4 import BeautifulSoup
import lxml

AMAZON_URL = "https://www.amazon.in/Logitech-Hyperion-Ultra-Gaming-Mouse/dp/B00NFD0ETQ/ref=pd_ys_c_rfy_976419031_3?_encoding=UTF8&pd_rd_i=B00NFD0ETQ&pd_rd_r=3WAFG6WBTF6S10ZN0WK0&pd_rd_w=hkdHJ&pd_rd_wg=UqhDE&pf_rd_p=a48c231b-e90e-4225-8c14-1ea8f540ac4f&psc=1&refRID=7GZ73WYN98CB709YKVCA"
my_email = YOUR_GMAIL  # Remember only gmailwill work here because we have chosen our host as gmail, you can change it if you want
password = YOUR_PASSWORD

#change your headers from http://myhttpheader.com/
headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "en-US,en;q=0.9",
    "X-Real-Ip": X_REAL_IP,
    "Accept": ACCEPT,
    "Accept-Encoding": ACCEPT_ENCODING,
}

response = requests.get(url=AMAZON_URL, headers=headers)
webpage = response.text
# print(webpage)

soup = BeautifulSoup(webpage, 'lxml')
# print(soup.prettify())
result = soup.find("span", id="priceblock_ourprice").getText()
price = result.split("₹")[1]
price = price.split(",")
price = "".join(price)
float_price = float(price)
print(float_price)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    # This line makes the connection secure by encrypting the message
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=TO_EMAIL_ADDRESS,
                        msg= f"Subject:Amazon Price Tracker Bot\n\nHello,\nThe product Logitech G402 Hyperion Fury "
                             f"Wired Gaming Mouse is available for Rs.{float_price} \nURL:{AMAZON_URL}")
