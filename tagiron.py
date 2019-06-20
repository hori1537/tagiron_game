

import random
# first

def q1(cards):
    return sum(cards)

def q2(cards):
    return cards[2] - cards[0]
def q3(cards):
    return cards[1]
def q4(cards):
    return cards[0]
def q5(cards):
    return cards[2]

def Choose_question_or_declaration():
    input_ = input("Choose_question_or_declaration ... ")

    if input_ in ['']:
        return Choose_question_or_declaration()

    elif input_ in 'declaration' or input_ in '宣言':
        print(input_ in 'declaration')
        print(input_ in '宣言')

        print('declaration')
        return 'declaration'

    elif input_ in field_question:

        print('field_question')
        print(field_question)
        return input_
    else:
        print('input number in field question... ', field_question)
        return Choose_question_or_declaration()

def declaration():
    def input_num_mark():
        cards_de = []
        def input_num():
            num_ = input('please input the num... ')

            if num_ in ['0', '1', '2', '3', '4', '6', '7', '8', '9']:
                pass
            elif num_ in ['5']:
                pass
            else:
                print('please input 0 to 9')
                return input_num()

            return num_

        def input_mark(num_):
            if num_ != '5':
                mark_ = input('please input the mark... ')

                if mark_ in 'blue':
                    mark_ = '1-blue'

                elif mark_ in 'red':
                    mark_ = '0-red'

                else:
                    print('please input blue or red')
                    return input_suit(num_)

            elif num_ == '5':
                mark_ = '2-yellow'

            return mark_

        for i in range(5):
            num_ = input_num()
            mark_ = input_mark(num_)

            card_ = [num_, mark_]
            cards_de.append(card_)

            print('入力カードは')
            print(cards_de)

        is_yes = input('OK?')

        if is_yes in ['yes', 'ye', 'y', 'ok', 'OK', '']:
            return cards_de
        else:
            print(' ')
            return Choose_question_or_declaration

    cards_de = input_num_mark()
    return cards_de

def choose_question(input_):

    if input_ in field_question:
        question = question_dict[input_][0]

    else:
        print('input the question in the field')
        return choose_question

    return question


## main part
print('start')

cards = [0,0]
cards[0] = [0,1,2]
cards[1] = [3,5,7]
print(cards[0])

question_dict =  {'1': [q1, 'm_q1'],'2': [q2, 'm_q2'],'3': [q3, 'm_q3'],'4': [q4, 'm_q4'],'5': [q5, 'm_q5']}
stock_question = ['1','2','3','4','5']
random.shuffle(stock_question)

field_num = 2
field_question = stock_question[0:field_num]

print('stock_question')
print(stock_question)

print('field_question')
print(field_question)
field_question.sort()

for turn in range(15):
    player = turn % 2
    print('player-',  player + 1)

    print('field_question')
    #print(field_question)

    q_d = Choose_question_or_declaration()

    if q_d == 'declaration':
        cards_de = declaration()
        victory_ = check_answer(cards_de)
    else:
        question_number = q_d
        question_func = choose_question(q_d)

        print('answer')
        answer = question_func(cards[not player])
        print(answer)

        print('field_question')
        print(field_question)

        print('question')
        print(question_number)


        field_question.remove(question_number)
        if turn <=2:
            field_question.append(stock_question[field_num + turn : field_num  + turn + 1][0])

        print(field_question)
