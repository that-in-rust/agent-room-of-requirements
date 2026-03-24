# Problem Solving

``` text

1000 integrations in Composio

Each app can have multiple actions
    - API calls with a particular API format

50k + APIs across 1000 appps

Each integration first draft
    - builds
    - tests ships it

Agent generates description
    - input parameters
    - output
    - range
    - constraints
    - dos and donts
    - best practices

Primary key is Tool x Utility x Configuration

Question
    - LLMs miss the nuances
    - Documentation is not
        - Wrong
        - Incomplete
        - Out of date

This affects the reliability of the integrations and the ability to use them in a production environment

Leads to lower trust amongst the customers

How to solve this?

Tools 
    - Tools not deterministic, generally behavior follows univariate
        - MongoDB constraints, edges cases which their documentation has not covered
        - How to discover these constraints?

- OSS tools
    - Spend tokens to find API behavior variance from git clone
        - Static analysis of the codebase
    - Decompile the code of the tool
        - Static analysis of the decompiled code
    - Dynamic analysis of the tools
        - Runtime analysis of tool
            - Happy path testing by putting it in a VM and having observability logs on it
            - Random use cases of testing inside the VM - chaos monkey testing - CPU
            - Collecting all PUBLIC info of the tool from internet and creating corpuse of test cases to simulate in a VM
    - Beta testing of pareto tools or pareto use cases
        - Top 20% cases can use x Humans to test out the edge cases
    - VIP Beta group - special group - whom share your top early access, as customers
    - Constantly keep enriching the corpus of test cases by using the tools in production

- Product Release
    - Tools some telemetry - anonymized - you find usage patterns
        - to find errors before users report them
        - to find logs when users report them
        - to find which are the most of used parameters or utilities
        - Agentic tool which integrates this into your documentation or feedback loop to even the underlying repos or companies that your tools is facig this setof problems

            



```