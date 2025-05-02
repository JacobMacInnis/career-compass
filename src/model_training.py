import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Dense, Dropout
# Scale numeric features
from sklearn.preprocessing import StandardScaler
from feature_engineering import (
    load_and_split_features_labels,
    split_train_test,
    scale_numerical_features
)
import joblib
import os


def build_model(input_dim):
    model = Sequential([
        InputLayer(shape=(input_dim,)),
        Dense(256, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        Dropout(0.3),
        Dense(128, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        Dropout(0.3),
        Dense(1, activation='sigmoid')  # binary classification (0/1)
    ])
    return model

if __name__ == "__main__":
    # Load data
    X, y = load_and_split_features_labels()
    X_train, X_test, y_train, y_test = split_train_test(X, y)

    print(f"✅ Data loaded: X_train: {X_train.shape}, X_test: {X_test.shape}")

    # Define numeric columns to scale
    numeric_cols = ['YearsCode', 'YearsCodePro', 'PreviousSalary', 'ComputerSkills']


    # numeric_cols = [col for col in X_train.columns if X_train[col].dtype in ['float64', 'int64']]
    scaler = StandardScaler()
    X_train[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
    X_test[numeric_cols] = scaler.transform(X_test[numeric_cols])
    print(f"✅ Numeric columns scaled: {numeric_cols}")

    print(f"✅ Data prepared: X_train: {X_train.shape}, X_test: {X_test.shape}")

    # Save scaler
    os.makedirs('models', exist_ok=True)

    joblib.dump(scaler, 'models/scaler.pkl')
    print("✅ Saved scaler to models/scaler.pkl")
    joblib.dump(X_train.columns.tolist(), 'models/trained_columns.pkl')
    print("✅ Saved trained columns to models/trained_columns.pkl")
    joblib.dump(numeric_cols, 'models/numeric_columns.pkl')
    print("✅ Saved numeric columns to models/numeric_columns.pkl")

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
        patience=5,
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

    # Save model
    model.save('models/career_employability_predictor.keras')
    print("✅ Model saved to models/career_employability_predictor.keras")
