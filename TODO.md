# TODO

This file lists high-level tasks and ideas for the asteroids project. Use this as a lightweight tracker for work-in-progress. Move long-running items to issues when appropriate.

## Priorities (short-term)

- [ ] Add a `run.py` wrapper or package `asteroids` so the project can be executed with `python -m asteroids`.
- [ ] Add basic audio (thrust sounds, explosion)
- [ ] Create keyboard remapping / input settings
- [ ] Implement player thrust and friction; use `self.velocity` for movement
- [ ] Destroy bullets when they go off screen

## Features (medium-term)

- [ ] Spawn asteroids with different velocities
- [ ] Implement collisions between shots, asteroids and player
- [ ] Add scoring, lives, and HUD
- [ ] Add pause/resume and a start menu

## Code & tooling

- [ ] Add docstrings to all public modules (follow PEP 257)
- [ ] Add unit tests for core game logic (collision detection, spawn logic)
- [ ] Add a VS Code `tasks.json` and `launch.json` for quick run/debug
- [ ] Add CI (GitHub Actions) to run tests and build docs

## Nice-to-have

- [ ] Packaging into an executable (PyInstaller) for distribution
- [ ] Add joystick/gamepad support
- [ ] Online high score board (backend)


---

Contributing:
- Prefer small, focused PRs for new features.
- For changes that affect game feel (physics or speed), add a simple test or playtest note in the PR description.

License: See `pyproject.toml` for project metadata.
