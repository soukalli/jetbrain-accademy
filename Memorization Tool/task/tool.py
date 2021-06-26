# write your code here
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
successor = {'A': 'B', 'B': 'C'}

class FlashCard(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True)
    question = Column(String(255))
    answer = Column(String(255))
    box = Column(String(1))


Base.metadata.create_all(engine)


def print_main_menu():
    print("1. Add flashcards")
    print("2. Practice flashcards")
    print("3. Exit")


def process_menu_1():
    sub_menu_choice = ""
    while sub_menu_choice != "2":
        print("1. Add a new flashcard")
        print("2. Exit")
        sub_menu_choice = input()
        if sub_menu_choice == "1":
            print("Question:")
            question = input()
            while question.strip() == "":
                print("Question:")
                question = input()
            print("Answer:")
            answer = input()
            while answer.strip() == "":
                print("Answer:")
                answer = input()
            card = FlashCard(question=question, answer=answer, box='A')
            session.add(card)
            session.commit()
        elif sub_menu_choice != "2":
            print("{0} is not an option".format(sub_menu_choice))


def update_card_status(flashcard, is_success):
    if not is_success:
        flashcard.box = 'A'
    else:
        if flashcard.box == 'C':
            session.delete(flashcard)
        else:
            flashcard.box = successor.get(flashcard.box)
    session.commit()


def process_confirmation_flashcard(flashcard):
    print("Answer: {}".format(flashcard.answer))


def process_answer_flashcard(flashcard):
    print('press "y" if your answer is correct:')
    print('press "n" if your answer is wrong:')
    choice = ""
    while choice != "y" and choice != "n":
        choice = input()
        if choice == "y" or choice == "n":
            update_card_status(flashcard, choice == "y")
            break
        else:
            print("{0} is not an option".format(choice))


def process_update_flashcard(flashcard):
    print('press "d" to delete the flashcard:')
    print('press "e" to edit the flashcard:')
    choice = ""
    while choice != "d" and choice != "e":
        choice = input()
        if choice == "e":
            print("current question: {0}".format(flashcard.question))
            question = input("please write a new question:\n")
            flashcard.question = question
            print("current answer: {0}".format(flashcard.answer))
            answer = input("please write a new answer:\n")
            flashcard.answer = answer
            global session
            session.commit()
            break
        elif choice == "d":
            session.delete(flashcard)
            break
        else:
            print("{0} is not an option".format(choice))


def process_flashcard(flashcard):
    print("Question: {}".format(flashcard.question))
    print('press "y" to see the answer:')
    print('press "n" to skip:')
    print('press "u" to update:')
    sub_menu_choice = ""
    while sub_menu_choice != "n":
        sub_menu_choice = input()
        if sub_menu_choice == "y":
            process_confirmation_flashcard(flashcard)
            process_answer_flashcard(flashcard)
            break
        elif sub_menu_choice == "n":
            process_answer_flashcard(flashcard)
            break
        elif sub_menu_choice == "u":
            process_update_flashcard(flashcard)
            break
        elif sub_menu_choice != "n":
            print("{0} is not an option".format(sub_menu_choice))


def process_menu_2():
    flashcards = session.query(FlashCard).all()
    if len(flashcards) == 0:
        print('There is no flashcard to practice!')
    else:
        for flashcard in flashcards:
            process_flashcard(flashcard)


def process_main_menu(choice):
    if choice == "1":
        process_menu_1()
    elif choice == "2":
        process_menu_2()
    elif choice != "3":
        print("{} is not an option".format(choice))


def main_loop():
    choice = ""
    while choice != "3":
        print_main_menu()
        choice = input()
        process_main_menu(choice)
    print("Bye!")


main_loop()
