import seq_features
import pytest

def n_neg(seq):
    seq = seq.upper()
    return seq.count('E') + seq.count('D')

    
def test_n_neg():
    """Perform unit tests on n_neg."""
    assert n_neg('E') == 1
    assert n_neg('D') == 1
    assert n_neg('') == 0
    assert n_neg('ACKLWTTAE') == 1
    assert n_neg('DDDDEEEE') == 8
    assert n_neg('acklwttae') == 1

def test_n_neg_for_lower_case_sequences():
    assert seq_features.n_neg('acklwttae') == 1

def test_n_neg_for_invalid_amino_acid():
    with pytest.raises(RuntimeError) as excinfo:
        seq_features.n_neg('Z')
    excinfo.match("Z is not a valid amino acid")
