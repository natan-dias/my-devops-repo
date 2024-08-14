import pytest 
import os
import subprocess
from unittest.mock import patch, Mock, call

from build_and_push import build_image, build_and_push_image

mock_run = Mock()
def test_build_image():
    build_image('images/webserver-example')

def test_build_and_push_image():
    # Mock the subprocess.run calls
    with patch('subprocess.run') as mock_run:
        # Test case 1: Successful build and push
        folder_path = 'images/webserver-example'
        folder_name = os.path.basename(folder_path)
        image_name = f"natandias1/{folder_name}:latest"
        
        mock_run.side_effect = [None, None]

        build_and_push_image(folder_path)
        
        # Assert that the correct commands were run
        expected_build_command = ['docker', 'build', '-t', image_name, folder_path]
        expected_push_command = ['docker', 'push', image_name]
        
        mock_run.assert_has_calls([
            call(expected_build_command),
            call(expected_push_command)
        ])
        
        # Test case 2: Build failure
        mock_run.side_effect = subprocess.CalledProcessError(returncode=1, cmd=expected_build_command)
        with pytest.raises(subprocess.CalledProcessError):
            build_and_push_image(folder_path)
        
        # Test case 3: Push failure
        mock_run.side_effect = None
        mock_run.return_value = None
        mock_run.side_effect = subprocess.CalledProcessError(returncode=1, cmd=expected_push_command)
        with pytest.raises(subprocess.CalledProcessError):
            build_and_push_image(folder_path)