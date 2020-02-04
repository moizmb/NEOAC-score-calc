import json

class NEOACScoreCalculator:
    '''
    Class takes responses from the NEO 5 Factor inventory profile
    and returns the NEOAC scores
    Test No. 3
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
    BACKWARDS_QUESTIONS = [
        1, 3, 8, 9, 12,
        14, 15, 16, 18,
        23, 24, 27, 29,
        30, 31, 33, 38,
        39, 42, 44, 45,
        46, 48, 54, 55,
        57, 59
    ]
    RAW_TO_T_CONVERTER = json.load(open('./conversion/neo_raw_to_t.json', 'r'))

    def __init__(self, responses, gender):
        '''
        Function calculates N, E, O, A and C scores
        for the NEO 5 Factor inventory profile

        Params:
            responses(Dict): Dict in the form
            {
                question_number: 'SD / D / N / A / SA'
            }
            gender(Str): 'male', 'female' or 'combined'
        Response(Dict): Dict with the 5 T scores for each of the personality traits
        '''

        self.responses = responses
        self.gender = gender
        self.scores = {
            'n': [],
            'e': [],
            'o': [],
            'a': [],
            'c': []
        }

    def calculate_scores(self):
        '''
        Function calculates N, E, O, A and C scores
        for the NEO 5 Factor inventory profile

        '''

        for question_id, response in self.responses.items():
            response = self.__class__.RESPONSE_MAP[response]

            if question_id in self.__class__.BACKWARDS_QUESTIONS:
                score = self.__class__.BACKWARD_SCORE_ARRAY[response]
            else:
                score = self.__class__.FORWARD_SCORE_ARRAY[response]

            if question_id % 5 == 1:
                self.scores['n'].append(score)
            elif question_id % 5 == 2:
                self.scores['e'].append(score)
            elif question_id % 5 == 3:
                self.scores['o'].append(score)
            elif question_id % 5 == 4:
                self.scores['a'].append(score)
            else:
                self.scores['c'].append(score)

        return self.raw_to_t({
            'n': sum(self.scores['n']),
            'e': sum(self.scores['e']),
            'o': sum(self.scores['o']),
            'a': sum(self.scores['a']),
            'c': sum(self.scores['c'])
        })

    def raw_to_t(self, raw_scores):
        t_scores = {
            'n': None,
            'e': None,
            'o': None,
            'a': None,
            'c': None
        }
        gender_converter = self.__class__.RAW_TO_T_CONVERTER[self.gender]
        for trait, score in raw_scores.items():
            converted_score = gender_converter[trait].get(str(score), None)
            if converted_score:
                t_scores[trait] = converted_score
            elif score > int(gender_converter[trait]['max']):
                t_scores[trait] = gender_converter[trait][gender_converter[trait]['max']]
            elif score < int(gender_converter[trait]['min']):
                t_scores[trait] = gender_converter[trait][gender_converter[trait]['min']]

        return t_scores

class PESScoreCalculator:
    '''
    Class calculates psychological entitlement scale
    scores from responses
    Test No. 2
    '''

    FORWARD_SCORE_ARRAY = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7
    }

    BACKWARD_SCORE_ARRAY = {
        1: 7,
        2: 6,
        3: 5,
        4: 4,
        5: 3,
        6: 2,
        7: 1
    }

    BACKWARDS_QUESTIONS = [5]

    def __init__(self, responses):
        # responses takes a dict in the form {question_code: response}
        self.responses = responses

    def calculate_scores(self):
        scores = []
        for question_code, response in self.responses.items():
            if question_code in self.__class__.BACKWARDS_QUESTIONS:
                score = self.__class__.BACKWARD_SCORE_ARRAY[response]
            else:
                score = self.__class__.FORWARD_SCORE_ARRAY[response]
            scores.append(score)

        return sum(scores)


class IATScoreCalculator:
    '''
    Calculates scores for the Internet Addition Test
    Test No. 1
    '''

    def __init__(self, responses):
        # responses takes a list
        self.responses = responses

    def calculate_scores(self):
        return sum(list(self.responses))
