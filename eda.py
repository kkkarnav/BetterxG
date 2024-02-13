import json
import matplotlib.pyplot as plt
from collections import Counter

import os
import warnings
from pprint import pprint
import numpy as np
import pandas as pd
from tqdm import tqdm

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def plot_coordinates(x, y):
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', alpha=0.5)
    plt.title('Scatter Plot of X and Y Coordinates')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.show()


def plot_bar_chart(data_df, column):
    value_counts = data_df[column].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    value_counts.plot(kind='bar', color='skyblue')
    plt.title(f'Frequency of {column}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.show()


def plot_area_chart(sequence):
    plt.fill_between(range(len(sequence)), sequence, color="skyblue", alpha=0.4)
    plt.plot(sequence, color="Slateblue", alpha=0.6, linewidth=2)
    plt.xlabel("Threshold (times 10)")
    plt.ylabel("F1 score")
    plt.title("ROC")
    plt.show()


def construct_data_df(raw_df):
    data = pd.DataFrame()
    data["period"] = raw_df["period"]
    data["minute"] = raw_df["minute"]
    data["possession"] = raw_df["possession"]
    data["play_pattern"] = raw_df["play_pattern"].apply(lambda x: x["id"])
    data["position"] = raw_df["position"].apply(lambda x: x["id"])
    data["location_x"] = raw_df["location"].apply(lambda x: x[0])
    data["location_y"] = raw_df["location"].apply(lambda x: x[1])
    data["duration"] = raw_df["duration"]
    data["technique"] = raw_df["shot"].apply(lambda x: x["technique"]["id"])
    data["body_part"] = raw_df["shot"].apply(lambda x: x["body_part"]["id"])
    data["type"] = raw_df["shot"].apply(lambda x: x["type"]["id"])
    data["statsbomb_xg"] = raw_df["shot"].apply(lambda x: x["statsbomb_xg"])
    return data


def eda(data_df):
    print(data_df.shape)
    print(data_df.info())
    print(data_df.nunique())
    print(data_df['statsbomb_xg'].hist())

    plot_coordinates(data_df['location_x'], data_df['location_y'])

    # 93: normal, 91: half volley, 95: volley, 02: lob, 94: overhead kick, 89: backheel, 90: diving header
    plot_bar_chart(data_df, "technique")
    # 40: right foot, 38: left foot, 37: head, 70: other
    plot_bar_chart(data_df, "body_part")
    # 87: open play, 62: free kick, 88: penalty, 61: corner, 65: kick off
    plot_bar_chart(data_df, "type")
    # 1: open play, 3: free kick, 4: throw in, 2: corner, 6: counter, 7: goal kick, 8: keeper, 5: other, 9: kick off
    plot_bar_chart(data_df, "play_pattern")
    plot_bar_chart(data_df, "minute")
    plot_area_chart(data_df["duration"])


def onehot(data_df):
    for column_name in ["play_pattern", "position", "technique", "body_part", "type"]:
        one_hot_encoded = pd.get_dummies(data_df[column_name], prefix=column_name)
        data_df.drop(column_name, axis=1)
        data_df = pd.concat([data_df, one_hot_encoded], axis=1)

    return data_df


def lin_regression(data_df):
    X = data_df.drop("statsbomb_xg", axis=1)

    Y = data_df["statsbomb_xg"]

    scaler = StandardScaler().fit(X)
    X = scaler.transform(X)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=20)

    linear_r = LinearRegression()

    linear_r.fit(X_train, Y_train)

    y_pred = linear_r.predict(X_test)

    print("\nLinear Regression")
    mae = mean_absolute_error(Y_test, y_pred)
    rmse = root_mean_squared_error(Y_test, y_pred)
    r2 = r2_score(Y_test, y_pred)
    print("Mean Absolute Error:", mae)
    print("Root Mean Squared Error:", rmse)
    print("R-squared (R2 Score):", r2)


def log_regression(data_df):
    X = data_df.drop("statsbomb_xg", axis=1)

    Y = data_df["statsbomb_xg"]
    threshold = 0.5
    Y = Y.apply(lambda x: x > threshold)

    scaler = StandardScaler().fit(X)
    X = scaler.transform(X)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=20)

    logistic_r = LogisticRegression()

    logistic_r.fit(X_train, Y_train)

    y_pred = logistic_r.predict(X_test)

    cm = confusion_matrix(Y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Not a goal", "Goal"])
    disp.plot(cmap=plt.cm.Blues)
    plt.title('Confusion Matrix LR')
    plt.show()

    print("\nLogistic Regression")
    accuracy = accuracy_score(Y_test, y_pred)
    precision = precision_score(Y_test, y_pred)
    recall = recall_score(Y_test, y_pred)
    f1 = f1_score(Y_test, y_pred)
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1:", f1)


def decision_tree(data_df):
    for threshold in range(1, 10, 1):
        X = data_df.drop("statsbomb_xg", axis=1)

        Y = data_df["statsbomb_xg"]
        # threshold = 0.5
        Y = Y.apply(lambda x: x > (threshold/10))

        scaler = StandardScaler().fit(X)
        X = scaler.transform(X)

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=20)

        clf = DecisionTreeClassifier()
        clf.fit(X_train, Y_train)
        y_pred = clf.predict(X_test)

        cm = confusion_matrix(Y_test, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Not a goal", "Goal"])
        disp.plot(cmap=plt.cm.Blues)
        plt.title('Confusion Matrix DT')
        plt.show()

        print(f"\nDecision Tree {threshold/10}")
        accuracy = accuracy_score(Y_test, y_pred)
        precision = precision_score(Y_test, y_pred)
        recall = recall_score(Y_test, y_pred)
        f1 = f1_score(Y_test, y_pred)
        print("Accuracy:", accuracy)
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1:", f1)


def main():

    folder = "../../open-data/data/events/"
    file_paths = []
    json_list = []

    try:
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_paths.append(os.path.join(root, file))
        print(file_paths[1722])
        for file_path in tqdm(file_paths[:2000]):
            with open(file_path, 'r', encoding='utf8') as json_file:
                json_list += json.load(json_file)

        print(len(json_list))
        # explore_json_list(json_list)

        shot_list = []
        for event in json_list:
            if "shot" in event.keys():
                shot_list.append(event)
        print(len(shot_list))

        df = pd.DataFrame(shot_list)
        # df = pd.DataFrame(pd.json_normalize(shot_list))
        # df = df.drop("shot.freeze_frame", axis=1)
        print([x for x in df])
        data = construct_data_df(df)
        eda(data)
        data = onehot(data)
        lin_regression(data)
        log_regression(data)
        decision_tree(data)

    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")


if __name__ == "__main__":
    main()
