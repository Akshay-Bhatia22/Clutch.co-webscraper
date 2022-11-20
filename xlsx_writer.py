import pandas as pd


writer = pd.ExcelWriter("data.xlsx")

def run(data_dict, domain, counter):

        if counter==1:
            start_row = -1
            header=True
        else:
            start_row = (counter-1)*40
            header=False
        print(start_row)
        df = pd.DataFrame(data_dict)
        # print (df)
        df.to_excel(writer, sheet_name=domain, startrow=start_row+1, index=False, header=header)
        # df.to_excel(writer, sheet_name=f"test{counter}", index=False)

        writer.save()
