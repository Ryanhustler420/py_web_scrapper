from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html>
<head>
	<title>Raisehand LLC</title>
</head>
<body>
	<<p>
		<<b>Raisehand LLC</b>
	</p>
	<<p class="story">
		Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
		<a href="http://example.com/elsie" class="sister" id="link1">Email Elsie</a>
		<a href="http://example.com/lacie" class="sister" id="link2">Email lacie</a>
		<a href="http://example.com/tille" class="sister" id="link3">Email tille</a>
		consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
		cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
		proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
	</p>
	<<p class="story">...</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

p = soup.find('p', class_ = 'story')

# Search for all child
# all_p_children = p.findChildren()
# print(all_p_children)


# Search for parent
# p_parent = p.findParent()
# print(p_parent)

# Search for Sibling
first_a = soup.find('a')
remain_sibling = first_a.findNextSiblings()
print(remain_sibling)