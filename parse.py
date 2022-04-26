from bs4 import BeautifulSoup
import pandas as pd
import winsound
import os

# Get the list of all files and directories
path = "./XML data/03302022/"
dir_list = os.listdir(path)

print("dir_list",dir_list)

# prints all files
# len(dir_list)
for i in range(0,len(dir_list)):
    print(i)
    full_path = os.path.join(path, 'dir_list[i]')
    outdir = '.\output\\' + (dir_list[i]).removesuffix('.txt')

    if not os.path.exists(outdir):
        os.mkdir(outdir)
    with open(full_path, 'r') as f:
        data = f.read().encode()
        Bs_data = BeautifulSoup(data, "xml")
        b_unique = Bs_data.find_all('ReportDetail7')
        # ReportDetail7
        ReportDetail7 = []
        for i in range(0, 2):
            rows = [
                b_unique[i].CustomerIdentifier.get_text(),
                int(i + 1),
                b_unique[i].RequestCode.get_text(),
                b_unique[i].EmailAddress.get_text(),
                b_unique[i].InstitutionName.get_text(),
                b_unique[i].AccountName.get_text(),
                b_unique[i].RoutingNumberEntered.get_text(),
                b_unique[i].RoutingNumberReturned.get_text(),
                b_unique[i].AccountType.get_text(),
                b_unique[i].AccountNumberEntered.get_text(),
                b_unique[i].AccountNumberFound.get_text(),
                b_unique[i].AccountNumberConfidence.get_text(),
                b_unique[i].NameEntered.get_text(),
                b_unique[i].NameFound.get_text(),
                b_unique[i].NameConfidence.get_text(),
                b_unique[i].AmountInput.get_text(),
                b_unique[i].AvailableBalance.get_text(),
                b_unique[i].AverageBalance.get_text(),
                b_unique[i].AverageBalanceRecent.get_text(),
                b_unique[i].IsLoginValid.get_text(),
                b_unique[i].IsVerified.get_text(),
                b_unique[i].AsOfDate.get_text(),
                b_unique[i].ActivityStartDate.get_text(),
                b_unique[i].ActivityEndDate.get_text(),
                b_unique[i].TotalCredits.get_text(),
                b_unique[i].TotalDebits.get_text(),
                b_unique[i].CurrentBalance.get_text(),
                b_unique[i].IsActivityAvailable.get_text(),
                b_unique[i].ProcessedStatus.get_text(),
                b_unique[i].IsStarted.get_text(),
                b_unique[i].IsCompleted.get_text(),
                b_unique[i].Notes.get_text(),
                b_unique[i].Status.get_text(),
                b_unique[i].StatusText.get_text(),
                b_unique[i].StatusCodeColor.get_text(),
                b_unique[i].IsError.get_text(),
                b_unique[i].ErrorMessage.get_text(),
                b_unique[i].IsACHSupported.get_text(),
                b_unique[i].ChartsId.get_text(),
                b_unique[i].AdditionalAPI.get_text(),
                b_unique[i].IsRequestRefreshable.get_text()
            ]
            ReportDetail7.append(rows)
            # creating Dataframe
            df = pd.DataFrame(ReportDetail7, columns=[
                'CustomerIdentifier',
                'ReportDetail7_index',
                'RequestCode',
                'EmailAddress',
                'InstitutionName',
                'AccountName',
                'RoutingNumberEntered',
                'RoutingNumberReturned',
                'AccountType',
                'AccountNumberEntered',
                'AccountNumberFound',
                'AccountNumberConfidence',
                'NameEntered',
                'NameFound',
                'NameConfidence',
                'AmountInput',
                'AvailableBalance',
                'AverageBalance',
                'AverageBalanceRecent',
                'IsLoginValid',
                'IsVerified',
                'AsOfDate',
                'ActivityStartDate',
                'ActivityEndDate',
                'TotalCredits',
                'TotalDebits',
                'CurrentBalance',
                'IsActivityAvailable',
                'ProcessedStatus',
                'IsStarted',
                'IsCompleted',
                'Notes',
                'Status',
                'StatusText',
                'StatusCodeColor',
                'IsError',
                'ErrorMessage',
                'IsACHSupported',
                'ChartsId',
                'AdditionalAPI',
                'IsRequestRefreshable'
            ], dtype=float)
            print(df)
            # converting dataframe into csv
            df.to_csv(outdir + '\Report_detail.csv', index=False)
        i = 0
        j = 0
        arr = []
        # TransactionAnalysisSummaries
        i = 0
        j = 0
        arr=[]
        for meal_tag in b_unique:
            i = i + 1
            description_tag_list = meal_tag.find_all("TransactionAnalysisSummaryWithScores")
            # print('\n description_tag_list',len(description_tag_list),description_tag_list)
            for description_tag in description_tag_list:
                j = j + 1
                # print('\n description_tag', len(description_tag), description_tag.TypeName.get_text())
                rows = [
                    b_unique[0].CustomerIdentifier.get_text(),
                    int(i),
                    int(j),
                    description_tag.TypeName.get_text(),
                    description_tag.TypeCode.get_text(),
                    description_tag.TotalCount.get_text(),
                    description_tag.TotalAmount.get_text(),
                    description_tag.RecentCount.get_text(),
                    description_tag.RecentAmount.get_text(),
                    description_tag.DisplayOrder.get_text(),
                    description_tag.Score.get_text(),
                    description_tag.Message.get_text(),
                    description_tag.TransactionInterval.get_text(),
                    description_tag.NumberOfMissingIntervals.get_text(),
                    description_tag.MostRecentTransactionAmount.get_text(),
                    description_tag.MostRecentTransactionDate.get_text(),
                    description_tag.AverageTransactionAmount.get_text()
                ]
                arr.append(rows)
                b_tsum = pd.DataFrame(arr, columns=[
                    'CustomerIdentifier',
                    'ReportDetail7_index',
                    'TransactionAnalysisSummaryWithScores_index',
                    'TypeName',
                    'TypeCode',
                    'TotalCount',
                    'TotalAmount',
                    'RecentCount',
                    'RecentAmount',
                    'DisplayOrder',
                    'Score',
                    'Message',
                    'TransactionInterval',
                    'NumberOfMissingIntervals',
                    'MostRecentTransactionAmount',
                    'MostRecentTransactionDate',
                    'AverageTransactionAmount'
                ], dtype=float)

                b_tsum.to_csv(outdir + '\Transaction_analysis.csv', index=False)
        # TransactionAnalysisSummaries
        # TransactionSummary7
        i = 0
        j = 0
        arr = []
        for meal_tag in b_unique:
            i = i + 1
            description_tag_list = meal_tag.find_all("TransactionSummary7")
            # print('\n description_tag_list',len(description_tag_list),description_tag_list)
            for description_tag in description_tag_list:
                j=j+1
                # print('\n description_tag', len(description_tag), description_tag.TypeName.get_text())
                rows = [
                    b_unique[0].CustomerIdentifier.get_text(),
                    int(i),
                    int(j),
                    description_tag.TransactionDate.get_text(),
                    description_tag.Amount.get_text(),
                    description_tag.RunningBalance.get_text(),
                    description_tag.Description.get_text(),
                    description_tag.IsRefresh.get_text(),
                    description_tag.Status.get_text(),
                    description_tag.Category.get_text()
                    ]
                arr.append(rows)
                b_tsum = pd.DataFrame(arr, columns=[
                    'CustomerIdentifier',
                    'ReportDetail7_index',
                    'TransactionSummary7_index',
                    'TransactionDate',
                    'Amount',
                    'RunningBalance',
                    'Description',
                    'IsRefresh',
                    'Status',
                    'Category'
                ], dtype=float)

                b_tsum.to_csv(outdir+'\Transaction_summary.csv', index=False)

                # pprint(data)
            #     description_text = description_tag.find("Text").text
            #     print(description_text)
        # AccountExpense7
        i = 0
        j = 0
        lol = []
        for meal_tag in b_unique:
            i = i + 1
            description_tag_list = meal_tag.find_all("AccountExpense7")
            # print('\n description_tag_list',len(description_tag_list),description_tag_list)
            for description_tag in description_tag_list:
                j=j+1
                # print('\n description_tag', len(description_tag), description_tag.TypeName.get_text())
                rows = [
                    b_unique[0].CustomerIdentifier.get_text(),
                    int(i),
                    int(j),
                    description_tag.Category.get_text(),
                    description_tag.Amount.get_text(),
                    description_tag.Percent.get_text(),
                    ]
                lol.append(rows)
                b_tsum = pd.DataFrame(lol, columns=[
                    'CustomerIdentifier',
                    'ReportDetail7_index',
                    'AccountExpenses7_index',
                    'Category',
                    'Amount',
                    'Percent'
                ], dtype=float)

                b_tsum.to_csv(outdir+'\Account_expenses.csv', index=False)

                # pprint(data)
            #     description_text = description_tag.find("Text").text
            #     print(description_text)

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 8000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)