import csv


def writeResult(df):
    print("Importem llibreries per carregar les variables")

    with open('output.csv', 'w+') as f:
        f.write(df.to_csv(index=False))

    print("S'ha creat un arxiu csv output.csv amb les dades obtingudes")
