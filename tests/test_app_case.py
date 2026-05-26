# tests/test_app_case.py
#
# Simple, clear pytest examples.
# Show how to test basic EDA functions.
#
# Assumptions:
# - module is importable
# - pytest running from project root
#
# Run:
#   uv run pytest


import pandas as pd
import pytest

from datafun_04_notebooks import app_case


def test_load_data_returns_dataframe():
    """Test that load_data returns a pandas DataFrame."""
    df = app_case.load_data()
    assert isinstance(df, pd.DataFrame)


def test_load_data_has_expected_columns():
    """Test that the DataFrame has the expected columns."""
    df = app_case.load_data()
    expected_cols = [
        "species",
        "island",
        "bill_length_mm",
        "flipper_length_mm",
        "body_mass_g",
    ]
    for col in expected_cols:
        assert col in df.columns


def test_load_data_not_empty():
    """Test that the DataFrame is not empty."""
    df = app_case.load_data()
    assert len(df) > 0


def test_make_clean_view_removes_missing():
    """Test that make_clean_view removes rows with missing values."""
    df = app_case.load_data()
    df_clean = app_case.make_clean_view(df)
    # Clean view should have fewer or equal rows
    assert len(df_clean) <= len(df)
    # Clean view should have no missing values in key columns
    for col in app_case.NUMERIC_COLS:
        assert df_clean[col].isna().sum() == 0


def test_correlation_matrix_shape():
    """Test that correlation matrix is square with correct dimensions."""
    df = app_case.load_data()
    df_clean = app_case.make_clean_view(df)
    corr = app_case.correlation_matrix(df_clean)
    num_cols = len(app_case.NUMERIC_COLS)
    assert corr.shape == (num_cols, num_cols)


def test_correlation_matrix_diagonal_is_one():
    """Test that diagonal values of correlation matrix are 1.0."""
    df = app_case.load_data()
    df_clean = app_case.make_clean_view(df)
    corr = app_case.correlation_matrix(df_clean)
    for col in corr.columns:
        assert corr.loc[col, col] == pytest.approx(1.0)
