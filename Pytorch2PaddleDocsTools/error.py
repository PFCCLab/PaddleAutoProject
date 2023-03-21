import re


class TorchAliasFor(Exception):
    def __init__(self, torch_page, torch_url):
        self.torch_url = torch_url
        self.torch_page = torch_page
        self.new_url = ""
        self.get_new_url()

    def __str__(self):
        return "Alias for: " + self.new_url

    def get_new_url(self):
        temp_url = str(re.findall(
            r'Alias for <a class="reference internal" href="(.*?)" title="', self.torch_page, re.DOTALL)[0])
        self.new_url = '/'.join(self.torch_url.split('/')[:-1]) + "/" + temp_url
