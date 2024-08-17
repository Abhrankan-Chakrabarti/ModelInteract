from console_menu import Console, Menu

def model_selector():
    console = Console(width=59, height=30)
    while True:
        text = 'Select AI Model:'
        options = {1: 'Gemini', 2: 'Load Custom Model'}
        starting_menu = Menu(text, options, console)
        starting_menu.print_menu()
        starting_menu.print_options()
        try:
            a = starting_menu.choice()
            if a == 1:
                import gemini
                return gemini
            elif a == 2:
                import load_model
                return load_model
            else:
                print("Invalid selection. Please choose again.")
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

selected_model = model_selector()
model = selected_model.model
stream = selected_model.stream