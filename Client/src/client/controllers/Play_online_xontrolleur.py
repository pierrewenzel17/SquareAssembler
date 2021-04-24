from client.models.serveur import MyAgent
from core.models.position import Position


class play_controlleur:
    def __init__(self,state_online,myturn):
        self.agent = MyAgent("my_agent", state_online)
        self.game_controlleur = None
        self.my_turn=myturn

    def exodia(self):
        def no_play(agent):
            self.game_controlleur.pass_to_my_turn()
            if not self.game_controlleur.game.playercanplay():
                self.agent.send_msg("no")
                self.game_controlleur.pas_to_other_turn()

        def play(agent, position):
            # voir avec cyril fonction qui represente le coup de l'adversaire
            # reception du coup
            # supperssion des cube

            self.game_controlleur.coup_adverse(position)

        def disconect(agent):
            self.agent.stop()
            self.agent=None
            self.game_controlleur.end_controlleur.print_end()

        # self.agent.bind_msg(play_little_game, f'pos=(.*)')
        self.agent.bind_msg(disconect, 'parti')
        self.agent.bind_msg(play, f'pos=(.*)')
        self.agent.bind_msg(no_play, 'no')
        ##Timer(2.0, lambda: self.agent.start()).start()
        # sleep(3)
        self.agent.start()
        # print(self.agent.get_subscriptions())


    def turn_click(self, position: Position):
        # voir avec Cyril
        if self.my_turn:
            # test sur si la couleur est disponible ; suppersion des cube de la met envoyer le cube clicker a l'autre
            self.agent.send_msg(position.__str__())
