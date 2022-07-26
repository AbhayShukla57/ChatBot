from nltk.chat.util import Chat, reflections
QA = [
    [
        r"Hi|Hello|Hey",
        ["Hello there","Hey there"]
    ],
    [
        r"Quit",
        ["Bye"]
    ],
    [
        r"What is the college timing?",
        ["College timing is from 9:00 am to 5:00 pm."]
    ],
    [
        r"How many seats are there in any Branch?",
        ["Generally, there are 60 seats in every branch. Except 'Artificial Intelligence and Data Science' has 30 seats."]
    ],
    [
        r"Where is the college located?",
        ["The college is located at at K.T. Marg, Vartak College Campus Vasai Road, Vasai-Virar, Maharashtra 401202."]
    ],
    [
        r"How many courses are available in the college?",
        ["There are 8 courses in the college."]
    ],
    [
        r"Name the courses available in the college?",
        ["1.COMPUTER ENGINEERING\n2.INFORMATION TECHNOLOGY\n3.ELECTRONICS AND TELECOMMUNICATIONS ENGINEERING\n4.INSTRUMENTATION ENGINEERING\n5.COMPUTER SCIENCE AND ENGINEERING(DATA SCIENCE)\n6.CIVIL ENGINEERING\n7.ARTIFICIAL INTELLIGENCE AND DATA SCIENCE\n8.MECHANICAL ENGINEERING"]
    ],
    [
        r"What are the library’s working hours?",
        ["The timing for library is from 10:00 am to 5:00 pm."]
    ]
]

def bott():
    print("Hi,there. I'm Bot from Vidyavardhini's College of Engineering and Technology.\nType 'Quit' to leave the chat")
    chat = Chat(QA, reflections)
    chat.converse()

if __name__ == "__main__":
    bott()