### Workflow for LLM Integration with External API via Function Calls

1. Client sends user prompt to the LLM.
2. LLM determines if a function call is needed and returns a JSON object with arguments matching the external API schema.
3. Client invokes the external API function using the provided arguments.
4. Client processes the API response.
5. Client sends a follow-up message to the LLM including the API response.
6. LLM makes another external API call based on the updated conversation.
7. LLM summarizes the results of the API call and returns the summary to the user.


---

### Mapping LLM API Attack Surface and Excessive Agency

* **Excessive Agency:**
  When an LLM has access to APIs capable of handling sensitive data and can be manipulated to invoke those APIs unsafely. This may let attackers push the LLM beyond its intended boundaries to exploit APIs or plugins.

* **Stage 1: Identifying Accessible APIs**
  To assess risk, first determine which APIs and plugins the LLM can access. A straightforward method is to ask the LLM directly about its accessible APIs.

* **Gathering More Information:**
  After identifying APIs, ask the LLM for further details about each API to understand their capabilities and risks.

* **Bypassing Non-Cooperation:**
  If the LLM refuses to disclose API info, try providing misleading context (e.g., claiming to be the LLM’s developer with higher privileges) and re-ask the question to trick it into revealing more.

---


![image](https://github.com/user-attachments/assets/2736e164-44c3-4200-a9d5-3b52677dc6c2)
😳
