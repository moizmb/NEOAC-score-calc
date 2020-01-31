import glob

from openpyxl import load_workbook

def main():
    response_files = glob.glob('./data/responses/*.xlsx')

    for response_file in response_files:
        wb = load_workbook(response_file)



if __name__ == '__main__':
    main()
