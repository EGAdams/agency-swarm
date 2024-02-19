```mermaid
sequenceDiagram
	user->>Agency: get_completion(message)
	Agency-->>Thread: get_completion(message)
	Thread-->>Agent: Process and respond
	Agent-->>Thread: get_response()
	Thread-->>Agency: Return response
	Agency-->>user: Return response
```
