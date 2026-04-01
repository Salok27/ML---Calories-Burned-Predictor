
@echo off

echo Training model...
python ml_model.py

echo Starting app...
streamlit run app.py

pause