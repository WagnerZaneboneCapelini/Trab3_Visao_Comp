"""Test Snap Package Template."""

import trab3_visao_comp


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(trab3_visao_comp.__name__, str)
