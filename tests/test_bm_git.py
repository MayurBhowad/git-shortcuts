#!/usr/bin/env python3

import importlib.util
import subprocess
import unittest
from pathlib import Path
from unittest.mock import patch

# python3 -m unittest discover -s tests -v


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BM_GIT = PROJECT_ROOT / "src" / "bm-git"


loader = importlib.machinery.SourceFileLoader("bm_git", str(BM_GIT))
spec = importlib.util.spec_from_loader("bm_git", loader)
bm_git = importlib.util.module_from_spec(spec)
loader.exec_module(bm_git)


class TestBuildCommand(unittest.TestCase):

    def test_gpl(self):
        self.assertEqual(
            bm_git.build_command("gpl", []),
            ["git", "pull"],
        )

    def test_gps(self):
        self.assertEqual(
            bm_git.build_command("gps", []),
            ["git", "push"],
        )

    def test_gst(self):
        self.assertEqual(
            bm_git.build_command("gst", []),
            ["git", "status"],
        )

    def test_gco(self):
        self.assertEqual(
            bm_git.build_command("gco", ["main"]),
            ["git", "checkout", "main"],
        )

    def test_gcb(self):
        self.assertEqual(
            bm_git.build_command("gcb", ["feature/login"]),
            ["git", "checkout", "-b", "feature/login"],
        )

    def test_gcm(self):
        self.assertEqual(
            bm_git.build_command("gcm", ["fix login"]),
            ["git", "commit", "-m", "fix login"],
        )

    def test_gca(self):
        self.assertEqual(
            bm_git.build_command("gca", ["--no-edit"]),
            ["git", "commit", "--amend", "--no-edit"],
        )

    def test_gdf(self):
        self.assertEqual(
            bm_git.build_command("gdf", ["--stat"]),
            ["git", "diff", "--stat"],
        )

    def test_gbr(self):
        self.assertEqual(
            bm_git.build_command("gbr", []),
            ["git", "branch"],
        )

    def test_gss(self):
        self.assertEqual(
            bm_git.build_command("gss", []),
            ["git", "stash"],
        )

    def test_gsp(self):
        self.assertEqual(
            bm_git.build_command("gsp", []),
            ["git", "stash", "pop"],
        )

    def test_glg(self):
        self.assertEqual(
            bm_git.build_command("glg", []),
            ["git", "log", "--oneline", "--graph"],
        )

    def test_arguments_are_preserved(self):
        args = ["origin", "main", "--force-with-lease"]

        self.assertEqual(
            bm_git.build_command("gps", args),
            ["git", "push", "origin", "main", "--force-with-lease"],
        )

    def test_arguments_with_spaces_are_preserved(self):
        args = ["fix login issue"]

        self.assertEqual(
            bm_git.build_command("gcm", args),
            ["git", "commit", "-m", "fix login issue"],
        )

    def test_unknown_command(self):
        with self.assertRaises(ValueError):
            bm_git.build_command("unknown", [])


class TestGitExecution(unittest.TestCase):

    @patch.object(bm_git.subprocess, "run")
    def test_git_exit_code_is_returned(self, mock_run):
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "status"],
            returncode=42,
        )

        with patch.object(bm_git.sys, "argv", ["gst"]):
            result = bm_git.main()

        self.assertEqual(result, 42)

    @patch.object(bm_git.subprocess, "run")
    def test_correct_command_is_executed(self, mock_run):
        mock_run.return_value = subprocess.CompletedProcess(
            args=["git", "status"],
            returncode=0,
        )

        with patch.object(bm_git.sys, "argv", ["gst"]):
            result = bm_git.main()

        self.assertEqual(result, 0)
        mock_run.assert_called_once_with(["git", "status"])

    @patch.object(bm_git.subprocess, "run", side_effect=FileNotFoundError)
    def test_git_not_found(self, mock_run):
        with patch.object(bm_git.sys, "argv", ["gst"]):
            result = bm_git.main()

        self.assertEqual(result, 127)


if __name__ == "__main__":
    unittest.main()
