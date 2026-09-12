# BM Git Shortcuts — User Guide

This guide covers the features available in version **0.1.0**.

You run a short command. The matching Git command runs, with your
arguments passed through unchanged.

```text
gst
```

is the same as:

```text
git status
```

You never type `bm-git` first.

---

## Before you start

1. Install Git.
2. Install the package:

   ```bash
   sudo dpkg -i bm-git-shortcuts_0.1.0-1_all.deb
   ```

3. Work inside a Git repository for commands that need one (`gst`,
   `gpl`, `gcm`, and so on).

If Git is missing, the shortcut prints a clear error instead of failing
obscurely.

---

## Feature list (0.1.0)

These twelve commands are the current feature set.

| Shortcut | Git command | Typical use |
| -------- | ----------- | ----------- |
| `gpl` | `git pull` | Update the current branch |
| `gps` | `git push` | Publish commits |
| `gst` | `git status` | See working tree state |
| `gco` | `git checkout` | Switch branch or restore files |
| `gcb` | `git checkout -b` | Create and switch to a branch |
| `gcm` | `git commit -m` | Commit with a message |
| `gca` | `git commit --amend` | Amend the last commit |
| `gdf` | `git diff` | Show unstaged (or other) diffs |
| `gbr` | `git branch` | List or manage branches |
| `gss` | `git stash` | Stash local changes |
| `gsp` | `git stash pop` | Restore the latest stash |
| `glg` | `git log --oneline --graph` | Compact history graph |

Anything you would pass to the Git command, you pass to the shortcut.

---

## Command reference

### `gst` — status

```bash
gst
gst -sb
```

Runs `git status`, then any extra flags you add.

### `gpl` — pull

```bash
gpl
gpl --rebase
gpl origin main
```

Runs `git pull` with the same arguments.

### `gps` — push

```bash
gps
gps origin main
gps -u origin feature/login
```

Runs `git push` with the same arguments.

### `gco` — checkout

```bash
gco main
gco --
gco -- path/to/file
```

Runs `git checkout`. Use this to switch branches or restore paths.

### `gcb` — new branch

```bash
gcb feature/login
gcb fix/typo
```

Runs `git checkout -b`. Creates the branch and switches to it.

### `gcm` — commit with message

```bash
gcm "fix login issue"
gcm "docs: add user guide"
```

Runs `git commit -m`. Keep the message in quotes if it contains spaces.

Stage files first (`git add`) the same way you would for a normal
commit. `gcm` does not add files for you.

### `gca` — amend last commit

```bash
gca
gca --no-edit
gca -m "corrected message"
```

Runs `git commit --amend`. Git's usual amend rules still apply
(including not rewriting published history unless you intend to).

### `gdf` — diff

```bash
gdf
gdf --staged
gdf HEAD
gdf -- path/to/file
```

Runs `git diff`.

### `gbr` — branch

```bash
gbr
gbr -a
gbr -d old-branch
```

Runs `git branch`.

### `gss` — stash

```bash
gss
gss push -m "wip login"
gss list
```

Runs `git stash`. Extra subcommands and flags are forwarded.

### `gsp` — stash pop

```bash
gsp
```

Runs `git stash pop` and restores the most recent stash onto the working
tree.

### `glg` — compact log

```bash
glg
glg -20
glg --all
```

Runs `git log --oneline --graph`. Extra flags are appended after that
fixed log format.

---

## Everyday workflows

### See where you are, then update

```bash
gst
gpl
```

### Start a feature branch and commit

```bash
gcb feature/login
# ... edit files, then: git add ...
gcm "add login form"
gps -u origin feature/login
```

### Switch branches

```bash
gco main
gpl
gco feature/login
```

### Park work, pull, then restore

```bash
gss
gpl
gsp
```

### Review history and diff

```bash
glg
gdf
gdf --staged
```

### Fix the last commit message

```bash
gca -m "fix login validation"
```

---

## How arguments work

Shortcuts do not rewrite your arguments. They append them to the mapped
Git command.

| You type | Git runs |
| -------- | -------- |
| `gpl` | `git pull` |
| `gpl --rebase` | `git pull --rebase` |
| `gps origin main` | `git push origin main` |
| `gco main` | `git checkout main` |
| `gcb feature/login` | `git checkout -b feature/login` |
| `gcm "fix login issue"` | `git commit -m "fix login issue"` |
| `glg -10 --all` | `git log --oneline --graph -10 --all` |

Quotes and spaces are preserved. If you would quote something for Git,
quote it the same way for the shortcut.

---

## Errors and exit codes

- If Git is not installed, you get a clear error.
- If Git fails (not a repo, rejected push, nothing to commit), the
  shortcut exits with Git's exit code.
- Invalid flags fail the same way they would with Git.

Example:

```bash
gpl
echo $?    # same status Git returned
```

---

## Install, check, remove

Install:

```bash
sudo dpkg -i bm-git-shortcuts_0.1.0-1_all.deb
```

Confirm commands exist:

```bash
which gpl gps gst gco gcb gcm gca gdf gbr gss gsp glg
```

Remove:

```bash
sudo dpkg -r bm-git-shortcuts
```

After removal, those commands should no longer be on your `PATH`.

---

## What this version does not include

These ideas are not available yet. They are tracked for later, not
shipped in 0.1.0:

- Combined helpers such as add+commit or undo
- Configurable / custom shortcut files
- Shell completion (Bash / Zsh / Fish)
- `apt` repository install
- Packages for architectures other than `amd64`

---

## Need the project overview?

See [README.md](README.md) for repository identity, requirements, and a
short start. Project status is tracked in
[GIT_SHORTCUTS_CONTEXT.md](GIT_SHORTCUTS_CONTEXT.md).
