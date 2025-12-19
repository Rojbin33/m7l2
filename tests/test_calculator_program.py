import pytest
from calculate.calculator_program import calculate

# Mevcut testler (düzgün olanlar)
def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Bilinmeyen işlem."

# --- ÇIKARMA TESTLERİ ---
def test_calculate_subtraction_positive():
    assert calculate(10, 4, '-') == 6

def test_calculate_subtraction_negative_result():
    assert calculate(4, 10, '-') == -6

# --- ÇARPMA TESTLERİ ---
def test_calculate_multiplication_positive():
    assert calculate(7, 3, '*') == 21

def test_calculate_multiplication_with_zero():
    assert calculate(5, 0, '*') == 0

# --- EKSTRA (BONUS) TESTLER ---
def test_calculate_division_by_zero():
    assert calculate(5, 0, '/') == "Sıfıra bölme hatası."

def test_calculate_with_negative_numbers():
    assert calculate(-3, -2, '+') ==  -5
