import requests
paddle_url = "https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/amax_cn.html"
paddle_page = requests.get(paddle_url).text

from bs4 import BeautifulSoup
soup = BeautifulSoup(paddle_page, 'html.parser')

for link in soup.find_all("dt", attrs={"class" :"sig sig-object py"}):
    function_name = link.get('id')

function_str = ''
for link in soup.find_all("em", attrs={"class" :"sig-param"}):
    for ll in link.find_all("span", attrs={"class" :"pre"}):
        function_str+=ll.string
    function_str+=','

# 去除最后多余的','
function_str = function_str[:len(function_str)-1]

print(function_name)
print(function_str)

function_paddle = f'{function_name}({function_str})'
print("解析的结果为:",function_paddle)