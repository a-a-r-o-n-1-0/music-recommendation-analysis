from src.data_preparation import load_and_prepare_data
from src.preprocessing import prepare_features, FEATURES
from src.clustering import assign_clusters
from src.recommender import recommend_by_track


def load_recommendation_system():
    """
    Load the Spotify dataset, prepare its audio features,
    and assign each track to a cluster.
    """

    recommendation_data = load_and_prepare_data()

    # Scaled features are needed for calculating recommendation distances
    recommendation_features = prepare_features(recommendation_data)

    # The saved Pipeline handles scaling and cluster prediction
    clusters = assign_clusters(recommendation_data[FEATURES])

    recommendation_data['cluster'] = clusters

    return recommendation_data, recommendation_features


def get_recommendations(
    track_name,
    artist_name,
    recommendation_data,
    recommendation_features,
    match_index=None,
    number_of_recommendations=5
):
    """
    Generate recommendations for a track using its name and artist.
    """

    return recommend_by_track(
        track_name=track_name,
        artist_name=artist_name,
        recommendation_data=recommendation_data,
        recommendation_features=recommendation_features,
        match_index=match_index,
        number_of_recommendations=number_of_recommendations
    )