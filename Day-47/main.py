import os
import smtplib
import lxml
import requests 
import bs4

USERNAME= os.environ.get('Email')
PASSWORD= os.environ.get('password')
User_ID = "rohityou000@gmail.com"

URL ="https://www.amazon.in/kossto-Premium-Magnetic-Corrector-Shoulder/dp/B08PF8SV1R/ref=pd_rhf_gw_s_trq_n2gl_se2cg5gn_sccl_1_7"
header = { "Accept-Language" : "en-US,en;q=0.9,bn;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
            "Cookie":"PHPSESSID=nia9hbcr3r4alqo36shlnh9o24; _ga=GA1.2.1156547150.1651159273; _gid=GA1.2.1553951680.1651159273"}

response = requests.get(URL,headers=header)


soup = bs4.BeautifulSoup(response.content ,'lxml')
# print(soup.prettify)    
title = soup.find(id="productTitle").get_text().strip()
price = soup.find(class_="a-price-whole").get_text()


price = float(price)
target_price = 499.0

if price <= target_price:
    message = f"{title} is now at ₹{price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connections:
        connections.starttls()
        connections.login(user=USERNAME, password=PASSWORD)
        connections.sendmail(from_addr= USERNAME,
            to_addrs=User_ID,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
else:
    pass

