import openpyxl
import os

def main():
    cur_path = os.path.dirname(__file__)
    f_path = os.path.join(cur_path, "..", "advisee_bios.xlsx")
    wb = openpyxl.load_workbook(f_path)
    print(wb.sheetnames)

if __name__ == '__main__':
    main()