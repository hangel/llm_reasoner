PROMPT_PREAMBLE = """
Keep this consideration before proceeding  with INSTRUCTIONS:

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
And now after considering the previous instructions...
"""

PROMPT_INSTRUCTIONS = f"""
Follow these **INSTRUCTIONS**:
0. Ask for as many directions needed to perform completely the task
1. Act as a {LANGUAGE} guru. Taking a sequence of steps such as:
  1.1. Plan an outline.
  1.2. Decide what, if any, web searches are needed to gather more information making it a list
  1.3. Write a first draft.
  1.4. Read over the first draft to spot unjustified arguments or extraneous information.
  1.5. Revise the draft taking into account any weaknesses spotted.
A {RESOURCE} will be supplied as an annexed file.
"""

PROMPT_TASKS = f"""
YOUR TASKS ARE:
0. **Verify {LANGUAGE} code Syntax**
1. **GENERATE A TABLE WITH CODE COMPONENTS**
Use headers like this for the table:
  * Line Number: Number, where the element described, appears
  * Element Type ( Variable | Procedure | Function | Subroutine | Other): the type of element described
  * Name: Element Name
  * Description: Element description according is purpose in the code
2. **DESCRIPTION, the purpose of the {RESOURCE} annexed**, complete lists for:
   * Librairies | Packages required
   * Variables
   * Procedures
   
3. **WORKFLOW**: Give a workflow diagram including all components from the {RESOURCE} in Mermaid notation making clearly labeled subgraphs for every funcion | porocedure | routine, and wel labeled data flow

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
PROMPT_RESOURCE = f"{RESOURCE}:"

FINAL_PROMPT = PROMPT_PREAMBLE + PROMPT_INSTRUCTIONS + PROMPT_TASKS + PROMPT_RESOURCE
