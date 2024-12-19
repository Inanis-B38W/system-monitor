# tests/test_system_monitor.py
 
import pytest
from unittest.mock import patch, MagicMock
import system_monitor
 
# Test CPU usage function
@patch('psutil.cpu_percent')
def test_check_cpu_usage(mock_cpu_percent):
    # Mock cpu_percent to return a value of 90%
    mock_cpu_percent.return_value = 90
    with patch('builtins.print') as mock_print:
        system_monitor.check_cpu_usage()
        mock_print.assert_called_with("ALERT: High CPU usage detected: 90% (Threshold: 85%)")
 
    # Test when CPU usage is below threshold
    mock_cpu_percent.return_value = 50
    with patch('builtins.print') as mock_print:
        system_monitor.check_cpu_usage()
        mock_print.assert_not_called()
 
# Test Memory usage function
@patch('psutil.virtual_memory')
def test_check_memory_usage(mock_virtual_memory):
    # Mock virtual_memory to return a memory usage of 90%
    mock_virtual_memory.return_value.percent = 90
    with patch('builtins.print') as mock_print:
        system_monitor.check_memory_usage()
        mock_print.assert_called_with("ALERT: High memory usage detected: 90% (Threshold: 85%)")
 
    # Test when memory usage is below threshold
    mock_virtual_memory.return_value.percent = 50
    with patch('builtins.print') as mock_print:
        system_monitor.check_memory_usage()
        mock_print.assert_not_called()
 
# Test Disk usage function
@patch('psutil.disk_usage')
def test_check_disk_usage(mock_disk_usage):
    # Mock disk_usage to return disk usage of 90%
    mock_disk_usage.return_value.percent = 90
    with patch('builtins.print') as mock_print:
        system_monitor.check_disk_usage()
        mock_print.assert_called_with("ALERT: High disk usage detected: 90% (Threshold: 85%)")
 
    # Test when disk usage is below threshold
    mock_disk_usage.return_value.percent = 50
    with patch('builtins.print') as mock_print:
        system_monitor.check_disk_usage()
        mock_print.assert_not_called()