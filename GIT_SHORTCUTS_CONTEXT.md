# BM Git Shortcuts --- AI Project Context

## 1. Project Identity

**Project name:** `bm-git-shortcuts`

**Purpose:** Create a small Linux utility that provides short standalone
commands for common Git operations.

The project must be installable as a Debian package (`.deb`) using
`dpkg`.

Example installation:

``` bash
sudo dpkg -i bm-git-shortcuts_0.1.0_amd64.deb
```

After installation, the user should be able to run:

``` bash
gpl
gps
gst
```

The commands must be standalone. **Do not require a `bm-git` prefix.**

------------------------------------------------------------------------

## 2. Core Requirement

The desired user experience is:

``` text
gpl  -> git pull
gps  -> git push
gst  -> git status
```

NOT:

``` text
bm-git pl
bm-git ps
bm-git st
```

The shortcut itself is the command.

------------------------------------------------------------------------

## 3. Initial Shortcut Map

Version `0.1.0` should target these commands:

  Shortcut   Git command
  ---------- -----------------------------
  `gpl`      `git pull`
  `gps`      `git push`
  `gst`      `git status`
  `gco`      `git checkout`
  `gcb`      `git checkout -b`
  `gcm`      `git commit -m`
  `gca`      `git commit --amend`
  `gdf`      `git diff`
  `gbr`      `git branch`
  `gss`      `git stash`
  `gsp`      `git stash pop`
  `glg`      `git log --oneline --graph`

This list can grow in future versions.

------------------------------------------------------------------------

## 4. CLI Behavior

Commands must forward arguments correctly.

Examples:

``` bash
gpl
```

runs:

``` bash
git pull
```

``` bash
gps origin main
```

runs:

``` bash
git push origin main
```

``` bash
gco main
```

runs:

``` bash
git checkout main
```

``` bash
gcb feature/login
```

runs:

``` bash
git checkout -b feature/login
```

``` bash
gcm "fix login issue"
```

runs:

``` bash
git commit -m "fix login issue"
```

The implementation must preserve argument boundaries and handle quoted
arguments correctly.

------------------------------------------------------------------------

## 5. Architecture

Prefer one common implementation with standalone command entry points.

Conceptually:

``` text
/usr/bin/gpl ──┐
/usr/bin/gps ──┤
/usr/bin/gst ──┤
/usr/bin/gco ──┤
/usr/bin/gcb ──┤
               ↓
        common bm-git implementation
               ↓
             git
```

The implementation can determine the requested operation from the
invoked command name (`argv[0]`) or use lightweight wrappers.

### Important

The package should expose the standalone commands:

``` text
gpl
gps
gst
gco
gcb
gcm
gca
gdf
gbr
gss
gsp
glg
```

`bm-git` may exist internally, but the user-facing workflow is the
standalone shortcuts.

------------------------------------------------------------------------

## 6. Debian Package

The project must produce a Debian package:

``` text
bm-git-shortcuts_<version>_<architecture>.deb
```

Example:

``` text
bm-git-shortcuts_0.1.0_amd64.deb
```

Expected installation:

``` bash
sudo dpkg -i bm-git-shortcuts_0.1.0_amd64.deb
```

Expected removal:

``` bash
sudo dpkg -r bm-git-shortcuts
```

The package must not require manual copying of files after installation.

------------------------------------------------------------------------

## 7. Proposed Repository Structure

Initial target:

``` text
bm-git-shortcuts/
├── src/
│   └── bm-git
├── debian/
│   ├── control
│   ├── rules
│   ├── install
│   └── changelog
├── tests/
│   └── test_commands.sh
├── Makefile
├── README.md
├── USER_GUIDE.md
├── VERSION
└── GIT_SHORTCUTS_CONTEXT.md
```

The structure can change if there is a technically better Debian-native
approach, but keep the project simple.

User-facing docs already in the repo:

- `README.md` --- repository overview, install, quick start
- `USER_GUIDE.md` --- current features and how to use them
- `GIT_SHORTCUTS_CONTEXT.md` --- this file (project goals and tracking)

------------------------------------------------------------------------

## 8. Development Principles

### Keep it small

This is a utility, not a large framework.

Avoid unnecessary dependencies.

Prefer standard Linux tooling where practical.

### Safe execution

Do not construct shell commands by concatenating untrusted strings.

Prefer direct process execution, for example conceptually:

``` python
subprocess.run(["git", "pull", *args])
```

or the equivalent safe mechanism in the selected implementation
language.

### Preserve Git behavior

The shortcut should behave like Git.

For example:

``` bash
gpl --rebase
```

should effectively behave like:

``` bash
git pull --rebase
```

Do not silently modify Git arguments.

### Error propagation

If Git returns a non-zero exit code, the shortcut should return the same
failure status to the shell.

Example:

``` bash
gpl
echo $?
```

should reflect Git's result.

### Git availability

If Git is not installed, provide a clear error message rather than an
obscure runtime failure.

------------------------------------------------------------------------

## 9. Testing Requirements

Before releasing a version, test:

### Basic commands

``` bash
gpl
gps
gst
gdf
gbr
gss
gsp
glg
```

### Commands with arguments

``` bash
gco main
gcb feature/test
gps origin main
gpl --rebase
gcm "test commit"
```

### Error handling

Test:

-   Git is unavailable.
-   The command is executed outside a Git repository where appropriate.
-   Git returns a failure.
-   Invalid arguments are passed.
-   Arguments containing spaces are preserved.

### Package testing

After building the `.deb`:

``` bash
dpkg -i bm-git-shortcuts_0.1.0_amd64.deb
```

verify:

``` bash
which gpl
which gps
which gst
```

and:

``` bash
gpl --help
```

or equivalent behavior where applicable.

Also test removal:

``` bash
sudo dpkg -r bm-git-shortcuts
```

and verify that the installed shortcuts are removed.

------------------------------------------------------------------------

## 10. Versioning

Start with:

``` text
0.1.0
```

Use semantic-version-style progression:

``` text
0.1.x  -> fixes
0.2.x  -> additional functionality
1.0.0  -> stable first release
```

Keep the version consistent between the project metadata and Debian
package metadata.

------------------------------------------------------------------------

## 11. Future Ideas

These are ideas only. Do not implement them until explicitly agreed.

Possible future features:

-   `gundo` --- useful Git undo helpers
-   `gclean` --- clean local branches
-   `glog` --- improved log view
-   `gac` --- add + commit
-   `gap` --- add + push
-   configurable shortcuts
-   `bm-git-shortcuts config`
-   shell completion
-   Bash/Zsh/Fish support
-   architecture packages beyond `amd64`
-   `.deb` release automation
-   GitHub Actions for package builds
-   Debian repository / package hosting
-   installation via `apt`
-   uninstall/upgrade handling
-   command aliases configured by a file

Do not add complexity merely because it is possible.

------------------------------------------------------------------------

## 12. Release Goal

The first useful release should allow a Linux user to:

``` bash
sudo dpkg -i bm-git-shortcuts_0.1.0_amd64.deb
```

and immediately use:

``` bash
gpl
gps
gst
gco main
gcb feature/login
gcm "fix login"
```

without modifying `.bashrc` manually.

------------------------------------------------------------------------

## 13. AI Working Rules

When continuing work on this project:

1.  Read `GIT_SHORTCUTS_CONTEXT.md` first.
2.  Treat this document as the source of truth for the project's current
    goals.
3.  Do not change the core UX from standalone commands.
4.  Never replace `gpl`/`gps` with `bm-git pl`/`bm-git ps`.
5.  Keep Debian installation as a first-class requirement.
6.  Prefer simple, maintainable implementations.
7.  Add tests with new functionality.
8.  Update this context file when an important architectural or product
    decision changes.
9.  Before introducing a major dependency or architectural change,
    explain why it is needed.
10. Keep version and packaging information synchronized.
11. Do not implement future ideas unless they become an explicit
    requirement.
12. At each major milestone, verify the project against the requirements
    in this file.
13. Keep `README.md` and `USER_GUIDE.md` in sync with shipped features.
    When a shortcut is added, changed, or removed, update the user guide
    feature list and this status section in the same change.

------------------------------------------------------------------------

## 14. Current Status

**Project:** `bm-git-shortcuts`

**Current version:** `0.1.0`

**Status:** Implementation and local Debian packaging are complete and
verified. The `0.1.0-1` Debian package has been built, installed,
runtime-tested, and removed successfully.

### Completed

-   [x] Project name selected.
-   [x] Standalone shortcut UX selected.
-   [x] `.deb` / `dpkg` distribution selected.
-   [x] Initial shortcut list defined.
-   [x] Initial architecture direction defined.
-   [x] Write user-facing `README.md` (repo overview, install, start).
-   [x] Write `USER_GUIDE.md` (current 0.1.0 features and usage).
-   [x] Create repository structure.
-   [x] Implement shortcut dispatcher.
-   [x] Create all standalone shortcut entry points.
-   [x] Add automated tests.
-   [x] All 18 automated tests passing.
-   [x] Implement Debian packaging.
-   [x] Configure Debian source format (`3.0 (quilt)`).
-   [x] Build `bm-git-shortcuts_0.1.0-1_all.deb`.
-   [x] Inspect Debian package contents.
-   [x] Install package locally with `dpkg`.
-   [x] Verify installed commands.
-   [x] Test shortcut execution against Git.
-   [x] Verify argument forwarding with `gdf --stat` and
    `gpl --dry-run`.
-   [x] Verify package removal with `dpkg`.
-   [x] Verify shortcut commands disappear after package removal.

### Current Build Artifacts

The successful local build produces:

-   `bm-git-shortcuts_0.1.0-1_all.deb`
-   `bm-git-shortcuts_0.1.0-1.dsc`
-   `bm-git-shortcuts_0.1.0-1.debian.tar.xz`
-   `bm-git-shortcuts_0.1.0.orig.tar.gz`

The binary package is `Architecture: all`.

### Next

-   [ ] Review and synchronize `README.md` and `USER_GUIDE.md` with the
    verified Debian package workflow.
-   [ ] Clean up obsolete/generated build artifacts.
-   [ ] Add appropriate Debian/package build artifacts to `.gitignore`.
-   [ ] Review package metadata and release files.
-   [ ] Prepare the `0.1.0` release.
-   [ ] Push the completed work to `origin/dev`.

------------------------------------------------------------------------

## 15. Non-Negotiable UX

The most important requirement:

``` text
User types:

gpl

and the system executes:

git pull
```

and:

``` text
User types:

gps

and the system executes:

git push
```

The user should **not** need to type `bm-git` before the shortcut.

That is the core identity of `bm-git-shortcuts`.

------------------------------------------------------------------------

## 16. Documentation Tracking

Keep these three files aligned whenever product behavior changes.

  File                       Audience    What it tracks
  -------------------------- ----------- -----------------------------------------
  `README.md`                Users       What the repo is, install, quick start
  `USER_GUIDE.md`            Users       Features available now, with examples
  `GIT_SHORTCUTS_CONTEXT.md` Maintainers Goals, architecture, status, next work

### User-facing docs (current)

| Doc | Last updated | Covers |
| --- | ------------ | ------ |
| `README.md` | 2026-09-12 | Repo identity, 12 shortcuts, `dpkg` install/remove |
| `USER_GUIDE.md` | 2026-09-12 | All 0.1.0 commands, workflows, arguments, errors |

### Feature set documented in the user guide

These are the features described as available in `USER_GUIDE.md`.
Implementation of the dispatcher and `.deb` is still pending (see
section 14).

-   `gpl` `gps` `gst` `gco` `gcb` `gcm`
-   `gca` `gdf` `gbr` `gss` `gsp` `glg`

### When to update docs

-   New shortcut shipped → add it to README table, USER_GUIDE reference,
    section 3 map, and this list.
-   Shortcut behavior changes → update USER_GUIDE examples first.
-   Install or package name changes → update README, USER_GUIDE, and
    sections 6 / 12 here.
-   A future idea from section 11 is accepted → move it into the
    shortcut map and the user guide; do not leave it only in Future
    Ideas.
