import pandas as pd
import os
import winsound

dir_list = os.listdir('.\output\\')

#     Merge 6,278 ReportDetail7 csv data
for i in range(0, len(dir_list)):
    print(i)
    next = '.\output\\' + dir_list[i] + '\Report_detail.csv'
    if i == 0:
        first = '.\output\\' + dir_list[i] + '\Report_detail.csv'
        second = '.\output\\' + dir_list[i + 1] + '\Report_detail.csv'
        #  merging two csv files
        df = pd.concat(
            map(pd.read_csv, [first, second]), ignore_index=True)
    else:
        df = pd.concat(
            map(pd.read_csv, ['.\csv_files\ReportDetail7.csv', next]), ignore_index=True)
    df.to_csv('.\csv_files\ReportDetail7.csv', index=False)

    #     Merge 6,278 TransactionAnalysisSummaries csv data
for i in range(0, 500):
    print(i)
    next = '.\output\\' + dir_list[i] + '\Transaction_analysis.csv'
    if i == 0:
        first = '.\output\\' + dir_list[i] + '\Transaction_analysis.csv'
        second = '.\output\\' + dir_list[i + 1] + '\Transaction_analysis.csv'
        #  merging two csv files
        df = pd.concat(
            map(pd.read_csv, [first, second]), ignore_index=True)
    else:
        df = pd.concat(
            map(pd.read_csv, ['.\csv_files\TransactionAnalysisSummaries\TransactionAnalysisSummaries.csv', next]), ignore_index=True)
    df.to_csv('.\csv_files\TransactionAnalysisSummaries\TransactionAnalysisSummaries.csv', index=False)

    #     Merge 6,278 TransactionSummaries csv data
for i in range(0, len(dir_list)):
    print(i)
    next = '.\output\\' + dir_list[i] + '\Transaction_summary.csv'
    if i == 0:
        first = '.\output\\' + dir_list[i] + '\Transaction_summary.csv'
        second = '.\output\\' + dir_list[i + 1] + '\Transaction_summary.csv'
        #  merging two csv files
        df = pd.concat(map(pd.read_csv, [first, second]), ignore_index=True)
    else:
        df = pd.concat(
            map(pd.read_csv, ['.\csv_files\TransactionSummaries\TransactionSummaries.csv', next]), ignore_index=True)
    df.to_csv('.\csv_files\TransactionSummaries\TransactionSummaries.csv', index=False)

    #     Merge 6,278 Account_expenses csv data
for i in range(0, len(dir_list)):
    print(i)
    next = '.\output\\' + dir_list[i] + '\Account_expenses.csv'
    if i == 0:
        first = '.\output\\' + dir_list[i] + '\Account_expenses.csv'
        second = '.\output\\' + dir_list[i + 1] + '\Account_expenses.csv'
        #  merging two csv files
        df = pd.concat(map(pd.read_csv, [first, second]), ignore_index=True)
    else:
        df = pd.concat(
                map(pd.read_csv, ['.\csv_files\AccountExpenses\AccountExpenses.csv', next]), ignore_index=True)
    df.to_csv('.\csv_files\AccountExpenses\AccountExpenses.csv', index=False)
