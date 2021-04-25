import psycopg2
import pandas as pd

#     connect to an existing database
connection = psycopg2.connect(
    user = "postgres",
    password = "Pml99",
    host = "localhost",
    port = "5432",
    database = "pipelinefirst"
)
    # create cursor
cursor = connection.cursor()

def main():
    a = int(input("""----------- Menu 
        1. Tampilkan
        2. Masukkan
        (X) Keluar
        ----------- Masukkan pilihan : """))
    if a == 1:
        view()
    elif a == 2:
        model()
    else :
        print("Keluar")
        exit()

def view():
    cursor.execute ("""
    select
        *
    from irispipeline
    """)
    data = cursor.fetchall()
    for i in data :
        df = pd.DataFrame (data, columns = [
            'id','sepal_length','sepal_width',
            'petal_length','petal_width',
            'species'
        ])
        print(df.head())
        main()
        # return df

def dataset():
    cursor.execute ("""
    select
        *
    from irispipeline
    """)
    data = cursor.fetchall()
    for i in data :
        df = pd.DataFrame (data, columns = [
            'id','sepal_length','sepal_width',
            'petal_length','petal_width',
            'species'
        ])
        # print(df.tail())
        # main()
        return df

def model():
    df = dataset()

    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report
    from sklearn import metrics

    x = df.drop(['id','species'], axis = 1)
    y = df['species']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5)
    from sklearn import tree

    classifier=tree.DecisionTreeClassifier()
    classifier.fit(x_train,y_train)

    print("Input : ")
    a = input('sepal_length = ')
    b = input('sepal_width = ')
    c = input('petal_length = ')
    d = input('petal_width = ')

    x_test = pd.DataFrame(data=[[a,b,c,d]], columns=['sepal_length',
                                                    'sepal_width',
                                                    'petal_length',
                                                    'petal_width'])

    predictions=classifier.predict(x_test)
    x_test['species'] = pd.DataFrame(predictions)

    cols = ",".join([str(i) for i in x_test.columns.tolist()])
    for i,row in x_test.iterrows():
        sql = "INSERT INTO irispipeline (" +cols + ") VALUES (" + "%s,"*(len(row)-1) + "%s)"
        cursor.execute(sql, tuple(row))

        connection.commit()
    print("done!")
    main()

    

if __name__ == '__main__':
    main()