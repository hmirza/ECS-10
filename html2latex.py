#this program should convert an inputted HTML string to LaTeX string
#First, it should ask for an HTML string, user will then input the statement and hit enter
HTML = input('Please enter a HTML string: ')

#The next few lines executes the language conversions (HTML 2 LaTeX)

HTML = (HTML.replace("&ldquo;", "``"))
HTML = HTML.replace('&rdquo;', '"')
HTML = HTML.replace('&apos;', "'")
HTML = HTML.replace('&amp;', '&')
HTML = HTML.replace('&lt;', '<')
HTML = HTML.replace('&gt;', '>')
HTML = HTML.replace('{', '\{')
HTML = HTML.replace('}','\}')
HTML = HTML.replace('%', '\%')

#This next line should print the final statement which is a conversion from HTML to LaTeX
print(HTML)





