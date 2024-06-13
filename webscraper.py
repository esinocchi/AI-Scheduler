# Evan Sinocchi
# 2024-03-20
# webscraper to collect data for AI Advisor
import requests
from bs4 import BeautifulSoup
import json
import html



url = ['https://bulletins.psu.edu/undergraduate/general-education/course-lists/arts/', 
       'https://bulletins.psu.edu/undergraduate/general-education/course-lists/health-wellness/',
       'https://bulletins.psu.edu/undergraduate/general-education/course-lists/humanities/',
       'https://bulletins.psu.edu/undergraduate/general-education/course-lists/natural-sciences/',
       'https://bulletins.psu.edu/undergraduate/general-education/course-lists/quantification/',
       'https://bulletins.psu.edu/undergraduate/general-education/course-lists/social-behavioral-sciences/',
       'https://bulletins.psu.edu/undergraduate/general-education/course-lists/writing-speaking/',
       'https://bulletins.psu.edu/undergraduate/general-education/course-lists/inter-domain/',
       'https://bulletins.psu.edu/undergraduate/general-education/course-lists/first-year-seminar/']

file_name = ['arts.json', 'health-wellness.json', 'humanities.json', 'natural-sciences.json', 'quantification.json',
             'social-behavioral-sciences.json', 'writing-speaking.json', 'inter-domain.json', 'first-year-seminar.json']



def fetch_data(encoded_code):
        xhr_url = f'https://bulletins.psu.edu/ribbit/index.cgi?page=getcourse.rjs&code={encoded_code}'
        response = requests.get(xhr_url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to fetch data for {encoded_code}: {response.status_code}")
        return None

def getPrerequisites(data: BeautifulSoup, find):

    def isCourseCode(string):
        if string.isalpha() and string.isupper():
            return True
        return False
    
    def isOperator(string):
        if string == 'and' or string == 'or':
            return True
    
    d = data.find(find)
    if d:
        parent_p = d.parent
        content_parent = str(parent_p)
        parent_soup = BeautifulSoup(content_parent, 'html.parser')
        parent_text = parent_soup.get_text(' ', strip=True).replace(u'\xa0', ' ')
        parse = parent_text.split(':')
        concurrent = ''
        additional_concurrent = False
        course_list = []
        operation = []
        for i, item in enumerate(parse):
            if i == 0:
                if 'Concurrent' in item:
                    concurrent = '--' # marks if concurrent pre-requisite
            if i == 1:
                if 'Concurrent' in item:
                    additional_concurrent = True
                splitted = item.split(' ')
                
                
                for j in range(len(splitted)):

                    if isCourseCode(splitted[j]): # course code
                        course_list.append(splitted[j] + ' ' + splitted[j + 1] + concurrent)

                    elif '_' in splitted[j]: # special case
                        course_list.append(splitted[j])
                        
                    elif isOperator(splitted[j]) and isCourseCode(splitted[j + 1]): # operators
                        operation.append(splitted[j])


                '''for k in range(len(course_list) - 1):
                    c1 = course_list[k]
                    c2 = course_list[k + 1]
                    if operation:
                        op = operation[k]
                        if op == 'or': # appends * to indicate or
                            if '*' not in c1:
                                course_list[k] = c1 + '*'
                            if '*' not in c2:
                                course_list[k + 1] = c2 + '*'''
                for k in range(len(course_list) - 1):
                    if k < len(operation):
                        c1 = course_list[k]
                        c2 = course_list[k + 1]
                        op = operation[k]
                        if op == 'or':  # appends * to indicate or
                            if '*' not in c1:
                                course_list[k] = c1 + '*'
                            if '*' not in c2:
                                course_list[k + 1] = c2 + '*'

            if additional_concurrent and i == 2:
                courses = item.split()
                print(courses)
                if len(courses) > 1:
                    for k in range(len(courses)):

                        if isCourseCode(courses[k]):
                            course_list.append(courses[k] + ' ' + courses[k + 1] + '--')
                        elif isOperator(courses[k]) and isCourseCode(courses[k + 1]): # operators
                            operation.append(courses[k])

                        '''if len(course_list) > len(operation) and k > 0: 
                            ### FIX THIS ISSUE ####
                            c1 = courses[k]
                            c2 = courses[k + 1]
                            counter = 0
                            if operation:
                                op = operation[counter]
                                counter += 1
                                if op == 'or': # appends * to indicate or
                                    if '*' not in c1:
                                        course_list[k] = c1 + '*'
                                    if '*' not in c2:
                                        course_list[k + 1] = c2 + '*'''
                        if k < len(courses) - 1 and isOperator(courses[k]):
                            operation.append(courses[k])
                            if k + 1 < len(course_list) and isCourseCode(courses[k + 1]):
                                c1 = course_list[k]
                                c2 = course_list[k + 1]
                                if operation:
                                    op = operation[-1]
                                    if op == 'or':
                                        if '*' not in c1:
                                            course_list[-1] = c1 + '*'
                                        if '*' not in c2:
                                            course_list.append(c2 + '*')

        return course_list
    return None
    
def writeToJSON(data, file_name):
    with open(file_name, 'w') as json_file:
        json_file.write(data)

def xml_to_html(data, search):
    soup = BeautifulSoup(data, 'lxml-xml')
    element = soup.find(search)
    decoded_html = html.unescape(element.string)
    extracted_data = BeautifulSoup(decoded_html, 'html.parser')
    return extracted_data

'''testing
code = 'CHEM%20113'
xml = fetch_data(code)
d = xml_to_html(xml, 'course')
print(getPrerequisites(d, 'strong'))
testing'''


for i in range(len(url)):
    response = requests.get(url[i])

    if response.status_code == 200:

        dataset = {}
        codes = []
        descriptions = []
        credits = []
        pre_requisites = []

        content = BeautifulSoup(response.content, 'html.parser')
        course_table = content.find('table', class_ = 'sc_courselist')

        rows = course_table.find_all('td')

        for k, row in enumerate(rows):

            if k % 3 == 0:
                clean_code = row.text.replace(u'\xa0', ' ')
                print(clean_code)
                encoded_code = (clean_code).replace(' ', '%20')
                xml_data = fetch_data(encoded_code)
                codes.append(clean_code)

                extracted_data = xml_to_html(xml_data, 'course')
                p = getPrerequisites(extracted_data, 'strong')

                if p == None:
                    pre_requisites.append([])
                else:
                    pre_requisites.append(p)

            elif k % 3 == 1:
                descriptions.append(row.text)

            else:
                credits.append(row.text)
        
        
        for j in range(len(credits)):
            dataset[codes[j]] = {
                "description": descriptions[j].strip(),
                'pre-requisite': pre_requisites[j],
                "credits": credits[j].strip()
                }
            
        json_data = json.dumps(dataset, indent = 4)

        writeToJSON(json_data, file_name[i]) # writes to JSON file

        print('Done!')

    else:
        print("Page not found")