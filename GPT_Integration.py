from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
My_API_KEY = os.getenv('MY_API_KEY')
import Flowchart

client = OpenAI(api_key = My_API_KEY)

semester = 0
taken_courses = 'hi'
preferences = 'None'
introduction = "You are a Penn State Engineering Advisor, specifically for Computer Science. Your goal is to create an academic schedule based off the given content."
explain_main_courses = "Here is a dictionary with all the keys as required courses to take as a Computer Science Major. \
           An element can be a equivalent course you can take if there is a dash (-) in front of it. \
           If the last element of the list in the value is an integer, the integer represents the minimum semester status the user must be in to take that specific course.\
           If the characters -c are attached to the end of a course, this signifies that the course is a concurrent requirement for the key course.\
           Every other element is a pre-requisite (prereq) course. Every course (key) within this dictionary should be considered a major course."
explain_general_education = "Here is a dictionary with all of the general education credits. \
           Each key refers to a category of general education, this can be treated as a course. \
           Each key's value refers to the total credits that are needed for that specific course.\
           General education credit courses can be displayed as their key values (type of general education credit - not actual specific course) when put into a schedule.\
           Within a single semester in the schedule, aim to include 1-2 general education courses."
explain_CMPSC_electives = f"Within the dictionary of all the general education credits, there is a key that is labeled \"CMPSC Electives\"\
           Here is an additional dictionary named CMPSC_Electives. Based on the user's preferences being: {preferences}, choose 6 credits worth of courses."
explain_credit_values = "Here is a list of all the courses with a credit value of 4.\
           CMPSC 111 is 1 credit. If a course is not within this list and is not CMPSC 111, it can be assumed that the course is worth 3 credits."
explain_courses_taken = "Here is a list of all of the credits that the student has already taken. \
            Add all of these credits to the total credits needed for the student's degree"
explain_major_credits = "This number is the total required major credits, that is, the total number of credits from courses that are not considered general education credits needed for a student to obtain their Computer Science degree."
create = "Create a schedule for the student's remaining semesters that satisfies the major credits that are still needed and the general education credits that are still needed.\
           Attempt to satisfy the student's CMPSC_electives courses preferences but do not prioritize those preferences.\
           Try to keep the total credits that a student takes within a semester between 15 and 17. Format the schedule as a dictionary "


chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": ""},
        {"role": "system", "content": explain_main_courses},  # Explain main courses
        {"role": "system", "content": Flowchart.cmpsc_courses},
        {"role": "system", "content": explain_general_education}, # Explain gen eds
        {"role": "system", "content": Flowchart.general_education},
        {"role": "system", "content": explain_CMPSC_electives}, # Explain CMPSC Electives (preferences)
        {"role": "system", "content": Flowchart.CMPSC_Electives},
        {"role": "system", "content": explain_credit_values}, # Explain credit values
        {"role": "system", "content": Flowchart.four_credit},
        {"role": "system", "content": explain_courses_taken}, # Explain courses taken
        {"role": "system", "content": taken_courses},
        {"role": "system", "content": explain_major_credits}, # Explain major credits
        {"role": "system", "content": Flowchart.major_cred},
        {"role": "system", "content": create}, # Create the schedule
    ],
    model = "gpt-3.5-turbo"
)

schedule = chat_completion.choices[0].message.content

