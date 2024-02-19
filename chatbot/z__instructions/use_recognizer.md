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
    +startListening(): void
}

class CommandHandler {
    +process_command(command: string): boolean
}
class SpeechRecognizer {
    -recognizer: Recognizer
    +recognize_speech(audio_data: any): string
}
class Recognizer {
    -command_handler: CommandHandler
    -speech_recognizer: SpeechRecognizer
    +process_audio(audio_data: any): void
    +run_speech_recognition(): void
    +run_stdin_recognition(): void
}
User --o Microphone
User --|> Chatbot
Chatbot --o Memory
Chatbot --|> Recognizer
Dashboard --o Indicator
Memory --|> FAISS
Memory --|> Pinecone
Chatbot --|> ConversationHistory
CommandHandler --|> Recognizer
SpeechRecognizer --|> Recognizer