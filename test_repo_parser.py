#!/usr/bin/env python3

import unittest
import tempfile
# import shutil
import os.path
from unittest.mock import patch, Mock, MagicMock, mock_open
from app.controllers.repo_parser import GitRepoParser
from app import create_app
from git import GitCommandError


class GitRepoParserTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.parser = GitRepoParser('/path-to-download')

    def test_get_folder_path(self):
        folder_path = self.parser.get_folder_path(service_name='oleg-service')
        self.assertIsInstance(folder_path, str)

    @patch('os.path.isdir')
    def test_create_new_service_without_dir(self, mock_isdir):
        mock_isdir.return_value = False

        self.assertEqual(self.check_path('/tmp/configuration/settings/test-service'), False)

    def test_create_new_service(self):
        self.parser.create_new_service('test-service', '0.0.1-SNAPSHOT')

    @staticmethod
    def check_path(directory):
        if os.path.isdir(directory):
            return True
        else:
            return False

