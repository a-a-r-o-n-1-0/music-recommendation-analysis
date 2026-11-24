
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances


def recommend_tracks(
    track_index,
    recommendation_data,
    recommendation_features,
    number_of_recommendations=5
):
    """
    Recommend tracks from the same cluster, ranked by
    Euclidean distance, while avoiding repeated artists.
    """

    # Retrieve the selected track and its cluster
    selected_track = recommendation_data.iloc[track_index]
    selected_cluster = selected_track['cluster']

    # Identify tracks belonging to the same cluster
    candidate_indices = np.where(
        recommendation_data['cluster'].values == selected_cluster
    )[0]

    # Exclude the selected track
    candidate_indices = candidate_indices[
        candidate_indices != track_index
    ]

    # Exclude artists from the selected track
    selected_artists = set(
        str(selected_track['artists']).split(';')
    )

    candidate_indices = [
        index for index in candidate_indices
        if not selected_artists.intersection(
            str(recommendation_data.iloc[index]['artists']).split(';')
        )
    ]

    # Calculate Euclidean distances
    distances = euclidean_distances(
        [recommendation_features[track_index]],
        recommendation_features[candidate_indices]
    ).flatten()

    # Sort candidates by distance (closest first)
    sorted_positions = np.argsort(distances)

    # Select recommendations without repeating artists
    recommended_indices = []
    recommended_artists = set()

    for position in sorted_positions:
        index = candidate_indices[position]

        candidate_artists = set(
            str(recommendation_data.iloc[index]['artists']).split(';')
        )

        if not recommended_artists.intersection(candidate_artists):
            recommended_indices.append(index)
            recommended_artists.update(candidate_artists)

        if len(recommended_indices) == number_of_recommendations:
            break

    # Build the results
    recommendations = []

    for index in recommended_indices:
        position = candidate_indices.index(index)

        recommendations.append({
            'track_name': recommendation_data.iloc[index]['track_name'],
            'artists': recommendation_data.iloc[index]['artists'],
            'track_genre': recommendation_data.iloc[index]['track_genre'],
            'distance': distances[position]
        })

    return pd.DataFrame(recommendations)




def recommend_by_track(
    track_name,
    artist_name,
    recommendation_data,
    recommendation_features,
    match_index=None,
    number_of_recommendations=5
):
    """
    Find a track by its exact name and artist, then
    generate recommendations for that track.
    """

    # Search for the track and artist
    matches = recommendation_data[
        (recommendation_data['track_name'].str.lower() == track_name.lower()) &
        (recommendation_data['artists'].str.lower() == artist_name.lower())
    ]

    if matches.empty:
        print("Track not found. Please check the track name and artist.")
        return

    # Check for multiple matching tracks
    if len(matches) > 1 and match_index is None:
        print("Multiple matches found. Please select a track using its index:")
        print(matches[['track_name', 'artists', 'track_genre', 'cluster']])
        return

    # Validate the selected index
    if match_index is not None:
        if match_index not in matches.index:
            print("Invalid selection. Please choose an index from the results.")
            return
        selected_index = match_index
    else:
        selected_index = matches.index[0]

    # Convert the dataframe index label to a positional index
    track_position = recommendation_data.index.get_loc(selected_index)

    # Generate recommendations
    return recommend_tracks(
        track_index=track_position,
        recommendation_data=recommendation_data,
        recommendation_features=recommendation_features,
        number_of_recommendations=number_of_recommendations
    )
