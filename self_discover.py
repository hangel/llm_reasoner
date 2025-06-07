from reasoning_modules import REASONING_MODULES
"""
self_discover.py
"""

def select_reasoning_modules(reasoning_modules, task):
  """
  Step 1: SELECT relevant reasoning modules for the task.
  """
  return f"""
{task}
Given the TASK above, which three of the following reasoning modules are the most relevant?
""" + "\n".join(reasoning_modules) + f"""\n
In your answer, ONLY RETURN the number and description of each module, one per line. NEVER GIVE ANY ELABORATION ON WHY.
""".lstrip()

def adapt_reasoning_modules(selected_modules, task):
  """
  Step 2: ADAPT the selected reasoning modules to be more specific to the task.
  """
  return f"""
Without working out the full solution, adapt the following reasoning modules to be specific to the TASK below:
{selected_modules}
{task}""".lstrip()

def implement_reasoning_structure(adapted_modules, task):
  """
  Step 3: IMPLEMENT the adapted reasoning modules into an actionable reasoning structure.
  """
  return f"""
Without working out the full solution, create an actionable reasoning structure for the TASK below using these adapted reasoning modules:
{adapted_modules}
{task}""".lstrip()

def execute_reasoning_structure(reasoning_structure, task):
  """
  Execute the reasoning structure to solve a specific task instance.
  """
  return f"""
Using the following reasoning structure:
{reasoning_structure}

Solve this TASK, providing your final answer:
{task}
""".lstrip()
