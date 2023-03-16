import requests
torch_url = "https://pytorch.org/docs/1.13/generated/torch.abs.html?highlight=abs#torch.abs"
torch_page = requests.get(torch_url).text
print(torch_page)