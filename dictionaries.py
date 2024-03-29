
digital_info_questions_hard = {
    1: {
        'question': "The binary number system uses only two digits, 0 and 1.",
        'options': {
            'a': "True",
            'b': "False"
        },
        'answer': 'a',
        'keywords': ['true']
    },
    2: {
        'question': "Convert the decimal number 10 to binary.",
        'options': {
            'a': "1010",
            'b': "1001",
            'c': "101",
            'd': "10"
        },
        'answer': 'a',
        'keywords': ['1010']
    },
    3: {
        'question': "Which of the following represent the most data",
        'options': {
            'a': "kilobyte",
            'b': "megabyte",
            'c': "gigabyte",
            'd': "terabyte"
        },
        'answer': 'd',
        'keywords': ['terabyte']
    }, 
    4: {
        'question': "The first, middle, and last words of ASCII",
        'options': {
            'a': "American, Code, Interchange",
            'b': "Advanced Scientific Computer",
            'c': "Automated, Code, Information",
            'd': "All, Central, Interchange"
        },
        'answer': 'a',
        'keywords': ['american standard code for information interchange']
    },
    5: {
        'question': "How many bits are required to represent 8 unique values?",
        'options': {
            'a': "4",
            'b': "8",
            'c': "3",
            'd': "16"
        },
        'answer': 'c',
        'keywords': ['3']
    },
    6: {
        'question': "Largest decimal value representable using 8 bits?",
        'options': {
            'a': "128",
            'b': "255",
            'c': "512",
            'd': "64"
        },
        'answer': 'b',
        'keywords': ['255']
    },
    7: {
        'question': "The largest value here:",
        'options': {
            'a': "10000000",
            'b': "01010101",
            'c': "11111111",
            'd': "00110011"
        },
        'answer': 'c',
        'keywords': ['11111111']
    }, 
    8: {
        'question': "2B(hex) to decimal?",
        'options': {
            'a': "68",
            'b': "32",
            'c': "43",
            'd': "44"
        },
        'answer': 'c',
        'keywords': ['43']
    },
    9: {
        'question': "Decimal equivalent of binary number 100001 ?",
        'options': {
            'a': "16",
            'b': "26",
            'c': "12",
            'd': "33"
        },
        'answer': 'd',
        'keywords':["33"]
    },

    10: {
        'question': "Decimal value of binary number 11101?",
        'options': {
            'a': "13",
            'b': "15",
            'c': "37",
            'd': "29"
        },
        'answer': 'd',
        'keywords':["29"]
    },
    11: {
        "question": "What is the definition of data in relation to computing?",
        "options": {
            "a": "Information for movement",
            "b": "Binary numbers that do things",
            "c": "Facts and statistics",
            "d": "The output of a computer program"
        },
        "answer": "a",
        "keywords": ["encoding schemes", "digital communication", "binary data"]
    },
    12: {
        "question": "Describe digital compression:",
        "options": {
            "a": "Reducing data size.",
            "b": "Encrypting data for security.",
            "c": "Analog->digital info.",
            "d": "Ensuring integrity of data."
        },
        "answer": "a",
        "keywords": ["data compression", "digital systems", "size of data", "storage", "transmission"]
    },

    13: {
        "question": "What is the purpose of the XOR operation?",
        "options": {
            "a": "Performs an OR operation",
            "b": "To perform a AND operation",
            "c": "An exclusive OR operation",
            "d": "Performs a  NOT operation"
        },
        "answer": "c",
        "keywords": ["XOR operation", "digital logic", "bitwise"]
    },

    14: {
        "question": "Lossless compression works by eliminating some data.",
        "options": {
            "a": "True",
            "b": "False"
        },
        "answer": "b",
        "keywords": ["false"]
    },
    15: {
        "question": "What is the purpose of a cache in computer systems?",
        "options": {
            "a": "Stores temporary files",
            "b": "Performs arithmetic on data",
            "c": "Stores files in a drive",
            "d": "Stores files for deletion"
        },
        "answer": "a",
        "keywords": ["cache", "computer systems", "data storage", "faster retrieval"]
    },
    16: {
        "question": "Symmetric vs asymmetric encryption and decryption?",
        "options": {
            "a": "Single vs public/private key",
            "b": "One is asymmetrical",
            "c": "Same vs altered keys",
            "d": "Compresses data differently"
        },
        "answer": "a",
        "keywords": ["symmetric encryption", "asymmetric encryption", "encryption", "decryption", "keys"]
    },
    17: {
        "question": "What is the purpose of a digital signature?",
        "options": {
            "a": "To encrypt data",
            "b": "Confirms integrity of data",
            "c": "Analog signals into digital",
            "d": "Temporary storage"
        },
        "answer": "b",
        "keywords": ["digital signature", "authenticity", "integrity", "digital data"]
    },
    18: {
        "question": "What is the purpose of a digital certificate?",
        "options": {
            "a": "Validates sender of data",
            "b": "Checks data integrity",
            "c": "Analog signals to digital",
            "d": "An award "
        },
        "answer": "a",
        "keywords": ["digital certificate", "secure communication", "authenticity", "integrity", "secure connection"]
    }
}


decision_structure_questions_hard = {
    1: {
        "question": "What is the purpose of an 'if' statement?",
        "options": {
            "a": "Iteration over sequences",
            "b": "Check for conditions",
            "c": "Perform repetition",
            "d": "Store multiple variables"
        },
        "answer": "b",
        "keywords": ["if statement", "condition", "block of code"]
    },
    2: {
        "question": "What is the purpose of the 'elif' statement?",
        "options": {
            "a": "Conditions within 'if' ",
            "b": "Check for another condition",
            "c": "Perform repetition",
            "d": "Store multiple variables"
        },
        "answer": "b",
        "keywords": ["elif statement", "if statement", "multiple conditions"]
    },
    3: {
        "question": "Output of the following code snippet.", ##THE CODE SNIPPET IS THE IMAGE
        "options": {
            "a": "1st Print",
            "b": "2nd Print",
            "c": "3rd Print",
            "d": "valueError"
        },
        "answer": "c",
        "keywords": ["output", "code snippet", "if-elif-else", "condition"],
        "code": ["pretend I have code here this is just for checking Hi ms. Lal"],
        "name": "Images\Q3codesnippet.jpg"
    },
    4: {
        "question": "Choose the operator that doesn't exist",
        "options": {
            "a": "==",
            "b": "!=",
            "c": "<=",
            "d": "><"
        },
        "answer": "d",
        "keywords": ["comparison operator", "Python"]
    },
    5: {
        "question": "Check if a variable x is equal to 10?",
        "options": {
            "a": "x = 10",
            "b": "x == 10",
            "c": "x >= 10",
            "d": "x <= 10"
        },
        "answer": "b",
        "keywords": ["condition", "variable", "equal to"]
    },
    6: {
        "question": "Describe a 'pass' operator",
        "options": {
            "a": "Skip a loop iteration",
            "b": "Terminate a program",
            "c": "Check a condition",
            "d": "Act as a placeholder"
        },
        "answer": "d",
        "keywords": ["pass statement", "Python", "decision structure", "placeholder"]
    },
    7: {
        "question": "Check if a string s starts with a specific substring.",
        "options": {
            "a": "s == 'substring'",
            "b": "s in ('substring')",
            "c": "s[0]==('substring')",
            "d": "s.contains('substring')"
        },
        "answer": "c",
        "keywords": ["condition", "string", "starts with", "substring"]
    },
    8: {
        "question": "What is the purpose of a ternary operator in Python?",
        "options": {
            "a": "Concatenates two strings",
            "b": "Performs operations",
            "c": "Condition-based assigning",
            "d": "Converts decimal to binary"
        },
        "answer": "c",
        "keywords": ["ternary operator", "Python", "assign", "value", "condition"]
    },
    9: {
        "question": "How do you check if a list contains a specific element?",
        "options": {
            "a": "element in list",
            "b": "list in element",
            "c": "element.contains(list)",
            "d": "list.contains(element)"
        },
        "answer": "a",
        "keywords": ["condition", "list", "contains", "specific element"]
    },
    10: {
        "question": "Purpose of the 'not' operator.",
        "options": {
            "a": "To negate a Boolean value",
            "b": "To combine multiple conditions",
            "c": "To compare two variables",
            "d": "To assign a value to a variable"
        },
        "answer": "a",
        "keywords": ["not operator", "Python", "Boolean value", "negate"]
    },
    11: {
        "question": "Describe an OR operator.",
        "options": {
            "a": "Both conditions are true",
            "b": "Either condition is true",
            "c": "No conditions are true",
            "d": "One true, One false"
        },
        "answer": "b",
        "keywords": ["or operator", "Python", "decision structure", "conditions"]
    },
    12: {
        "question": "Describe an and operator",
        "options": {
            "a": "Both conditions are true",
            "b": "Either condition is true",
            "c": "No conditions are true",
            "d": "One true, One false"
        },
        "answer": "a",
        "keywords": ["and operator", "Python", "decision structure", "conditions"]
    },
  
    13: {
        "question": "What does a nested if statement do",
        "options": {
            "a": "Conditions within 'if' ",
            "b": "Check for another condition",
            "c": "Perform repetition",
            "d": "Store multiple variables"
        },
        "answer": "a",
        "keywords": ["nested if statement", "Python", "multiple conditions"]
    },
    14: {
        "question": "Write code to check if x is positive and print x ",
        "answer": "if x>0: print(x) ",
        "keywords": ["if x>0:","if (x>0):","if x> 0:","if x >0:", "print(x)","repetition"],
        "keywordThreshold": 2,
        "instantWrongs": ["x<1","x>1","<","print('x')"]
    },
    15: {
        "question": "What is the difference between else and elif?",
        "options": {
            "a": "Else is nested",
            "b": "Else has no condition",
            "c": "Else performs repetition",
            "d": "All of the above"
        },
        "answer": "b",
        "keywords": ["else statement", "Python", "decision structure", "none of the conditions"]
    },
    16: {
        "question": "What does 'continue' do in a loop?",
        "options": {
            "a": "Handles conditions in a loop",
            "b": "Executes conditions in a loop",
            "c": "Skips a loop iteration",
            "d": "Placeholder for code"
        },
        "answer": "c",
        "keywords": ["switch statement", "programming", "different code blocks", "expression"]
    },
    17: {
        "question": "Which binary number represents 109?",
        "options": {
            "a": "01101101",
            "b": "11011010",
            "c": "01010101",
            "d": "10101010"
        },
        "answer": "a",
        "keywords": ["01101101"]
    },
    18: {
        "question": "Which binary number represents 122?",
        "options": {
            "a": "1111010",
            "b": "1101110",
            "c": "0100111",
            "d": "1010010"
        },
        "answer": "a",
        "keywords": ["1111010"]
    }
}



repetition_structure_questions_hard = {
    1: {
        "question": "'Describe a for loop in Python?",
        "options": {
            "a": "Executes code x times.",
            "b": "Indefinite code repetition",
            "c": "Checks for a condition(s)",
            "d": "Stores/retrieves data."
        },
        "answer": "a",
        "keywords": "none"
    },
    2: {
        "question": "Write a for loop going from 1 to 10(inclusive).",
        "answer": "for i in range(1, 11)",
        "keywords": ["for i in range(1,11)","for i in range(1, 11)","for i in range(1,12-1)","for i in range(0+1,11)"],
        "keywordThreshold": 1,
        "instantWrongs": ["while"],
        "short answer": "help me god"
    },
    3: {
        "question": "A while loop counting 10->1, printing each time. Use x. ",
        "answer": "x = 10;while x>=1:;print(x);x-=1",
        "keywordThreshold": 3,
        "keywords": ["x=10","x = 10","x= 10","x =10","while x >= 1", "while x=>1","while x=> 1", "while x =>1","print(x)","x-=1","x -=1", "x-= 1"],
        "instantWrongs": ["for","11","12","9","<=","=>","+="]
    },
    4: {
        "question": "Loop structure to use when the number of iterations is unknown.",
        "options": {
            "a": "'for' loop",
            "b": "'while' loop",
            "c": "'do-while' loop",
            "d": "'if' statement"
        },
        "answer": "b",
        "keywords": "none"
    },
    5: {
        "question": "Describe a break statement.",
        "answer": ["A break statement terminates the loop entirely", "A break statement stops the loop."],
        "keywords": ["break statement","terminates the loop","terminates loop","stops loop","breaks loop","stop the loop","A break"],
        "keywordThreshold": 2,
        "instantWrongs": ["asdfghjkjhgfdsadfghjk"]
    },
    6: {
        "question": "Prints even numbers from 2 to 10, use 'for','i'.",
        "answer": "for i in range(2, 11, 2) | print(i)",
        "keywords": ["for i in range(2,11,2)","for i in range(2, 11,2)","for i in range(2,11, 2)", "for i in range(2, 11, 2)","print(i)"],
        "keywordThreshold": 2,
        "instantWrongs": ["xcfvghjjhgfdfghj"]
    },
    7: {
        "question": "A loop must always execute at least once",
        "options": {
            "a": "true",
            "b": "false",
        },
        "answer": "b",
        "keywords": "false"
    },
    8: {
        "question": "Describe an infinite loop in Python.",
        "answer": "An infinite loop in Python is a loop that keeps executing without ever terminating.",
        "keywords": ["infinite loop", "break out", "condition", "'break' statement", "exit","never stops","never stop","always runs","forever","forever running"],
        "keywordThreshold": 2,
        "instantWrongs": ["jijijijijijij"]
    },
    9: {
        "question": "Why are loops useful?",
        "answer": "To execute the same piece of code over and over.",
        "keywords": ["execute","same piece","reduce code","save time","Don't have to","repetition"],
        "keywordThreshold": 2,
        "instantWrongs": ["saodjad"]

    },
    10: {
        "question": "Which loop structure in Python is suitable for iterating over elements of an array?",
        "options": {
            "a": "'for' loop",
            "b": "'while' loop",
            "c": "'do-while' loop",
            "d": "'if' statement"
        },
        "answer": "a",
        "keywords": "none",
    },
    11: {
        "question": "What is the output of the following Python code snippet?",
        "options": {
            "a": "2, 4",
            "b": "1, 2, 3, 4, 5",
            "c": "1,3,5",
            "d": "12345"
        },
        "answer": "a",
        "code": "yas",
        "keywords": "none",
        "name": "Images\Q11Codesnippet.jpg"
    },
    12: {
        "question": "What is the output of the following Python code snippet?",
        "options": {
            "a": "1 2 3 4",
            "b": "1 2 3 4 5",
            "c": "12345",
            "d": "1 3 5"
        },
        "answer": "a",
        "code": "yas",
        "keywords": "none",
        "name": "Images\Q12Codesnippet.jpg"
    },
    13: {
        "question": "When do you use a while loop?",
        "options": {
            "a": "Don't know iteration numbers",
            "b": "Know iteration numbers.",
            "c": "Condition-based assignment",
            "d": "To store and retrieve data"
        },
        "answer": "a",
        "keywords": ["Python", "'for' loop", "purpose"]
    },
    14: {
        "question": "Write a 'for' loop in Python that prints the numbers from 2 to 5. Use i.",
        "answer": "for i in range(2,6): print(i)",
        "keywords": ["for","i in","range","(2, 6)","(2,6)","(2,5+1)","(2, 5 +1)","(2, 5+ 1)",":","print(i)"],
        "keywordThreshold": 5,
        "instantWrongs": ["while", "(1,5)","in (2,5)"]
    },
    15: {
        "question": "Write a 'while' loop counting from 2 to 5. Use x.",
        "answer": "x=2 while(x<=5): print(x) x+=1",
        "keywords": ["x=2", "x = 2","x= 2","x =2", "while(x<=5):","while(x <=5):","while(x<= 5):","print(x)","x+=1","x +=1", "x+= 1"],
        "keywordThreshold": 3,
        "instantWrongs": ["for"]
    },
    16: {
        "question": "Select proper syntax:",
        "options": {
            "a": "for i in range(0,10)",
            "b": "for i in len(10)",
            "c": "for i in range(0,10):",
            "d": "for i in 20:"
        },
        "answer": "c",
        "keywords": ["Python", "'for' loop", "purpose"]
    },
    17: {
        "question": "Write a 'for' loop in Python that prints the even numbers from 6 to 36. Use 'i'.",
        "answer": "for i in range(6,37,6): print(i)",
        "keywords": ["for","i in","range","(6, 37)","(6,37)","(6,36+1)","(6, 36+ 1)","(6, 36 +1)",":","print(i)"],
        "keywordThreshold": 5,
        "instantWrongs": ["while"]
    },
    18: {
        "question": "Which loop structure in Python is appropriate when you want to execute the loop body at least once?",
        "options": {
            "a": "'for' loop",
            "b": "'while' loop",
            "c": "'do-while' loop",
            "d": "'if' statement"
        },
        "answer": "c",
        "keywords": ["Python", "loop structure", "execute", "at least once"]
    }
}
