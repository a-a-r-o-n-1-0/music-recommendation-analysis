# Spotify Music Recommendation System Using K-Means Clustering

## Project Overview

This project explores how Spotify audio features can be used to identify similarities between tracks and generate music recommendations.

Using a dataset of Spotify tracks, the project applies **K-Means clustering** to group tracks according to their audio characteristics. A recommendation system then uses Euclidean distance to identify similar tracks within the same cluster.

The project covers the complete process, from data cleaning and exploratory analysis to machine learning, recommendation generation and evaluation.

## Project Objective

The objective is to investigate whether unsupervised machine learning can identify meaningful groups of Spotify tracks based on their audio characteristics, and how these groups can support a content-based music recommendation system.

The project aims to:

- Explore and prepare Spotify track data.
- Investigate relationships between audio features.
- Identify groups of similar tracks using K-Means clustering.
- Develop a recommendation system that suggests tracks based on audio similarity.
- Evaluate the recommendations using audio-feature distances and genre overlap.

## Research Question

**Can unsupervised machine learning identify meaningful groups of Spotify tracks based on their audio characteristics, and how can these groups be used to support music recommendations?**

Supporting questions:

1. Which audio features help distinguish between groups of tracks?
2. How effectively can K-Means clustering group tracks with similar audio characteristics?
3. Can Euclidean distance identify similar tracks within the same cluster?
4. How can recommendation diversity be improved while maintaining audio similarity?

## Dataset

This project uses the **Spotify Tracks Dataset**, sourced from Hugging Face.

- **Dataset:** [Spotify Tracks Dataset](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset)
- **Original size:** 114,000 rows and 21 columns.
- **Data:** Track metadata, popularity information, genre labels and numerical audio features.

The dataset includes audio characteristics such as danceability, energy, acousticness, instrumentalness, valence and tempo. These features provide a basis for comparing tracks according to their musical properties.

## Tools and Technologies

- **Python** – programming language.
- **Jupyter Notebook** – exploratory analysis, model development and evaluation.
- **pandas** – data loading, cleaning and manipulation.
- **NumPy** – numerical operations.
- **Matplotlib and Seaborn** – data visualisation.
- **scikit-learn** – feature scaling, K-Means clustering, pipelines and model evaluation.
- **joblib** – saving and loading trained models.
- **Hugging Face Hub** – accessing the Spotify dataset.

## Methodology

The project follows these stages:

1. **Data loading and inspection:** Load the dataset from Hugging Face and examine its structure, dimensions, data types and quality.
2. **Data cleaning:** Remove the unnecessary exported index column and investigate missing values and duplicate records.
3. **Track consolidation:** Consolidate repeated track IDs while preserving their associated genre labels.
4. **Exploratory data analysis:** Investigate feature distributions, correlations and differences between genres.
5. **Feature selection:** Select nine numerical audio features for clustering.
6. **Feature scaling:** Apply RobustScaler to reduce the influence of outliers when comparing numerical features.
7. **Model development:** Apply K-Means clustering and compare different values of K and feature-scaling approaches.
8. **Model evaluation:** Compare clustering performance using silhouette scores and examine cluster characteristics.
9. **Recommendation development:** Generate recommendations using Euclidean distance between tracks within the same cluster.
10. **Recommendation evaluation:** Assess audio similarity, genre overlap and artist diversity across example recommendations.

## Data Cleaning and Preparation

The original dataset contained 114,000 rows and 21 columns.

The `Unnamed: 0` column was identified as an unnecessary exported index and removed.

One record contained missing artist, album and track names, although its track ID, genre and numerical audio features remained available.

The dataset also contained repeated track IDs associated with different genre labels. Since these records had consistent audio-feature values, they were consolidated into a single record per track, with associated genres preserved.

Following consolidation, the dataset contained:

- **89,741 unique tracks**
- **20 columns**
- No repeated track IDs
- Genre associations retained as lists

### Selected Audio Features

Nine numerical features were selected for clustering:

- Danceability
- Energy
- Acousticness
- Instrumentalness
- Valence
- Tempo
- Speechiness
- Liveness
- Loudness

These features were selected to represent different aspects of a track's musical characteristics.

## Exploratory Data Analysis

Exploratory analysis investigated the distributions and relationships between Spotify audio features.

The analysis included:

- Descriptive statistics to understand feature ranges and distributions.
- Correlation analysis to identify relationships between audio features.
- Comparisons of energy and acousticness across genres.
- Visualisations to investigate differences in musical characteristics.

Some notable relationships included:

- Energy and acousticness had a strong negative correlation of approximately **-0.73**.
- Energy and loudness had a positive correlation of approximately **0.76**.

Genre comparisons also highlighted differences in musical characteristics. For example, classical tracks had relatively low median energy, while metal tracks had relatively high median energy.

These findings helped inform the selection of audio features for the clustering model.

## K-Means Clustering

### Feature Scaling

RobustScaler was selected to scale the numerical audio features.

Unlike StandardScaler, RobustScaler uses the median and interquartile range, making it less sensitive to extreme values.

### Selecting the Number of Clusters

Different values of K were investigated using silhouette scores.

Both StandardScaler and RobustScaler were considered. RobustScaler produced stronger clustering results for the selected features.

A five-cluster model was ultimately selected as a balance between clustering performance and interpretability.

The two-cluster model achieved a higher silhouette score, but produced broader groups. Five clusters provided more detailed distinctions between different types of tracks.

### Model Performance

The selected model achieved:

| Evaluation | Silhouette score |
|---|---:|
| Training data | 0.3500 |
| Test data (sample of 5,000 tracks) | 0.3497 |

The similar scores suggest that the clustering structure generalises reasonably consistently to the held-out test data.

### Cluster Profiles

The model identified five clusters with different average audio characteristics.

| Cluster | Main characteristics | Tracks |
|---|---|---:|
| 0 | Broad general music profile | 54,305 |
| 1 | High instrumentalness and lower energy | 17,401 |
| 2 | High danceability, energy and speechiness | 7,812 |
| 3 | High speechiness and liveness | 929 |
| 4 | High energy and liveness | 9,294 |

These profiles provide an indication of the types of tracks grouped together.

For example, Cluster 1 contains tracks with particularly high instrumentalness, while Cluster 3 has very high speechiness, making it more suited to spoken-word and comedy-style content.

The clusters are based on numerical audio features rather than predefined genres.

## Music Recommendation System

A recommendation system was developed using the trained K-Means model and scaled audio features.

### Recommendation Process

The recommendation system follows these steps:

1. The user selects a track by providing its name and artist.
2. The system locates the selected track in the dataset.
3. The saved clustering model identifies its cluster.
4. Candidate tracks are restricted to the same cluster.
5. Euclidean distance is calculated between the selected track and candidate tracks using their scaled audio features.
6. Candidates are ranked by distance, with smaller distances indicating greater audio-feature similarity.
7. The selected track's artist is excluded from recommendations.
8. Additional artist filtering is applied to avoid repeatedly recommending the same artist.

The system returns up to five recommendations by default, including the track name, artist, genre and Euclidean distance.

### Recommendation Diversity

An artist-diversity filter was introduced to reduce repeated artist recommendations.

This means that recommendations are not simply the five closest tracks. The system considers the closest candidates while avoiding artists that have already appeared in the recommendation list.

This provides a greater variety of recommendations while retaining the audio-similarity approach.

## Recommendation Evaluation

The recommendation system was tested using five example tracks, with one selected from each cluster.

Recommendations were evaluated using:

- Mean Euclidean distance between the selected track and its recommendations.
- Mean absolute difference across the nine audio features.
- Genre overlap between the selected track and recommended tracks.
- Artist diversity within the recommendation list.

### Key Findings

The evaluation highlighted differences between clusters.

- **Cluster 4** produced the strongest overall combination of audio similarity and genre overlap, with a mean Euclidean distance of approximately 0.458 and genre overlap of 80%.
- **Cluster 0** produced relatively close audio-feature matches, with a mean Euclidean distance of approximately 0.549, despite having no genre overlap in the example evaluation.
- **Cluster 3** achieved 100% genre overlap, although its mean Euclidean distance was higher at approximately 1.267.

These results demonstrate that audio similarity and genre similarity are not necessarily the same thing. Tracks can have similar audio characteristics despite belonging to different genres.

The evaluation also showed that restricting recommendations to the same cluster does not guarantee identical genres, which is expected because clustering is based on audio features rather than genre labels.

The evaluation uses a small number of example tracks and should therefore be treated as an initial assessment rather than a comprehensive measure of recommendation quality.

## Project Structure

The project uses a modular structure to separate data preparation, preprocessing, clustering and recommendation functionality.

```text
music-recommendation-analysis/
│
├── models/
│   ├── scaler.joblib
│   ├── kmeans_model.joblib
│   └── clustering_pipeline.joblib
│
├── src/
│   ├── preprocessing.py
│   ├── clustering.py
│   ├── recommender.py
│   ├── data_preparation.py
│   └── pipeline.py
│
├── music_analysis.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```

### Main Components

- `data_preparation.py` – loads the Spotify dataset and consolidates repeated track IDs.
- `preprocessing.py` – extracts and scales the selected audio features for similarity calculations.
- `clustering.py` – loads the saved scikit-learn Pipeline and assigns tracks to clusters.
- `recommender.py` – contains the recommendation functions.
- `pipeline.py` – connects the components and provides the main functions for loading the recommendation system and generating recommendations.
- `models/` – stores the fitted scaler, K-Means model and combined clustering Pipeline.
- `music_analysis.ipynb` – contains the exploratory analysis, model development, evaluation and project findings.

The combined `clustering_pipeline.joblib` contains the fitted RobustScaler and K-Means model, allowing new tracks to be assigned to clusters without retraining the model.

## How to Run the Project

### Prerequisites

Install Python and use either Jupyter Notebook or Visual Studio Code with the Python and Jupyter extensions.

Clone or download the repository and open the project root directory.

### 1. Install Dependencies

Create and activate a Python environment if necessary.

Install the required libraries using:

```bash
pip install -r requirements.txt
```

### 2. Configure SSL Certificates (if required)

If you encounter an SSL certificate error when downloading the dataset from Hugging Face, configure Conda to use the certificate file installed by `certifi`:

```bash
conda env config vars set SSL_CERT_FILE="<path-to-environment>/Lib/site-packages/certifi/cacert.pem"
```

Replace the placeholder with the path to your active environment.

Deactivate and reactivate the environment for the change to take effect:

```bash
conda deactivate
conda activate <environment-name>
```

### 3. Run the Notebook

Open `music_analysis.ipynb` and run the cells in order.

The notebook contains the exploratory analysis, data preparation, model development and evaluation.

### 4. Generate Recommendations

The recommendation system can be accessed through the modular Python files.

From the project root directory, run:

```python
from src.pipeline import load_recommendation_system, get_recommendations

# Load the dataset and trained recommendation system
recommendation_data, recommendation_features = load_recommendation_system()

# Generate recommendations for a selected track
recommendations = get_recommendations(
    track_name="Tief",
    artist_name="Paul Kalkbrenner",
    recommendation_data=recommendation_data,
    recommendation_features=recommendation_features
)

print(recommendations)
```

The example uses *Tief* by Paul Kalkbrenner. Replace the track name and artist with another exact track and artist combination from the dataset.

The system loads the dataset from Hugging Face and uses the saved models in the `models/` directory. An internet connection is therefore required to load the dataset.

If multiple tracks have the same name and artist, the system displays the matching records and allows a specific match to be selected using its index.

## Limitations

There are several limitations to the current recommendation system:

- Recommendations are based on numerical audio features rather than individual listening histories or user preferences.
- Genre labels do not necessarily capture every aspect of musical similarity.
- Tracks within the same cluster may still have noticeable differences in their audio characteristics.
- The number of clusters affects how broad or specific the recommendations become.
- Artist filtering can exclude otherwise highly similar tracks.
- The recommendation system has not been evaluated using real user feedback or listening behaviour.
- Evaluation was performed using a limited number of example tracks rather than a large-scale user study.

Consequently, the system demonstrates a content-based recommendation approach, but its recommendations should not be considered a measure of individual listener preference.

## Future Improvements

Potential improvements include:

- Experimenting with alternative clustering algorithms and different numbers of clusters.
- Comparing alternative distance and similarity measures.
- Incorporating genre information into the recommendation process.
- Introducing user preferences and listening histories.
- Developing a user interface to make recommendations easier to explore.
- Expanding evaluation using a larger and more representative selection of tracks.
- Investigating alternative methods for improving recommendation diversity.

## Conclusion

This project demonstrates how unsupervised machine learning can be applied to Spotify audio features to support a content-based music recommendation system.

After cleaning and consolidating the original dataset, 89,741 unique tracks were available for analysis. Nine numerical audio features were selected and scaled using RobustScaler before applying K-Means clustering.

The five-cluster model achieved a training silhouette score of 0.3500 and a test score of 0.3497, indicating a reasonably consistent clustering structure.

A recommendation system was then developed using Euclidean distance to identify similar tracks within the same cluster. Artist filtering was introduced to improve recommendation diversity.

The evaluation demonstrated that tracks can share similar audio characteristics even when their genre labels differ. This highlights the potential of audio-feature-based recommendations while also demonstrating the limitations of relying on genre labels alone.

Overall, the project provides a foundation for further development of music recommendation systems using unsupervised machine learning.