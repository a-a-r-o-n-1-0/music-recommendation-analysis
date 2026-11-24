
from sklearn.preprocessing import RobustScaler
import joblib

# Audio features used by the clustering model
FEATURES = [
    'danceability',
    'energy',
    'acousticness',
    'instrumentalness',
    'valence',
    'tempo',
    'speechiness',
    'liveness',
    'loudness'
]


def prepare_features(df, scaler_path='models/scaler.joblib'):
    """
    Extract the audio features and scale them using the
    fitted RobustScaler saved during model development.
    """
    scaler = joblib.load(scaler_path)

    X = df[FEATURES]
    X_scaled = scaler.transform(X)

    return X_scaled
