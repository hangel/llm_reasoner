MVP_ARCHITECTURE_GEMINI = """
graph TD
    A[Users] --> B(Frontend: Streamlit on GCP Cloud Run);
    B -->|HTTP API Calls| C{Backend: FastAPI on GCP Cloud Run};
    C -->|CRUD Ops & Auth| D[DBaaS: Supabase];
    C -->|AI Tasks| E[AI: Google Gemini API];
    C -->|Config| F[Config: Env Vars / GCP Secret Manager];
    C -->|Logging| G[Logging: GCP Cloud Logging];

    subgraph FastAPI_Backend_GCP_Cloud_Run [FastAPI Backend GCP Cloud Run]
        H[API Routers: /books, /users, /ai]
        I[Services/Use Cases: Business Logic]
        J[AI Integration Layer: Gemini Service]
        K[Auth Module: JWT Validation, Role Checks]
        L[Pydantic Models: Schemas & Validation]
        M[Database Client: Supabase Client]
        N[Configuration Loading: Pydantic BaseSettings]
        O[Logging Middleware]
    end

    C --> H; 
    H --> I; 
    H --> K;
    I --> J; 
    I --> M; 
    I --> K;
    J --> E;
    K -->|Reads User Roles| D;
    C -->|Reads Config| N; 
    N -->|Reads Secrets| F;
    C -->|Writes Logs| O; 
    O -->|Sends to Logging| G;

    style D fill:#d6f5d6,stroke:#333,stroke-width:2px
    style E fill:#cce6ff,stroke:#333,stroke-width:2px
    style F fill:#fff0cc,stroke:#333,stroke-width:2px
    style G fill:#ffe6cc,stroke:#333,stroke-width:2px
    style B fill:#f0e6ff,stroke:#333,stroke-width:2px
"""

MERMAID_FLOWCHART_STYLES = """
graph TB
    sq[Square shape] --> ci((Circle shape))

    subgraph A
        od>Odd shape]-- Two line<br/>edge comment --> ro
        di{Diamond with <br/> line break} -.-> ro(Rounded<br>square<br>shape)
        di==>ro2(Rounded square shape)
    end

    %% Notice that no text in shape are added here instead that is appended further down
    e --> od3>Really long text with linebreak<br>in an Odd shape]

    %% Comments after double percent signs
    e((Inner / circle<br>and some odd <br>special characters)) --> f(,.?!+-*ز)

    cyr[Cyrillic]-->cyr2((Circle shape Начало));

     classDef green fill:#9f6,stroke:#333,stroke-width:2px;
     classDef orange fill:#f96,stroke:#333,stroke-width:4px;
     class sq,e green
     class di orange
"""
MERMAID_CODE_BASE = """graph LR;
    A((START));
    B([Open File]);
    C([Main Loop]);
    D{Main Menu};
    E([Create Record]);
    F([Read Record]);
    G([Update Record]);
    H([Delete Record]);
    I([Save File]);
    J([Quit Program]);
    K([Safe Close]);
    L([Create File]);
    L1((File Status));
    Z((STOP))
    A ==> B;
    L1 ==o|Normal Start| C;
    C --> D;
    D -->|C Pressed| E;
    D -->|R Pressed| F;
    D -->|U Pressed| G;
    D -->|D Pressed| H;
    E ..-> C;
    F ..-> C;
    G ..-> C;
    H ..-> C;
    I --> K;
    D -->|Q Pressed| J;
    J -->|Safe Exit| I;
    L1 --> |File Not Found| L;
    L ..-> B;
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


"""
#MERMAID_CODE = st.text_area("**__Mermaid code__**", key="tab2", height=400, value=MERMAID_CODE_BASE)

CRUD_NICE_EXAMPLE = """graph LR
    Start((START)) --> MAIN-PROCEDURE([MAIN-PROCEDURE])
    MAIN-PROCEDURE --> OPEN-FILE([OPEN-FILE])
    OPEN-FILE --> MAIN-LOOP([MAIN-LOOP])
    MAIN-LOOP --> DISPLAY-OPTIONS_([DISPLAY OPTIONS])
    DISPLAY-OPTIONS_ --> ACCEPT-OPTION_([ACCEPT OPTION])
    ACCEPT-OPTION_ --> EVALUATE-OPTION_([EVALUATE-OPTION])
    EVALUATE-OPTION_ -->|1. Create Employee | CREATE-EMPLOYEE_([CREATE-EMPLOYEE])
    EVALUATE-OPTION_ -->|2. Read Employee    | READ-EMPLOYEE_([READ-EMPLOYEE])
    EVALUATE-OPTION_ -->|3. Update Employee| UPDATE-EMPLOYEE_([UPDATE-EMPLOYEE])
    EVALUATE-OPTION_ -->|4. Delete Employee  | DELETE-EMPLOYEE_([DELETE-EMPLOYEE])
    EVALUATE-OPTION_ -->|5. Exit| CLOSE-FILE_([CLOSE-FILE])
    RETURN-MAIN-LOOP_ --> MAIN-LOOP
    CREATE-EMPLOYEE_ --> RETURN-MAIN-LOOP_
    READ-EMPLOYEE_ --> RETURN-MAIN-LOOP_
    UPDATE-EMPLOYEE_ --> RETURN-MAIN-LOOP_
    DELETE-EMPLOYEE_ --> RETURN-MAIN-LOOP_
    CLOSE-FILE_ --> STOP((STOP))

subgraph MAIN_LOOP
     MAIN-LOOP; DISPLAY-OPTIONS_; ACCEPT-OPTION_;
end

subgraph MENU
   EVALUATE-OPTION_ ;
   CREATE-EMPLOYEE_;
   READ-EMPLOYEE_;
   UPDATE-EMPLOYEE_;
   DELETE-EMPLOYEE_;
   CLOSE-FILE_;
   RETURN-MAIN-LOOP_;
end
"""
CRUD_DEEPSEEK_MERMAID = """graph LR
   A[START] --> B[OPEN FILE];
   B --> L1[FILE NOT FOUND];
   L1 -->  A1[INITIALIZE FILE];
   A1 --> B;
   B --> B1[FILE READY];
   B1 --> C[DISPLAY MENU];
   C --> D[ACCEPT OPTION];
   O1 --> E[VALID OPTION];
   O1 --> O[INVALID OPTION];
   D --> O1[EVALUATE OPTION];
   E --> F[CREATE EMPLOYEE];
   F--> G[INVALID KEY: Create Employee];
   G --> F;
   E --> I[READ EMPLOYEE];
   I--> J[INVALID KEY: Read Employee] ;
   J --> I[READ EMPLOYEE];
   E --> K[UPDATE EMPLOYEE];
   K --> L[INVALID KEY: Update Employee] ;
   L --> K[UPDATE EMPLOYEE];
   E --> M[DELETE EMPLOYEE];
   M --> N[INVALID KEY: Delete Employee] ;
   N --> M[DELETE EMPLOYEE];
   O --> C[DISPLAY MENU];
   E --> Q[EXIT PROGRAM];
   Q --> R[STOP RUN];

    subgraph get-input
     C; D; O; O1;
    end

    subgraph main-menu
     F; I; K; M; Q;
    end

    subgraph fix-open
     A1; L1; 
    end
"""

ER_EXAMPLE = """erDiagram
          CUSTOMER }|..|{ DELIVERY-ADDRESS : has
          CUSTOMER ||--o{ ORDER : places
          CUSTOMER ||--o{ INVOICE : "liable for"
          DELIVERY-ADDRESS ||--o{ ORDER : receives
          INVOICE ||--|{ ORDER : covers
          ORDER ||--|{ ORDER-ITEM : includes
          PRODUCT-CATEGORY ||--|{ PRODUCT : contains
          PRODUCT ||--o{ ORDER-ITEM : "ordered in"
"""

COBOLagencyASPER_Process = """flowchart LR

CLOUD([CLOUD])
WEB([WEB])     
LLM([LLM])
API([API])
TP([TEST POINTS])

R0([REQUIREMENTS]) --> A(ANALIZE) --> S(STRUCTURE) --> P(PLAN) --> E(EXECUTE) --> R([REVIEW]) --> D([DELIVERABLES ])
P ..-> PR

PR([PROPOSAL])

EX[[EXPERIENCE<br/>CAPTURE]]

SAFE_START <-..->|Knowledge<br/>Use & Acquisition| EX
ITERATE_CYCLE <-..->|Knowledge<br/>Use &<br/>Acquisition| EX

subgraph SERVICES
           CLOUD; WEB; LLM; API; TP
end

subgraph SAFE_START
      direction LR
       A; S; P;
end

subgraph ITERATE_CYCLE
      direction TB
       E; R; 
end

subgraph KNOWLEDGE_MANAGEMENT
     EX
end

subgraph CUSTOMER
       D; PR
end

P <-..->|Plan Adjustment Cycle| R

SAFE_START <==>|Pre External Access| SERVICES
ITERATE_CYCLE<==>|Post External Access| SERVICES
"""

BASIC_SEQUENCE = """sequenceDiagram
    Alice ->> Bob: Hello Bob, how are you?
    Bob-->>John: How about you John?
    Bob--x Alice: I am good thanks!
    Bob-x John: I am good thanks!
    Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

    Bob-->Alice: Checking with John...
    Alice->John: Yes... John, how are you?
"""
