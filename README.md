# Music Recommendation: Data Analysis and Preparation

## Project Objective

The objective of this project is to investigate how Spotify track features can be used to identify similarities between songs and support the development of a music recommendation system. Using a dataset of Spotify tracks, the project will focus on data cleaning, exploratory data analysis and identifying the audio features that may be useful for recommending music. This analysis will establish a foundation for developing a recommendation algorithm in a future stage.

## Research Questions

1. **Which audio features are most useful for identifying similarities between songs?**  
   Investigate features such as danceability, energy, acousticness, valence and tempo to understand how they vary across tracks.

2. **What relationships exist between Spotify's audio features?**  
   Explore correlations and patterns between audio features to determine whether some features are related and how this might affect the measurement of musical similarity.

3. **How suitable is the dataset for developing a music recommendation system?**  
   Assess the dataset's completeness, consistency and quality, identifying any missing values, duplicate records or other issues that could affect future recommendations.

## Dataset

This project uses the **Spotify Tracks Dataset**, sourced from Hugging Face.

- **Dataset:** [Spotify Tracks Dataset](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset)
- **Original size:** 114,000 rows and 21 columns
- **Data type:** Track metadata, popularity information, genre labels and numerical audio features.

The dataset contains information about individual tracks, including their artists, albums, genres and audio characteristics. Audio features such as danceability, energy, acousticness, instrumentalness and valence can help describe the musical properties of a track.

These features provide a starting point for investigating how tracks could be compared in a content-based music recommendation system.

## Project Scope

The focus of this project is **data analysis and preparation for a future music recommendation algorithm**. It does not build or evaluate a complete recommendation system.

The project explores the dataset, investigates relationships between audio features, compares selected features across genres and prepares numerical data for potential use in a similarity-based model.

## Tools and Technologies

The project uses the following tools and libraries:

- **Python** — data analysis and preparation.
- **Jupyter Notebook** — documenting the analysis, code and findings.
- **pandas** — loading, cleaning and manipulating the dataset.
- **NumPy** — numerical operations.
- **Matplotlib and Seaborn** — visualising distributions, relationships and differences between genres.
- **scikit-learn** — standardising numerical features in preparation for future modelling.

## Methodology

The project follows these stages:

1. **Data loading and inspection:** Load the dataset and examine its dimensions, columns, data types and initial quality.
2. **Data quality assessment:** Investigate missing values, exact duplicate rows, repeated track IDs and the exported index column.
3. **Data cleaning and consolidation:** Remove the unnecessary index column and consolidate repeated track IDs while preserving their associated genre labels.
4. **Exploratory data analysis:** Examine descriptive statistics, feature distributions and correlations between numerical audio features.
5. **Genre comparisons:** Compare selected audio features, including energy and acousticness, across genres to investigate differences in musical characteristics.
6. **Feature selection:** Select nine numerical audio features for potential use in a future content-based recommendation model.
7. **Feature standardisation:** Use `StandardScaler` from scikit-learn to place the selected numerical features on comparable scales.

## Data Cleaning and Preparation

The original dataset contained 114,000 rows. The `Unnamed: 0` column was identified as an unnecessary exported index and removed from the cleaned dataset.

One record was missing its artist, album and track names, although its track ID, genre and numerical audio features remained available. The missing metadata was not artificially filled in.

The dataset also contained repeated track IDs across different genre labels. Since these records had consistent audio-feature values, they were consolidated into **89,741 unique tracks**, with associated genres preserved for each track.

Nine numerical audio features were selected for future modelling:

- Danceability
- Energy
- Acousticness
- Instrumentalness
- Valence
- Tempo
- Speechiness
- Liveness
- Loudness

The selected feature matrix was checked for missing values and standardised using `StandardScaler`.

## Key Findings

The exploratory analysis investigated how Spotify audio features vary across tracks and genres, as well as how some features relate to one another.

The analysis included:

- Descriptive statistics to understand the distributions and ranges of audio features.
- Correlation analysis to identify relationships between numerical features.
- Comparisons of energy and acousticness across selected genres.
- Consolidation of repeated track IDs to create a dataset with one row per unique track while retaining genre associations.

These findings help assess which audio features may be useful when comparing tracks for a future recommendation system. The analysis provides a foundation for further investigation rather than demonstrating that a recommendation algorithm already produces accurate recommendations.

Classical tracks have the lowest median energy, at approximately 0.14, while metal tracks have the highest, at approximately 0.89. Jazz has a median of around 0.33, compared with approximately 0.62 for pop and 0.70 for rock.

When cross-referenced with the analyzed energy distribution plot, a clear inverse relationship emerges between these two features across genres:

    Classical and Metal act as polar opposites: Classical features maximum acousticness and minimum energy, while Metal features maximum energy and minimum acousticness.

    Jazz vs. Rock/Pop: Jazz mirrors Rock and Pop in reverse structural behavior; Jazz keeps a high acoustic/lower energy profile, whereas Rock and Pop lean significantly higher in energy while giving up acoustic dominance.

## Limitations

There are several limitations to this project:

- The analysis uses audio features and metadata rather than individual listening histories or user preferences.
- Genre labels do not necessarily capture all the ways listeners perceive musical similarity.
- Tracks can belong to multiple genres, which makes genre-based comparisons more complex.
- The analysis does not yet calculate track-to-track similarity or generate recommendations.
- Recommendation quality has not been evaluated using user feedback or quantitative evaluation metrics.

Consequently, the findings indicate potential uses for audio features but do not establish how effective a completed recommendation system would be.

## Future Work

Potential extensions of this project include:

- Calculating similarity between tracks using their standardised audio features.
- Building a content-based recommendation system that suggests tracks similar to a selected song.
- Comparing similarity methods, such as cosine similarity and Euclidean distance.
- Investigating how genre information could complement numerical audio features.
- Evaluating recommendations using suitable quantitative measures and, where possible, user feedback.

## How to Run the Project

### Prerequisites

Install Python and Jupyter Notebook, or use Visual Studio Code with its Python and Jupyter extensions.

Install the required libraries using:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn datasets
```

If you use a Conda environment, activate it before installing the dependencies.

### Running the Notebook

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code or Jupyter Notebook.
3. Select the Python environment containing the required libraries.
4. Open `music_analysis.ipynb`.
5. Run the notebook cells in order, from top to bottom.

The notebook loads the dataset, performs the analysis and prepares the numerical feature matrix.

## Repository Structure

```text
music-recommendation-analysis/
├── README.md
├── music_analysis.ipynb
├── requirements.txt
└── .gitignore
```

The notebook contains the code, visualisations and written analysis. The README summarises the project's purpose, methodology, findings and instructions for reproducing the work.
