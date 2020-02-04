import os
import glob
import csv

from openpyxl import load_workbook

from score_calculator import (
    NEOACScoreCalculator,
    PESScoreCalculator,
    IATScoreCalculator
)

result_path = 'data/Results'
csv_header = [
    'response_id',
    'initials',
    'age',
    'gender',
    'education',
    'occupation',
    'iat_score',
    'pes_score',
    'neoac_score_n',
    'neoac_score_e',
    'neoac_score_o',
    'neoac_score_a',
    'neoac_score_c',
]

def main():
    '''
    Function takes files from the data folder.
    Sends excel files through score_aggregator that
    get all three test scores.

    Prints all the data to an excel file. This function
    is a glue function
    '''
    gender_files = {
        'male': glob.glob('data/Male/*.xlsx', recursive=True),
        'female': glob.glob('data/Female/*.xlsx', recursive=True)
    }


    for gender, files in gender_files.items():
        scores = []
        gender_result_file = open('{}/{}.csv'.format(result_path, gender), 'w')
        gender_csv_writer = csv.writer(gender_result_file)
        gender_csv_writer.writerow(csv_header)

        for score_file in files:
            print('Processing {}'.format(score_file))

            wb = load_workbook(score_file)
            if len(wb.sheetnames) != 3:
                print('Please check file {} for number of tabs'.format(score_file))

            iat_column = list(wb['Sheet1'].columns)[0]
            iat_responses = list(map(lambda x: x.value, iat_column))

            pes_column = list(wb['Sheet2'].columns)[0]
            pes_responses = {idx + 1: value for idx, value in enumerate(list(map(lambda x: x.value, pes_column)))}

            neoac_column = list(wb['Sheet3'].columns)[0]
            neoac_responses = {idx + 1: value for idx, value in enumerate(list(map(lambda x: x.value, neoac_column)))}

            if (len(iat_column) != 20 or len(pes_column) != 9 or len(neoac_column) != 60):
                print('Please check file {} for survey scores'.format(score_file))
                next

            response_id, initials, age, education, occupation = os.path.basename(score_file).split('.')[0].split('_')[:5]

            iat_score = IATScoreCalculator(iat_responses).calculate_scores()
            pes_score = PESScoreCalculator(pes_responses).calculate_scores()
            neoac_score = NEOACScoreCalculator(neoac_responses, gender).calculate_scores()

            csv_row = [
                response_id,
                initials,
                age,
                gender,
                education,
                occupation,
                iat_score,
                pes_score,
                neoac_score['n'],
                neoac_score['e'],
                neoac_score['o'],
                neoac_score['a'],
                neoac_score['c'],
            ]

            gender_csv_writer.writerow(csv_row)

        gender_result_file.close()


if __name__ == '__main__':
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    main()



## Output of csv has to be in the form
# ID, Initials, Age, Gender, N, E, O, A, C, PES, IAT
