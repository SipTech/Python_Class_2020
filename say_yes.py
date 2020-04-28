# the question in code
answer = False

while not answer:
    question = 'Will you marry me?\n Pick an option\n a = yes\n b = a\n c = b\n Else enter any key for yes..: '
    answer = input(question)
    if answer:
        print('Hooray!! I will move ahead with wedding arrangements.. :D')
        break