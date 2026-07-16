FAQS = [

    {
        "question": "library eessa jira",
        "answer": "MWU Library barattootaaf kitaabota fi resources barnootaa dhiyeessa.",
        "topic": "library"
    },

    {
        "question": "dorm akkamittan argadha",
        "answer": "Dorm argachuuf Student Service fi Housing office hordofi.",
        "topic": "dormitory"
    },

    {
        "question": "registration yoom jalqaba",
        "answer": "Registration yeroo university beeksisu keessatti jalqaba.",
        "topic": "registration"
    },

    {
        "question": "ict email akkamittan argadha",
        "answer": "ICT office irraa university email argachuu dandeessa.",
        "topic": "ict"
    },

]


def get_faqs():

    return FAQS



def search_question(question, language="en"):

    question = question.lower().strip()


    for faq in FAQS:

        if faq["question"] in question or question in faq["question"]:

            return {
                "answer": faq["answer"],
                "topic": faq["topic"]
            }


    # keyword search

    if "library" in question:

        return {
            "answer": "MWU Library keessatti kitaabota fi resources barnootaa argachuu dandeessa.",
            "topic": "library"
        }


    elif "dorm" in question:

        return {
            "answer": "Dorm information argachuuf Student Service ilaali.",
            "topic": "dormitory"
        }


    elif "ict" in question or "email" in question:

        return {
            "answer": "ICT office irraa university email argachuu dandeessa.",
            "topic": "ict"
        }


    elif "register" in question or "registration" in question:

        return {
            "answer": "Registration odeeffannoo argachuuf Admission office ilaali.",
            "topic": "admission"
        }


    return {

        "answer": "Dhiifama, gaaffii kanaaf deebii hin qabu.",

        "topic": ""

    }