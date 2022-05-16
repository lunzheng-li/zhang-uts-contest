from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    # timeout_seconds = 1200

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

        tab_tickets_total_blue = tab_tickets1 + tab_tickets2
        tab_tickets_total_red = tab_tickets3 + tab_tickets4
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
            tab_tickets_total_blue=tab_tickets_total_blue,
            tab_tickets_total_red=tab_tickets_total_red,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}',
        )


class Question1to4(Page):
    form_model = 'player'
    form_fields = ['b', 'c', 'd']

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

        tab_tickets_total_blue = tab_tickets1 + tab_tickets2
        tab_tickets_total_red = tab_tickets3 + tab_tickets4

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
            tab_tickets_total_blue=tab_tickets_total_blue,
            tab_tickets_total_red=tab_tickets_total_red,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}',

            fields=fields,
            show_solutions=False,
        )


class Result1to4(Page):
    form_model = 'player'
    form_fields = ['b', 'c', 'd']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        fields = self.subsession.get_quiz_data()[0:3]

        # we add an extra key 'is_correct' to each field
        answers = [self.player.b, self.player.c, self.player.d]
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

        tab_tickets_total_blue = tab_tickets1 + tab_tickets2
        tab_tickets_total_red = tab_tickets3 + tab_tickets4

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
            tab_tickets_total_blue=tab_tickets_total_blue,
            tab_tickets_total_red=tab_tickets_total_red,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}',

            fields=fields,
            show_solutions=False,
        )


class Result_e(Page):
    # form_model = 'player'
    # form_fields = ['e']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        fields = self.subsession.get_quiz_data()[3:4]

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

        tab_tickets_total_blue = tab_tickets1 + tab_tickets2
        tab_tickets_total_red = tab_tickets3 + tab_tickets4

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
            tab_tickets_total_blue=tab_tickets_total_blue,
            tab_tickets_total_red=tab_tickets_total_red,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}',

            fields=fields,
            show_solutions=False,
        )


class Result_f(Page):
    # form_model = 'player'
    # form_fields = ['f']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        fields = self.subsession.get_quiz_data()[4:5]

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

        tab_tickets_total_blue = tab_tickets1 + tab_tickets2
        tab_tickets_total_red = tab_tickets3 + tab_tickets4

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
            tab_tickets_total_blue=tab_tickets_total_blue,
            tab_tickets_total_red=tab_tickets_total_red,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}',

            fields=fields,
            show_solutions=False,
        )


class Result_g(Page):
    form_model = 'player'
    form_fields = ['g']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        fields = self.subsession.get_quiz_data()[5:6]

        # we add an extra key 'is_correct' to each field
        answers = [self.player.g]
        i = 0
        for d in fields:
            print(d['name'])
            # name = d['name']
            d['is_correct'] = answers[i] == d['solution']
            i += 1
        return dict(fields=fields, show_solutions=True)


class Question_h(Page):
    form_model = 'player'
    form_fields = ['h']

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

        tab_tickets_total_blue = tab_tickets1 + tab_tickets2
        tab_tickets_total_red = tab_tickets3 + tab_tickets4

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
            tab_tickets_total_blue=tab_tickets_total_blue,
            tab_tickets_total_red=tab_tickets_total_red,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}',

            fields=fields,
            show_solutions=False,
        )


class Result_h(Page):
    form_model = 'player'
    form_fields = ['h']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        fields = self.subsession.get_quiz_data()[6:7]

        # we add an extra key 'is_correct' to each field
        answers = [self.player.h]
        i = 0
        for d in fields:
            print(d['name'])
            # name = d['name']
            d['is_correct'] = answers[i] == d['solution']
            i += 1
        return dict(fields=fields, show_solutions=True)


class Question_i(Page):
    form_model = 'player'
    form_fields = ['i']

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

        tab_tickets_total_blue = tab_tickets1 + tab_tickets2
        tab_tickets_total_red = tab_tickets3 + tab_tickets4

        fields = self.subsession.get_quiz_data()[7:8]
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
            tab_tickets_total_blue=tab_tickets_total_blue,
            tab_tickets_total_red=tab_tickets_total_red,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}',

            fields=fields,
            show_solutions=False,
        )


class Result_i(Page):
    form_model = 'player'
    form_fields = ['i']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        fields = self.subsession.get_quiz_data()[7:8]

        # we add an extra key 'is_correct' to each field
        answers = [self.player.i]
        i = 0
        for d in fields:
            print(d['name'])
            # name = d['name']
            d['is_correct'] = answers[i] == d['solution']
            i += 1
        return dict(fields=fields, show_solutions=True)


class Question_j(Page):
    form_model = 'player'
    form_fields = ['j']

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

        tab_tickets_total_blue = tab_tickets1 + tab_tickets2
        tab_tickets_total_red = tab_tickets3 + tab_tickets4

        fields = self.subsession.get_quiz_data()[8:9]
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
            tab_tickets_total_blue=tab_tickets_total_blue,
            tab_tickets_total_red=tab_tickets_total_red,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}',

            fields=fields,
            show_solutions=False,
        )


class Result_j(Page):
    form_model = 'player'
    form_fields = ['j']

    def is_displayed(self):
        return self.player.round_number == 1

    def vars_for_template(self):
        fields = self.subsession.get_quiz_data()[8:9]

        # we add an extra key 'is_correct' to each field
        answers = [self.player.j]
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

    def error_message(self, values):
        # print('values is', values)
        if (values['spend1'] % 0.5) != 0:
            return 'Please enter a number which is a mulitplier of 0.5!'

    def vars_for_template(self):
        other_players = self.player.get_others_in_group()
        for p in other_players:
            if p.division1 == self.player.division1:
                other_id = p.id_in_group

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

        tab_tickets_total_blue = tab_tickets1 + tab_tickets2
        tab_tickets_total_red = tab_tickets3 + tab_tickets4
        return dict(
            other_id=other_id,

            exchange_rate=exchange_rate,
            endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total_blue=tab_tickets_total_blue,
            tab_tickets_total_red=tab_tickets_total_red,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}',
        )


class Stage1Wait(WaitPage):
    after_all_players_arrive = 'set_payoffs1'
    pass


class Outcome1(Page):
    def js_vars(self):
        players = self.group.get_players()

        tickets_red = [i.spend1 *
                       i.tpp for i in players if i.division1 == 'Red']
        total_tickets_red = [sum(tickets_red)] * 2
        if sum(tickets_red) != 0:
            float1_red_lst = [i / sum(tickets_red) for i in tickets_red]
        else:
            float1_red_lst = [1 / 2, 1 / 2]

        tickets_blue = [i.spend1 *
                        i.tpp for i in players if i.division1 == 'Blue']
        total_tickets_blue = [sum(tickets_blue)] * 2
        if sum(tickets_blue) != 0:
            float1_blue_lst = [i / sum(tickets_blue) for i in tickets_blue]
        else:
            float1_blue_lst = [1 / 2, 1 / 2]

        id_red = [i.id_in_group for i in players if i.division1 == 'Red']
        id_blue = [i.id_in_group for i in players if i.division1 == 'Blue']

        float1_lst = [x for _, x in sorted(
            zip(id_red + id_blue, float1_red_lst + float1_blue_lst))]
        tickets = [x for _, x in sorted(
            zip(id_red + id_blue, tickets_red + tickets_blue))]
        total_tickets = [x for _, x in sorted(
            zip(id_red + id_blue, total_tickets_red + total_tickets_blue))]
        # do the same as the pooled, and {% if division == %} in the template
        tickets_red_sorted = [x for _, x in sorted(zip(id_red, tickets_red))]
        id_red_sorted = sorted(id_red)

        tickets_blue_sorted = [
            x for _, x in sorted(zip(id_blue, tickets_blue))]
        id_blue_sorted = sorted(id_blue)

        return dict(
            id_lst=[i.id_in_group for i in players],
            typo1_lst=[i.typo for i in players],
            spend1_lst=[i.spend1 for i in players],
            tickets1_lst=tickets,
            total_tickets=total_tickets,
            prob1_lst=[f'{i*100:.2f}%' for i in float1_lst],
            your_id=self.player.id_in_group,

            division1_lst=[i.division1 for i in players],
            tickets_red_sorted=tickets_red_sorted,
            id_red_sorted=id_red_sorted,
            tickets_blue_sorted=tickets_blue_sorted,
            id_blue_sorted=id_blue_sorted,
        )

    def vars_for_template(self):
        your_tickets = f'{self.player.tpp * self.player.spend1:.0f}'
        endowment = self.session.config['endowment']
        total_int_red = f'{self.group.total_tickets1_red:.0f}'
        total_int_blue = f'{self.group.total_tickets1_blue:.0f}'

        # some more vars in instruction
        exchange_rate = self.session.config['exchange_rate']
        # endowment = self.session.config['endowment']

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

        tab_tickets_total_blue = tab_tickets1 + tab_tickets2
        tab_tickets_total_red = tab_tickets3 + tab_tickets4

        fields = self.subsession.get_quiz_data()[9:10]
        return dict(
            endowment=endowment,
            your_tickets=your_tickets,
            total_int_red=total_int_red,
            total_int_blue=total_int_blue,

            exchange_rate=exchange_rate,
            # endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total_blue=tab_tickets_total_blue,
            tab_tickets_total_red=tab_tickets_total_red,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}',
        )


class Stage2(Page):
    form_model = 'player'
    form_fields = ['spend2']

    def vars_for_template(self):
        other_players = self.player.get_others_in_group()
        for p in other_players:
            if p.division2 == self.player.division2:
                other_id = p.id_in_group
                other_typo = p.typo
                other_tpp = p.tpp

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

        tab_tickets_total_blue = tab_tickets1 + tab_tickets2
        tab_tickets_total_red = tab_tickets3 + tab_tickets4
        return dict(
            other_id=other_id,
            other_typo=other_typo,
            other_tpp=other_tpp,

            exchange_rate=exchange_rate,
            endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total_blue=tab_tickets_total_blue,
            tab_tickets_total_red=tab_tickets_total_red,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}',
        )

    def error_message(self, values):
        # print('values is', values)
        if (values['spend2'] % 0.5) != 0:
            return 'Please enter a number which is a mulitplier of 0.5!'


class Stage2Wait(WaitPage):
    after_all_players_arrive = 'set_payoffs2'
    pass


class Outcome2(Page):
    def js_vars(self):
        players = self.group.get_players()

        tickets_red = [i.spend2 *
                       i.tpp for i in players if i.division2 == 'Red']
        total_tickets_red = [sum(tickets_red)] * 2
        if sum(tickets_red) != 0:
            float2_red_lst = [i / sum(tickets_red) for i in tickets_red]
        else:
            float2_red_lst = [1 / 2, 1 / 2]

        tickets_blue = [i.spend2 *
                        i.tpp for i in players if i.division2 == 'Blue']
        total_tickets_blue = [sum(tickets_blue)] * 2
        if sum(tickets_blue) != 0:
            float2_blue_lst = [i / sum(tickets_blue) for i in tickets_blue]
        else:
            float2_blue_lst = [1 / 2, 1 / 2]

        id_red = [i.id_in_group for i in players if i.division2 == 'Red']
        id_blue = [i.id_in_group for i in players if i.division2 == 'Blue']

        float2_lst = [x for _, x in sorted(
            zip(id_red + id_blue, float2_red_lst + float2_blue_lst))]
        tickets = [x for _, x in sorted(
            zip(id_red + id_blue, tickets_red + tickets_blue))]
        total_tickets = [x for _, x in sorted(
            zip(id_red + id_blue, total_tickets_red + total_tickets_blue))]
        # do the same as the pooled, and {% if division == %} in the template
        tickets_red_sorted = [x for _, x in sorted(zip(id_red, tickets_red))]
        id_red_sorted = sorted(id_red)

        tickets_blue_sorted = [
            x for _, x in sorted(zip(id_blue, tickets_blue))]
        id_blue_sorted = sorted(id_blue)

        return dict(
            id_lst=[i.id_in_group for i in players],
            typo2_lst=[i.typo for i in players],
            spend2_lst=[i.spend2 for i in players],
            tickets2_lst=tickets,
            total_tickets=total_tickets,
            prob2_lst=[f'{i*100:.2f}%' for i in float2_lst],
            your_id=self.player.id_in_group,

            division2_lst=[i.division2 for i in players],
            tickets_red_sorted=tickets_red_sorted,
            id_red_sorted=id_red_sorted,
            tickets_blue_sorted=tickets_blue_sorted,
            id_blue_sorted=id_blue_sorted,
        )

    def vars_for_template(self):
        your_tickets = f'{self.player.tpp * self.player.spend2:.0f}'
        endowment = self.session.config['endowment']
        total_int_red = f'{self.group.total_tickets2_red:.0f}'
        total_int_blue = f'{self.group.total_tickets2_blue:.0f}'
        # some more vars in instruction
        exchange_rate = self.session.config['exchange_rate']
        # endowment = self.session.config['endowment']

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

        tab_tickets_total_blue = tab_tickets1 + tab_tickets2
        tab_tickets_total_red = tab_tickets3 + tab_tickets4
        return dict(
            endowment=endowment,
            your_tickets=your_tickets,
            total_int_red=total_int_red,
            total_int_blue=total_int_blue,

            exchange_rate=exchange_rate,
            # endowment=endowment,

            tpp_A=tpp_A,
            tpp_B=tpp_B,
            num_of_participant=num_of_participant,
            tab_tickets1=tab_tickets1,
            tab_tickets2=tab_tickets2,
            tab_tickets3=tab_tickets3,
            tab_tickets4=tab_tickets4,
            tab_tickets_total_blue=tab_tickets_total_blue,
            tab_tickets_total_red=tab_tickets_total_red,
            tab_prob1=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}%',
            tab_prob2=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}%',
            tab_prob3=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}%',
            tab_prob4=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}%',
            tab_prob1_100=f'{tab_tickets1 / tab_tickets_total_blue*100:.2f}',
            tab_prob2_100=f'{tab_tickets2 / tab_tickets_total_blue*100:.2f}',
            tab_prob3_100=f'{tab_tickets3 / tab_tickets_total_red*100:.2f}',
            tab_prob4_100=f'{tab_tickets4 / tab_tickets_total_red*100:.2f}',
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
        if (values['motivation'] == 4):
            if not (values['mot_openend']):
                return 'Please specify your motivation!'


page_sequence = [
    Instructions,
    Question1to4,
    Result1to4,
    Question_e,
    Result_e,
    Question_f,
    Result_f,
    Question_g,
    Result_g,
    Question_h,
    Result_h,
    Question_i,
    Result_i,
    Question_j,
    Result_j,
    Stage1,
    Stage1Wait,
    Outcome1,
    Stage2,
    Stage2Wait,
    Outcome2,
    End_main,
    Questionnaire,
]
