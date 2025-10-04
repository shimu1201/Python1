url = input("Enter website url : ")

print(url)

if url.startswith("http://") or url.startswith("https://"):
    if url.endswith(".com") or url.endswith(".in") or url.endswith(".co"):
        print("Valid Url")
    else:
        print("Make sure your url ends with specific domain")
else:
    print("Port not found!!!")