
import joblib


def assign_clusters(
    X,
    pipeline_path='models/clustering_pipeline.joblib'
):
    """
    Assign clusters using the saved scikit-learn Pipeline.
    The pipeline handles scaling and K-Means prediction.
    """

    clustering_pipeline = joblib.load(pipeline_path)

    clusters = clustering_pipeline.predict(X)

    return clusters

