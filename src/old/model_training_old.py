import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Dense, Dropout
from feature_engineering_old import (
    load_and_split_features_labels,
    filter_rare_classes,
    encode_features,
    encode_labels,
    split_train_test
)

def build_model(input_dim, output_dim):
    model = Sequential([
        InputLayer(shape=(input_dim,)),
        Dense(512, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        Dropout(0.3),
        Dense(256, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        Dropout(0.3),
        Dense(output_dim, activation='softmax')
    ])
    return model

if __name__ == "__main__":
    # Data prep
    X, y = load_and_split_features_labels()
    X, y = filter_rare_classes(X, y, min_samples=2)
    X_encoded = encode_features(X)
    y_encoded, label_encoder = encode_labels(y)
    X_train, X_test, y_train, y_test = split_train_test(X_encoded, y_encoded)
    
    
    input_dim = X_train.shape[1]
    output_dim = len(set(y_train))
    print(f"Input dimension: {input_dim}")
    print(f"Output dimension: {output_dim}")
    print("✅ Data preprocessed")

    # Build model
    model = build_model(input_dim, output_dim)
    print("✅ Model built")
    model.summary()

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        metrics=['accuracy']
    )

    # Callbacks
    early_stop = tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    )
    
    # Train model
    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        epochs=100,
        batch_size=32,
        callbacks=[early_stop]
    )
    print("✅ Model trained")

    model.save('models/career_recommendation_model.keras')

    print("✅ Model saved to models/career_recommender_model")