```mermaid
classDiagram
    class MicrophoneInputHandler {
        +listen()
    }
    class SpeechRecognitionService {
        +convertSpeechToText(audio)
    }
    class ChatbotProcessor {
        +processInput(text)
        +generateResponse()
    }
    class ResponseOutputHandler {
        +outputText(text)
    }
    class GizDetector {
        +detectTriggerWord(text)
        +activateIndicator()
    }
    class ConversationHistoryManager {
        +storeConversation(conversation)
        +retrieveHistory()
    }
    class StorageInterface {
        <<interface>>
        +store(data)
        +retrieve()
    }
    class FileSystemStorage {
        +store(data)
        +retrieve()
    }
    class FAISSStorage {
        +store(data)
        +retrieve()
    }
    class PineconeStorage {
        +store(data)
        +retrieve()
    }
    class DashboardIndicator {
        +lightUpGreen()
    }

    MicrophoneInputHandler --> SpeechRecognitionService : sends audio
    SpeechRecognitionService --> ChatbotProcessor : sends text
    ChatbotProcessor --> ResponseOutputHandler : sends response
    ChatbotProcessor --> GizDetector : sends text
    ChatbotProcessor --> ConversationHistoryManager : sends conversation data
    ConversationHistoryManager --> StorageInterface : uses
    FileSystemStorage ..|> StorageInterface
    FAISSStorage ..|> StorageInterface
    PineconeStorage ..|> StorageInterface
    GizDetector --> DashboardIndicator : activates indicator
```