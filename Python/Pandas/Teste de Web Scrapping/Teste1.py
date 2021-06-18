import pandas

data = pandas.read_html("https://modin.readthedocs.io/en/latest/supported_apis/io_supported.html")
print(data)