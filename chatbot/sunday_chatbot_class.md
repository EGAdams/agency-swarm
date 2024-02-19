```mermaid
classDiagram
class User {
-name: string
-input: string
-output: string
+speakIntoMicrophone(): void
+waitForIndicator(): void
+storeConversationHistory(): void
}


class Chatbot {
    -memory: Memory
    +respondToUser(input: string): string
    +detectIndicator(input: string): boolean
}

class Memory {
    +store(data: string): void
    +retrieve(): string
}

class Indicator {
    +lightUp(color: string): void
}

class Dashboard {
    +addIndicator(indicator: Indicator): void
}

class Microphone {
    +listen(): void
}

class FAISS {
    +storeVector(vector: string): void
    +retrieveVector(query: string): string
}

class Pinecone {
    +storeVector(vector: string): void
    +retrieveVector(query: string): string
}

class ConversationHistory {
    +addEntry(entry: string): void
    +retrieveHistory(): string
}

User --o Microphone
User --|> Chatbot
Chatbot --o Memory
Chatbot --|> Indicator
Dashboard --o Indicator
Memory --|> FAISS
Memory --|> Pinecone
Chatbot --|> ConversationHistory