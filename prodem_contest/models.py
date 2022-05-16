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

"""


class Constants(BaseConstants):
    name_in_url = 'prodem_contest'
    players_per_group = 4

    num_real_rounds = 2
    num_trial_rounds = 1
    num_rounds = num_real_rounds + num_trial_rounds

    typos = ['A', 'B', 'A', 'B']

    reward_blue = 100
    reward_red = 0

    instructions_template = 'prodem_contest/Instructions_temp.html'


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
                player.division1 = 'Blue'
                self.session.vars['typoA_in_subsession'].append(
                    player.id_in_subsession)
            else:
                player.tpp = tpp_B
                player.division1 = 'Red'
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
        sol_g = self.session.config['endowment'] + Constants.reward_blue - 10
        sol_h = self.session.config['endowment'] - 10
        return [
            dict(
                name='a',
                solution=tpp_A,
                explanation="Your answer is wrong. Type A participants receive " +
                str(tpp_A) + " lottery tickets per point spent.",
            ),
            dict(
                name='b',
                solution=tpp_B,
                explanation="Your answer is wrong. Type B participants receive " +
                str(tpp_B) + " lottery tickets per point spent.",
            ),
            dict(
                name='c',
                solution=Constants.reward_blue,
                explanation="Your answer is wrong. For participants in the Blue division the reward is worth " +
                str(Constants.reward_blue) + " points."
            ),
            dict(
                name='d',
                solution=Constants.reward_red,
                explanation="Your answer is wrong. For participants in the Red division the reward is worth " +
                str(Constants.reward_red) + " points."
            ),
            dict(
                name='e',
                solution=20,
                explanation='''Your answer is wrong.
                Recall, you purchased 10 lottery tickets and the other participant
                purcahsed 40 lottery tickets. Hence, in total 50 lottery tickets 
                were purchased in your division. The probability that you will receive 
                the reward is simply the number of lottery
                tickets you purchased divided by the total number of lottery tickets
                purchased in your division. Therefore, the probability that you will
                receive the reward in this example is (10/50)*100% = 20%.'''
            ),
            dict(
                name='f',
                solution=60,
                explanation='''Your answer is wrong.
                Recall, you purchased 60 lottery tickets and the other participant
                purcahsed total of 40 lottery tickets. Hence, in total
                100 lottery tickets were purchased in your division. The probability
                that you will receive the reward is simply the number of lottery
                tickets you purchased divided by the total number of lottery tickets
                purchased in your division. Therefore, the probability that you will
                receive the reward in this example is (60/100)*100% = 60%.'''
            ),
            dict(
                name='g',
                solution=sol_g,
                explanation='''Your answer is wrong.
                Recall, you were endowed with ''' + str(self.session.config['endowment']) + ''' points
                and you were in the Blue division. You spent 10 points on
                lottery tickets and you received the reward. Your Earning = Endowment
                + Reward - Points you spent in that stage = ''' + str(self.session.config['endowment']) + ''' + 100 - 10 = ''' + str(sol_g) + ''' points.
                '''
            ),
            dict(
                name='h',
                solution=sol_h,
                explanation='''Your answer is wrong.
                Recall, you were endowed with ''' + str(self.session.config['endowment']) + ''' points
                and you were in the Blue division. You spent 10 points on
                lottery tickets and you did not received the reward. Your Earning
                = Endowment - Points you spent in that stage = ''' + str(self.session.config['endowment']) + ''' - 10 = ''' + str(sol_h) + ''' points.'''
            ),
            dict(
                name='i',
                solution=1,
                explanation='''Your answer is wrong.
                The correct answer is Yes. If you do not receive the reward in the
                Blue division in stage 1, you will be moved to the Red division in stage 2.'''
            ),
            dict(
                name='j',
                solution=1,
                explanation='''Your answer is wrong.
                The correct answer is Yes. If you do receive the reward in the Red division in
                stage 1, you will be moved to the Blue division in stage 2.
                '''
            ),
        ]


class Group(BaseGroup):
    # stage 1
    winner_ticket_num1_red = models.IntegerField()
    winner_ticket_num1_blue = models.IntegerField()

    total_points1_red = models.FloatField()
    total_tickets1_red = models.FloatField()

    total_points1_blue = models.FloatField()
    total_tickets1_blue = models.FloatField()

    # stage 2
    winner_ticket_num2_red = models.IntegerField()
    winner_ticket_num2_blue = models.IntegerField()

    total_points2_red = models.FloatField()
    total_tickets2_red = models.FloatField()

    total_points2_blue = models.FloatField()
    total_tickets2_blue = models.FloatField()

    # two stages
    total_points_twostages = models.FloatField()
    total_tickets_twostages = models.FloatField()

    def set_payoffs1(self):
        players = self.get_players()

        ################
        # Red division #
        ################
        points_red = [p.spend1 for p in players if p.division1 == 'Red']
        tickets_red = [p.spend1 *
                       p.tpp for p in players if p.division1 == 'Red']
        id_red = [p.id_in_group for p in players if p.division1 == 'Red']

        self.total_points1_red = sum(points_red)
        self.total_tickets1_red = sum(tickets_red)

        # let's get a sorted tickets_Red, in which smaller id player's tickets is
        # before the larger id player
        tickets_red_sorted = [x for _, x in sorted(zip(id_red, tickets_red))]
        id_red_sorted = sorted(id_red)

        if self.total_tickets1_red == 0:
            winner_id_red = random.choice(id_red)

        else:
            self.winner_ticket_num1_red = random.choice(
                np.arange(1, self.total_tickets1_red + 1))

            # I can get the winner_id_red
            if self.winner_ticket_num1_red <= tickets_red_sorted[0]:
                winner_id_red = id_red_sorted[0]
            else:
                winner_id_red = id_red_sorted[1]
        for i in id_red:
            p = self.get_player_by_id(i)
            if winner_id_red == p.id_in_group:
                p.is_winner1_red = 'Yes'
                p.payoff1 = p.subsession.endowment - p.spend1 + Constants.reward_red
            else:
                p.is_winner1_red = 'No'
                p.payoff1 = p.subsession.endowment - p.spend1
        # print(winner_id_red)

        #################
        # Blue division #
        #################
        points_blue = [p.spend1 for p in players if p.division1 == 'Blue']
        tickets_blue = [p.spend1 *
                        p.tpp for p in players if p.division1 == 'Blue']
        id_blue = [p.id_in_group for p in players if p.division1 == 'Blue']

        self.total_points1_blue = sum(points_blue)
        self.total_tickets1_blue = sum(tickets_blue)

        # let's get a sorted tickets_Red, in which smaller id player's tickets is
        # before the larger id player
        tickets_blue_sorted = [
            x for _, x in sorted(zip(id_blue, tickets_blue))]
        id_blue_sorted = sorted(id_blue)

        if self.total_tickets1_blue == 0:
            winner_id_blue = random.choice(id_blue)

        else:
            self.winner_ticket_num1_blue = random.choice(
                np.arange(1, self.total_tickets1_blue + 1))

            # I can get the winner_id_blue
            if self.winner_ticket_num1_blue <= tickets_blue_sorted[0]:
                winner_id_blue = id_blue_sorted[0]
            else:
                winner_id_blue = id_blue_sorted[1]

        for i in id_blue:
            p = self.get_player_by_id(i)
            if winner_id_blue == p.id_in_group:
                p.is_winner1_blue = 'Yes'
                p.payoff1 = p.subsession.endowment - p.spend1 + Constants.reward_blue
            else:
                p.is_winner1_blue = 'No'
                p.payoff1 = p.subsession.endowment - p.spend1
        # print(winner_id_blue)

        ##########
        # prodem #
        ##########
        for p in players:
            if p.division1 == 'Red':
                if p.is_winner1_red == 'Yes':
                    p.division2 = 'Blue'
                else:
                    p.division2 = 'Red'
            else:
                if p.is_winner1_blue == 'Yes':
                    p.division2 = 'Blue'
                else:
                    p.division2 = 'Red'

    def set_payoffs2(self):
        players = self.get_players()

        ################
        # Red division #
        ################
        points_red = [p.spend2 for p in players if p.division2 == 'Red']
        tickets_red = [p.spend2 *
                       p.tpp for p in players if p.division2 == 'Red']
        id_red = [p.id_in_group for p in players if p.division2 == 'Red']

        self.total_points2_red = sum(points_red)
        self.total_tickets2_red = sum(tickets_red)

        # let's get a sorted tickets_Red, in which smaller id player's tickets is
        # before the larger id player
        tickets_red_sorted = [x for _, x in sorted(zip(id_red, tickets_red))]
        id_red_sorted = sorted(id_red)

        if self.total_tickets2_red == 0:
            winner_id_red = random.choice(id_red)

        else:
            self.winner_ticket_num2_red = random.choice(
                np.arange(1, self.total_tickets2_red + 1))

            # I can get the winner_id_red
            if self.winner_ticket_num2_red <= tickets_red_sorted[0]:
                winner_id_red = id_red_sorted[0]
            else:
                winner_id_red = id_red_sorted[1]
        for i in id_red:
            p = self.get_player_by_id(i)
            if winner_id_red == p.id_in_group:
                p.is_winner2_red = 'Yes'
                p.payoff2 = p.subsession.endowment - p.spend2 + Constants.reward_red
            else:
                p.is_winner2_red = 'No'
                p.payoff2 = p.subsession.endowment - p.spend2
        # print(winner_id_red)

        #################
        # Blue division #
        #################
        points_blue = [p.spend2 for p in players if p.division2 == 'Blue']
        tickets_blue = [p.spend2 *
                        p.tpp for p in players if p.division2 == 'Blue']
        id_blue = [p.id_in_group for p in players if p.division2 == 'Blue']

        self.total_points2_blue = sum(points_blue)
        self.total_tickets2_blue = sum(tickets_blue)

        # let's get a sorted tickets_Red, in which smaller id player's tickets is
        # before the larger id player
        tickets_blue_sorted = [
            x for _, x in sorted(zip(id_blue, tickets_blue))]
        id_blue_sorted = sorted(id_blue)

        if self.total_tickets2_blue == 0:
            winner_id_blue = random.choice(id_blue)

        else:
            self.winner_ticket_num2_blue = random.choice(
                np.arange(1, self.total_tickets2_blue + 1))

            # I can get the winner_id_blue
            if self.winner_ticket_num2_blue <= tickets_blue_sorted[0]:
                winner_id_blue = id_blue_sorted[0]
            else:
                winner_id_blue = id_blue_sorted[1]

        for i in id_blue:
            p = self.get_player_by_id(i)
            if winner_id_blue == p.id_in_group:
                p.is_winner2_blue = 'Yes'
                p.payoff2 = p.subsession.endowment - p.spend2 + Constants.reward_blue
            else:
                p.is_winner2_blue = 'No'
                p.payoff2 = p.subsession.endowment - p.spend2
        # print(winner_id_blue)
        for p in players:
            p.payoff_twostages = p.payoff1 + p.payoff2

        # the sum of tickets and points
        self.total_points_twostages = self.total_points1_blue + \
            self.total_points1_red + self.total_points2_blue + self.total_points2_red

        self.total_tickets_twostages = self.total_tickets1_blue + \
            self.total_tickets1_red + self.total_tickets2_blue + self.total_tickets2_red


class Player(BasePlayer):
    # In both stages, types and tpp are keep the same
    typo = models.StringField()  # the player's type
    tpp = models.IntegerField()  # tickets per point

    # In Stage1
    spend1 = models.FloatField(
        min=0, label='How many points would you like to spend?')

    def spend1_max(self):
        return self.subsession.endowment

    division1 = models.StringField()

    is_winner1_red = models.StringField()
    is_winner1_blue = models.StringField()
    payoff1 = models.FloatField()

    # In Stage2
    spend2 = models.FloatField(
        min=0, label='How many points would you like to spend?')

    def spend2_max(self):
        return self.subsession.endowment

    division2 = models.StringField()

    is_winner2_red = models.StringField()
    is_winner2_blue = models.StringField()
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
            [1, 'I enjoyed competing in the Blue division per se, not so much for payoff maximization'],
            [2, 'I wanted to experience the joy of winning'],
            [3, 'I wanted to avoid the pain of losing'],
            [4, 'Other, please specify below'],
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
        label="3. How many points is the reward worth in the Blue division?")
    d = models.IntegerField(
        label="4. How many points is the reward worth in the Red division?")
    e = models.IntegerField(
        label='''5. Suppose you purchase 10 lottery tickets and the other
        participant in your division purchases a 40 lottery tickets.
        What is your probability of receiving the reward in percentage terms?
        (Please refer to formula 4)''')
    f = models.IntegerField(
        label='''6. Suppose you purchase 60 lottery tickets and the other
        participant in your division purchases 40 lottery tickets.
        What is your probability of receiving the reward in percentage terms?
        (Please refer to formula 4)''')
    g = models.IntegerField(
        label='''7. Suppose you were in the Blue division and you spent 10 points 
        on lottery tickets and you received the reward. What are your earnings for 
        that stage? (Please refer to formula 1)
        ''')
    h = models.IntegerField(
        label='''8. Suppose you were in the Blue division and you spent 10 points 
        on lottery tickets and you did not received the reward. What are your earnings 
        for that stage? (Please refer to formula 3)
        ''')
    i = models.IntegerField(
        choices=[
            [1, 'Yes'],
            [0, 'No'],
        ],
        label='''9. Suppose you were in the Blue division in stage 1 and you didn't receive
        the reward. Will you move to the Red division in stage 2?''',
        widget=widgets.RadioSelect)
    j = models.IntegerField(
        choices=[
            [1, 'Yes'],
            [0, 'No'],
        ],
        label='''10. Suppose you were in the Red division in stage 1 and you did receive
        the reward. Will you move to the Blue division in stage 2?''',
        widget=widgets.RadioSelect)
