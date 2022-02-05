import numpy as np
import pandas
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
from sklearn.model_selection import TimeSeriesSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from src.colours import wes_anderson_colours
from src.constants import constants
from src.paths import path_manager
from src.strings import strings
from src.utils import add_spines_to_axes


"""Section 2: Preprocess the data"""
df = pandas.read_csv(path_manager.eight_hr_data, parse_dates=['Date'])
df[strings.WSR0].replace('?', np.nan)
for feature in strings.float_columns():
    df[feature] = df[feature].replace('?', np.nan).astype(float)
df = df.fillna(method="ffill")
df[strings.ozone] = df[strings.ozone].astype(int)

"""Section 3: Exploratory data analysis"""
if constants.EXPLORE_MODE:
    print(df.info())
    print(df.head(5))
    ax = plt.gca()
    add_spines_to_axes(ax, wes_anderson_colours[1])
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature T5 (C)")
    ax.plot(
        df[strings.date], df[strings.T5],
        c=wes_anderson_colours[0],
    )
    plt.show()

"""Section 4: Define a benchmark"""
counts = df.groupby([strings.ozone])[strings.date].nunique()
counts_safe = counts[0]
counts_ozone_event = counts[1]
mean = counts_ozone_event/(counts_safe + counts_ozone_event)
print("Population mean occurrence rate:", mean)
benchmark = log_loss(df[strings.ozone], [mean]*len(df[strings.ozone]))

"""Section 5: Create new features"""
# Use shifting to avoid look-ahead bias
new_features = dict()

# Create date features
new_features['month'] = df[strings.date].apply(lambda x: x.month)
new_features['day'] = df[strings.date].apply(lambda x: x.day)

for feature in strings.float_columns():
    # Create windowed feature
    new_features[feature + "window"] = df[feature].rolling(constants.lag, 1).apply(
        lambda x: np.nanmean(x)).shift(1)

    # Create lagged features
    for ii in range(1, constants.lag + 1):
        new_features[feature + "_lag" + str(ii)] = df[feature].shift(ii)

lag_df = pandas.DataFrame(new_features)
X = lag_df[constants.lag:]
y = df.loc[constants.lag:, strings.ozone]
reduced_full_df = df[constants.lag:]
best_n_features = X.columns

"""Section 6: Find best features"""
split = TimeSeriesSplit(
    n_splits=constants.n_splits,
    test_size=constants.test_size,
    gap=10
)

# Initialise loop variables
test_index, test_y, predicted_ozone_probability = None, None, None
train_index = None
for train_index, test_index in split.split(X):
    train_X = X.iloc[train_index]
    train_y = y.iloc[train_index]
    test_X = X.iloc[test_index]
    test_y = y.iloc[test_index]

    pipe = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=constants.max_iter)
    )
    pipe.fit(train_X, train_y)
    predicted_ozone_probability = pipe.predict_proba(test_X)
    loss = log_loss(test_y, predicted_ozone_probability)
    labels = train_X.columns
    coefficients = np.abs(pipe['logisticregression'].coef_[0])
    _, labels = zip(*sorted(zip(coefficients, labels), reverse=True))
    best_n_features = list(labels[:constants.n_features])

"""Section 7: Rebuild the model using only the best features"""
best_X = X[best_n_features]
print("Best features: ")
[print(f, end=" ") for f in best_n_features]
pipe2 = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=constants.max_iter)
)
pipe2.fit(best_X.iloc[train_index], y.iloc[train_index])
predicted_ozone_probability = pipe2.predict_proba(
    best_X.iloc[test_index])[:, 1]

"""Section 8: Score the model using log loss to evaluate probability"""
print("\n--- Log loss ---")
loss = log_loss(test_y, predicted_ozone_probability)
print("Lower is better!")
print("Benchmark log loss:", benchmark)
print("Final split predictive log loss:", loss)
print("Improvement over baseline log loss:", benchmark - loss)

"""
Section 9: Show the predicted probability of an ozone event with
vertical markers for actual events using the test split only.
"""
test_df = reduced_full_df.iloc[test_index]
fig = plt.gcf()
ax = plt.gca()
add_spines_to_axes(ax, wes_anderson_colours[10])
ax.plot(
    test_df[strings.date],
    predicted_ozone_probability,
    c=wes_anderson_colours[1],
    label="Model predicted ozone event probability"
)
events = test_df.loc[df[strings.ozone] == 1, strings.date]
for event in events:
    ax.axvline(event, c=wes_anderson_colours[11], alpha=0.3)
ax.plot([], [], c=wes_anderson_colours[11], label="Actual adverse events")
ax.set_xlabel("Date (test set only)")
ax.set_ylabel("Predicted probability of adverse event")
ax.legend()
plt.show()
