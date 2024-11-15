from controllers.tournament_controller import TournamentController
from views.main_menu_view import MainMenuView
from views.tournament_view import TournamentView


class ApplicationController:
    def __init__(self):
        self.tournament_controller = TournamentController()

    def run(self):
        """Main program loop."""
        while True:
            choice = MainMenuView.display_main_menu()
            if choice == "1":
                self.start_new_tournament()
            elif choice == "2":
                self.load_existing_tournament()
            elif choice == "3":
                self.show_reports()  # New option for reports
            elif choice == "4":
                MainMenuView.display_quit_message()
                break
            else:
                print("Choix non valide, veuillez réessayer.")

    def show_reports(self):
        """Display the reports menu and handle the selected report."""
        while True:
            report_choice = MainMenuView.display_reports_menu()
            if report_choice in ["3", "4", "5"]:  # Options that require a tournament
                search_str = input("Entrez les lettres présentes dans le nom du tournoi : ").strip().lower()
                filtered_tournaments = self.tournament_controller.search_tournaments_by_name(search_str)

                if not filtered_tournaments:
                    print("Aucun tournoi ne correspond à ces lettres.")
                    continue

                print("\n=== Tournois correspondants ===")
                for idx, tournament in enumerate(filtered_tournaments, start=1):
                    print(f"{idx}: {tournament['name']}")

                try:
                    selected_index = int(input("Veuillez entrer le numéro du tournoi choisi : ").strip()) - 1
                    if 0 <= selected_index < len(filtered_tournaments):
                        selected_tournament = filtered_tournaments[selected_index]
                    else:
                        print("Numéro de tournoi invalide.")
                        continue
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un numéro.")
                    continue

                tournament_id = selected_tournament['id']
                tournament = self.tournament_controller.load_tournament_by_id(tournament_id)

                if not tournament:
                    print("Erreur lors du chargement du tournoi.")
                    continue

                if report_choice == "3":
                    details = self.tournament_controller.get_tournament_details(tournament_id)
                    if details:
                        TournamentView.display_tournament_details(*details)
                    else:
                        print("Tournoi non trouvé.")
                elif report_choice == "4":
                    players = self.tournament_controller.get_tournament_players_sorted(tournament_id)
                    TournamentView.display_tournament_players(players)
                elif report_choice == "5":
                    rounds = self.tournament_controller.get_tournament_rounds_and_matches(tournament_id)
                    TournamentView.display_tournament_rounds_and_matches(rounds, tournament)
            elif report_choice == "1":
                players = self.tournament_controller.get_all_players_sorted()
                TournamentView.display_all_players(players)
            elif report_choice == "2":
                tournaments = self.tournament_controller.get_all_tournaments()
                TournamentView.display_all_tournaments(tournaments)
            elif report_choice == "6":
                break
            else:
                print("Choix non valide, veuillez réessayer.")

    def start_new_tournament(self):
        """Initialize and start a new tournament."""
        tournament_details = MainMenuView.get_tournament_details()
        self.tournament_controller.create_tournament(*tournament_details)
        self.tournament_controller.add_players()
        self.tournament_controller.start_tournament()

    def load_existing_tournament(self):
        """Loads an existing tournament by displaying
        available tournaments for selection.
        """
        search_str = input("Entrez les lettres présentes"
                           " dans le nom du tournoi : ").strip().lower()
        filtered_tournaments = (self.tournament_controller.
                                search_tournaments_by_name(search_str))

        if not filtered_tournaments:
            print("Aucun tournoi en cours ne correspond à ces lettres.")
            return

        print("\n=== Tournois en cours correspondants ===")
        for idx, tournament in enumerate(filtered_tournaments, start=1):
            print(f"{idx}: {tournament['name']}")

        try:
            selected_index = (
                    int(input("Veuillez entrer le numéro du tournoi choisi : ")
                                .strip()) - 1)
            if 0 <= selected_index < len(filtered_tournaments):
                selected_tournament = filtered_tournaments[selected_index]
            else:
                print("Numéro de tournoi invalide.")
                return
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro.")
            return

        tournament_id = selected_tournament['id']
        if self.tournament_controller.load_tournament_by_id(tournament_id):
            print("Tournoi chargé avec succès.")

            if self.tournament_controller.can_resume_tournament():
                resume_choice = (
                    input("Souhaitez-vous reprendre le tournoi ? (o/n) : ").
                    strip().lower())
                if resume_choice == "o":
                    self.tournament_controller.start_tournament()
                else:
                    print("Retour au menu principal.")
            else:
                print("Ce tournoi est déjà terminé.")
        else:
            print("Le tournoi n'a pas pu être chargé correctement.")
