# st_scan_fs_000_app_PROMPT
Generate app code to do this:
* Set the  page to Wide
* Prepare a session states initializing with this values if not present:
  * STAT_SCAN_DIR = "/home1/hugo/PycharmProjects/okrocket/cobol/code/aws-mainframe-modernization-carddemo"
  * STAT_HIDE_N = False
  * STAT_HIDE_TYPE = False
  * STAT_HIDE_PARENT = False
  * STAT_HIDE_HIDDEN = True
  * STAT_HIDE_NAME = False
  * STAT_HIDE_EXTENSION = False
  * STAT_HIDE_PATH = False
  * STAT_HIDE_SIZE = False
  * STAT_MULT_SELECT_TYPE = ["Any",]
  * STAT_MULT_EXTENSION = ["Any"]

* Under an st.expander "SESSION_STATE" on the sidebar, display a table with every sessionstate name and its value
* Create a Separate A submit button "SCAN" SUBMIT BUTTON
When SCAN is pressed do:
* Recursively Scan the tree structure from the starting directory and store the result in a dictionary JSON structure with this info:
   * "ID": Node sequential counter
   * "TYPE": File / Dir
   * "PARENT": Parent Node "ID"
   * "HID": Hidden status
   * "NAME": Complete node name
   * "EXTENSION": File extension according with name suffix after "."
   * "PATH": Full path
   * "SIZE": Size for TYPE = File
* Create a list of unique "EXTENSION" and a counter for each filextension found
* Save "Any"+ "EXTENSION" Unique list in STAT_MULT_EXTENSION

* In the sidebar create a form with id = "TABLE_FILTER" With these widgets:
The initial value of the widgets will be of corresponding session states
  * HIDE_N CHECKBOX
  * HIDE_TYPE CHECKBOX
  * HIDE_PARENT CHECKBOX
  * HIDE_HIDDEN CHECKBOX
  * HIDE_NAME CHECKBOX
  * HIDE_EXTENSION CHECKBOX
  * HIDE_PATH CHECKBOX
  * HIDE_SIZE CHECKBOX
  * SCAN_DIR TEXTINPUT
  * MULT_SELECT_TYPE MULTISELECT
  * MULT_EXTENSION MULTISELECT
  * A "SHOW TABLE" SUBMIT BUTTON
When any change is done on any widget of this "TABLE FILTER", update the corresponding session state
* Make MULT_SELECT_TYPE MULTISELECT list as "Any"+ "EXTENSION" Unique list
Display the STAT_MULT_EXTENSION updated list

* When "SHOW TABLE" Button presed
Create and display a table from the results with this headers applying the filters
   * "N": sequential counter
   * "TYPE": File / Dir / Link (ln)
   * "PARENT": Parent dir
   * "HID": Hidden status
   * "NAME": Complete node name
   * "FILETYPE": File type according with name suffix after "."
   * "PATH": Full path
   * "SIZE": Size for TYPE = File
  Each column has "Hide/Show" option defaulting to show
  Additionally some columns have filters for each as:
  * "TYPE": File / Dir / Any
  * "FILETYPE": Multiple selection from Unique Filetype List
* A "SUMMARY" with 
  * "TOTAL NODES": Todal nodes scanned
  * "TOTAL DIRS"
  * "TOTAL HIDDEN DIRS"
  * "TOTAL LINKED DIRS"
  * "TOTAL FILES"
  * "TOTAL HIDDEN FILES"
  * "TOTAL LINKED FILES"
  * "TOTAL LINKS"

Besides generating the code, do CODE_EXPLANATION as:
A table with a row for each line of code genereated, with following headers:
"N" The line number
"IND": Indentation level (being 0 the first level)
"ST": 1 for Streamlit specific /operator/content,
"TYPE": A generic type of code (i.e. import, loop, variable (definition), function (definition), logical, arithmetic, string
"CODE": The whole corresponding code
A Table with the summary of the names used in the code, with this headers
"NAME". Variable, Function name
"USED" a list of the line numbers where NAME is used
"CODE": The code snippet corresponding to the function
A Table with the summary of the functions used in the code, with this headers
"NAME". Function name
"USED" a list of the line numbers where NAME is used
A list of the required packages, in the format appropiate for install using pip -r requirements.txt commands
A general description of the purpose of the code
