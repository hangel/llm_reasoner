### >>> COBOL code for CRUD over indexed file with a control menu

Here is an example of COBOL code for a simple CRUD application using an indexed file and a control menu:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. main.
DATA DIVISION.
WORKING-STORAGE SECTION.
01  input-line PIC X(80).
01  i-index PIC 9(4) VALUE 1.
01  file-status PIC 9(2) VALUE 0.
01  num-records PIC 9(4) VALUE 0.
01  record-id PIC 9(4).
01  file-name PIC X(8).
01  control-menu-choice PIC X(80).

PROCEDURE DIVISION.
MAIN.
    ACCEPT input-line TIMEOUT(5)
    DISPLAY "MAIN MENU"
    DISPLAY "1. Add new record"
    DISPLAY "2. Update existing record"
    DISPLAY "3. Delete existing record"
    DISPLAY "4. Show all records"
    ACCEPT control-menu-choice TIMEOUT(5)
    EVALUATE TRUE
        WHEN control-menu-choice = "1"
            CALL "add_record" USING i-index, input-line
        WHEN control-menu-choice = "2"
            CALL "update_record" USING i-index, input-line
        WHEN control-menu-choice = "3"
            CALL "delete_record" USING i-index
        WHEN control-menu-choice = "4"
            CALL "show_records" USING num-records
    END-EVALUATE
    GO TO MAIN.
```
This code uses the COBOL `ACCEPT` statement to accept input from the user with a 5 second timeout, and the `DISPLAY` statement to display a menu of options for the 
user to choose from. The user's choice is then evaluated using an `EVALUATE` statement, which calls specific subroutines based on the user's selection.

##### Here are some sample subroutines that could be called based on the user's input:
```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. add_record.
DATA DIVISION.
WORKING-STORAGE SECTION.
01  record PIC X(80).
01  i-index PIC 9(4) VALUE 1.

PROCEDURE DIVISION.
ADD_RECORD.
    DISPLAY "Enter the new record: " WITH NO ADVANCING
    ACCEPT input-line TIMEOUT(5)
    MOVE input-line TO record
    WRITE record FROM i-index END-WRITE
    GO TO MAIN.
```
* This subroutine uses the `MOVE` statement to move the user's input to a variable called `record`, and then writes the record to an indexed file using the `WRITE` statement with the `FROM` clause. The `i-index` variable is used to keep track of the current index number for the record being written.

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. update_record.
DATA DIVISION.
WORKING-STORAGE SECTION.
01  i-index PIC 9(4) VALUE 1.
01  record PIC X(80).

PROCEDURE DIVISION.
UPDATE_RECORD.
    DISPLAY "Enter the record to update: " WITH NO ADVANCING
    ACCEPT input-line TIMEOUT(5)
    MOVE input-line TO record
    READ record FROM i-index END-READ
    IF file-status = 1 THEN
        DISPLAY "Record does not exist"
        GO TO MAIN
    END-IF
    DISPLAY "Enter the new value: " WITH NO ADVANCING
    ACCEPT input-line TIMEOUT(5)
    MOVE input-line TO record
    WRITE record FROM i-index END-WRITE
    GO TO MAIN.
```

* This subroutine uses the `READ` statement to read a record from an indexed file using the `FROM` clause, and then uses the `MOVE` statement to move the user's input to a variable called `record`. The `IF` statement is used to check if the record exists in the file, and if it does not, the program displays a message and goes back to the main menu. If the record exists, the user's input is moved to the `record` variable again, and then the `WRITE` statement with the `FROM` clause is used to update the record in the indexed file.

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. delete_record.
DATA DIVISION.
WORKING-STORAGE SECTION.
01  i-index PIC 9(4) VALUE 1.
01  record PIC X(80).

PROCEDURE DIVISION.
DELETE_RECORD.
    DISPLAY "Enter the record to delete: " WITH NO ADVANCING
    ACCEPT input-line TIMEOUT(5)
    MOVE input-line TO record
    READ record FROM i-index END-READ
    IF file-status = 1 THEN
        DISPLAY "Record does not exist"
        GO TO MAIN
    END-IF
    DELETE record FROM i-index END-DELETE
    GO TO MAIN.
```
* This subroutine uses the `READ` statement to read a record from an indexed file using the `FROM` clause, and then uses the `MOVE` statement to move the user's input to a variable called `record`. The `IF` statement is used to check if the record exists in the file, and if it does not, the program displays a message and goes back to the main menu. If the record exists, the `DELETE` statement with the `FROM` clause is used to delete the record from the indexed file.

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. show_records.
DATA DIVISION.
WORKING-STORAGE SECTION.
01  i-index PIC 9(4) VALUE 1.
01  record PIC X(80).
01  file-name PIC X(8).

PROCEDURE DIVISION.
SHOW_RECORDS.
    MOVE "myfile" TO file-name
    OPEN INPUT file-name.
    DISPLAY "Records in myfile:" WITH NO ADVANCING
    PERFORM UNTIL i-index > num-records
        READ record FROM i-index END-READ
        IF file-status = 1 THEN
            GO TO MAIN
        ELSE
            DISPLAY "Record: " WITH NO ADVANCING
            DISPLAY record
            ADD 1 TO i-index
        END-IF
    END-PERFORM
    CLOSE file-name.
    GO TO MAIN.
```

* This subroutine uses the `MOVE` statement to move a file name to a variable called `file-name`, and then opens an input file using the `OPEN` statement with the `INPUT` clause. The `DISPLAY` statement is used to display a message indicating that the records are being displayed, and the `PERFORM` statement is used to read each record from the indexed file in turn. The `IF` statement is used to check if the record exists in the file, and if it does not, the program goes back to the main menu. 
* If the record exists, the `DISPLAY` statement is used to display the record, and the `ADD` statement is used to increment the index number for the next record. The file is closed using the `CLOSE` statement.
* These are just examples of how you could structure your COBOL program to perform CRUD operations on an indexed file with a control menu. You can customize these 
examples to fit your specific needs and requirements.

