# Python libraries
import matplotlib.pyplot as plt
import pandas as pd


class DataVisualization:

    def __init__(self, folder_path, csv_file):
        self.folder_path = folder_path
        self.csv_file = csv_file

    def data_show(self):
        """
        showing data according to every .csv file
        """
        df = pd.read_csv(f'./{self.folder_path}/{self.csv_file}.csv')

        names = df['Technology'].tolist()
        numbers = df['Numbers'].tolist()

        x_pos = [i for i, _ in enumerate(names)]

        plt.figure(figsize=(14, 5))
        # Avoiding errors when generating .jpg files
        plt.rcParams.update({'figure.max_open_warning': 0})

        plt.bar(x_pos, numbers, color='blue')
        plt.xlabel("Tecnologia requerida")
        plt.ylabel("Numero de puestos en 240 ofertas")
        plt.title("Demanda de Trabajo")

        plt.xticks(x_pos, names)

        plt.savefig(f'./{self.folder_path}/{self.csv_file}.jpg',
                    pil_kwargs={'quality': 95})
