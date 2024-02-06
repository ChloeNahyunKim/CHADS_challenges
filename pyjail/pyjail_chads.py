import re
from sys import version

banned = "import|chr|os|sys|system|builtin|exec|eval|subprocess|pty|popen|read|get_data"
search_func = lambda word: re.compile(r"\b({0})\b".format(word), flags=re.IGNORECASE).search

def main():
    print("Your goal is to find the flag. Can you do it?")
    status = False
    while not status:
        text = input('>>> ').lower()
        check = search_func(banned)(''.join(text.split("__")))
        if check:
            print(check, banned)
            print(f"Nope, you can't use {check.group(0)}!")
            break
        if re.match("^(_?[A-Za-z0-9])*[A-Za-z](_?[A-Za-z0-9])*$", text):
            print("You aren't getting through that easily, come on.")
            break
        if not re.search("(^|[^A-Za-z0-9])os([^A-Za-z0-9]|$)", banned):
            status = True
            exec(text)
            for _ in range(2):
                text = input('>>> ').lower()
                exec(text) 
        else:
            exec(text, {'globals': globals()})


if __name__ == "__main__":
    main()
