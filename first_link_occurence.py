page="<html><body><a href="https://www.w3schools.com">This is a link</a></body></html>"
start_link=page.find('<a hef')
start_quote=page.find('"',start_link)
end_quote=page.find('"',start_quote+1)
url=page[start_quote+1:end_quote]
