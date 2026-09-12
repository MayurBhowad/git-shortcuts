# BM Git Shortcuts

Short standalone commands for everyday Git work on Linux.

After you install the package, you type the shortcut itself. There is no
`bm-git` prefix.

```text
gpl  ->  git pull
gps  ->  git push
gst  ->  git status
```

## What this repository is

`bm-git-shortcuts` is a small Linux utility that ships as a Debian
package (`.deb`). Install it with `dpkg`, and the shortcuts land on your
`PATH` as normal commands such as `gpl`, `gps`, and `gst`.

The project is intentionally small:

- No extra Git wrapper CLI for day-to-day use
- Arguments are forwarded to Git as you typed them
- Git's exit status is returned unchanged
- No `.bashrc` edits are required after install

Current version: **0.1.0**

## Current shortcuts

| Shortcut | Runs |
| -------- | ---- |
| `gpl` | `git pull` |
| `gps` | `git push` |
| `gst` | `git status` |
| `gco` | `git checkout` |
| `gcb` | `git checkout -b` |
| `gcm` | `git commit -m` |
| `gca` | `git commit --amend` |
| `gdf` | `git diff` |
| `gbr` | `git branch` |
| `gss` | `git stash` |
| `gsp` | `git stash pop` |
| `glg` | `git log --oneline --graph` |

Full examples, workflows, and notes are in the
[User Guide](USER_GUIDE.md).

## Requirements

- Linux (Debian/Ubuntu or another `dpkg`-based system)
- Git installed and available as `git`

## Install

```bash
sudo dpkg -i bm-git-shortcuts_0.1.0-1_all.deb
```

The package installs the shortcut commands. You do not copy files by
hand.

Confirm they are on your `PATH`:

```bash
which gpl
which gps
which gst
```

## Quick start

```bash
gst                 # git status
gpl                 # git pull
gco main            # git checkout main
gcb feature/login   # git checkout -b feature/login
gcm "fix login"     # git commit -m "fix login"
gps origin main     # git push origin main
```

Quoted arguments stay quoted. Extra flags are passed through to Git:

```bash
gpl --rebase
gca --no-edit
```

## Uninstall

```bash
sudo dpkg -r bm-git-shortcuts
```

That removes the installed shortcuts.

## Repository layout

```text
git-shortcuts/
├── README.md                  # this file — repo overview
├── USER_GUIDE.md              # how to use the current features
└── GIT_SHORTCUTS_CONTEXT.md   # project goals, status, and AI context
```

Implementation, Debian packaging, and tests will live alongside these
docs as the 0.1.0 package is built.

## Documentation

| File | Purpose |
| ---- | ------- |
| [README.md](README.md) | What the repo is, install, and a short start |
| [USER_GUIDE.md](USER_GUIDE.md) | Every current command, with examples |
| [GIT_SHORTCUTS_CONTEXT.md](GIT_SHORTCUTS_CONTEXT.md) | Internal project context and tracking |

## License

Not specified yet.
