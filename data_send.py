from sheets import create_spreadsheet,  write_columns_names, export_pandas_df_to_sheets, write_mean, clear_sheet, write_action, write_students_number, write_students_left
from dotenv import load_dotenv
import os
import pandas as pd

class DataSending:
    def __init__(self):
        load_dotenv()
        self.file_path = "data.csv"

    def enviar_dados(self, media_atencao, alunos_sala, alunos_fora):
                
        if os.getenv("ID") is None:
            spreadsheet_id = create_spreadsheet()
            write_columns_names(spreadsheet_id, self.file_path)
            export_pandas_df_to_sheets(spreadsheet_id, self.file_path)

            with open(".env", "a") as file:
                file.write(f"ID={spreadsheet_id}")

        else:
            spreadsheet_id = os.getenv("ID")
            write_columns_names(spreadsheet_id, self.file_path)
            export_pandas_df_to_sheets(spreadsheet_id, self.file_path)
            write_mean(spreadsheet_id, media_atencao)
            write_students_number(spreadsheet_id, alunos_sala)
            write_students_left(spreadsheet_id, alunos_fora)
            action = "intervalo" if media_atencao < 0.3 else "aula"
            write_action(spreadsheet_id, action)

    def clear(self):
        clear_sheet(os.getenv("ID"), ["Data", "Mean"])  # clear the sheet