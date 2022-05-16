from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        # some more vars in instruction
        exchange_rate = self.session.config['exchange_rate']
        endowment = self.session.config['endowment']

        # num_of_participant seems exists in session
        num_of_participant = Constants.players_per_group * \
            len(self.subsession.get_groups())
        # print(num_of_participant)
        tpp_A = self.session.config['tickets_per_point_A']
        tpp_B = self.session.config['tickets_per_point_B']
        # The following are all vars in the example table
        tab_tickets1 = tpp_A * 15
        tab_tickets2 = tpp_A * 5
        tab_tickets3 = tpp_B * 4
        tab_tickets4 = tpp_B * 4

        tab_tickets_total = tab_tickets1 + tab_tickets2 + tab_tickets3 + tab_tickets4
        return dict(
            exchange_rate=exchange_rate,
            endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total=tab_tickets_total,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total*100:.2f}',
        )


class Question1to3(Page):
    form_model = 'player'
    form_fields = ['a', 'b', 'c', ]

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        # some more vars in instruction
        exchange_rate = self.session.config['exchange_rate']
        endowment = self.session.config['endowment']

        # num_of_participant seems exists in session
        num_of_participant = Constants.players_per_group * \
            len(self.subsession.get_groups())
        # print(num_of_participant)
        tpp_A = self.session.config['tickets_per_point_A']
        tpp_B = self.session.config['tickets_per_point_B']
        # The following are all vars in the example table
        tab_tickets1 = tpp_A * 15
        tab_tickets2 = tpp_A * 5
        tab_tickets3 = tpp_B * 4
        tab_tickets4 = tpp_B * 4

        tab_tickets_total = tab_tickets1 + tab_tickets2 + tab_tickets3 + tab_tickets4

        # for some reason, [::3] is not working, of course! it's wrong
        # it should be [:3], need learn more about list slicing.
        fields = self.subsession.get_quiz_data()[0:3]
        return dict(
            exchange_rate=exchange_rate,
            endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total=tab_tickets_total,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total*100:.2f}',
            fields=fields,
            show_solutions=False,
        )


class Result1to3(Page):
    form_model = 'player'
    form_fields = ['a', 'b', 'c', ]

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        fields = self.subsession.get_quiz_data()[0:3]

        # we add an extra key 'is_correct' to each field
        answers = [self.player.a, self.player.b, self.player.c, ]
        i = 0
        for d in fields:
            print(d['name'])
            # name = d['name']
            d['is_correct'] = answers[i] == d['solution']
            i += 1
        return dict(fields=fields, show_solutions=True)


class Question_d(Page):
    form_model = 'player'
    form_fields = ['d']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        # some more vars in instruction
        exchange_rate = self.session.config['exchange_rate']
        endowment = self.session.config['endowment']

        # num_of_participant seems exists in session
        num_of_participant = Constants.players_per_group * \
            len(self.subsession.get_groups())
        # print(num_of_participant)
        tpp_A = self.session.config['tickets_per_point_A']
        tpp_B = self.session.config['tickets_per_point_B']
        # The following are all vars in the example table
        tab_tickets1 = tpp_A * 15
        tab_tickets2 = tpp_A * 5
        tab_tickets3 = tpp_B * 4
        tab_tickets4 = tpp_B * 4

        tab_tickets_total = tab_tickets1 + tab_tickets2 + tab_tickets3 + tab_tickets4

        fields = self.subsession.get_quiz_data()[3:4]
        return dict(
            exchange_rate=exchange_rate,
            endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total=tab_tickets_total,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total*100:.2f}',
            fields=fields, show_solutions=False
        )


class Result_d(Page):
    # form_model = 'player'
    # form_fields = ['d']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        fields = self.subsession.get_quiz_data()[3:4]
        # we add an extra key 'is_correct' to each field
        answers = [self.player.d]
        i = 0
        for d in fields:
            print(d['name'])
            # name = d['name']
            d['is_correct'] = answers[i] == d['solution']
            i += 1
        return dict(fields=fields, show_solutions=True)


class Question_e(Page):
    form_model = 'player'
    form_fields = ['e']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        # some more vars in instruction
        exchange_rate = self.session.config['exchange_rate']
        endowment = self.session.config['endowment']

        # num_of_participant seems exists in session
        num_of_participant = Constants.players_per_group * \
            len(self.subsession.get_groups())
        # print(num_of_participant)
        tpp_A = self.session.config['tickets_per_point_A']
        tpp_B = self.session.config['tickets_per_point_B']
        # The following are all vars in the example table
        tab_tickets1 = tpp_A * 15
        tab_tickets2 = tpp_A * 5
        tab_tickets3 = tpp_B * 4
        tab_tickets4 = tpp_B * 4

        tab_tickets_total = tab_tickets1 + tab_tickets2 + tab_tickets3 + tab_tickets4

        fields = self.subsession.get_quiz_data()[4:5]
        return dict(
            exchange_rate=exchange_rate,
            endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total=tab_tickets_total,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total*100:.2f}',
            fields=fields, show_solutions=False
        )


class Result_e(Page):
    # form_model = 'player'
    # form_fields = ['e']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        fields = self.subsession.get_quiz_data()[4:5]
        # we add an extra key 'is_correct' to each field
        answers = [self.player.e]
        i = 0
        for d in fields:
            print(d['name'])
            # name = d['name']
            d['is_correct'] = answers[i] == d['solution']
            i += 1
        return dict(fields=fields, show_solutions=True)


class Question_f(Page):
    form_model = 'player'
    form_fields = ['f']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        # some more vars in instruction
        exchange_rate = self.session.config['exchange_rate']
        endowment = self.session.config['endowment']

        # num_of_participant seems exists in session
        num_of_participant = Constants.players_per_group * \
            len(self.subsession.get_groups())
        # print(num_of_participant)
        tpp_A = self.session.config['tickets_per_point_A']
        tpp_B = self.session.config['tickets_per_point_B']
        # The following are all vars in the example table
        tab_tickets1 = tpp_A * 15
        tab_tickets2 = tpp_A * 5
        tab_tickets3 = tpp_B * 4
        tab_tickets4 = tpp_B * 4

        tab_tickets_total = tab_tickets1 + tab_tickets2 + tab_tickets3 + tab_tickets4

        fields = self.subsession.get_quiz_data()[5:6]
        return dict(
            exchange_rate=exchange_rate,
            endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total=tab_tickets_total,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total*100:.2f}',
            fields=fields, show_solutions=False
        )


class Result_f(Page):
    form_model = 'player'
    form_fields = ['f']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        fields = self.subsession.get_quiz_data()[5:6]
        # we add an extra key 'is_correct' to each field
        answers = [self.player.f]
        i = 0
        for d in fields:
            print(d['name'])
            # name = d['name']
            d['is_correct'] = answers[i] == d['solution']
            i += 1
        return dict(fields=fields, show_solutions=True)


class Question_g(Page):
    form_model = 'player'
    form_fields = ['g']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        # some more vars in instruction
        exchange_rate = self.session.config['exchange_rate']
        endowment = self.session.config['endowment']

        # num_of_participant seems exists in session
        num_of_participant = Constants.players_per_group * \
            len(self.subsession.get_groups())
        # print(num_of_participant)
        tpp_A = self.session.config['tickets_per_point_A']
        tpp_B = self.session.config['tickets_per_point_B']
        # The following are all vars in the example table
        tab_tickets1 = tpp_A * 15
        tab_tickets2 = tpp_A * 5
        tab_tickets3 = tpp_B * 4
        tab_tickets4 = tpp_B * 4

        tab_tickets_total = tab_tickets1 + tab_tickets2 + tab_tickets3 + tab_tickets4

        fields = self.subsession.get_quiz_data()[6:7]
        return dict(
            exchange_rate=exchange_rate,
            endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total=tab_tickets_total,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total*100:.2f}',
            fields=fields, show_solutions=False
        )


class Result_g(Page):
    form_model = 'player'
    form_fields = ['g']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        fields = self.subsession.get_quiz_data()[6:7]
        # we add an extra key 'is_correct' to each field
        answers = [self.player.g]
        i = 0
        for d in fields:
            print(d['name'])
            # name = d['name']
            d['is_correct'] = answers[i] == d['solution']
            i += 1
        return dict(fields=fields, show_solutions=True)


class Stage1(Page):
    form_model = 'player'
    form_fields = ['spend1']

    def js_vars(self):
        # other_players = self.player.get_others_in_group()
        players = self.group.get_players()

        return dict(
            id_lst=[i.id_in_group for i in players],
            typo1_lst=[i.typo for i in players],
            tpp1_lst=[i.tpp for i in players],
            your_id=self.player.id_in_group,
        )
    # points are integers in oTree

    def error_message(self, values):
        # print('values is', values)
        if (values['spend1'] % 0.5) != 0:
            return 'Please enter a number which is a mulitplier of 0.5!'

    def vars_for_template(self):
        # some more vars in instruction
        exchange_rate = self.session.config['exchange_rate']
        endowment = self.session.config['endowment']

        # num_of_participant seems exists in session
        num_of_participant = Constants.players_per_group * \
            len(self.subsession.get_groups())
        tpp_A = self.session.config['tickets_per_point_A']
        tpp_B = self.session.config['tickets_per_point_B']
        # The following are all vars in the example table
        tab_tickets1 = tpp_A * 15
        tab_tickets2 = tpp_A * 5
        tab_tickets3 = tpp_B * 4
        tab_tickets4 = tpp_B * 4

        tab_tickets_total = tab_tickets1 + tab_tickets2 + tab_tickets3 + tab_tickets4
        return dict(
            exchange_rate=exchange_rate,
            endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total=tab_tickets_total,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total*100:.2f}',
        )
    pass


class Stage1Wait(WaitPage):
    after_all_players_arrive = 'set_payoffs1'
    pass


class Outcome1(Page):
    def js_vars(self):
        players = self.group.get_players()
        tickets = [i.spend1 * i.tpp for i in players]
        if sum(tickets) != 0:
            float1_lst = [i / sum(tickets) for i in tickets]
            # print('Outcome1')
            # print(tickets)
            # print([i.id_in_group for i in players])
            # print([i.spend1 for i in players])
            # print(sum(tickets))
            # print([i / sum(tickets) for i in tickets])
            return dict(
                id_lst=[i.id_in_group for i in players],
                typo1_lst=[i.typo for i in players],
                spend1_lst=[i.spend1 for i in players],
                tickets1_lst=tickets,
                total_tickets=sum(tickets),
                prob1_lst=[f'{i*100:.2f}%' for i in float1_lst],
                your_id=self.player.id_in_group,
            )

    def vars_for_template(self):
        # some more vars in instruction
        exchange_rate = self.session.config['exchange_rate']
        endowment = self.session.config['endowment']

        # num_of_participant seems exists in session
        num_of_participant = Constants.players_per_group * \
            len(self.subsession.get_groups())
        tpp_A = self.session.config['tickets_per_point_A']
        tpp_B = self.session.config['tickets_per_point_B']
        # The following are all vars in the example table
        tab_tickets1 = tpp_A * 15
        tab_tickets2 = tpp_A * 5
        tab_tickets3 = tpp_B * 4
        tab_tickets4 = tpp_B * 4

        tab_tickets_total = tab_tickets1 + tab_tickets2 + tab_tickets3 + tab_tickets4
        return dict(
            exchange_rate=exchange_rate,
            endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total=tab_tickets_total,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total*100:.2f}',
        )
    pass


class Stage2(Page):
    form_model = 'player'
    form_fields = ['spend2']

    def js_vars(self):
        # other_players = self.player.get_others_in_group()
        players = self.group.get_players()

        return dict(
            id_lst=[i.id_in_group for i in players],
            typo2_lst=[i.typo for i in players],
            tpp2_lst=[i.tpp for i in players],
            your_id=self.player.id_in_group,
        )
    # points are integers in oTree

    def error_message(self, values):
        # print('values is', values)
        if (values['spend2'] % 0.5) != 0:
            return 'Please enter a number which is a mulitplier of 0.5!'

    def vars_for_template(self):
        # some more vars in instruction
        exchange_rate = self.session.config['exchange_rate']
        endowment = self.session.config['endowment']

        # num_of_participant seems exists in session
        num_of_participant = Constants.players_per_group * \
            len(self.subsession.get_groups())
        tpp_A = self.session.config['tickets_per_point_A']
        tpp_B = self.session.config['tickets_per_point_B']
        # The following are all vars in the example table
        tab_tickets1 = tpp_A * 15
        tab_tickets2 = tpp_A * 5
        tab_tickets3 = tpp_B * 4
        tab_tickets4 = tpp_B * 4

        tab_tickets_total = tab_tickets1 + tab_tickets2 + tab_tickets3 + tab_tickets4
        return dict(
            exchange_rate=exchange_rate,
            endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total=tab_tickets_total,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total*100:.2f}',
        )


class Stage2Wait(WaitPage):
    after_all_players_arrive = 'set_payoffs2'
    pass


class Outcome2(Page):
    def js_vars(self):
        players = self.group.get_players()
        tickets = [i.spend2 * i.tpp for i in players]
        if sum(tickets) != 0:
            float2_lst = [i / sum(tickets) for i in tickets]
            # print('Outcome2')
            # print(tickets)
            # print([i.id_in_group for i in players])
            # print([i.spend2 for i in players])
            # print(sum(tickets))
            # print([i / sum(tickets) for i in tickets])
            return dict(
                id_lst=[i.id_in_group for i in players],
                typo2_lst=[i.typo for i in players],
                spend2_lst=[i.spend2 for i in players],
                tickets2_lst=tickets,
                total_tickets=sum(tickets),
                prob2_lst=[f'{i*100:.2f}%' for i in float2_lst],
                your_id=self.player.id_in_group,
            )

    def vars_for_template(self):
        # some more vars in instruction
        exchange_rate = self.session.config['exchange_rate']
        endowment = self.session.config['endowment']

        # num_of_participant seems exists in session
        num_of_participant = Constants.players_per_group * \
            len(self.subsession.get_groups())
        tpp_A = self.session.config['tickets_per_point_A']
        tpp_B = self.session.config['tickets_per_point_B']
        # The following are all vars in the example table
        tab_tickets1 = tpp_A * 15
        tab_tickets2 = tpp_A * 5
        tab_tickets3 = tpp_B * 4
        tab_tickets4 = tpp_B * 4

        tab_tickets_total = tab_tickets1 + tab_tickets2 + tab_tickets3 + tab_tickets4
        return dict(
            exchange_rate=exchange_rate,
            endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total=tab_tickets_total,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total*100:.2f}',
        )

    def before_next_page(self):
        if self.player.round_number == Constants.num_rounds:
            player = self.player
            player.set_final_payoffs()


class End_main(Page):
    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds

    def vars_for_template(self):
        payoff_in_AUD = self.player.participant.vars['payoff_in_AUD']
        paying_real_round = self.player.paying_round - Constants.num_trial_rounds
        return dict(
            paying_real_round=paying_real_round,
            payoff_in_AUD=payoff_in_AUD
        )


class Questionnaire(Page):
    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds
    form_model = 'player'
    form_fields = ['age', 'gender', 'ethnicity',
                   'major', 'risk', 'motivation', 'mot_openend']

    def error_message(self, values):
        # print('values is', values)
        if (values['motivation'] == 3):
            if not (values['mot_openend']):
                return 'Please specify your motivation!'


page_sequence = [
    Instructions,
    Question1to3,
    Result1to3,
    Question_d,
    Result_d,
    Question_e,
    Result_e,
    Question_f,
    Result_f,
    Question_g,
    Result_g,
    Stage1,
    Stage1Wait,
    Outcome1,
    Stage2,
    Stage2Wait,
    Outcome2,
    End_main,
    Questionnaire,
]
