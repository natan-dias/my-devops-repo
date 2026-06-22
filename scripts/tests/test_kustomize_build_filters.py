import pytest
import subprocess
from unittest.mock import patch

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
try:
    sys.path.remove(str(parent))
except ValueError:
    pass

import yaml
from kustomize_build_filters import kustomize_build_filter, DEFAULT_KINDS, main

SAMPLE_RESOURCE = yaml.dump({
    'apiVersion': 'apps/v1',
    'kind': 'Deployment',
    'metadata': {'name': 'my-app'},
    'spec': {}
}).encode()


def test_matching_resource_is_printed(capsys):
    with patch('subprocess.check_output', return_value=SAMPLE_RESOURCE):
        kustomize_build_filter('infra/redis', 'my-app', kinds=['Deployment'])
    out = capsys.readouterr().out
    assert 'my-app' in out
    assert 'Deployment' in out


def test_kustomize_error_returns_none(capsys):
    with patch('subprocess.check_output', side_effect=subprocess.CalledProcessError(1, 'kustomize')):
        result = kustomize_build_filter('infra/redis', 'my-app')
    assert result is None
    assert 'Error' in capsys.readouterr().out


def test_missing_kind_prints_error(capsys):
    with patch('subprocess.check_output', return_value=SAMPLE_RESOURCE):
        kustomize_build_filter('infra/redis', 'my-app', kinds=['Service'])
    out = capsys.readouterr().out
    assert "Error: Resource kind 'Service' not found" in out


def test_default_kinds_used_when_none_provided():
    with patch('subprocess.check_output', return_value=SAMPLE_RESOURCE):
        with patch('kustomize_build_filters.DEFAULT_KINDS', ['Deployment']):
            with patch('builtins.print') as mock_print:
                kustomize_build_filter('infra/redis', 'my-app', kinds=None)
                printed = ' '.join(str(c) for c in mock_print.call_args_list)
                assert 'my-app' in printed


def test_main(capsys):
    with patch('subprocess.check_output', return_value=SAMPLE_RESOURCE):
        with patch('sys.argv', ['kustomize_build_filters.py', '--path', 'infra/redis', '--name', 'my-app', '--kind', 'Deployment']):
            main()
    out = capsys.readouterr().out
    assert 'my-app' in out
    assert 'Deployment' in out
