import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report,confusion_matrix
import pickle  


def clean_data():
        data=pd.read_csv("C:/Users/fadys/Desktop/streamlit/model/data/breast-cancer.csv")
        data.drop("id",axis=1,inplace=True) 
        #print(data.head())
        return data     
def creat_model(data):
        #print(data.describe().T)
        #spliting data :
        x=data.drop("diagnosis",axis=1)
        #rescaling data :
        scaler=StandardScaler()
        x=scaler.fit_transform(x)
        y=data["diagnosis"]
        y=y.map({"M":0,"B":1})
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
        print("shape of x_test:",x_test.shape)
        print("shape of y_test:",y_test.shape)
        model=LogisticRegression()
        model.fit(x_train,y_train)
        # testing
        y_pred=model.predict(x_test)
        print(accuracy_score(y_test,y_pred))
        cm=confusion_matrix(y_test,y_pred)

        print("confusion matrix:\n",confusion_matrix(y_test,y_pred))
        print ("classification report : \n",classification_report(y_test,y_pred))
        return model , scaler 

def main():
        

        data=clean_data()
        model,scaler=creat_model(data)
        with open("model.pkl","wb") as f :
                pickle.dump(model,f)
        with open("scaler.pkl","wb") as k:
                pickle.dump(scaler,k)         


if __name__=='__main__':
        main()
        