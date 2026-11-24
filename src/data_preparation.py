
import pandas as pd


def load_and_prepare_data():
    """
    Load the Spotify dataset from Hugging Face,
    remove the unnecessary index column, and
    consolidate repeated track IDs.
    """

    # Load dataset
    df = pd.read_csv(
        "hf://datasets/maharshipandya/spotify-tracks-dataset/dataset.csv"
    )

    # Remove unnecessary index column
    df_clean = df.drop(columns=['Unnamed: 0'])

    # Consolidate repeated track IDs
    df_consolidated = df_clean.groupby('track_id').agg({
        'artists': 'first',
        'album_name': 'first',
        'track_name': 'first',
        'popularity': 'first',
        'duration_ms': 'first',
        'explicit': 'first',
        'danceability': 'first',
        'energy': 'first',
        'key': 'first',
        'loudness': 'first',
        'mode': 'first',
        'speechiness': 'first',
        'acousticness': 'first',
        'instrumentalness': 'first',
        'liveness': 'first',
        'valence': 'first',
        'tempo': 'first',
        'time_signature': 'first',
        'track_genre': lambda x: list(x.unique())
    }).reset_index()

    return df_consolidated
