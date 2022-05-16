from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random
import numpy as np

author = 'Lunzheng Li'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'pooled_contest'
    players_per_group = 4

    num_real_rounds = 2
    num_trial_rounds = 1
    num_rounds = num_real_rounds + num_trial_rounds

    # type is a function of python, I use typo here
    typos = ['A', 'B', 'A', 'B']

    # endowment = 100
    reward = 100

    instructions_template = 'pooled_contest/Instructions_temp.html'


class Subsession(BaseSubsession):

    real_round_number = models.IntegerField()
    endowment = models.IntegerField()

    def creating_session(self):
        self.endowment = self.session.config['endowment']

        # tpp = tickets per point
        tpp_A = self.session.config['tickets_per_point_A']
        tpp_B = self.session.config['tickets_per_point_B']

        # all participant have the same type across all periods.
        typos_in_subsession = sorted(Constants.typos * len(self.get_groups()))
        # random.shuffle(typos_in_subsession)
        # print(typos_in_subsession)

        self.session.vars['typoA_in_subsession'] = []
        self.session.vars['typoB_in_subsession'] = []

        for player in self.get_players():
            # get which round to pay
            if self.round_number == Constants.num_rounds:
                player.paying_round = random.randint(
                    1 + Constants.num_trial_rounds, Constants.num_rounds)

            player.participant.vars['typo'] = typos_in_subsession[0]
            del typos_in_subsession[0]
            player.typo = player.participant.vars['typo']

            if player.typo == 'A':
                player.tpp = tpp_A
                self.session.vars['typoA_in_subsession'].append(
                    player.id_in_subsession)
            else:
                player.tpp = tpp_B
                self.session.vars['typoB_in_subsession'].append(
                    player.id_in_subsession)
        # print(self.round_number, self.session.vars)
        matrix = []
        random.shuffle(self.session.vars['typoA_in_subsession'])
        random.shuffle(self.session.vars['typoB_in_subsession'])
        # print(self.round_number, self.session.vars)
        for i in range(0, len(self.session.vars['typoA_in_subsession']), 2):
            row = self.session.vars['typoA_in_subsession'][i:i + 2] + \
                self.session.vars['typoB_in_subsession'][i:i + 2]
            random.shuffle(row)
            matrix.append(row)

        self.set_group_matrix(matrix)

        # adding a trial round
        self.real_round_number = self.round_number - Constants.num_trial_rounds

        print(self.round_number, self.get_group_matrix())

    # data for the quiz
    def get_quiz_data(self):
        tpp_A = self.session.config['tickets_per_point_A']
        tpp_B = self.session.config['tickets_per_point_B']
        sol_f = self.session.config['endowment'] + Constants.reward - 10
        sol_g = self.session.config['endowment'] - 10
        return [
            dict(
                name='a',
                solution=tpp_A,
                explanation="Your answer is wrong. Type A participants receive " + str(tpp_A) +" lottery tickets per point spent.",
            ),
            dict(
                name='b',
                solution=tpp_B,
                explanation="Your answer is wrong. Type B participants receive " + str(tpp_B) +" lottery tickets per point spent.",
            ),
            dict(
                name='c',
                solution=100,
                explanation="Your answer is wrong. The reward is worth 100 points."
            ),
            dict(
                name='d',
                solution=20,
                explanation='''Your answer is wrong.
                Recall, you purchased 10 lottery tickets and the other three participants
                purcahsed a combined total of 40 lottery tickets. Hence, in total
                50 lottery tickets were purchased in your group. The probability
                that you will receive the reward is simply the number of lottery
                tickets you purchased divided by the total number of lottery tickets
                purchased in your group. Therefore, the probability that you will
                receive the reward in this example is (10/50)*100% = 20%.'''
            ),
            dict(
                name='e',
                solution=60,
                explanation='''Your answer is wrong.
                Recall, you purchased 60 lottery tickets and the other three participants
                purcahsed a combined total of 40 lottery tickets. Hence, in total
                100 lottery tickets were purchased in your group. The probability
                that you will receive the reward is simply the number of lottery
                tickets you purchased divided by the total number of lottery tickets
                purchased in your group. Therefore, the probability that you will
                receive the reward in this example is (60/100)*100% = 60%.'''
            ),
            dict(
                name='f',
                solution=sol_f,
                explanation='''Your answer is wrong. 
                Recall, you were endowed with '''+ str(self.session.config['endowment']) + ''' points. You spent 10 points on
                lottery tickets and you received the reward. Your Earning = Endowment
                + Reward - Points you spent in that stage = '''+ str(self.session.config['endowment']) + ''' + 100 - 10 = '''+str(sol_f)+''' points.
                '''
            ),
            dict(
                name='g',
                solution=sol_g,
                explanation='''Your answer is wrong. 
                Recall, you were endowed with '''+ str(self.session.config['endowment']) + ''' points. You spent 10 points on
                lottery tickets and you did not received the reward. Your Earning 
                = Endowment - Points you spent in that stage = '''+ str(self.session.config['endowment']) + ''' - 10 = '''+str(sol_g)+''' points.'''
            ),

        ]


class Group(BaseGroup):
    # In Stage 1
    winner_ticket_num1 = models.IntegerField()
    total_tickets1 = models.FloatField()
    total_points1 = models.FloatField()

    # In Stage 2
    winner_ticket_num2 = models.IntegerField()
    total_tickets2 = models.FloatField()
    total_points2 = models.FloatField()

    # All stages
    total_points_twostages = models.FloatField()

    def set_payoffs1(self):
        players = self.get_players()
        # # Note, the following is imporant, even though you have done random
        # # grouping, the lst is still[1, 2, 3, 4]
        # print([p.id_in_group for p in players])
        points = [p.spend1 for p in players]
        tickets = [p.spend1 * p.tpp for p in players]

        self.total_points1 = sum(points)
        self.total_tickets1 = sum(tickets)
        # print(tickets)
        # print(np.arange(1, self.total_tickets1 + 1))
        if self.total_tickets1 == 0:
            winner_id = random.choice(
                np.arange(1, Constants.players_per_group + 1))

        else:
            self.winner_ticket_num1 = random.choice(
                np.arange(1, self.total_tickets1 + 1))
            # print(self.winner_ticket_num1)

            # I can get the winner_id
            if self.winner_ticket_num1 <= tickets[0]:
                winner_id = 1
            elif self.winner_ticket_num1 <= sum(tickets[:2]):
                winner_id = 2
            elif self.winner_ticket_num1 <= sum(tickets[:3]):
                winner_id = 3
            else:
                winner_id = 4

        for p in players:
            if winner_id == p.id_in_group:
                p.is_winner1 = 'Yes'
                p.payoff1 = p.subsession.endowment - p.spend1 + Constants.reward
            else:
                p.is_winner1 = 'No'
                p.payoff1 = p.subsession.endowment - p.spend1
        # print(winner_id)

    def set_payoffs2(self):
        players = self.get_players()
        # # Note, the following is imporant, even though you have done random
        # # grouping, the lst is still[1, 2, 3, 4]
        # print([p.id_in_group for p in players])
        points = [p.spend2 for p in players]
        tickets = [p.spend2 * p.tpp for p in players]

        self.total_points2 = sum(points)
        self.total_tickets2 = sum(tickets)
        self.total_points_twostages = self.total_points1 + self.total_points2
        # print(tickets)
        # print(np.arange(1, self.total_tickets2 + 1))
        if self.total_tickets2 == 0:
            winner_id = random.choice(
                np.arange(1, Constants.players_per_group + 1))

        else:
            self.winner_ticket_num2 = random.choice(
                np.arange(1, self.total_tickets2 + 1))
            # print(self.winner_ticket_num2)

            # I can get the winner_id
            if self.winner_ticket_num2 <= tickets[0]:
                winner_id = 1
            elif self.winner_ticket_num2 <= sum(tickets[:2]):
                winner_id = 2
            elif self.winner_ticket_num2 <= sum(tickets[:3]):
                winner_id = 3
            else:
                winner_id = 4

        for p in players:
            if winner_id == p.id_in_group:
                p.is_winner2 = 'Yes'
                p.payoff2 = p.subsession.endowment - p.spend2 + Constants.reward
            else:
                p.is_winner2 = 'No'
                p.payoff2 = p.subsession.endowment - p.spend2
        # print(winner_id)
            p.payoff_twostages = p.payoff1 + p.payoff2


class Player(BasePlayer):
    # In both stages, types and tpp are keep the same
    typo = models.StringField()  # the player's type
    tpp = models.IntegerField()  # tickets per point

    # In Stage1
    spend1 = models.FloatField(
        min=0, label='How many points would you like to spend?')

    def spend1_max(self):
        return self.subsession.endowment

    is_winner1 = models.StringField()
    payoff1 = models.FloatField()

    # In Stage2
    spend2 = models.FloatField(
        min=0, label='How many points would you like to spend?')

    def spend2_max(self):
        return self.subsession.endowment
    is_winner2 = models.StringField()
    payoff2 = models.FloatField()

    # All stages
    payoff_twostages = models.FloatField()  # total payoff in two stages

    # final payment
    # note this includes real and trial periods
    paying_round = models.IntegerField()
    # For instance, if paying_round is 3, the
    # payoff of period 2 is realised.

    payoff_final1 = models.FloatField()  # shall match the stage 1 payoff in
                                         # the paying_round
    payoff_final2 = models.FloatField()

    def set_final_payoffs(self):
        rate = self.session.config['exchange_rate']
        print(self.paying_round)
        self.payoff_final1 = self.in_round(
            self.paying_round).payoff1
        self.payoff_final2 = self.in_round(
            self.paying_round).payoff2
        self.participant.vars['payoff_in_AUD'] = self.in_round(
            self.paying_round).payoff_twostages / rate

    # form fields in the questionnaire
    age = models.IntegerField(min=18, max=100, label='What is your age?')
    gender = models.IntegerField(
        choices=[
            [0, 'Male'],
            [1, 'Female'],
            [2, 'Other'],
            [3, 'Prefer not to say'],
        ],
        label='What is your gender?',
        widget=widgets.RadioSelectHorizontal
    )
    ethnicity = models.IntegerField(
        choices=[
                [0, 'Caucasian'],
                [1, 'Asian'],
                [2, 'Black'],
                [3, 'Other'],
                [4, 'Prefer not to say'],
        ],
        label='What is your ethnicity?',
        widget=widgets.RadioSelectHorizontal
    )
    major = models.IntegerField(
        choices=[
            [0, 'No'],
            [1, 'Yes'],
        ],
        label='Is your major in Economics or Finance?',
        widget=widgets.RadioSelectHorizontal
    )
    risk = models.IntegerField(
        choices=[
                [0, '0'],
                [1, '1'],
                [2, '2'],
                [3, '3'],
                [4, '4'],
                [5, '5'],
                [6, '6'],
                [7, '7'],
                [8, '8'],
                [9, '9'],
                [10, '10'],
        ],
        label='''Are you generally a person who is fully prepared to take risks
         or do you try to avoid taking risks? (0: unwilling to take risks; 
         10: fully prepared to take risks).''',
        widget=widgets.RadioSelectHorizontal
    )
    
    motivation = models.IntegerField(
        choices=[
            [0, 'I wanted to make the highest possible payoff'],
            [1, 'I wanted to experience the joy of winning'],
            [2, 'I wanted to avoid the pain of losing'],
            [3, 'Other, please specify below'],
        ],
        label='What was the main motivation behind your points expenditure in the game?',
        widget=widgets.RadioSelect
    )

    mot_openend = models.StringField(blank=True)

    # form fields in the quiz
    a = models.IntegerField(
        label='1. If you are type A, how many lottery tickets do you receive per point spent?')
    b = models.IntegerField(
        label="2. If you are type B, how many lottery tickets do you receive per point spent?")
    c = models.IntegerField(
        label="3. How many points is the reward worth?")
    d = models.IntegerField(
        label='''4. Suppose you purchase 10 lottery tickets and the three other
        participants in your group purchase a combined total of 40 lottery tickets.
        What is your probability of receiving the reward in percentage terms? 
        (Please refer to formula 3)''')
    e = models.IntegerField(
        label='''5. Suppose you purchase 60 lottery tickets and the three other
        participants in your group purchase a combined total of 40 lottery tickets.
        What is your probability of receiving the reward in percentage terms? 
        (Please refer to formula 3)''')
    f = models.IntegerField(
        label='''6. Suppose you spent 10 points on lottery tickets and you received
        the reward. What are your earnings for that stage? (Please refer to formula 1)
        ''')
    g = models.IntegerField(
        label='''7. Suppose you spent 10 points on lottery tickets and you did not received
        the reward. What are your earnings for that stage? (Please refer to formula 2)
        ''')
