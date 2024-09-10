# tests/test_vpn_connect.py
import pytest
from vpn_connect import connect_to_server

def test_connect_to_valid_server():
    result = connect_to_server("vpn1.example.com")
    assert result == True

def test_connect_to_invalid_server():
    result = connect_to_server("invalid.example.com")
    assert result == False
