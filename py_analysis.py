MD_APP = '''
###### **`app.py`- analysis of Python code

##### **Functions and Descriptions**

(These functions are imported from **`self_discover.py`)

* **`select_reasoning_modules(reasoning_modules, task)`**: Prompts for selecting relevant reasoning modules for a given task.
* **`adapt_reasoning_modules(selected_modules, task)`**: Prompts for adapting selected reasoning modules to a specific task.
* **`implement_reasoning_structure(adapted_modules, task)`**: Prompts for creating an actionable reasoning structure using adapted modules.
* **`execute_reasoning_structure(reasoning_structure, task)`**: Prompts for solving a task using the provided reasoning structure.

##### **Parameters and Purpose**

* **`API_KEY (str)`**: Groq API key used for authentication.
* **`system_prompt (str)`**: User input for the system's opening statement in the conversation.
* **`user_prompt (str)`**: User input for the prompt or question directed at the chatbot.
* **`model_list (list)`**: List of available Groq LLM model IDs.
* **`model (str)`**: User selection of the LLM model to be used for text generation.
* **`stream (streamlit.elements.StreamlitElement)`**: Streamlit element used to display the generated text incrementally.
* **`time_taken (streamlit.elements.StreamlitElement)`**: Streamlit element used to show the time taken for text generation.
* **`response (streamlit.elements.StreamlitElement)`**: Streamlit element used to display the final generated response.

##### **Overall Functionality**

This code implements a Streamlit web application for text generation using Groq LLMs. It offers two functionalities through tabs:

1. **Text Generation**: Users can provide a system prompt (opening statement) and a user prompt (question or request) for the chatbot. They can then select the desired Groq LLM model from a list. Clicking the "Generate" button triggers the process, which:
    * Retrieves the user prompts.
    * Establishes a streaming connection to the Groq chat completion API.
    * Sends the system and user prompts to the API for text generation.
    * Incrementally displays the generated text in a streamlit element (`stream`).
    * Measures the time taken for generation and displays it afterwards (`time_taken`).
    * Once complete, displays the final generated response (`response`).

2. **Self-Discover** (**Not implemented in this code snippet**): This section likely utilizes the imported functions from **`self_discover.py`** to guide users through a structured problem-solving approach. However, the provided code only shows the imports and no implementation for this tab.

**Note:** The code retrieves the Groq API key from environment variables or Streamlit secrets. It includes error handling for cases where the API key is not found.

'''

MD_SEARCH = '''
###### **`self_discover.py`- analysis of Python code

##### **Functions and Descriptions**

* **`select_reasoning_modules(reasoning_modules, task)`**:
      - Takes a list of reasoning modules and a task description as input.
      - Presents the task and prompts for the three most relevant reasoning modules from the list.
      - Returns a formatted string containing the task and a request for module numbers and descriptions.
* **`adapt_reasoning_modules(selected_modules, task)`**:
      - Takes the selected reasoning modules and the task description as input.  
      - Prompts for adapting those modules to be more specific to the task.
      - Returns a formatted string containing the task, selected modules, and a request for adaptation.
* **`implement_reasoning_structure(adapted_modules, task)`**:
      - Takes the adapted reasoning modules and the task description as input.
      - Prompts for creating an actionable reasoning structure using those modules.
      - Returns a formatted string containing the task, adapted modules, and a request for structure implementation.
* **`execute_reasoning_structure(reasoning_structure, task)`**:
      - Takes a reasoning structure and a task description as input.
      - Prompts for solving the task using the provided structure.
      - Returns a formatted string containing the task, reasoning structure, and a request for the final answer.

##### **Parameters and Purpose**

* **`reasoning_modules (list)`**: A list of strings representing different reasoning approaches or strategies.
* **`task (str)`**: A string containing a description of the task to be solved.
* **`selected_modules (str)`**: A string containing the numbers and descriptions of the selected reasoning modules (from Step 1).
* **`adapted_modules (str)`**: A string containing the adapted versions of the selected reasoning modules (from Step 2).
* **`reasoning_structure (str)`**: A string representing the actionable reasoning structure to be used for solving the task (from Step 3).

##### **Overall Functionality**

This code defines a framework for solving problems using a structured approach involving four steps:

1. **Select relevant reasoning modules** based on the task.
2. **Adapt** those modules to be more specific to the task.
3. **Implement** them into an actionable reasoning structure.
4. **Execute** the reasoning structure to generate a solution.

The functions in the code provide prompts for each step, but they don't directly perform the reasoning or problem-solving themselves. They are designed to guide a user or another system through the process.

'''

MD_AGENT = '''
###### **`app_agent.py`- analysis of Python code

##### **Functions and Descriptions**

* **`execute_search_agent(query)`**: This function takes a search query as input. It performs the following tasks:
    * Defines a Groq language model (LLM).
    * Sets up a web search tool.
    * Retrieves a prompt from LangChain Hub.
    * Constructs a ReAct agent combining these elements.
    * Executes the agent with the provided query and returns the results.
* **`check_text(text)`**: This function checks if the provided text is flagged as inappropriate using OpenAI's moderation API. It returns **`True`** if flagged, **`False`** otherwise.
* **`is_fake_question(text)`** (Commented out): This function (currently disabled) uses OpenAI's chat completion API to classify whether the text is an actual question. It returns **`0`** if a question, **`1`** otherwise.
* **`append_to_sheet(prompt, generated, answer)`**: This function adds a new row to a private Google Sheet. It takes the prompt, generated response (from the search agent), and answer as input and logs them along with the current timestamp.

##### **Parameters and Purpose**

* **`query (str)`**: The search query entered by the user.
* **`text (str)`**: Text used for safety checks.
* **`prompt (str)`**: Prompt used for the LangChain agent.
* **`generated (str)`**: Response generated by the search agent.
* **`answer (str)`**: Answer extracted from the search results.
* **`is_nsfw (bool)`**: Flag indicating if the query is flagged as inappropriate.

##### **Overall Functionality**

This code implements a Streamlit web application for search queries. Here's a breakdown of its functionality:

1. **User Input**: Users can enter their search query in the text input field labeled "Search Query".
2. **Safety Check**: The application checks the query for inappropriate content using OpenAI's moderation API.
    * If flagged (`is_nsfw`** is **`True`), the user is warned, and the process stops.
3. **Search Execution**: If the query is safe, the **`execute_search_agent`** function is called with the user's query. This function utilizes a Groq LLM, web search tools, and a LangChain prompt to retrieve search results.
4. **Displaying Results**: The application displays the retrieved answer and the time taken to complete the search.
5. **Logging**: The prompt, generated response, and answer are logged to a private Google Sheet.

**Note**: The **`is_fake_question`** function is currently commented out, suggesting a potential feature for checking if the user input is a valid question that might be implemented in the future.

'''

MD_GROQ_AGENT_DEMO = '''
###### **`st_groq_agent_demo.py`** - analysis of Python code
##### **Functions and Descriptions**

1. **`show_code(i)`**: Displays the source code of a script from the **`TAB_LIST`** using Streamlit's **`expander`** and **`markdown`** components. Takes an index **`i`** as a parameter.

2. **`select_reasoning_modules(REASONING_MODULES, task)`**: Selects relevant reasoning modules based on the given task. Imported from **`self_discover.py`**.

3. **`adapt_reasoning_modules(select_reasoning_modules, task)`**: Adapts the selected reasoning modules to make them more specific to the given task. Imported from **`self_discover.py`**.

4. **`implement_reasoning_structure(adapted_modules, task)`**: Implements the adapted reasoning modules into an actionable reasoning structure. Imported from **`self_discover.py`**.

5. **`execute_reasoning_structure(reasoning_structure, task)`**: Executes the reasoning structure to solve a specific task instance. Imported from **`self_discover.py`**.

##### **Parameters and Purpose**

1. **`REASONING_MODULES`**: A list of available reasoning modules imported from **`self_discover.py`**.
2. **`MODELS`**: A dictionary containing information about different language models available in the Groq API.
3. **`API_KEY`**: The API key obtained from the environment variable or Streamlit secrets, required to authenticate with the Groq API.
4. **`task`**: A user-provided text input representing the task for which the reasoning structure needs to be built.
5. **`reasoning_model`**: The selected language model from the **`MODELS`** dictionary, used for generating reasoning structures and task solutions.

##### **Overall Functionality**

The code sets up a Streamlit application with multiple tabs for different functionalities:

1. **Text Generation**: Allows users to input a system prompt and a user prompt, and generate responses using the selected language model from the Groq API.

1. **Self-Discover**: Implements the Self-Discover approach for building reasoning structures based on the user-provided task. It involves the following steps:
  * **Step 1**: Select relevant reasoning modules for the task.
  * **Step 2**: Adapt the selected reasoning modules to make them more specific to the task.
  * **Step 3**: Implement the adapted reasoning modules into an actionable reasoning structure.
  * **Step 4**: Execute the reasoning structure to solve the specific task instance.

  Each step is performed by calling the corresponding function from **`self_discover.py`** and generating responses using the selected language model from the Groq API. The responses are displayed in the Streamlit app in real-time.

The code also includes various sections for displaying information such as session state, headers, Groq logo, and source code of different scripts.

Overall, this application demonstrates the integration of the Groq API with Streamlit for natural language processing tasks, specifically focusing on the Self-Discover approach for building reasoning structures to solve user-provided tasks.
'''
