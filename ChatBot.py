from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')
trainer = ListTrainer(bot)
trainer.train([
    'Hi',
    'Hello there',
    'What is the college timing',
    'College timing is from 9:00 am to 5:00 pm',
    'How many seats are there in any Branch',
    'Generally, there are 60 seats in every branch. Except "Artificial Intelligence and Data Science" has 30 seats',
    'Where is the college located',
    'The college is located at at K.T. Marg, Vartak College Campus Vasai Road, Vasai-Virar, Maharashtra 401202',
    'How many courses are available in the college',
    'There are 8 courses in the college',
    'Name the courses available in the college',
    '1.COMPUTER ENGINEERING\n2.INFORMATION TECHNOLOGY\n3.ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING\n4.INSTRUMENTATION ENGINEERING\n5.COMPUTER SCIENCE AND ENGINEERING(DATA SCIENCE)\n6.CIVIL ENGINEERING\n7.ARTIFICIAL INTELLIGENCE AND DATA SCIENCE\n8.MECHANICAL ENGINEERING',
    'What are the library’s working hours',
    'The timing for library is from 10:00 am to 5:00 pm',
    'Ok Thanks',
    'No Problem! Have a Good Day!'
])

while True:
    request = input('You:')
    if request == 'Bye' or request == 'quit':
        print('Bot: Bye')
        break
    else:
        response = bot.get_response(request)
        print('Bot:', response)