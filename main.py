import streamlit as st
import joblib
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

filename = "C:\\Users\\ergou\\PycharmProjects\\Data_analysis_report\\concrete_data.csv"
df = pd.read_csv(filename)


def main():
    st.title("Concrete strength analysis report")
    st.write(
        "Concrete is the most important material in civil engineering. The concrete compressive strength is a highly nonlinear function of age and ingredients. These ingredients include cement, blast furnace slag, fly ash,water, superplasticizer, coarse aggregate, and fine aggregate.")
    st.write(
        "From the following Report our **Goal** is to evaluate the *dataset* step by step and see if I should add how much of what part to the mixture so that it increases the strength of the mixture and the materials are not also wasted")
    filename = "C:\\Users\\ergou\\PycharmProjects\\Data_analysis_report\\concrete_data.csv"
    df = pd.read_csv(filename)
    st.write(df)
    st.header("Introduction")
    st.write(
        "Concrete is the most important material in civil engineering. The concrete compressive strength is a highly nonlinear function of age and ingredients. These ingredients include cement, blast furnace slag, fly ash,water, superplasticizer, coarse aggregate, and fine aggregate.")
    st.write("Objective:")
    st.markdown("1. what are the features that determine the strength of concrete mixture?"
                "2. how these features are usefull to determine the strength of mixture?"
                "3. how to get the mixture to give best strength?")
    st.write("Data")
    st.write(df)
    st.markdown(
        "The following dataset is provided by :Prof. I-Cheng Yeh Department of Information Management Chung-Hua University,Hsin Chu, Taiwan")
    st.write("The dataset contains:features such as "
             "Cement (component 1) -- quantitative -- kg in a m3 mixture -- Input Variable"
             "Blast Furnace Slag (component 2) -- quantitative -- kg in a m3 mixture -- Input Variable"
             "Fly Ash (component 3) -- quantitative -- kg in a m3 mixture -- Input Variable"
             "Water (component 4) -- quantitative -- kg in a m3 mixture -- Input Variable"
             "Superplasticizer (component 5) -- quantitative -- kg in a m3 mixture -- Input Variable"
             ''"Coarse Aggregate (component 6) -- quantitative -- kg in a m3 mixture -- Input Variable"
             "Fine Aggregate (component 7) -- quantitative -- kg in a m3 mixture -- Input Variable"
             "Age -- quantitative -- Day (1~365) -- Input Variable"
             "Concrete compressive strength -- quantitative -- MPa -- Output Variable ")
    st.write(
        "for the above dataset I am using seaborn library to analysis the relation between the features and how they are "
        "related to the strength")
    st.write("Age and Strength")
    ScatterPlot("Age")
    st.write("Blast Furnace Slag vs strength")
    ScatterPlot("Blast Furnace Slag")
    st.write("Fly Ash vs strength")
    ScatterPlot("Fly Ash")
    st.write("Water vs strength")
    ScatterPlot("Water")
    st.write("Superplasticizer vs strength")
    ScatterPlot("Superplasticizer")
    st.write("Coarse Aggregate vs strength")
    ScatterPlot("Coarse Aggregate")
    st.write("Fine Aggregate vs strength")
    ScatterPlot("Fine Aggregate")
    st.write("Age vs strength")
    ScatterPlot("Age")
    st.write("From the above graphs we can state that features like   "
             "a. Cement(0.50)<br>"
             "b. Vlast furnance slag(0.13)<br>"
             "c. superplasticizer(0.37)<br>"
             "d. Age(0.33)<br>"
             "Determine the strength of the mixture as increasing the cement will result in increasing the strength of mixture and "
             "features like bleast furnance slag and super plasticizers are used to increase the reaction's time taken and Age play a different role as we can say that when the applied mixture gets old then"
             "its strength is incresed by the time but as the time passes and gets more then 100 it start to loss its strength thats why eperts suggest renovation by times")
    st.write("Whereas features like "
             "  a. fly Ash(-0.11)<br>"
             "  b. Water(-0.29)<br>"
             "  c. Coarse aggregate(-0.16)<br>"
             "  d. fine aggregate(-0.17)<br>"
             "Determines that how increasing these feature will cause the decrease in the strength of the mixture because features like water and "
             "fine aggregate will result in decrease of strength if not added in relevent amount")

    st.write("how to create a mixture with best propersonate?"
             "for such working we are using machine learning algorithm and have created a model ")

    model="C:\\Users\\ergou\\PycharmProjects\\Data_analysis_report\\finalized_model.sav"
    loaded_model = joblib.load(model)

    st.write("enter details to check the strength of your mixture")
    Cement = st.number_input(label="Cement - - kg in m3")
    Blast_Furnace_Slag = st.number_input(label="Blast_Furnace_Slag - - kg in m3")
    Fly_Ash = st.number_input(label="Fly_Ash - - kg in am3")
    Water = st.number_input(label="water")
    Super_plasticizer = st.number_input(label="Super_plasticizer - - kg in am3")
    Coarse_Aggregate = st.number_input(label="Coarse_Aggregate")
    Fine_Aggregate =st.number_input(label="Fine_Aggregate - - kg in am3 ")
    Age = st.number_input(label="systolic blood pressure")


    if st.button('prediction results are:'):
        feature = [[Cement, Blast_Furnace_Slag, Fly_Ash, Water, Super_plasticizer, Coarse_Aggregate, Fine_Aggregate, Age]]
        result = loaded_model.predict(feature)
        st.write(result)




def ScatterPlot(x_col):
    fig = plt.figure(figsize=(10, 4))
    sns.scatterplot(x = x_col, y = "Strength", data = df)
    st.pyplot(fig)

if __name__ == "__main__":
    main()