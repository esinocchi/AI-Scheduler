#HACKPSU AI Schedule Advisor

cmpsc_courses = {

    # format
    # course: optional equivalent course, prerequisites, semester

    "CMPSC 131": {'Concurrent': ['MATH 140'], 'Prereq': [], 'Difficulty': '1'}, # Introduction to Programming with Python
    "CMPSC 132": {'Concurrent': [], 'Prereq': ['CMPSC 131'],'Difficulty': '2'},  # Advanced Programming with Python
    "CAS 100 A/B": {'Concurrent': [], 'Prereq': [], 'Difficulty': '1'},  # Effective Speech
    "ENGL 015": {'Concurrent': [], 'Prereq': [], 'Difficulty': '1'},  # Rhetoric and Composition
    "MATH 140": {'Concurrent': [], 'Prereq': [], 'Difficulty': '1'},  # Calculus With Analytic Geometry I
    "CMPSC 111": {'Concurrent': [], 'Prereq': [], 'Difficulty': '1'},  # Introductory Seminar in Computer Science
    "MATH 141": {'Concurrent': [], 'Prereq': ['MATH 140'], 'Difficulty': '2'},  # Calculus With Analytic Geometry II
    "CMPSC 221": {'Concurrent': [], 'Prereq': ['CMPSC 132'], 'Difficulty': '1'},  # Object Oriented Programming with Web-Based Applications
    "MATH 220": {'Concurrent': [], 'Prereq': ['MATH 140'], 'Difficulty': '1'},  # Matrices
    "CMPSC 311": {'Concurrent': [], 'Prereq': ['CMPSC 221'], 'Difficulty': '3'},  # Introduction to Systems Programming
    "CMPSC 465": {'Concurrent': [], 'Prereq': ['CMPSC 360'], 'Difficulty': '3'},  # Data Structures and Algorithms
    "CMPSC 360": {'Concurrent': ['CMPSC 132'], 'Prereq': [], 'Difficulty': '2'},  # Discrete Mathematics for Computer Science
    "STAT 318": {'Concurrent': [], 'Prereq': ['MATH 141'], 'Difficulty': '1'},  # Elementary Probability
    "ENGL 202C": {'Concurrent': [], 'Prereq': ['ENGL 015'], 'Difficulty': '2'}, #["ENGL 015", "4"],  # Technical Writing
    "STAT 319": {'Concurrent': [], 'Prereq': ['STAT 318'], 'Difficulty': '1'},  # Elementary Statistics
    "PHYS 211": {'Concurrent': ['MATH 140'], 'Prereq': [], 'Difficulty': '2'},  # General Physics: Mechanics
    "MATH 230": {'Concurrent': [], 'Prereq': ['MATH 141'], 'Difficulty': '3'},  # Calculus and Vector Analysis
    "CMPSC 461": {'Concurrent': [], 'Prereq': ['CMPSC 360', 'CMPSC 221'], 'Difficulty': '1'},  # Programming Language Concepts
    "CMPSC 464": {'Concurrent': [], 'Prereq': ['CMPSC 465'], 'Difficulty': '1'},  # Introduction to the Theory of Computation
    "PHYS 212": {'Concurrent': ['MATH 141'], 'Prereq': ['PHYS 211'], 'Difficulty': '3'},  # General Physics: Electricity and Magnetism
    "CMPEN 270": {'Concurrent': ['PHYS 212'], 'Prereq': [], 'Difficulty': '2'},  # Digital Design: Theory and Practice
    "CMPEN 331": {'Concurrent': [], 'Prereq': ['CMPEN 270', 'CMPSC 131'], 'Difficulty': '1'},  # Computer Organization and Design
    "CMPSC 473": {'Concurrent': [], 'Prereq': ['CMPSC 311', 'CMPEN 331'], 'Difficulty': '3'},  # Operating Systems Design and Construction
    "CMPSC 483W": {'Concurrent': [], 'Prereq': ['CMPSC 465'], 'Difficulty': '1', 'Interchange': ['CMPSC 431W']},  # Software Design
    "CMPSC 431W": {'Concurrent': [], 'Prereq': ['ENGL 202C', 'CMPSC 221'], 'Difficulty': '1', 'Interchange': ['CMPSC 483W']} # Database Management Systems
}
four_credit = ["MATH 140", 'MATH 141', 'PHYS 211', 'MATH 230', 'CMPEN 270', 'PHYS 212', 'Foreign Language']

priority = ['CMPSC 131', 'CMPSC 132', 'MATH 140', 'MATH 141', 'PHYS 211', 'ENG 015', 'PHYS 212', 'CMPEN 270', 'CMPSC 221', 'CMPSC 360']

general_education = {
            'GWS': 9,
            'GA': 3,
            'GHW': 3,
            'GH': 3,
            'GS': 3,
            'GN': 9,
            'Inter-Domain': 6,
            'World-Language': 6,
            'Non-CMPSC 400': 6,
            'Department (Engineering) Electives': 10,
            'CMPSC_Electives': 6
        }

CMPSC_Electives = {
    'CMPEN 362': {'Description': "Communication Networks", 'Prereq': ['CMPEN 270', 'STAT 318-c']},
    'CMPEN 431': {'Description': 'Introduction to Computer Architecture', 'Prereq': ['CMPEN 331']},
    'CMPEN 454': {'Description': 'Fundamentals of Computer Vision', 'Prereq': ['MATH 230', 'MATH 220']},
    'CMPSC 442': {'Description': 'Artificial Intelligence', 'Prereq': ['CMPSC 221', 'CMPSC 465-c']},
    'CMPSC 443': {'Description': 'Introduction to Computer and Network Security', 'Prereq': ['CMPEN 362', 'CMPSC 473-c']},
    'CMPSC 444': {'Description': 'Secure Programming', 'Prereq': ['CMPSC 221']},
    'CMPSC 450': {'Description': 'Concurrent Scientific Programming', 'Prereq': ['CMPSC 131', 'MATH 220', 'MATH 230']},
    'CMPSC 451': {'Description': 'Numeric Computations', 'Prereq': ['CMPSC 131, MATH 230']},
    'CMPSC 455': {'Description': 'Introduction to Numerical Analysis I', 'Prereq': ['CMPSC 131', 'MATH 220', 'MATH 230']},
    'CMPSC 456': {'Description': 'Introduction to Nuneriacal Analysis II', 'Prereq': ['MATH 455']},
    'CMPSC 458': {'Description': 'Fundamentals of Computer Graphics', 'Prereq': ['CMPSC 311', 'MATH 220', 'MATH 230']},
    'CMPSC 467': {'Description': 'Factorization and Primality Testing', 'Prereq': ['CMPSC 360']},
    'CMPSC 471': {'Description': 'Introductions to Compiler Construction', 'Prereq': ['CMPSC 461']},
    'CMPSC 475': {'Description': 'Applications Programming', 'Prereq': ['CMPSC 221', 'CMPSC 311', 'CMPSC 465']},
    'EE 456': {'Description': 'Introduction to Neural Networks', 'Prereq': ['CMPSC 131', 'MATH 220']},
}



gened_cred = '45'
major_cred = '82'
