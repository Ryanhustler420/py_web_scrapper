from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html>
<head>
	<title>HTML Tables</title>
</head>
<body>
	<table border="1">
		<tr>
			<td>Row 1, Cloumn 1</td>
			<td>Row 1, Cloumn 2</td>
		</tr>
		<tr>
			<td>Row 2, Cloumn 1</td>
			<td>Row 2, Cloumn 2</td>
		</tr>
	</table>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

for tr in soup.find_all('tr'):
	for td in tr.find_all('td'):
		print(td.text)