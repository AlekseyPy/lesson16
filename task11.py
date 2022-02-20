def html(tag, info):
     return f"<{tag}>{info}</{tag}>"
a = input("Tag: ")
b = input("Info: ")
print(html(a,b))
