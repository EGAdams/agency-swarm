from agency_swarm import Agency


agency = Agency([ceo, [ceo, FileManager],
 [ceo, DirectoryManager]],
shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio()
