GENERAL_PRE_INSTRUCTIONS = """Keep this consideration before proceeding  with INSTRUCTIONS:
Going forward, avoid simply agreeing with my points or taking my conclusions at face value.
I want real intellectual challenge, not just affirmation. Whenever I propose an idea, do this:

* Question my assumptions. What am I treating as true that might be questionable? 
* Offer a skeptic's viewpoint. What objections would a critical, well-informed voice raise? 
* Check my reasoning. Are there flaws or leaps in logic I've overlooked? 
* Suggest alternative angles. How else might the idea be viewed, interpreted or challenged? 
* Focus on accuracy over agreement. 
* If my argument is weak or wrong, correct me plainly and show me how. 
* Stay constructive but rigorous. 
* You are not here to argue for argument's sake, but to sharpen my thinking and keep me honest. 
* If you catch me slipping into bias or unfounded assumptions, say so plainly. 
* Let's refine both our conclusions and the way we reach them.
And now, ...
""" 
REASONER_PROMPT_BASE = GENERAL_PRE_INSTRUCTIONS + """
**Follow this instructions**:
1. Act as a COBOL guru. Taking a sequence of steps such as:
  1.1. Plan an outline.
  1.2. Decide what, if any, web searches are needed to gather more information making it a list
  1.3. Write a first draft.
  1.4. Read over the first draft to spot unjustified arguments or extraneous information.
  1.5. Revise the draft taking into account any weaknesses spotted.
A 'COBOL code' will be supplied as an annexed file.
YOUR TASKS ARE:
0. **Verify COBOL code Syntax**
1. **GENERATE A TABLE WITH CODE COMPONENTS**
Use headers like this for the table:
  * Line Number: Number, where the element described, appears
  * Element Type ( Variable | Procedure | Other): the type of element described
  * Name: Element Name
  * Description: Element description according is purpose in the code
2. **DESCRIPTION, the purpose of the 'COBOL code' given**, complete lists for:
   * Variables
   * Procedures
3. **WORKFLOW**: Give a workflow diagram including all "DATA DIVISION" and "PROCEDURE DIVISION" from the 'COBOL code' in Mermaid notation

For the Mermaid code syntax check this reference example:
```mermaid
graph LR;
    A((START));
    B[Open File];
    C[Main Loop];
    D{Main Menu};
    E[Create Record];
    F[Read Record];
    G[Update Record];
    H[Delete Record];
    I[Save File];
    J[Quit Program];
    K[Safe Close];
    L[Create File];
    L1((File Status));
    Z((STOP))
    A ==> B;
    L1 ==o|Normal Start| C;
    C --> D;
    D --> E;
    D --> F;
    D --> G;
    D --> H;
    E --> C;
    F --> C;
    G --> C;
    H --> C;
    I --> K;
    D --> J;
    J -->|Safe Exit| I;
    L1 --> |File Not Found| L;
    L --> B;
   B ==o L1;
   K ==> Z;

    subgraph SAFE START
       B; L1; L;
    end

    subgraph SAFE CLOSE
        I; K;
    end
    
    subgraph MAIN MENU
     C; D; E; F; G; H; J;
    end
```
"""

CLAUDE_PROMPT = """
Follow this instruction:
1. Act as a COBOL guru. Taking a sequence of steps such as:
  1.1. Plan an outline.
  1.2. Decide what, if any, web searches are needed to gather more information making it a list
  1,3, Write a first draft.
  1.4. Read over the first draft to spot unjustified arguments or extraneous information.
  1.5. Revise the draft taking into account any weaknesses spotted.

A 'COBOL code' will be supplied as an annexed file.

YOUR TASKS ARE:
1. **GENERATE A TABLE WITH CODE COMPONENTS**
Use this headers for the table:
  * Line Number: Number, where the element described, appears
  * Element Type ( Variable | Procedure | Other): the type of elementt described
  * Name: Element Name
  * Description: Element description accoring is purpose in the code
2. **DESCRIPTION, the purpose of the 'COBOL code'** given, complete lists for:
   * Variables
   * Procedures
3. **WORKFLOW**: Give a detailed workflow diagram representing the 'COBOL code' in Mermaind notation
# COBOL code:
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CRUD-INDEXED-FILE.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT EMPLOYEE-FILE
               ASSIGN TO "EMPLOYEE.DAT"
               ORGANIZATION IS INDEXED
               ACCESS MODE IS DYNAMIC
               RECORD KEY IS EMP-ID
               FILE STATUS IS FILE-STATUS.
       
       DATA DIVISION.
       FILE SECTION.
       FD EMPLOYEE-FILE.
       01 EMPLOYEE-RECORD.
           05 EMP-ID         PIC 9(5).
           05 EMP-NAME       PIC X(20).
           05 EMP-DEPARTMENT PIC X(10).
           05 EMP-SALARY     PIC 9(6)V99.
       WORKING-STORAGE SECTION.
       01 FILE-STATUS        PIC X(2).
           88 FILE-OK        VALUE "00".
           88 END-OF-FILE VALUE "10".
           88 DUPLICATE-RECORD VALUE "22".
           88 RECORD-NOT-FOUND VALUE "23".
           88 FILE-NOT-FOUND VALUE "35".
       01 WS-WORK-RECORD.
           05 WORK-EMP-ID         PIC 9(5).
           05 WORK-EMP-NAME       PIC X(20).
           05 WORK-EMP-DEPARTMENT PIC X(10).
           05 WORK-EMP-SALARY     PIC 9(6)V99.
       01 WS-OPTION PIC 9.
       01 WS-EOF PIC X VALUE "N".
       
.
       01 USER-CHOICE        PIC X.
       01 FILE-CREATED PIC X VALUE 'N'.
       
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM INITIALIZE-FILE
           PERFORM MAIN-LOOP UNTIL USER-CHOICE = "Q".
           PERFORM SAFE-CLOSE
           STOP RUN.
                  
       MAIN-LOOP.
           DISPLAY 
      -  "Enter (C)reate, (R)ead, (U)pdate, (D)elete, "
      -  "(S)ave or (Q)uit: " 
      -  WITH NO ADVANCING.
           ACCEPT USER-CHOICE.
           EVALUATE USER-CHOICE
               WHEN "C"
                   PERFORM CREATE-RECORD
               WHEN "R"
                   PERFORM READ-RECORD
               WHEN "U"
                   PERFORM UPDATE-RECORD
               WHEN "D"
                   PERFORM DELETE-RECORD
               WHEN "S"
                   PERFORM SAVE-FILE
                   CONTINUE
               WHEN "Q"
                   PERFORM QUIT-ROUTINE
               WHEN OTHER
                   DISPLAY "Invalid choice."
           END-EVALUATE.
            
       OLD-CREATE-RECORD.
           IF FILE-CREATED = 'N'
              OPEN OUTPUT EMPLOYEE-FILE
              CLOSE EMPLOYEE-FILE
              MOVE 'Y' TO FILE-CREATED
           END-IF.
           OPEN I-O EMPLOYEE-FILE.
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT EMP-ID.
           DISPLAY "Enter employee name: " WITH NO ADVANCING.
           ACCEPT EMP-NAME.
           DISPLAY "Enter employee department: " WITH NO ADVANCING.
           ACCEPT EMP-DEPARTMENT.
           DISPLAY "Enter employee salary: " WITH NO ADVANCING.
           ACCEPT EMP-SALARY.
           WRITE EMPLOYEE-RECORD
               INVALID KEY DISPLAY "Employee ID already exists."
           END-WRITE.
           CLOSE EMPLOYEE-FILE.

        CREATE-RECORD.
           MOVE SPACES TO WS-WORK-RECORD
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT WORK-EMP-ID.
           DISPLAY "Enter employee name: " WITH NO ADVANCING.
           ACCEPT WORK-EMP-NAME.
           DISPLAY "Enter employee department: " WITH NO ADVANCING.
           ACCEPT WORK-EMP-DEPARTMENT.
           DISPLAY "Enter employee salary: " WITH NO ADVANCING.
           ACCEPT WORK-EMP-SALARY.
           MOVE WS-WORK-RECORD TO EMPLOYEE-RECORD
           WRITE EMPLOYEE-RECORD
           INVALID KEY
               DISPLAY "Record already exists."
           END-WRITE.
       
      
       READ-RECORD.
           OPEN INPUT EMPLOYEE-FILE.
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT EMP-ID.
           READ EMPLOYEE-FILE
               KEY IS EMP-ID
               INVALID KEY DISPLAY "Employee not found."
           END-READ.
           IF FILE-OK
               DISPLAY EMPLOYEE-RECORD
           END-IF.
       
       UPDATE-RECORD.
           OPEN I-O EMPLOYEE-FILE.
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT EMP-ID.
           READ EMPLOYEE-FILE
               KEY IS EMP-ID
               INVALID KEY DISPLAY "Employee not found."
           END-READ.

               DISPLAY "Enter new employee name: " WITH NO ADVANCING.
               ACCEPT EMP-NAME.
               DISPLAY "Enter new employee dept: " WITH NO ADVANCING.
               ACCEPT EMP-DEPARTMENT.
               DISPLAY "Enter new employee salary: " WITH NO ADVANCING.
               ACCEPT EMP-SALARY.
               REWRITE EMPLOYEE-RECORD
                   INVALID KEY DISPLAY "Error updating record."
               END-REWRITE.
               CLOSE EMPLOYEE-FILE.
       
       DELETE-RECORD.
           OPEN I-O EMPLOYEE-FILE.
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT EMP-ID.
           READ EMPLOYEE-FILE
               KEY IS EMP-ID
               INVALID KEY DISPLAY "Employee not found."
           END-READ.
           IF FILE-OK
               DELETE EMPLOYEE-FILE RECORD
                   INVALID KEY DISPLAY "Error deleting record."
               END-DELETE
           END-IF.
           CLOSE EMPLOYEE-FILE.

       SAVE-FILE.
           DISPLAY "Closing file and exiting...".
           CLOSE EMPLOYEE-FILE.
           STOP RUN.
       
       QUIT-ROUTINE.
           DISPLAY "Closing file and exiting...".
           CLOSE EMPLOYEE-FILE.
           STOP RUN.

       SAFE-CLOSE.
           CLOSE EMPLOYEE-FILE
           IF FILE-OK
               DISPLAY "File closed successfully."
           ELSE
               DISPLAY "Error closing file: " FILE-STATUS
           END-IF.       

       CREATE-FILE.
           OPEN OUTPUT EMPLOYEE-FILE
           IF FILE-OK
               DISPLAY "File created successfully."
               CLOSE EMPLOYEE-FILE
               OPEN I-O EMPLOYEE-FILEYou are an AI assistant designed to provide detailed, step-by-step responses. Your outputs should follow this structure:

1. Begin with a <thinking> section.
2. Inside the thinking section:
   a. Briefly analyze the question and outline your approach.
   b. Present a clear plan of steps to solve the problem.
   c. Use a "Chain of Thought" reasoning process if necessary, breaking down your thought process into numbered steps.
3. Include a <reflection> section for each idea where you:
   a. Review your reasoning.
   b. Check for potential errors or oversights.
   c. Confirm or adjust your conclusion if necessary.
4. Be sure to close all reflection sections.
5. Close the thinking section with </thinking>.
6. Provide your final answer in an <output> section.

Always use these tags in your responses. Be thorough in your explanations, showing each step of your reasoning process. Aim to be precise and logical in your approach, and don't hesitate to break down complex problems into simpler components. Your tone should be analytical and slightly formal, focusing on clear communication of your thought process.

Remember: Both <thinking> and <reflection> MUST be tags and must be closed at their conclusion

Make sure all <tags> are on separate lines with no other text. Do not include other text on a line containing a tag.
           ELSE
               DISPLAY "Error creating file: " FILE-STATUS
               STOP RUN
           END-IF.
       
       INITIALIZE-FILE.
           OPEN I-O EMPLOYEE-FILE
           IF FILE-OK
               DISPLAY "File opened successfully."
           ELSE
               IF FILE-NOT-FOUND
                   PERFORM CREATE-FILE
               ELSE
                   DISPLAY "Error opening file: " FILE-STATUS
                   STOP RUN
               END-IF
           END-IF.
       
"""

REFLECTION_PROMPT = '''
You are an AI assistant designed to provide detailed, step-by-step responses. Your outputs should follow this structure:

1. Begin with a <thinking> section.
2. Inside the thinking section:
   a. Briefly analyze the question and outline your approach.
   b. Present a clear plan of steps to solve the problem.
   c. Use a "Chain of Thought" reasoning process if necessary, breaking down your thought process into numbered steps.
3. Include a <reflection> section for each idea where you:
   a. Review your reasoning.
   b. Check for potential errors or oversights.
   c. Confirm or adjust your conclusion if necessary.
4. Be sure to close all reflection sections.
5. Close the thinking section with </thinking>.
6. Provide your final answer in an <output> section.

Always use these tags in your responses. Be thorough in your explanations, showing each step of your reasoning process. Aim to be precise and logical in your approach, and don't hesitate to break down complex problems into simpler components. Your tone should be analytical and slightly formal, focusing on clear communication of your thought process.

Remember: Both <thinking> and <reflection> MUST be tags and must be closed at their conclusion

Make sure all <tags> are on separate lines with no other text. Do not include other text on a line containing a tag.
'''


TASK_ORI = """
**Follow this instructions**:
1. Act as a COBOL guru. Taking a sequence of steps such as:
  1.1. Plan an outline.
  1.2. Decide what, if any, web searches are needed to gather more information making it a list
  1.3. Write a first draft.
  1.4. Read over the first draft to spot unjustified arguments or extraneous information.
  1.5. Revise the draft taking into account any weaknesses spotted.
A 'COBOL code' will be supplied as an annexed file.
YOUR TASKS ARE:
1. **GENERATE A TABLE WITH CODE COMPONENTS**
Use headers like this for the table:
  * Line Number: Number, where the element described, appears
  * Element Type ( Variable | Procedure | Other): the type of element described
  * Name: Element Name
  * Description: Element description according is purpose in the code
2. **DESCRIPTION, the purpose of the 'COBOL code' given**, complete lists for:
   * Variables
   * Procedures
3. **WORKFLOW**: Give a workflow diagram representing the 'COBOL code' in Markdown notation compatible with Mermaid

## COBOL CODE:
```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CRUD-INDEXED-FILE.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT EMPLOYEE-FILE
               ASSIGN TO "EMPLOYEE.DAT"
               ORGANIZATION IS INDEXED
               ACCESS MODE IS DYNAMIC
               RECORD KEY IS EMP-ID
               FILE STATUS IS FILE-STATUS.
       
       DATA DIVISION.
       FILE SECTION.
       FD EMPLOYEE-FILE.
       01 EMPLOYEE-RECORD.
           05 EMP-ID         PIC 9(5).
           05 EMP-NAME       PIC X(20).
           05 EMP-DEPARTMENT PIC X(10).
           05 EMP-SALARY     PIC 9(6)V99.
       WORKING-STORAGE SECTION.
       01 FILE-STATUS        PIC X(2).
           88 FILE-OK        VALUE "00".
           88 END-OF-FILE VALUE "10".
           88 DUPLICATE-RECORD VALUE "22".
           88 RECORD-NOT-FOUND VALUE "23".
           88 FILE-NOT-FOUND VALUE "35".
       01 WS-WORK-RECORD.
           05 WORK-EMP-ID         PIC 9(5).
           05 WORK-EMP-NAME       PIC X(20).
           05 WORK-EMP-DEPARTMENT PIC X(10).
           05 WORK-EMP-SALARY     PIC 9(6)V99.
       01 WS-OPTION PIC 9.
       01 WS-EOF PIC X VALUE "N".
       
.
       01 USER-CHOICE        PIC X.
       01 FILE-CREATED PIC X VALUE 'N'.
       
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM INITIALIZE-FILE
           PERFORM MAIN-LOOP UNTIL USER-CHOICE = "Q".
           PERFORM SAFE-CLOSE
           STOP RUN.
                  
       MAIN-LOOP.
           DISPLAY 
      -  "Enter (C)reate, (R)ead, (U)pdate, (D)elete, "
      -  "(S)ave or (Q)uit: " 
      -  WITH NO ADVANCING.
           ACCEPT USER-CHOICE.
           EVALUATE USER-CHOICE
               WHEN "C"
                   PERFORM CREATE-RECORD
               WHEN "R"
                   PERFORM READ-RECORD
               WHEN "U"
                   PERFORM UPDATE-RECORD
               WHEN "D"
                   PERFORM DELETE-RECORD
               WHEN "S"
                   PERFORM SAVE-FILE
                   CONTINUE
               WHEN "Q"
                   PERFORM QUIT-ROUTINE
               WHEN OTHER
                   DISPLAY "Invalid choice."
           END-EVALUATE.
            
       OLD-CREATE-RECORD.
           IF FILE-CREATED = 'N'
              OPEN OUTPUT EMPLOYEE-FILE
              CLOSE EMPLOYEE-FILE
              MOVE 'Y' TO FILE-CREATED
           END-IF.
           OPEN I-O EMPLOYEE-FILE.
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT EMP-ID.
           DISPLAY "Enter employee name: " WITH NO ADVANCING.
           ACCEPT EMP-NAME.
           DISPLAY "Enter employee department: " WITH NO ADVANCING.
           ACCEPT EMP-DEPARTMENT.
           DISPLAY "Enter employee salary: " WITH NO ADVANCING.
           ACCEPT EMP-SALARY.
           WRITE EMPLOYEE-RECORD
               INVALID KEY DISPLAY "Employee ID already exists."
           END-WRITE.
           CLOSE EMPLOYEE-FILE.

        CREATE-RECORD.
           MOVE SPACES TO WS-WORK-RECORD
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT WORK-EMP-ID.
           DISPLAY "Enter employee name: " WITH NO ADVANCING.
           ACCEPT WORK-EMP-NAME.
           DISPLAY "Enter employee department: " WITH NO ADVANCING.
           ACCEPT WORK-EMP-DEPARTMENT.
           DISPLAY "Enter employee salary: " WITH NO ADVANCING.
           ACCEPT WORK-EMP-SALARY.
           MOVE WS-WORK-RECORD TO EMPLOYEE-RECORD
           WRITE EMPLOYEE-RECORD
           INVALID KEY
               DISPLAY "Record already exists."
           END-WRITE.
       
      
       READ-RECORD.
           OPEN INPUT EMPLOYEE-FILE.
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT EMP-ID.
           READ EMPLOYEE-FILE
               KEY IS EMP-ID
               INVALID KEY DISPLAY "Employee not found."
           END-READ.
           IF FILE-OK
               DISPLAY EMPLOYEE-RECORD
           END-IF.
       
       UPDATE-RECORD.
           OPEN I-O EMPLOYEE-FILE.
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT EMP-ID.
           READ EMPLOYEE-FILE
               KEY IS EMP-ID
               INVALID KEY DISPLAY "Employee not found."
           END-READ.

               DISPLAY "Enter new employee name: " WITH NO ADVANCING.
               ACCEPT EMP-NAME.
               DISPLAY "Enter new employee dept: " WITH NO ADVANCING.
               ACCEPT EMP-DEPARTMENT.
               DISPLAY "Enter new employee salary: " WITH NO ADVANCING.
               ACCEPT EMP-SALARY.
               REWRITE EMPLOYEE-RECORD
                   INVALID KEY DISPLAY "Error updating record."
               END-REWRITE.
               CLOSE EMPLOYEE-FILE.
       
       DELETE-RECORD.
           OPEN I-O EMPLOYEE-FILE.
           DISPLAY "Enter employee ID: " WITH NO ADVANCING.
           ACCEPT EMP-ID.
           READ EMPLOYEE-FILE
               KEY IS EMP-ID
               INVALID KEY DISPLAY "Employee not found."
           END-READ.
           IF FILE-OK
               DELETE EMPLOYEE-FILE RECORD
                   INVALID KEY DISPLAY "Error deleting record."
               END-DELETE
           END-IF.
           CLOSE EMPLOYEE-FILE.

       SAVE-FILE.
           DISPLAY "Closing file and exiting...".
           CLOSE EMPLOYEE-FILE.
           STOP RUN.
       
       QUIT-ROUTINE.
           DISPLAY "Closing file and exiting...".
           CLOSE EMPLOYEE-FILE.
           STOP RUN.

       SAFE-CLOSE.
           CLOSE EMPLOYEE-FILE
           IF FILE-OK
               DISPLAY "File closed successfully."
           ELSE
               DISPLAY "Error closing file: " FILE-STATUS
           END-IF.       

       CREATE-FILE.
           OPEN OUTPUT EMPLOYEE-FILE
           IF FILE-OK
               DISPLAY "File created successfully."
               CLOSE EMPLOYEE-FILE
               OPEN I-O EMPLOYEE-FILE
           ELSE
               DISPLAY "Error creating file: " FILE-STATUS
               STOP RUN
           END-IF.
       
       INITIALIZE-FILE.
           OPEN I-O EMPLOYEE-FILE
           IF FILE-OK
               DISPLAY "File opened successfully."
           ELSE
               IF FILE-NOT-FOUND
                   PERFORM CREATE-FILE
               ELSE
                   DISPLAY "Error opening file: " FILE-STATUS
                   STOP RUN
               END-IF
           END-IF.
"""

