# Course Recommendation System

## Overview
This project implements a robust, production-ready content-based recommendation engine designed to suggest the most relevant courses based on metadata similarity. By analyzing textual alignments across course titles, domains, instructors, and difficulty levels, the system surface-maps tailored curriculum alternatives for scaling e-learning setups.

## Key Pipeline Optimizations
Unlike basic text-matching configurations, this pipeline incorporates advanced data handling strategies to prevent standard production bugs:
1. **Title-Based Deduplication:** Avoids catastrophic data loss by preserving unique courses that erroneously share identical asset IDs in the source system.
2. **Token-Splitting Protection:** Normalizes categorical text entries (e.g., converting "Mike Ross" into "mikeross") ensuring the algorithm matches on precise individual entities rather than fragmented tokens.
3. **Self-Recommendation Isolation:** Explicitly intercepts the target query matrix mapping to ensure the algorithm never erroneously recommends the input course back to the user when multiple assets share identical high-similarity metrics.
4. **Flexible Query Ingestion:** Built with user-friendly case-insensitive lookups, making text matching immune to casing differences.

## Methodology
The system utilizes a structured **Content-Based Filtering** framework:
1. **Feature Engineering & Cleaning:** Combines clean categorical strings and lowercased titles to establish an explicit descriptive profile for every course entity.
2. **Text Vectorization:** Implements `CountVectorizer` to translate structural text data into high-dimensional Bag-of-Words frequency vectors.
3. **Similarity Mapping:** Computes pair-wise **Cosine Similarity** arrays across vectors to capture numerical spatial relationships.
4. **Production Preservation:** Serializes structural matrices alongside processed datasets into an efficient single-file deployment format (`model.pkl`).
5. **Artifact Validation:** Executes post-saving validation scripts to verify artifact deserialization integrity before deployment routing.

## Project Structure
- `course_data.csv`: Source matrix detailing curriculum metrics (IDs, titles, categories, ratings, difficulty, and student enrollment footprints).
- `recommendation_pipeline.ipynb`: Core notebook orchestrating data transformation, modeling constraints, search logic, and testing.
- `model.pkl`: Production binary artifact preserving serialized matrices and dataset arrays for instantaneous inference.
- `README.md`: System documentation.

## Prerequisites
Ensure your local or cloud environment contains the required operational packages:

```bash
pip install pandas numpy scikit-learn
```

## Usage
1. Open the development workflow asset: `recommendation_pipeline.ipynb`.
2. Execute the cells sequentially to ingest, map features, and establish similarity boundaries.
3. Call the inference module anywhere downstream to query recommendation arrays:

```python
# Querying recommendations safely (Case-Insensitive)
print(get_recommendations("cloud architecture basics"))
```

## Author
**Animesh Sanghi** *Google Certified Data Analytics Professional*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
**Email:** animeshsanghi.da@gmail.com  

## License
This project is open-source and free to use under standard personal and educational terms.