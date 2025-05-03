import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Dense, Dropout
from sklearn.preprocessing import StandardScaler
from feature_engineering import (
    load_and_split_features_labels,
    split_train_test,
    scale_numerical_features,
    select_important_features
)
import joblib
import os

## Model attempt 1
# def build_model(input_dim):
#     model = Sequential([
#         InputLayer(shape=(input_dim,)),
#         Dense(256, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
#         Dropout(0.3),
#         Dense(128, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
#         Dropout(0.3),
#         Dense(1, activation='sigmoid')  # binary classification (0/1)
#     ])
#     return model

## Model attempt 2
def build_model(input_dim):
    model = Sequential([
        InputLayer(shape=(input_dim,)),
        Dense(512, activation='relu'),
        Dropout(0.3),
        Dense(256, activation='relu'),
        Dropout(0.3),
        Dense(128, activation='relu'),
        Dropout(0.3),
        Dense(1, activation='sigmoid')  # Binary classification
    ])
    return model

if __name__ == "__main__":
    # Load data
    X, y = load_and_split_features_labels()
    X_train, X_test, y_train, y_test = split_train_test(X, y)

    print(f"✅ Data loaded: X_train: {X_train.shape}, X_test: {X_test.shape}")

    # Define numeric columns to scale
    numeric_cols = ['YearsCode', 'YearsCodePro', 'PreviousSalary', 'ComputerSkills']

    # Scale numeric columns
    X_train, X_test = scale_numerical_features(X_train, X_test, numeric_cols)
    print(f"✅ Numeric columns scaled: {numeric_cols}")

    # Feature Selection
    X_train, selected_features = select_important_features(X_train, y_train, threshold=0.01)
    X_test = X_test[selected_features]
    print(f"✅ Feature selection done: X_train: {X_train.shape}, X_test: {X_test.shape}")

    # Save scaler and feature names
    os.makedirs('models', exist_ok=True)
    joblib.dump(selected_features, 'models/trained_columns.pkl')
    joblib.dump(numeric_cols, 'models/numeric_columns.pkl')
    print("✅ Saved selected features and numeric columns.")

    # Build model
    input_dim = X_train.shape[1]
    model = build_model(input_dim)
    print("✅ Model built")
    model.summary()

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss=tf.keras.losses.BinaryCrossentropy(),
        metrics=['accuracy']
    )

    early_stop = tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=2,
        restore_best_weights=True
    )

    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        epochs=100,
        batch_size=32,
        callbacks=[early_stop]
    )

    print("✅ Model trained")

    # Save model and history
    model.save('models/career_employability_predictor.keras')
    joblib.dump(history.history, 'models/training_history.pkl')
    print("✅ Model and history saved to 'models/' folder.")
