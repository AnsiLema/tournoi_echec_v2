from datetime import datetime


class PlayerMenuView:
    """Class for displaying the player menu and handling user input."""
    @staticmethod
    def display_player_menu():
        print("\n=== Gestion des Joueurs ===")
        print("1. Ajouter un nouveau joueur")
        print("2. Rechercher un joueur dans la base de données JSON")
        choice = input("Veuillez choisir une option : ")
        return choice

    @staticmethod
    def display_add_player_menu():
        """Display the add player menu and return the user's input."""
        last_name = input("Nom : ")
        first_name = input("Prénom : ")

        # Making sure the date of birth is a valid date
        while True:
            date_of_birth = input("Date de naissance (format: JJ/MM/AAAA) : ")
            if PlayerMenuView.is_valid_date(date_of_birth):
                break
            else:
                print("Date invalide. Veuillez entrer une date valide au format JJ/MM/AAAA.")

        national_id = input("ID National : ")
        return last_name, first_name, date_of_birth, national_id

    @staticmethod
    def is_valid_date(date_str):
        """Validate the date format JJ/MM/AAAA and check if it is a real date."""
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    @staticmethod
    def display_player_already_added():
        """Display a message when the player is already added to the tournament."""
        print("Ce joueur a déjà été ajouté au tournoi. Veuillez en choisir un autre.")

    @staticmethod
    def display_player_count(current, required):
        """Display the number of players currently added to the tournament."""
        print(f"Nombre de joueurs enregistrés : {current} / {required} requis")

    @staticmethod
    def get_add_choice():
        """Get the player addition choice from the user."""
        return input("Voulez-vous :\n1. Créer un nouveau joueur\n2. Sélectionner un joueur existant\n> ")

    @staticmethod
    def display_invalid_option():
        """Display a message when the user makes an invalid choice."""
        print("Option non valide, veuillez réessayer.")

    @staticmethod
    def display_ready_to_start():
        """Display a message when the number of players is reached."""
        print("Le nombre requis de joueurs a été atteint. Le tournoi peut commencer.")

    @staticmethod
    def get_player_filter():
        """Get the player filter from the user."""
        return (input("Entrez une lettre ou plusieurs lettres pour filtrer les joueurs par nom de famille : ").
                strip().lower())

    @staticmethod
    def display_no_matching_players():
        """Display a message when no players match the filter."""
        print("Aucun joueur ne correspond à ce filtre.")

    @staticmethod
    def display_filtered_players(filtered_players):
        """Display the filtered players."""
        for i, player in enumerate(filtered_players, start=1):
            print(f"{i}. {player['first_name']} {player['last_name']} (ID: {player['national_id']})")

    @staticmethod
    def get_player_selection():
        """Get the player selection from the user."""
        return input("Entrez le numéro pour sélectionner un joueur ou 'r' pour réessayer le filtre : ").strip()

    @staticmethod
    def display_invalid_number():
        """Display a message when the player selection is invalid."""
        print("Numéro invalide, veuillez réessayer.")

    @staticmethod
    def display_invalid_entry():
        """Display a message when the user enters an invalid input."""
        print("Entrée invalide, veuillez réessayer.")

    @staticmethod
    def display_player_added(player):
        """Display a message when a player is added to the tournament."""
        print(f"{player.first_name} {player.last_name} a été ajouté au tournoi.")

    @staticmethod
    def display_add_player_success_menu():
        """Display a message when a player is added to the tournament."""
        print("\nJoueur ajouté avec succès.")
        input("Appuyez sur Entrée pour revenir au menu des joueurs.")
