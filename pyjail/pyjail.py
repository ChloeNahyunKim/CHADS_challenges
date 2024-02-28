import re
from sys import version

contraband = "import|chr|os|sys|system|builtin|exec|eval|subprocess|pty|popen|read|getdata"
search_func = lambda word: re.compile(r"\b({0})\b".format(word), flags=re.IGNORECASE).search

def main():

    print("[Guard] Welcome to Chloe's Cat Prison where we keep only th- hey wait where are you going? Those are where the prisoners are, NO CIVILIANS ALLOWED!")
    input("(Enter Any key)")
    print("[Kenny whispers to you from his cell] Hey kid you want to make 5 bucks? Well you gotta get me out, but it won't be easy. They've gotten rid of every tool we could use, however, I've keestered in this little magic lamp")
    print("It gives you the power to run code in python, and all you have to do is read the freekenny.txt file where they keep the master code for these gaddamn locks. You got this, I know you're purrrrrfect for the job.")
    status = False
    while not status:
        text = input('>>> ').lower()
        check = search_func(contraband)(''.join(text.split("__")))
        if check:
            print(f"Hey get your paws off of that {check.group(0)} function! It belongs in the 'contraband' pile")
            break
        if re.match("^(?[A-Za-z0-9])[A-Za-z](_?[A-Za-z0-9])$", text):
            print("You must be hisssssss-terical to think we would let you out that easily.")
            break
        if not re.search("(^|[^A-Za-z0-9])os([^A-Za-z0-9]|$)", contraband):
            status = True
            exec(text)
            for i in range(2):
                text = input('>>> ').lower()
                exec(text)
        else:
            exec(text)

main()