### Workflow for LLM Integration with External API via Function Calls

1. Client sends user prompt to the LLM.
2. LLM determines if a function call is needed and returns a JSON object with arguments matching the external API schema.
3. Client invokes the external API function using the provided arguments.
4. Client processes the API response.
5. Client sends a follow-up message to the LLM including the API response.
6. LLM makes another external API call based on the updated conversation.
7. LLM summarizes the results of the API call and returns the summary to the user.
=
