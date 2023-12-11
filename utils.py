import PyPDF2
import json
import traceback


def parse_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except PyPDF2.utils.PdfReadError:
            raise Exception("Error reading the PDF file.")

    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    else:
        raise Exception(
            "Unsupported file format. Only PDF and TXT files are supported."
        )


def get_table_data(quiz_str):
    try:
        # convert the quiz from a str to dict
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []
        # Iterate over the quiz dictionary and extract the required information

        for key, value in quiz_dict.items():
            if "mcq" in value:
                mcq = value["mcq"]
                options = " | ".join(
                    [
                        f"{option}: {option_value}"
                        for option, option_value in value["options"].items()
                    ]
                )
                correct = value["correct"]
                description = value["description"]
                quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct,"Solution":description})
            elif "tf" in value:
                # Process true/false question
                tf_question = value["tf"]
                tf_correct = value["correct"]
                tf_description = value["description"]
                quiz_table_data.append({"Question": tf_question, "Correct": tf_correct, "Solution": tf_description})
            elif "ShortAnswer" in value:
                # Process shortanswer
                ShortAnswer_question = value["ShortAnswer"]
                ShortAnswer_correct = value["correct"]
                ShortAnswer_description = value["description"]
                quiz_table_data.append({"Question": ShortAnswer_question, "Correct": ShortAnswer_correct, "Solution": ShortAnswer_description})

        return quiz_table_data
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False


RESPONSE_JSON = {
    "1": {
        "no": "1",
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
        "correct": "correct answer",
        "description":"Solution Description",
    },
    "2": {
        "no": "2",
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
        "correct": "correct answer",
        "description":"Solution Description",
    },
    "3": {
        "no": "3",
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
        "correct": "correct answer",
        "description":"Solution Description",
    },
}

RESPONSE_JSON_TF = {
    "1": {
        "no": "1",
        "tf": "true or false question",
        "correct": "correct answer",
        "description":"Solution Description",
    },
    "2": {
        "no": "2",
        "tf": "true or false question",
        "correct": "correct answer",
        "description":"Solution Description",
    },
    "3": {
        "no": "3",
        "tf": "true or false question",
        "correct": "correct answer",
        "description":"Solution Description",
    },
}

RESPONSE_JSON_ShortAnswer = {
    "1": {
        "no": "1",
        "ShortAnswer": "ShortAnswer question",
        "correct": "correct answer",
        "description":"Solution Description",
    },
    "2": {
        "no": "2",
        "ShortAnswer": "ShortAnswer question",
        "correct": "correct answer",
        "description":"Solution Description",
    },
    "3": {
        "no": "3",
        "ShortAnswer": "ShortAnswer question",
        "correct": "correct answer",
        "description":"Solution Description",
    },
}