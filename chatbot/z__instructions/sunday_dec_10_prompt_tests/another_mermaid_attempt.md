 ```mermaid
classDiagram
class Chatbot {
+ listenToMicrophone()
+ processInput(input)
+ saveConversation()
}


class ConversationHistory {
    - conversations: list
    + addConversation(conversation)
    + searchConversation(query)
}

class Memory {
    + store(data)
    + retrieve(key)
    + update(key, data)
    + delete(key)
}

class FAISS {
    + connect()
    + search(query)
}

class Chroma {
    + connect()
    + analyze(data)
}

class Pinecone {
    + connect()
    + findSimilar(data)
}

class User {
    + input
    + output
}

class Microphone {
    + startListening()
    + stopListening()
}

class InputProcessor {
    + process(input)
}

Chatbot --> ConversationHistory
Chatbot --> Memory
Chatbot --> User
Chatbot --> Microphone
Chatbot --> InputProcessor
ConversationHistory --> Memory
Memory --> FAISS
Memory --> Chroma
Memory --> Pinecone
```
