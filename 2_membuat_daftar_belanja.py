file = open('list_belanja.txt','a+')

def add_to_list(newText):
    file.write('\n' + newText)
    ask_user()


def ask_user():
    add_to_list(input("Mau beli apa? "))

ask_user()