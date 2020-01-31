class ScoreCalculator:
    '''
    Class takes responses from the NEO 5 Factor inventory profile
    and returns the NEOAC scores
    '''

    SD, D, N, A, SA = 'SD', 'D', 'N', 'A', 'SA'
    RESPONSE_MAP = {
        1: SD,
        2: D,
        3: N,
        4: A,
        5: SA
    }
    FORWARD_SCORE_ARRAY = {
        SD: 0,
        D: 1,
        N: 2,
        A: 3,
        SA: 4
    }
    BACKWARD_SCORE_ARRAY = {
        SD: 4,
        D: 3,
        N: 2,
        A: 1,
        SA: 0
    }
    BACKWARDS_QUESTIONS = [1, 3, 8, 9, 12, 14, 15, 16, 18, 23, 24, 27, 29, 30, 31, 33, 38, 39, 42, 44, 45, 46, 48, 54, 55, 57, 59]

    def __init__(self, responses):
        self.responses = responses
        self.n_scores = []
        self.e_scores = []
        self.o_scores = []
        self.a_scores = []
        self.c_scores = []


    def calculate_raw_scores():
        '''
        Function calculates N, E, O, A and C scores
        for the NEO 5 Factor inventory profile

        Params:
            responses(Dict): Dict in the form
            {
                question_number: 'SD / D / N / A / SA'
            }
        Response(Dict): Dict with the 5 raw scores for each of the personality traits
        '''

        for question_id, response in self.responses:
            response = RESPONSE_MAP[response]

            if question_id in BACKWARDS_QUESTIONS:
                score = BACKWARD_SCORE_ARRAY[response]
            else:
                score = FORWARD_SCORE_ARRAY[response]

        if question_id % 5 == 1:
            self.n_scores.append(score)
        elif question_id % 5 == 2:
            self.e_scores.append(score)
        elif question_id % 5 == 3:
            self.o_scores.append(score)
        elif question_id % 5 == 4:
            self.a_scores.append(score)
        else:
            self.c_scores.append(score)

        return {
            n: sum(self.n_scores),
            e: sum(self.e_scores),
            o: sum(self.o_scores),
            a: sum(self.a_scores),
            c: sum(self.c_scores)
        }
